# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
import itertools
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
from abjad.tools import abctools


class RhythmManager(abctools.AbjadValueObject):
    r'''A rhythm manager.
    '''

    ### PRIVATE METHODS ###

    @staticmethod
    def _cleanup_logical_ties(segment_session):
        score = segment_session.score
        for voice in iterate(score).by_class(scoretools.Voice):
            for logical_tie in iterate(voice).by_logical_tie(
                nontrivial=True, pitched=True, reverse=True):
                if len(logical_tie) != 2:
                    continue
                if not logical_tie.all_leaves_are_in_same_parent:
                    continue
                if logical_tie.written_duration == \
                    durationtools.Duration(1, 8):
                    mutate(logical_tie).replace([scoretools.Note("c'8")])
                elif logical_tie.written_duration == \
                    durationtools.Duration(1, 16):
                    mutate(logical_tie).replace([scoretools.Note("c'16")])

    @staticmethod
    def _cleanup_silences(segment_session):
        import consort
        score = segment_session.score
        procedure = lambda x: isinstance(x, scoretools.MultimeasureRest)
        for voice in iterate(score).by_class(scoretools.Voice):
            for music in voice:
                music_specifier = inspect_(music).get_indicator(
                    consort.consorttools.MusicSpecifier)
                if not music_specifier.is_sentinel:
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
    def _collect_attack_points(segment_session):
        import consort
        score = segment_session.score
        attack_point_map = collections.OrderedDict()
        iterator = iterate(score).by_timeline(component_class=scoretools.Note)
        for note in iterator:
            logical_tie = inspect_(note).get_logical_tie()
            if note is not logical_tie.head:
                continue
            attack_point_signature = \
                consort.consorttools.AttackPointSignature.from_logical_tie(logical_tie)
            attack_point_map[logical_tie] = attack_point_signature
        segment_session.attack_point_map = attack_point_map

    @staticmethod
    def _consolidate_silences(segment_session):
        import consort
        score = segment_session.score
        meter_offsets = list(mathtools.cumulative_sums(
            x.implied_time_signature.duration
            for x in segment_session.meters))
        with systemtools.ForbidUpdate(score):
            assert score._is_forbidden_to_update
            for voice in iterate(score).by_class(scoretools.Voice):
                assert score._is_forbidden_to_update
                for music in reversed(voice):
                    assert score._is_forbidden_to_update
                    music_specifier = inspect_(music).get_indicator(
                        consort.consorttools.MusicSpecifier)
                    if not music_specifier.is_sentinel:
                        continue
                    timespan = inspect_(music).get_timespan()
                    start_offset = timespan.start_offset
                    stop_offset = timespan.stop_offset
                    split_offsets = [start_offset]
                    split_offsets.extend(
                        offset for offset in meter_offsets
                        if start_offset < offset < stop_offset
                        )
                    split_offsets.append(stop_offset)
                    split_durations = mathtools.difference_series(
                        split_offsets,
                        )
                    containers = []
                    for split_duration in split_durations:
                        durations = []
                        div, mod = divmod(
                            durationtools.Duration(split_duration),
                            durationtools.Duration(1),
                            )
                        durations = [durationtools.Duration(1)] * int(div)
                        if mod:
                            durations.append(mod)
                        rests = scoretools.make_rests(durations)
                        container = scoretools.Container(rests)
                        containers.append(container)
                    music[:] = containers

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
            beam = spannertools.GeneralizedBeam(
                durations=[division._get_duration() for division in music],
                include_long_duration_notes=True,
                include_long_duration_rests=False,
                isolated_nib_direction=None,
                use_stemlets=False,
                )
            attach(beam, music)
#            for division in music:
#                beam = spannertools.GeneralizedBeam(
#                    durations=[division._get_duration()],
#                    include_long_duration_notes=True,
#                    include_long_duration_rests=False,
#                    isolated_nib_direction=None,
#                    use_stemlets=True,
#                    )
#                attach(beam, division)
        assert sum([
            inspect_(music).get_duration(),
            inspect_(leading_silence).get_duration(),
            inspect_(tailing_silence).get_duration(),
            ]) == sum(durations)
        return leading_silence, music, tailing_silence

    @staticmethod
    def _populate_rhythms(segment_session):
        def grouper(timespan):
            music_specifier = None
            if isinstance(timespan, consort.consorttools.PerformedTimespan):
                music_specifier = timespan.music_specifier
                if music_specifier is None:
                    music_specifier = consort.consorttools.MusicSpecifier()
            return music_specifier
        import consort
        silent_music_specifier = consort.consorttools.MusicSpecifier(
            is_sentinel=True,
            )
        voicewise_timespans = segment_session.voicewise_timespans
        counter = collections.Counter()
        voice_names = voicewise_timespans.keys()
        voice_names = RhythmManager._sort_voice_names(
            score_template=segment_session.segment_maker.score_template,
            voice_names=voice_names,
            )
        for voice_name in voice_names:
            timespan_inventory = voicewise_timespans[voice_name]
            voice = segment_session.score[voice_name]
            previous_silence = scoretools.Container()
            for music_specifier, timespans in itertools.groupby(
                timespan_inventory, grouper):
                if music_specifier is None:
                    rhythm_maker = rhythmmakertools.NoteRhythmMaker(
                        output_masks=[
                            rhythmmakertools.BooleanPattern(
                                indices=[0],
                                period=1,
                                )
                            ],
                        )
                elif music_specifier.rhythm_maker is None:
                    rhythm_maker = rhythmmakertools.NoteRhythmMaker(
                        beam_specifier=rhythmmakertools.BeamSpecifier(
                            beam_each_division=False,
                            beam_divisions_together=False,
                            ),
                        tie_specifier=rhythmmakertools.TieSpecifier(
                            tie_across_divisions=True,
                            ),
                        )
                else:
                    rhythm_maker = music_specifier.rhythm_maker
                if music_specifier not in counter:
                    if music_specifier is None:
                        seed = 0
                    else:
                        seed = music_specifier.seed or 0
                    counter[music_specifier] = seed
                seed = counter[music_specifier]
                timespans = tuple(timespans)
                durations = [x.duration for x in timespans]
                start_offset = timespans[0].start_offset
                leading_silence, music, tailing_silence = \
                    RhythmManager._populate_rhythm_group(
                        durations=durations,
                        initial_offset=start_offset,
                        meters=segment_session.meters,
                        rhythm_maker=rhythm_maker,
                        seed=seed,
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
                counter[music_specifier] += 1
            if len(previous_silence.select_leaves()):
                attach(
                    silent_music_specifier,
                    previous_silence,
                    scope=scoretools.Voice,
                    )
                voice.append(previous_silence)

    @staticmethod
    def _populate_time_signature_context(segment_session):
        score = segment_session.score
        time_signatures = segment_session.time_signatures
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
                maximum_dot_count=1,
                )
            RhythmManager._rewrite_tuplet_meter(split_component)
            right_start = inspect_(right_group[0]).get_timespan().start_offset
            initial_offset = right_start - split_offset
            mutate(right_group).rewrite_meter(
                meter_two,
                boundary_depth=1,
                initial_offset=initial_offset,
                maximum_dot_count=1,
                )
        else:
            left, right = mutate(container[:]).split([split_duration])
            mutate(left).rewrite_meter(
                meter_one,
                boundary_depth=1,
                initial_offset=container_start_offset,
                maximum_dot_count=1,
                )
            mutate(right).rewrite_meter(
                meter_two,
                boundary_depth=1,
                maximum_dot_count=1,
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
            maximum_dot_count=1,
            )

    @staticmethod
    def _rewrite_meter(
        music=None,
        meters=None,
        ):
        import consort
        music_specifier = inspect_(music).get_indicator(consort.consorttools.MusicSpecifier)
        rhythm_maker = music_specifier.rhythm_maker
        if rhythm_maker is not None:
            if rhythm_maker.duration_spelling_specifier is not None:
                specifier = rhythm_maker.duration_spelling_specifier
                if specifier.permit_meter_rewriting is False:
                    return
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
                continue
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
                        maximum_dot_count=1,
                        )
            if is_tied:
                last_leaf = container.select_leaves()[-1]
                next_leaf = inspect_(last_leaf).get_leaf(1)
                selection = selectiontools.ContiguousSelection((
                    last_leaf, next_leaf))
                selection._attach_tie_spanner_to_leaf_pair()

    @staticmethod
    def _rewrite_meters(segment_session):
        score = segment_session.score
        with systemtools.ForbidUpdate(score):
            for voice in iterate(score).by_class(scoretools.Voice):
                if voice.context_name == 'Dynamics':
                    continue
                for music in voice:
                    RhythmManager._rewrite_meter(
                        music=music,
                        meters=segment_session.meters,
                        )

    @staticmethod
    def _sort_voice_names(
        score_template=None,
        voice_names=None,
        ):
        result = []
        score = score_template()
        for voice in iterate(score).by_class(scoretools.Voice):
            if voice.name in voice_names:
                result.append(voice.name)
        return tuple(result)

    ### PUBLIC METHODS ###

    @staticmethod
    def execute(
        annotation_specifier=None,
        segment_session=None,
        ):
        with systemtools.Timer() as timer:
            RhythmManager._populate_time_signature_context(segment_session)
        print('\tpopulated time signature context:', timer.elapsed_time)
        with systemtools.Timer() as timer:
            RhythmManager._populate_rhythms(segment_session)
        print('\tpopulated rhythms:', timer.elapsed_time)
        if annotation_specifier is not None and \
            annotation_specifier.show_stage_4:
            segment_session.unrewritten_score = \
                mutate(segment_session.score).copy()
        with systemtools.Timer() as timer:
            RhythmManager._consolidate_silences(segment_session)
        print('\tconsolidated silences:', timer.elapsed_time)
        with systemtools.Timer() as timer:
            RhythmManager._rewrite_meters(segment_session)
        print('\trewrote meters:', timer.elapsed_time)
        with systemtools.Timer() as timer:
            RhythmManager._cleanup_silences(segment_session)
        print('\tcleaned up silences:', timer.elapsed_time)
        with systemtools.Timer() as timer:
            RhythmManager._cleanup_logical_ties(segment_session)
        print('\tcleaned up logical ties:', timer.elapsed_time)
        with systemtools.Timer() as timer:
            RhythmManager._collect_attack_points(segment_session)
        print('\tcollected attack points:', timer.elapsed_time)
        return segment_session