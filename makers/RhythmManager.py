# -*- encoding: utf-8 -*-
import itertools
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import spannertools
from abjad.tools import mathtools
from abjad.tools import metertools
from abjad.tools import rhythmmakertools
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
        initial_offset=None,
        meters=None,
        music=None,
        ):
        assert isinstance(initial_offset, durationtools.Offset)
        assert 0 <= initial_offset
        assert all(isinstance(x, metertools.Meter) for x in meters)
        assert len(meters)
        current_meters = list(meters)
        current_meter_offsets = list(mathtools.cumulative_sums(
            x.implied_time_signature.duration for x in meters))
        for container in music[:]:
            container_start_offset = \
                inspect_(container).get_timespan().start_offset + \
                initial_offset
            while 2 < len(current_meter_offsets) and \
                current_meter_offsets[1] <= container_start_offset:
                current_meter_offsets.pop(0)
                current_meters.pop(0)
            current_meter = current_meters[0]
            current_meter_offset = current_meter_offsets[0]
            current_initial_offset = \
                container_start_offset - current_meter_offset
            yield container, current_meter, current_initial_offset

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
        RhythmManager._rewrite_meter(
            music,
            initial_offset=initial_offset,
            meters=meters,
            )
        assert inspect_(music).get_duration() == sum(durations)
        rest_prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            )
        leading_silence = scoretools.Container()
        tailing_silence = scoretools.Container()
        for division in music[:]:
            leaves = division.select_leaves()
            if all(isinstance(leaf, rest_prototype) for leaf in leaves):
                leading_silence.append(division)
            else:
                break
        for division in reversed(music[:]):
            leaves = division.select_leaves()
            if all(isinstance(leaf, rest_prototype) for leaf in leaves):
                tailing_silence.insert(0, division)
            else:
                break
        if music:
            beam = spannertools.GeneralizedBeam(
                durations=durations,
                include_long_duration_notes=True,
                include_long_duration_rests=True,
                isolated_nib_direction=None,
                use_stemlets=True,
                )
            attach(beam, music)
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
        timespan_inventory_mapping = segment_product.timespan_inventory_mapping
        seed = 0
        for voice_name in timespan_inventory_mapping:
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
                            tie_split_notes=True,
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
                        seed=seed,
                        )
                previous_silence.extend(leading_silence)
                if not len(music.select_leaves()):
                    previous_silence.extend(tailing_silence)
                else:
                    if len(previous_silence.select_leaves()):
                        voice.append(previous_silence)
                    attach(music_specifier, music)
                    voice.append(music)
                    previous_silence = tailing_silence
                seed += 1
            if len(previous_silence.select_leaves()):
                voice.append(previous_silence)

    @staticmethod
    def _populate_time_signature_context(segment_product):
        score = segment_product.score
        time_signatures = segment_product.time_signatures
        measures = scoretools.make_spacer_skip_measures(time_signatures)
        score['TimeSignatureContext'].extend(measures)

    @staticmethod
    def _rewrite_meter(
        music=None,
        initial_offset=None,
        meters=None,
        ):
        iterator = RhythmManager._iterate_music_and_meters(
            initial_offset=initial_offset,
            meters=meters,
            music=music,
            )
        for container, current_meter, container_start_offset in iterator:
            current_meter_duration = \
                current_meter.implied_time_signature.duration
            container_stop_offset = inspect_(container).get_duration() + \
                container_start_offset
            if isinstance(container, scoretools.Tuplet) or \
                current_meter_duration < container_stop_offset:
                contents_duration = container._contents_duration
                meter = metertools.Meter(contents_duration)
                mutate(container[:]).rewrite_meter(
                    meter,
                    boundary_depth=1,
                    maximum_dot_count=2,
                    )
            else:
                if inspect_(container).get_duration() == \
                    current_meter_duration and \
                    container_start_offset == 0 and \
                    all(isinstance(x, scoretools.Rest)
                        for x in container.select_leaves()):
                    multi_measure_rest = scoretools.MultimeasureRest(1)
                    multiplier = durationtools.Multiplier(
                        current_meter_duration)
                    attach(multiplier, multi_measure_rest)
                    container[:] = [multi_measure_rest]
                else:
                    mutate(container[:]).rewrite_meter(
                        current_meter,
                        boundary_depth=1,
                        initial_offset=container_start_offset,
                        maximum_dot_count=2,
                        )

    ### PUBLIC METHODS ###

    @staticmethod
    def execute(
        segment_product=None,
        ):
        RhythmManager._populate_time_signature_context(segment_product)
        RhythmManager._populate_rhythms(segment_product)
        RhythmManager._cleanup_silences(segment_product)
        return segment_product
