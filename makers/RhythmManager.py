# -*- encoding: utf-8 -*-
import collections
import itertools
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import spannertools
from abjad.tools import mathtools
from abjad.tools import metertools
from abjad.tools import rhythmmakertools
from abjad.tools import selectiontools
from abjad.tools import systemtools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import mutate


class RhythmManager(abctools.AbjadObject):
    r'''A rhythm manager.
    '''

    ### PRIVATE METHODS ###

    @staticmethod
    def _cleanup_silences(segment_product):
        from consort import makers
        score = segment_product.score
        procedure = lambda x: isinstance(x, scoretools.MultimeasureRest)
        for voice in iterate(score).by_class(scoretools.Voice):
            for music in voice:
                if inspect_(music).get_indicators(makers.MusicSpecifier):
                    continue
                leaves = music.select_leaves()
                for is_multimeasure_rest, group in itertools.groupby(
                    leaves, procedure):
                    if not is_multimeasure_rest:
                        continue
                    group = list(group)
                    spanner = spannertools.StaffLinesSpanner(lines=1)
                    attach(spanner, group)

    @staticmethod
    def _iterate_music_and_meters(
        meters=None,
        music=None,
        ):
        assert all(isinstance(x, metertools.Meter) for x in meters)
        assert len(meters)
        current_meters = list(meters)
        current_meter_offsets = list(mathtools.cumulative_sums(
            x.implied_time_signature.duration for x in meters))
        for container in music[:]:
            container_start_offset = \
                inspect_(container).get_timespan().start_offset
            while 2 < len(current_meter_offsets) and \
                current_meter_offsets[1] <= container_start_offset:
                current_meter_offsets.pop(0)
                current_meters.pop(0)
            current_meter = current_meters[0]
            current_meter_offset = current_meter_offsets[0]
            current_initial_offset = \
                container_start_offset - current_meter_offset
            next_meter = None
            if 1 < len(current_meters):
                next_meter = current_meters[1]
            yield container, current_meter, next_meter, current_initial_offset

    @staticmethod
    def _populate_rhythm_group(
        durations=None,
        initial_offset=None,
        meters=None,
        rhythm_maker=None,
        seed=None,
        ):
        music = rhythm_maker(durations, seeds=seed)
        for i, x in enumerate(music):
            if len(x) == 1 and isinstance(x[0], scoretools.Tuplet):
                music[i] = x[0]
            else:
                music[i] = scoretools.Container(x)
        music = scoretools.Container(music)
        for x in music[:]:
            if isinstance(x, scoretools.Tuplet) and x.multiplier == 1:
                mutate(x).swap(scoretools.Container())
#        RhythmManager._rewrite_meter(
#            music,
#            initial_offset=initial_offset,
#            meters=meters,
#            )
        assert inspect_(music).get_duration() == sum(durations)
        rest_prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            )
        leading_silence = scoretools.Container()
        tailing_silence = scoretools.Container()
        for division in music[:]:
            leaves = division.select_leaves()
            if not all(isinstance(leaf, rest_prototype) for leaf in leaves):
                break
            division = music.pop(music.index(division))
            if isinstance(division, scoretools.Tuplet):
                duration = inspect_(division).get_duration()
                rests = scoretools.make_rests([duration])
                division = scoretools.Container(rests)
            leading_silence.append(division)
        for division in reversed(music[:]):
            leaves = division.select_leaves()
            if not all(isinstance(leaf, rest_prototype) for leaf in leaves):
                break
            division = music.pop(music.index(division))
            if isinstance(division, scoretools.Tuplet):
                duration = inspect_(division).get_duration()
                rests = scoretools.make_rests([duration])
                division = scoretools.Container(rests)
            tailing_silence.insert(0, division)
        if music:
            if not isinstance(music[0], scoretools.Tuplet):
                leading_silence_container = scoretools.Container()
                while isinstance(music[0][0], rest_prototype):
                    leading_silence_container.append(music[0].pop(0))
                if leading_silence_container:
                    leading_silence.append(leading_silence_container)
            if not isinstance(music[-1], scoretools.Tuplet):
                tailing_silence_container = scoretools.Container()
                while isinstance(music[-1][-1], rest_prototype):
                    tailing_silence_container.append(music[-1].pop())
                if tailing_silence_container:
                    tailing_silence.insert(0, tailing_silence_container)
#        if music:
#            beam = spannertools.GeneralizedBeam(
#                durations=durations,
#                include_long_duration_notes=True,
#                include_long_duration_rests=True,
#                isolated_nib_direction=None,
#                use_stemlets=True,
#                )
#            attach(beam, music)
        assert sum([
            inspect_(music).get_duration(),
            inspect_(leading_silence).get_duration(),
            inspect_(tailing_silence).get_duration(),
            ]) == sum(durations)
        return leading_silence, music, tailing_silence

    @staticmethod
    def _populate_rhythms(segment_product):
        def grouper(timespan):
            music_specifier = None
            if isinstance(timespan, makers.PerformedTimespan):
                music_specifier = timespan.music_specifier
                if music_specifier is None:
                    music_specifier = makers.MusicSpecifier()
            return music_specifier
        from consort import makers
        silent_music_specifier = makers.MusicSpecifier()
        timespan_inventory_mapping = segment_product.timespan_inventory_mapping
        seeds = collections.Counter()
        voice_names = timespan_inventory_mapping.keys()
        voice_names = RhythmManager._sort_voice_names(
            template=segment_product.segment_maker.template,
            voice_names=voice_names,
            )
        for voice_name in voice_names:
            timespan_inventory = timespan_inventory_mapping[voice_name]
            voice = segment_product.score[voice_name]
            previous_silence = scoretools.Container()
            for music_specifier, timespans in itertools.groupby(
                timespan_inventory, grouper):
                if music_specifier is None:
                    rhythm_maker = rhythmmakertools.RestRhythmMaker()
                elif music_specifier.rhythm_maker is None:
                    rhythm_maker = rhythmmakertools.NoteRhythmMaker(
                        tie_specifier=rhythmmakertools.TieSpecifier(
                            tie_across_divisions=True,
                            ),
                        )
                else:
                    rhythm_maker = music_specifier.rhythm_maker
                timespans = tuple(timespans)
                durations = [x.duration for x in timespans]
                start_offset = timespans[0].start_offset
                leading_silence, music, tailing_silence = \
                    RhythmManager._populate_rhythm_group(
                        durations=durations,
                        initial_offset=start_offset,
                        meters=segment_product.meters,
                        rhythm_maker=rhythm_maker,
                        seed=seeds[music_specifier],
                        )
                previous_silence.extend(leading_silence)
                if not len(music.select_leaves()):
                    previous_silence.extend(tailing_silence)
                else:
                    if len(previous_silence.select_leaves()):
                        attach(
                            silent_music_specifier,
                            previous_silence,
                            scope=scoretools.Voice,
                            )
                        voice.append(previous_silence)
                    attach(
                        music_specifier,
                        music,
                        scope=scoretools.Voice,
                        )
                    voice.append(music)
                    previous_silence = tailing_silence
                seeds[music_specifier] += 1
            if len(previous_silence.select_leaves()):
                attach(
                    silent_music_specifier,
                    previous_silence,
                    scope=scoretools.Voice,
                    )
                voice.append(previous_silence)

    @staticmethod
    def _populate_time_signature_context(segment_product):
        score = segment_product.score
        time_signatures = segment_product.time_signatures
        measures = scoretools.make_spacer_skip_measures(time_signatures)
        score['TimeSignatureContext'].extend(measures)

    @staticmethod
    def _rewrite_barline_crossing_container_meter(
        container=None,
        container_start_offset=None,
        meter_one=None,
        meter_two=None,
        ):
        meter_one_duration = meter_one.implied_time_signature.duration
        split_duration = meter_one_duration - container_start_offset
        container_timespan = inspect_(container).get_timespan()
        split_offset = container_timespan.start_offset + split_duration
        left_group, split_component, right_group = [], None, []
        for component in container:
            component_timespan = inspect_(component).get_timespan()
            start_offset = component_timespan.start_offset
            stop_offset = component_timespan.stop_offset
            if start_offset < split_offset < stop_offset:
                split_component = component
            else:
                if start_offset < split_offset:
                    left_group.append(component)
                elif split_offset <= start_offset:
                    right_group.append(component)
        if isinstance(split_component, scoretools.Tuplet):
            mutate(left_group).rewrite_meter(
                meter_one,
                boundary_depth=1,
                initial_offset=container_start_offset,
                maximum_dot_count=2,
                )
            RhythmManager._rewrite_tuplet_meter(split_component)
            right_start = inspect_(right_group[0]).get_timespan().start_offset
            initial_offset = right_start - split_offset
            mutate(right_group).rewrite_meter(
                meter_two,
                boundary_depth=1,
                initial_offset=initial_offset,
                maximum_dot_count=2,
                )
        else:
            left, right = mutate(container[:]).split([split_duration])
            mutate(left).rewrite_meter(
                meter_one,
                boundary_depth=1,
                initial_offset=container_start_offset,
                maximum_dot_count=2,
                )
            mutate(right).rewrite_meter(
                meter_two,
                boundary_depth=1,
                maximum_dot_count=2,
                )

    @staticmethod
    def _rewrite_silent_container_meter(
        container=None,
        ):
        multi_measure_rest = scoretools.MultimeasureRest(1)
        duration = inspect_(container).get_duration()
        multiplier = durationtools.Multiplier(duration)
        attach(multiplier, multi_measure_rest)
        container[:] = [multi_measure_rest]

    @staticmethod
    def _rewrite_tuplet_meter(
        container=None,
        ):
        contents_duration = container._contents_duration
        meter = metertools.Meter(contents_duration)
        mutate(container[:]).rewrite_meter(
            meter,
            boundary_depth=1,
            maximum_dot_count=2,
            )

    @staticmethod
    def _rewrite_meter(
        music=None,
        meters=None,
        ):
        iterator = RhythmManager._iterate_music_and_meters(
            meters=meters,
            music=music,
            )
        for item in iterator:
            container = item[0]
            current_meter = item[1]
            next_meter = item[2]
            container_start_offset = item[3]
            current_meter_duration = \
                current_meter.implied_time_signature.duration
            container_stop_offset = inspect_(container).get_duration() + \
                container_start_offset
            last_leaf = container.select_leaves()[-1]
            is_tied = RhythmManager._leaf_is_tied(last_leaf)
            if isinstance(container, scoretools.Tuplet):
                RhythmManager._rewrite_tuplet_meter(
                    container=container,
                    )
            elif current_meter_duration < container_stop_offset:
                RhythmManager._rewrite_barline_crossing_container_meter(
                    container=container,
                    meter_one=current_meter,
                    meter_two=next_meter,
                    container_start_offset=container_start_offset,
                    )
            else:
                if inspect_(container).get_duration() == \
                    current_meter_duration and \
                    container_start_offset == 0 and \
                    all(isinstance(x, scoretools.Rest)
                        for x in container.select_leaves()):
                    RhythmManager._rewrite_silent_container_meter(
                        container=container,
                        )
                else:
                    mutate(container[:]).rewrite_meter(
                        current_meter,
                        boundary_depth=1,
                        initial_offset=container_start_offset,
                        maximum_dot_count=2,
                        )
            if is_tied:
                last_leaf = container.select_leaves()[-1]
                next_leaf = inspect_(last_leaf).get_leaf(1)
                selection = selectiontools.ContiguousSelection((
                    last_leaf, next_leaf))
                selection._attach_tie_spanner_to_leaf_pair()

    @staticmethod
    def _rewrite_meters(segment_product):
        score = segment_product.score
        for voice in iterate(score).by_class(scoretools.Voice):
            for music in voice:
                RhythmManager._rewrite_meter(
                    music=music,
                    meters=segment_product.meters,
                    )

    @staticmethod
    def _sort_voice_names(
        template=None,
        voice_names=None,
        ):
        result = []
        score = template()
        for voice in iterate(score).by_class(scoretools.Voice):
            if voice.name in voice_names:
                result.append(voice.name)
        return tuple(result)

    @staticmethod
    def _leaf_is_tied(leaf):
        prototype = spannertools.Tie
        leaf_tie = None
        if inspect_(leaf).get_spanners(prototype):
            leaf_tie = inspect_(leaf).get_spanner(prototype)
        else:
            return False
        next_leaf = inspect_(leaf).get_leaf(1)
        if next_leaf is not None:
            if inspect_(next_leaf).get_spanners(prototype):
                next_leaf_tie = inspect_(next_leaf).get_spanner(prototype)
                if leaf_tie is next_leaf_tie:
                    return True
        return False

    ### PUBLIC METHODS ###

    @staticmethod
    def execute(
        segment_product=None,
        ):
        RhythmManager._populate_time_signature_context(segment_product)
        RhythmManager._populate_rhythms(segment_product)
        # TODO: Implement silence consolidation, before meter rewriting
        RhythmManager._rewrite_meters(segment_product)
        RhythmManager._cleanup_silences(segment_product)
        return segment_product
