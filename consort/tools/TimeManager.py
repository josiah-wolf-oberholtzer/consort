# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
import itertools
from abjad import attach
from abjad import inspect_
from abjad import iterate
from abjad import mutate
from abjad import new
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import metertools
from abjad.tools import rhythmmakertools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools import spannertools
from abjad.tools import systemtools
from abjad.tools import timespantools


class TimeManager(abctools.AbjadValueObject):

    ### PUBLIC METHODS ###

    @staticmethod
    def can_rewrite_meter(inscribed_timespan):
        r'''Is true if containers to be inscribed into `inscribed_timespan` can
        undergo meter rewriting. Otherwise false.

        Returns boolean.
        '''
        import consort
        music_specifier = inscribed_timespan.music_specifier
        if music_specifier is None:
            return True
        rhythm_maker = music_specifier.rhythm_maker
        if rhythm_maker is None:
            return True
        if isinstance(rhythm_maker, consort.CompositeRhythmMaker):
            specifier = rhythm_maker.default.duration_spelling_specifier
        else:
            specifier = rhythm_maker.duration_spelling_specifier
        if specifier is None:
            return True
        if specifier.permit_meter_rewriting is False:
            return False
        return True

    @staticmethod
    def cleanup_logical_ties(music):
        for logical_tie in iterate(music).by_logical_tie(
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
    def collect_attack_points(score):
        import consort
        attack_point_map = collections.OrderedDict()
        iterator = iterate(score).by_timeline(component_class=scoretools.Note)
        for note in iterator:
            logical_tie = inspect_(note).get_logical_tie()
            if note is not logical_tie.head:
                continue
            attack_point_signature = \
                consort.AttackPointSignature.from_logical_tie(logical_tie)
            attack_point_map[logical_tie] = attack_point_signature
        return attack_point_map

    @staticmethod
    def consolidate_demultiplexed_timespans(demultiplexed_timespans):
        for voice_name in demultiplexed_timespans:
            timespans = demultiplexed_timespans[voice_name]
            consolidated_timespans = TimeManager.consolidate_timespans(
                timespans)
            demultiplexed_timespans[voice_name] = consolidated_timespans

    @staticmethod
    def consolidate_rests(music):
        r"""Consolidates non-tupleted rests into separate containers in
        `music`.

        ::

            >>> import consort

        ::

            >>> music = scoretools.Container(r'''
            ...     { r4 c'8 }
            ...     \times 2/3 { d'4 r8 }
            ...     { r4 e'4 f'4 r4 }
            ...     { r4 g8 r8 }
            ...     { r4 }
            ...     { r4 }
            ...     { a'4 \times 2/3 { b'4 r8 } }
            ...     { c''4 r8 }
            ...     ''')
            >>> print(format(music))
            {
                {
                    r4
                    c'8
                }
                \times 2/3 {
                    d'4
                    r8
                }
                {
                    r4
                    e'4
                    f'4
                    r4
                }
                {
                    r4
                    g8
                    r8
                }
                {
                    r4
                }
                {
                    r4
                }
                {
                    a'4
                    \times 2/3 {
                        b'4
                        r8
                    }
                }
                {
                    c''4
                    r8
                }
            }

        ::

            >>> music = consort.TimeManager.consolidate_rests(music)
            >>> print(format(music))
            {
                {
                    r4
                }
                {
                    c'8
                }
                \times 2/3 {
                    d'4
                    r8
                }
                {
                    r4
                }
                {
                    e'4
                    f'4
                }
                {
                    r4
                    r4
                }
                {
                    g8
                }
                {
                    r8
                    r4
                    r4
                }
                {
                    a'4
                    \times 2/3 {
                        b'4
                        r8
                    }
                }
                {
                    c''4
                }
                {
                    r8
                }
            }

        Returns `music`.
        """
        prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            )
        initial_music_duration = inspect_(music).get_duration()
        initial_leaves = music.select_leaves()
        if not isinstance(music[0], scoretools.Tuplet):
            leading_silence = scoretools.Container()
            while music[0] and isinstance(music[0][0], prototype):
                leading_silence.append(music[0].pop(0))
            if leading_silence:
                music.insert(0, leading_silence)
        if not isinstance(music[-1], scoretools.Tuplet):
            tailing_silence = scoretools.Container()
            while music[-1] and isinstance(music[-1][-1], prototype):
                tailing_silence.insert(0, music[-1].pop())
            if tailing_silence:
                music.append(tailing_silence)
        if len(music) < 2:
            return music
        indices = reversed(range(len(music) - 1))
        for index in indices:
            division = music[index]
            next_division = music[index + 1]
            silence = scoretools.Container()
            if not isinstance(division, scoretools.Tuplet):
                while division and isinstance(division[-1], prototype):
                    silence.insert(0, division.pop())
            if not isinstance(next_division, scoretools.Tuplet):
                while next_division and \
                    isinstance(next_division[0], prototype):
                    silence.append(next_division.pop(0))
            if silence:
                music.insert(index + 1, silence)
            if not division:
                music.remove(division)
            if not next_division:
                music.remove(next_division)
        for division in music[:]:
            if not division:
                music.remove(division)
        assert inspect_(music).get_duration() == initial_music_duration
        assert music.select_leaves() == initial_leaves
        return music

    @staticmethod
    def consolidate_timespans(timespans, allow_silences=False):
        r'''Consolidates contiguous performed timespans by music specifier.

        ::

            >>> import consort

        ::

            >>> timespans = timespantools.TimespanInventory([
            ...     consort.PerformedTimespan(
            ...         start_offset=0,
            ...         stop_offset=10,
            ...         music_specifier='foo',
            ...         ),
            ...     consort.PerformedTimespan(
            ...         start_offset=10,
            ...         stop_offset=20,
            ...         music_specifier='foo',
            ...         ),
            ...     consort.PerformedTimespan(
            ...         start_offset=20,
            ...         stop_offset=25,
            ...         music_specifier='bar',
            ...         ),
            ...     consort.PerformedTimespan(
            ...         start_offset=40,
            ...         stop_offset=50,
            ...         music_specifier='bar',
            ...         ),
            ...     consort.PerformedTimespan(
            ...         start_offset=50,
            ...         stop_offset=58,
            ...         music_specifier='bar',
            ...         ),
            ...     ])
            >>> print(format(timespans))
            timespantools.TimespanInventory(
                [
                    consort.tools.PerformedTimespan(
                        music_specifier='foo',
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(10, 1),
                        ),
                    consort.tools.PerformedTimespan(
                        music_specifier='foo',
                        start_offset=durationtools.Offset(10, 1),
                        stop_offset=durationtools.Offset(20, 1),
                        ),
                    consort.tools.PerformedTimespan(
                        music_specifier='bar',
                        start_offset=durationtools.Offset(20, 1),
                        stop_offset=durationtools.Offset(25, 1),
                        ),
                    consort.tools.PerformedTimespan(
                        music_specifier='bar',
                        start_offset=durationtools.Offset(40, 1),
                        stop_offset=durationtools.Offset(50, 1),
                        ),
                    consort.tools.PerformedTimespan(
                        music_specifier='bar',
                        start_offset=durationtools.Offset(50, 1),
                        stop_offset=durationtools.Offset(58, 1),
                        ),
                    ]
                )

        ::

            >>> timespans = consort.TimeManager.consolidate_timespans(
            ...     timespans)
            >>> print(format(timespans))
            timespantools.TimespanInventory(
                [
                    consort.tools.PerformedTimespan(
                        divisions=(
                            durationtools.Duration(10, 1),
                            durationtools.Duration(10, 1),
                            ),
                        music_specifier='foo',
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(20, 1),
                        ),
                    consort.tools.PerformedTimespan(
                        divisions=(
                            durationtools.Duration(5, 1),
                            ),
                        music_specifier='bar',
                        start_offset=durationtools.Offset(20, 1),
                        stop_offset=durationtools.Offset(25, 1),
                        ),
                    consort.tools.PerformedTimespan(
                        divisions=(
                            durationtools.Duration(10, 1),
                            durationtools.Duration(8, 1),
                            ),
                        music_specifier='bar',
                        start_offset=durationtools.Offset(40, 1),
                        stop_offset=durationtools.Offset(58, 1),
                        ),
                    ]
                )

        Returns new timespan inventory.
        '''
        consolidated_timespans = timespantools.TimespanInventory()
        for music_specifier, grouped_timespans in \
            TimeManager.group_timespans(timespans):
            if music_specifier is None and not allow_silences:
                continue
            if hasattr(music_specifier, 'minimum_phrase_duration'):
                duration = music_specifier.minimum_phrase_duration
                if duration and grouped_timespans.duration < duration:
                    continue
            divisions = tuple(_.duration for _ in grouped_timespans)
            first_timespan = grouped_timespans[0]
            last_timespan = grouped_timespans[-1]
            consolidated_timespan = new(
                first_timespan,
                divisions=divisions,
                stop_offset=last_timespan.stop_offset,
                original_stop_offset=last_timespan.original_stop_offset,
                )
            consolidated_timespans.append(consolidated_timespan)
        consolidated_timespans.sort()
        return consolidated_timespans

    @staticmethod
    def debug_timespans(timespans):
        import consort
        if not timespans:
            consort.debug('No timespans found.')
        else:
            consort.debug('DEBUG: Dumping timespans:')
        if isinstance(timespans, dict):
            for voice_name in timespans:
                consort.debug('\t' + voice_name)
                for timespan in timespans[voice_name]:
                    consort.debug('\t\t{}: {} to {}'.format(
                        type(timespan).__name__,
                        timespan.start_offset,
                        timespan.stop_offset,
                        ))
        else:
            for timespan in timespans:
                consort.debug('\t({}) {}: {} to {}'.format(
                    timespan.voice_name,
                    type(timespan).__name__,
                    timespan.start_offset,
                    timespan.stop_offset,
                    ))

    @staticmethod
    def demultiplex_timespans(multiplexed_timespans):
        demultiplexed_timespans = {}
        for timespan in multiplexed_timespans:
            voice_name, layer = timespan.voice_name, timespan.layer
            if voice_name not in demultiplexed_timespans:
                demultiplexed_timespans[voice_name] = {}
            if layer not in demultiplexed_timespans[voice_name]:
                demultiplexed_timespans[voice_name][layer] = \
                    timespantools.TimespanInventory()
            demultiplexed_timespans[voice_name][layer].append(
                timespan)
            demultiplexed_timespans[voice_name][layer]
        for voice_name in demultiplexed_timespans:
            timespan_inventories = demultiplexed_timespans[voice_name]
            timespan_inventory = \
                TimeManager.resolve_timespan_inventories(
                    timespan_inventories)
            demultiplexed_timespans[voice_name] = timespan_inventory
        return demultiplexed_timespans

    @staticmethod
    def division_is_silent(division):
        r'''Is true when division only contains rests, at any depth.

        ::

            >>> import consort

        ::

            >>> division = scoretools.Container("c'4 d'4 e'4 f'4")
            >>> consort.TimeManager.division_is_silent(division)
            False

        ::

            >>> division = scoretools.Container('r4 r8 r16 r32')
            >>> consort.TimeManager.division_is_silent(division)
            True

        ::

            >>> division = scoretools.Container(
            ...     r"c'4 \times 2/3 { d'8 r8 e'8 } f'4")
            >>> consort.TimeManager.division_is_silent(division)
            False

        ::

            >>> division = scoretools.Container(
            ...     r'\times 2/3 { r4 \times 2/3 { r8. } }')
            >>> consort.TimeManager.division_is_silent(division)
            True

        Returns boolean.
        '''
        rest_prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            )
        leaves = division.select_leaves()
        return all(isinstance(leaf, rest_prototype) for leaf in leaves)

    @staticmethod
    def execute(
        discard_final_silence=None,
        permitted_time_signatures=None,
        segment_session=None,
        desired_duration=None,
        score_template=None,
        settings=None,
        timespan_quantization=None,
        ):
        score = score_template()
        multiplexed_timespans = timespantools.TimespanInventory()
        with systemtools.Timer(
            enter_message='\tpopulating independent timespans:',
            exit_message='\t\ttotal:',
            ):
            meters, meter_offsets, multiplexed_timespans = \
                TimeManager.populate_independent_timespans(
                    discard_final_silence,
                    multiplexed_timespans,
                    permitted_time_signatures,
                    score,
                    score_template,
                    settings,
                    desired_duration,
                    timespan_quantization,
                    )
        with systemtools.Timer(
            enter_message='\tpopulating dependent timespans:',
            exit_message='\t\ttotal:',
            ):
            demultiplexed_timespans = TimeManager.populate_dependent_timespans(
                meter_offsets,
                multiplexed_timespans,
                score,
                score_template,
                settings,
                desired_duration,
                )
        with systemtools.Timer('\tpopulated silent timespans:'):
            demultiplexed_timespans = TimeManager.populate_silent_timespans(
                demultiplexed_timespans,
                meter_offsets,
                score,
                score_template,
                )

        with systemtools.Timer('\tvalidated timespans:'):
            TimeManager.validate_timespans(demultiplexed_timespans)

        with systemtools.Timer('\trewrote meters:'):
            TimeManager.rewrite_meters(
                demultiplexed_timespans,
                meters,
                )

        with systemtools.Timer('\tpopulated score:'):
            score = TimeManager.populate_score(
                demultiplexed_timespans,
                meters,
                score,
                )

        with systemtools.Timer('\tcollected attack points: '):
            attack_point_map = TimeManager.collect_attack_points(score)

        segment_session.attack_point_map = attack_point_map
        segment_session.meters = meters
        segment_session.score = score
        segment_session.voicewise_timespans = demultiplexed_timespans
        # rewrite meters? (magic)
        # perform other rhythmic processing
        return segment_session

    @staticmethod
    def find_meters(
        permitted_time_signatures=None,
        desired_duration=None,
        timespan_inventory=None,
        ):
        offset_counter = datastructuretools.TypedCounter(
            item_class=durationtools.Offset,
            )
        for timespan in timespan_inventory:
            offset_counter[timespan.start_offset] += 2
            offset_counter[timespan.stop_offset] += 1
        offset_counter[desired_duration] += 100
        meters = metertools.Meter.fit_meters_to_expr(
            offset_counter,
            permitted_time_signatures,
            maximum_repetitions=2,
            )
        return tuple(meters)

    @staticmethod
    def get_rhythm_maker(music_specifier):
        import consort
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
        elif isinstance(music_specifier.rhythm_maker,
            consort.CompositeRhythmMaker):
            rhythm_maker = music_specifier.rhythm_maker.new(
                beam_specifier=rhythmmakertools.BeamSpecifier(
                    beam_each_division=False,
                    beam_divisions_together=False,
                    ),
                )
        else:
            rhythm_maker = music_specifier.rhythm_maker
            rhythm_maker = new(
                rhythm_maker,
                beam_specifier=rhythmmakertools.BeamSpecifier(
                    beam_each_division=False,
                    beam_divisions_together=False,
                    ),
                )
        return rhythm_maker

    @staticmethod
    def group_nonsilent_divisions(music):
        r'''Groups non-silent divisions together.

        Yields groups in reverse order.

        ::

            >>> import consort

        ::

            >>> divisions = []
            >>> divisions.append(scoretools.Container('r4'))
            >>> divisions.append(scoretools.Container("c'4"))
            >>> divisions.append(scoretools.Container('r4 r4'))
            >>> divisions.append(scoretools.Container("d'4 d'4"))
            >>> divisions.append(scoretools.Container("e'4 e'4 e'4"))
            >>> divisions.append(scoretools.Container('r4 r4 r4'))
            >>> divisions.append(scoretools.Container("f'4 f'4 f'4 f'4"))

        ::

            >>> for group in consort.TimeManager.group_nonsilent_divisions(
            ...     divisions):
            ...     print(group)
            (Container("f'4 f'4 f'4 f'4"),)
            (Container("d'4 d'4"), Container("e'4 e'4 e'4"))
            (Container("c'4"),)

        Returns generator.
        '''
        group = []
        for division in tuple(reversed(music)):
            if TimeManager.division_is_silent(division):
                if group:
                    yield tuple(reversed(group))
                    group = []
            else:
                group.append(division)
        if group:
            yield tuple(reversed(group))

    @staticmethod
    def group_timespans(timespans):
        def grouper(timespan):
            music_specifier = None
            if isinstance(timespan, consort.PerformedTimespan):
                music_specifier = timespan.music_specifier
                if music_specifier is None:
                    music_specifier = consort.MusicSpecifier()
            forbid_fusing = timespan.forbid_fusing
            return music_specifier, forbid_fusing
        import consort
        for partitioned_timespans in timespans.partition(
            include_tangent_timespans=True):
            for key, grouped_timespans in itertools.groupby(
                partitioned_timespans, grouper):
                music_specifier, forbid_fusing = key
                if forbid_fusing:
                    for timespan in grouped_timespans:
                        group = timespantools.TimespanInventory([timespan])
                        yield music_specifier, group
                else:
                    group = timespantools.TimespanInventory(
                        grouped_timespans)
                    yield music_specifier, group

    @staticmethod
    def inscribe_demultiplexed_timespans(
        demultiplexed_timespans,
        score,
        ):
        counter = collections.Counter()
        voice_names = demultiplexed_timespans.keys()
        voice_names = TimeManager.sort_voice_names(score, voice_names)
        for voice_name in voice_names:
            inscribed_timespans = timespantools.TimespanInventory()
            uninscribed_timespans = demultiplexed_timespans[voice_name]
            for timespan in uninscribed_timespans:
                if timespan.music is None:
                    music_specifier = timespan.music_specifier
                    if music_specifier not in counter:
                        if music_specifier is None:
                            seed = 0
                        else:
                            seed = music_specifier.seed or 0
                        counter[music_specifier] = seed
                    seed = counter[music_specifier]
                    result = TimeManager.inscribe_timespan(timespan, seed=seed)
                    inscribed_timespans.extend(result)
                    # Negative rotation mimics advancing through a series.
                    counter[music_specifier] -= 1
                else:
                    inscribed_timespans.append(timespan)
            demultiplexed_timespans[voice_name] = inscribed_timespans

    @staticmethod
    def inscribe_timespan(timespan, seed=None):
        r'''Inscribes `timespan`.

        ::

            >>> import consort
            >>> music_specifier = consort.MusicSpecifier(
            ...     rhythm_maker=rhythmmakertools.NoteRhythmMaker(
            ...         beam_specifier=rhythmmakertools.BeamSpecifier(
            ...             beam_each_division=False,
            ...             ),
            ...         output_masks=[
            ...             rhythmmakertools.BooleanPattern(
            ...                 indices=[0],
            ...                 period=3,
            ...                 ),
            ...             ],
            ...         ),
            ...     )

        ::

            >>> timespan = consort.PerformedTimespan(
            ...     divisions=[durationtools.Duration(1, 4)] * 7,
            ...     start_offset=0,
            ...     stop_offset=(7, 4),
            ...     music_specifier=music_specifier,
            ...     )
            >>> print(format(timespan))
            consort.tools.PerformedTimespan(
                divisions=(
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    ),
                music_specifier=consort.tools.MusicSpecifier(
                    rhythm_maker=rhythmmakertools.NoteRhythmMaker(
                        beam_specifier=rhythmmakertools.BeamSpecifier(
                            beam_each_division=False,
                            beam_divisions_together=False,
                            ),
                        output_masks=(
                            rhythmmakertools.BooleanPattern(
                                indices=(0,),
                                period=3,
                                ),
                            ),
                        ),
                    ),
                start_offset=durationtools.Offset(0, 1),
                stop_offset=durationtools.Offset(7, 4),
                )

        ::

            >>> result = consort.TimeManager.inscribe_timespan(timespan)
            >>> print(format(result))
            timespantools.TimespanInventory(
                [
                    consort.tools.PerformedTimespan(
                        music=scoretools.Container(
                            "{ c'4 } { c'4 }"
                            ),
                        music_specifier=consort.tools.MusicSpecifier(
                            rhythm_maker=rhythmmakertools.NoteRhythmMaker(
                                beam_specifier=rhythmmakertools.BeamSpecifier(
                                    beam_each_division=False,
                                    beam_divisions_together=False,
                                    ),
                                output_masks=(
                                    rhythmmakertools.BooleanPattern(
                                        indices=(0,),
                                        period=3,
                                        ),
                                    ),
                                ),
                            ),
                        original_start_offset=durationtools.Offset(0, 1),
                        original_stop_offset=durationtools.Offset(7, 4),
                        start_offset=durationtools.Offset(1, 4),
                        stop_offset=durationtools.Offset(3, 4),
                        ),
                    consort.tools.PerformedTimespan(
                        music=scoretools.Container(
                            "{ c'4 } { c'4 }"
                            ),
                        music_specifier=consort.tools.MusicSpecifier(
                            rhythm_maker=rhythmmakertools.NoteRhythmMaker(
                                beam_specifier=rhythmmakertools.BeamSpecifier(
                                    beam_each_division=False,
                                    beam_divisions_together=False,
                                    ),
                                output_masks=(
                                    rhythmmakertools.BooleanPattern(
                                        indices=(0,),
                                        period=3,
                                        ),
                                    ),
                                ),
                            ),
                        original_start_offset=durationtools.Offset(0, 1),
                        original_stop_offset=durationtools.Offset(7, 4),
                        start_offset=durationtools.Offset(1, 1),
                        stop_offset=durationtools.Offset(3, 2),
                        ),
                    ]
                )

        Returns timespan inventory.
        '''
        inscribed_timespans = timespantools.TimespanInventory()
        rhythm_maker = TimeManager.get_rhythm_maker(timespan.music_specifier)
        durations = timespan.divisions[:]
        music = TimeManager.make_simple_music(
            rhythm_maker,
            durations,
            seed,
            )
        assert inspect_(music).get_duration() == timespan.duration
        for container, duration in zip(music, durations):
            assert inspect_(container).get_duration() == duration
        music = TimeManager.consolidate_rests(music)
        assert inspect_(music).get_duration() == timespan.duration
        for group in TimeManager.group_nonsilent_divisions(music):
            start_offset = inspect_(group[0]).get_timespan().start_offset
            stop_offset = inspect_(group[-1]).get_timespan().stop_offset
            start_offset += timespan.start_offset
            stop_offset += timespan.start_offset
            container = scoretools.Container()
            container.extend(group)
            beam = spannertools.GeneralizedBeam(
                durations=[division._get_duration() for division in music],
                include_long_duration_notes=True,
                include_long_duration_rests=False,
                isolated_nib_direction=None,
                use_stemlets=False,
                )
            attach(beam, container, name='beam')
            attach(timespan.music_specifier, container, scope=scoretools.Voice)
            inscribed_timespan = new(
                timespan,
                divisions=None,
                music=container,
                start_offset=start_offset,
                stop_offset=stop_offset,
                )
            assert inspect_(container).get_duration() == \
                inscribed_timespan.duration
            assert inspect_(container).get_timespan().start_offset == 0
            assert inspect_(container[0]).get_timespan().start_offset == 0
            inscribed_timespans.append(inscribed_timespan)
        inscribed_timespans.sort()
        return inscribed_timespans

    @staticmethod
    def leaf_is_tied(leaf):
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
    def make_simple_music(rhythm_maker, durations, seed=None):
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
        return music

    @staticmethod
    def meters_to_offsets(meters):
        r'''Converts `meters` to offsets.

        ::

            >>> import consort

        ::

            >>> meters = [
            ...     metertools.Meter((3, 4)),
            ...     metertools.Meter((2, 4)),
            ...     metertools.Meter((6, 8)),
            ...     metertools.Meter((5, 16)),
            ...     ]

        ::

            >>> offsets = consort.TimeManager.meters_to_offsets(meters)
            >>> for x in offsets:
            ...     x
            ...
            Offset(0, 1)
            Offset(3, 4)
            Offset(5, 4)
            Offset(2, 1)
            Offset(37, 16)

        Returns tuple of offsets.
        '''
        durations = [_.preprolated_duration for _ in meters]
        offsets = mathtools.cumulative_sums(durations)
        offsets = [durationtools.Offset(_) for _ in offsets]
        return tuple(offsets)

    @staticmethod
    def meters_to_timespans(meters):
        r'''Convert `meters` into a collection of annotated timespans.

        ::

            >>> import consort

        ::

            >>> meters = [
            ...     metertools.Meter((3, 4)),
            ...     metertools.Meter((2, 4)),
            ...     metertools.Meter((6, 8)),
            ...     metertools.Meter((5, 16)),
            ...     ]

        ::

            >>> timespans = consort.TimeManager.meters_to_timespans(meters)
            >>> print(format(timespans))
            consort.tools.TimespanCollection(
                [
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(3, 4),
                        annotation=metertools.Meter(
                            '(3/4 (1/4 1/4 1/4))'
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(3, 4),
                        stop_offset=durationtools.Offset(5, 4),
                        annotation=metertools.Meter(
                            '(2/4 (1/4 1/4))'
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(5, 4),
                        stop_offset=durationtools.Offset(2, 1),
                        annotation=metertools.Meter(
                            '(6/8 ((3/8 (1/8 1/8 1/8)) (3/8 (1/8 1/8 1/8))))'
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(2, 1),
                        stop_offset=durationtools.Offset(37, 16),
                        annotation=metertools.Meter(
                            '(5/16 (1/16 1/16 1/16 1/16 1/16))'
                            ),
                        ),
                    ]
                )

        Returns timespan collections.
        '''
        import consort
        timespans = consort.TimespanCollection()
        offsets = TimeManager.meters_to_offsets(meters)
        for i, meter in enumerate(meters):
            start_offset = offsets[i]
            stop_offset = offsets[i + 1]
            timespan = timespantools.AnnotatedTimespan(
                annotation=meter,
                start_offset=start_offset,
                stop_offset=stop_offset,
                )
            timespans.insert(timespan)
        return timespans

    @staticmethod
    def multiplex_timespans(demultiplexed_timespans):
        r'''Multiplexes `demultiplexed_timespans` into a single timespan
        inventory.

        ::

            >>> import consort

        ::

            >>> demultiplexed = {}
            >>> demultiplexed['foo'] = timespantools.TimespanInventory([
            ...     timespantools.Timespan(0, 10),
            ...     timespantools.Timespan(15, 30),
            ...     ])
            >>> demultiplexed['bar'] = timespantools.TimespanInventory([
            ...     timespantools.Timespan(5, 15),
            ...     timespantools.Timespan(20, 35),
            ...     ])
            >>> demultiplexed['baz'] = timespantools.TimespanInventory([
            ...     timespantools.Timespan(5, 40),
            ...     ])

        ::

            >>> multiplexed = consort.TimeManager.multiplex_timespans(
            ...     demultiplexed)
            >>> print(format(multiplexed))
            timespantools.TimespanInventory(
                [
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(10, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(5, 1),
                        stop_offset=durationtools.Offset(15, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(5, 1),
                        stop_offset=durationtools.Offset(40, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(15, 1),
                        stop_offset=durationtools.Offset(30, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(20, 1),
                        stop_offset=durationtools.Offset(35, 1),
                        ),
                    ]
                )

        Returns timespan inventory.
        '''
        multiplexed_timespans = timespantools.TimespanInventory()
        for timespans in demultiplexed_timespans.values():
            multiplexed_timespans.extend(timespans)
        multiplexed_timespans.sort()
        return multiplexed_timespans

    @staticmethod
    def populate_dependent_timespans(
        meter_offsets,
        multiplexed_timespans,
        score,
        score_template,
        settings,
        desired_duration,
        ):
        with systemtools.Timer('\t\tpopulated timespans:'):
            TimeManager.populate_multiplexed_timespans(
                dependent=True,
                score=score,
                score_template=score_template,
                settings=settings,
                desired_duration=desired_duration,
                timespan_inventory=multiplexed_timespans,
                )
        with systemtools.Timer('\t\tdemultiplexed timespans:'):
            demultiplexed_timespans = TimeManager.demultiplex_timespans(
                multiplexed_timespans)
        with systemtools.Timer('\t\tsplit timespans:'):
            TimeManager.split_demultiplexed_timespans(
                meter_offsets,
                demultiplexed_timespans,
                )
        with systemtools.Timer('\t\tpruned short timespans:'):
            for voice_name, timespans in demultiplexed_timespans.items():
                TimeManager.prune_short_timespans(timespans)
        with systemtools.Timer('\t\tconsolidated timespans:'):
            TimeManager.consolidate_demultiplexed_timespans(
                demultiplexed_timespans,
                )
        with systemtools.Timer('\t\tinscribed timespans:'):
            TimeManager.inscribe_demultiplexed_timespans(
                demultiplexed_timespans,
                score,
                )
        return demultiplexed_timespans

    @staticmethod
    def populate_independent_timespans(
        discard_final_silence,
        multiplexed_timespans,
        permitted_time_signatures,
        score,
        score_template,
        settings,
        desired_duration,
        timespan_quantization,
        ):
        with systemtools.Timer('\t\tpopulated timespans:'):
            TimeManager.populate_multiplexed_timespans(
                dependent=False,
                score=score,
                score_template=score_template,
                settings=settings,
                desired_duration=desired_duration,
                timespan_inventory=multiplexed_timespans,
                timespan_quantization=timespan_quantization,
                )
        with systemtools.Timer('\t\tfound meters:'):
            meters = TimeManager.find_meters(
                permitted_time_signatures=permitted_time_signatures,
                desired_duration=desired_duration,
                timespan_inventory=multiplexed_timespans,
                )
        meter_offsets = TimeManager.meters_to_offsets(meters)
        with systemtools.Timer('\t\tdemultiplexed timespans:'):
            demultiplexed_timespans = TimeManager.demultiplex_timespans(
                multiplexed_timespans)
        with systemtools.Timer('\t\tsplit timespans:'):
            TimeManager.split_demultiplexed_timespans(
                meter_offsets,
                demultiplexed_timespans,
                )
        with systemtools.Timer('\t\tconsolidated timespans:'):
            TimeManager.consolidate_demultiplexed_timespans(
                demultiplexed_timespans,
                )
        with systemtools.Timer('\t\tinscribed timespans:'):
            TimeManager.inscribe_demultiplexed_timespans(
                demultiplexed_timespans,
                score,
                )
        with systemtools.Timer('\t\tmultiplexed timespans:'):
            multiplexed_timespans = TimeManager.multiplex_timespans(
                demultiplexed_timespans)
        with systemtools.Timer('\t\tpruned short timespans:'):
            TimeManager.prune_short_timespans(multiplexed_timespans)
        with systemtools.Timer('\t\tpruned meters:'):
            meters = TimeManager.prune_meters(
                discard_final_silence,
                meters,
                multiplexed_timespans.stop_offset,
                )
            meter_offsets = TimeManager.meters_to_offsets(meters)
        return meters, meter_offsets, multiplexed_timespans

    @staticmethod
    def populate_multiplexed_timespans(
        dependent=False,
        score=None,
        score_template=None,
        settings=None,
        desired_duration=None,
        timespan_inventory=None,
        timespan_quantization=None,
        ):
        target_timespan = timespantools.Timespan(0, desired_duration)
        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
        independent_settings = [setting for setting in settings
            if not setting.timespan_maker.is_dependent
            ]
        dependent_settings = [setting for setting in settings
            if setting.timespan_maker.is_dependent
            ]
        if dependent:
            settings = dependent_settings
            start_index = len(independent_settings)
        else:
            settings = independent_settings
            start_index = 0
        for layer, music_setting in enumerate(settings, start_index):
            music_setting(
                layer=layer,
                score=score,
                score_template=score_template,
                target_timespan=target_timespan,
                timespan_inventory=timespan_inventory,
                timespan_quantization=timespan_quantization,
                )

    @staticmethod
    def populate_score(
        demultiplexed_timespans,
        meters,
        score,
        ):
        import consort
        time_signatures = [_.implied_time_signature for _ in meters]
        measures = scoretools.make_spacer_skip_measures(time_signatures)
        if 'TimeSignatureContext' not in score:
            time_signature_context = \
                consort.ScoreTemplateManager.make_time_signature_context()
            score.insert(0, time_signature_context)
        score['TimeSignatureContext'].extend(measures)
        for voice_name, timespans in demultiplexed_timespans.items():
            voice = score[voice_name]
            for timespan in timespans:
                assert timespan.duration == \
                    inspect_(timespan.music).get_duration()
                voice.append(timespan.music)
        return score

    @staticmethod
    def populate_silent_timespans(
        demultiplexed_timespans,
        meter_offsets,
        score,
        score_template,
        ):
        import consort
        silent_music_specifier = consort.MusicSpecifier(
            is_sentinel=True,
            )
        rhythm_maker = TimeManager.get_rhythm_maker(None)
        for voice in iterate(score).by_class(scoretools.Voice):
            voice_name = voice.name
            if voice_name not in demultiplexed_timespans:
                demultiplexed_timespans[voice_name] = \
                    timespantools.TimespanInventory()
            timespans = demultiplexed_timespans[voice_name]
            silences = timespantools.TimespanInventory([
                consort.SilentTimespan(
                    start_offset=0,
                    stop_offset=meter_offsets[-1],
                    voice_name=voice_name,
                    )
                ])
            silences = TimeManager.subtract_timespan_inventories(
                silences, timespans)
            silences = TimeManager.split_timespans(meter_offsets, silences)
            for group in silences.partition(include_tangent_timespans=True):
                start_offset = group.start_offset,
                stop_offset = group.stop_offset,
                durations = [_.duration for _ in group]
                silence = TimeManager.make_simple_music(
                    rhythm_maker,
                    durations,
                    )
                attach(silent_music_specifier, silence, scope=scoretools.Voice)
                silent_timespan = consort.PerformedTimespan(
                    music=silence,
                    start_offset=start_offset,
                    stop_offset=stop_offset,
                    voice_name=voice_name,
                    )
                timespans.append(silent_timespan)
            timespans.sort()
        return demultiplexed_timespans

    @staticmethod
    def prune_meters(
        discard_final_silence,
        meters,
        stop_offset,
        ):
        discard_final_silence = bool(discard_final_silence)
        if discard_final_silence:
            meters = list(meters)
            total_meter_durations = sum(_.duration for _ in meters[:-1])
            while stop_offset <= total_meter_durations:
                meters.pop()
                total_meter_durations = sum(_.duration for _ in meters[:-1])
        return tuple(meters)

    @staticmethod
    def prune_short_timespans(timespans):
        for timespan in timespans[:]:
            if timespan.minimum_duration and \
                timespan.duration < timespan.minimum_duration:
                timespans.remove(timespan)

    @staticmethod
    def resolve_timespan_inventories(
        timespan_inventories=None,
        ):
        import consort
        timespan_inventories = [x[1] for x in
            sorted(timespan_inventories.items(),
                key=lambda item: item[0],
                )
            ]
        resolved_inventory = consort.TimespanCollection()
        for timespan in timespan_inventories[0]:
            if isinstance(timespan, consort.SilentTimespan):
                continue
            resolved_inventory.insert(timespan)
        for timespan_inventory in timespan_inventories[1:]:
            resolved_inventory = TimeManager.subtract_timespan_inventories(
                resolved_inventory,
                timespan_inventory,
                )
            for timespan in resolved_inventory[:]:
                if timespan.minimum_duration and \
                    timespan.duration < timespan.minimum_duration:
                    resolved_inventory.remove(timespan)
            for timespan in timespan_inventory:
                if isinstance(timespan, consort.SilentTimespan):
                    continue
                resolved_inventory.append(timespan)
            resolved_inventory.sort()
        resolved_inventory = timespantools.TimespanInventory(
            resolved_inventory[:],
            )
        return resolved_inventory

    @staticmethod
    def rewrite_container_meter(
        container,
        meter_timespans,
        ):
        assert meter_timespans
        assert meter_timespans[0].start_offset <= \
            inspect_(container).get_timespan().start_offset
        last_leaf = container.select_leaves()[-1]
        is_tied = TimeManager.leaf_is_tied(last_leaf)
        container_timespan = inspect_(container).get_timespan()
        if isinstance(container, scoretools.Tuplet):
            contents_duration = container._contents_duration
            meter = metertools.Meter(contents_duration)
            mutate(container[:]).rewrite_meter(
                meter,
                boundary_depth=1,
                maximum_dot_count=1,
                )
        elif len(meter_timespans) == 1:
            container_timespan = inspect_(container).get_timespan()
            container_start_offset = container_timespan.start_offset
            container_stop_offset = container_timespan.stop_offset
            meter_timespan = meter_timespans[0]
            relative_meter_start_offset = meter_timespan.start_offset
            assert relative_meter_start_offset <= container_start_offset
            absolute_meter_stop_offset = (
                relative_meter_start_offset +
                container_start_offset +
                meter_timespan.duration
                )
            assert container_stop_offset <= absolute_meter_stop_offset
            if meter_timespan.is_congruent_to_timespan(container_timespan) \
                and TimeManager.division_is_silent(container):
                multi_measure_rest = scoretools.MultimeasureRest(1)
                duration = inspect_(container).get_duration()
                multiplier = durationtools.Multiplier(duration)
                attach(multiplier, multi_measure_rest)
                container[:] = [multi_measure_rest]
                staff_lines_spanner = spannertools.StaffLinesSpanner(1)
                attach(
                    staff_lines_spanner,
                    container,
                    name='staff_lines_spanner',
                    )
            else:
                meter = meter_timespan.annotation
                meter_offset = meter_timespan.start_offset
                initial_offset = container_start_offset - meter_offset
                mutate(container[:]).rewrite_meter(
                    meter,
                    boundary_depth=1,
                    initial_offset=initial_offset,
                    maximum_dot_count=1,
                    )
        else:
            # TODO: handle barline-crossing containers
            raise AssertionError('Barline-crossing containers not permitted.')
        if is_tied:
            last_leaf = container.select_leaves()[-1]
            next_leaf = inspect_(last_leaf).get_leaf(1)
            selection = selectiontools.ContiguousSelection((
                last_leaf, next_leaf))
            selection._attach_tie_spanner_to_leaf_pair()

    @staticmethod
    def rewrite_meters(
        demultiplexed_timespans,
        meters,
        ):
        import consort
        meter_timespans = TimeManager.meters_to_timespans(meters)
        for voice_name in sorted(demultiplexed_timespans):
            consort.debug('VOICE: {}'.format(voice_name))
            inscribed_timespans = demultiplexed_timespans[voice_name]
            for inscribed_timespan in inscribed_timespans:
                consort.debug('\t{!s} {!s} {!r}'.format(
                    inscribed_timespan.start_offset,
                    inscribed_timespan.stop_offset,
                    inscribed_timespan.music,
                    ))
                if not TimeManager.can_rewrite_meter(inscribed_timespan):
                    continue
                for i, container in enumerate(inscribed_timespan.music):
                    container_timespan = inspect_(container).get_timespan()
                    container_timespan = container_timespan.translate(
                        inscribed_timespan.start_offset)
                    if i == 0:
                        assert container_timespan.start_offset == \
                            inscribed_timespan.start_offset
                    if i == (len(inscribed_timespan.music) - 1):
                        assert container_timespan.stop_offset == \
                            inscribed_timespan.stop_offset
                    intersecting_meters = \
                        meter_timespans.find_timespans_intersecting_timespan(
                            container_timespan)
                    shifted_intersecting_meters = [
                        _.translate(-1 * inscribed_timespan.start_offset)
                        for _ in intersecting_meters
                        ]
                    consort.debug('\t\t{!r} {!r}'.format(
                        container,
                        container_timespan,
                        ))
                    for intersecting_meter in intersecting_meters:
                        consort.debug('\t\t\t' + repr(intersecting_meter))
                    TimeManager.rewrite_container_meter(
                        container,
                        shifted_intersecting_meters,
                        )
                    TimeManager.cleanup_logical_ties(container)

    @staticmethod
    def sort_voice_names(score, voice_names):
        result = []
        for voice in iterate(score).by_class(scoretools.Voice):
            if voice.name in voice_names:
                result.append(voice.name)
        return tuple(result)

    @staticmethod
    def split_demultiplexed_timespans(
        meter_offsets=None,
        demultiplexed_timespans=None,
        ):
        for voice_name in demultiplexed_timespans:
            timespan_inventory = demultiplexed_timespans[voice_name]
            split_inventory = TimeManager.split_timespans(
                meter_offsets,
                timespan_inventory,
                )
            demultiplexed_timespans[voice_name] = split_inventory

    @staticmethod
    def split_timespans(offsets, timespan_inventory):
        offsets = list(offsets)
        timespan_inventory.sort()
        split_inventory = timespantools.TimespanInventory()
        for timespan in timespan_inventory:
            current_offsets = []
            while offsets and offsets[0] <= timespan.start_offset:
                offsets.pop(0)
            while offsets and offsets[0] < timespan.stop_offset:
                current_offsets.append(offsets.pop(0))
            if hasattr(timespan, 'music') and timespan.music:
                # We don't need to split already-inscribed timespans
                split_inventory.append(timespan)
                continue
            elif timespan.forbid_splitting:
                continue
            if current_offsets:
                shards = timespan.split_at_offsets(current_offsets)
                for shard in shards:
                    if shard.minimum_duration:
                        if shard.minimum_duration <= shard.duration:
                            split_inventory.append(shard)
                    else:
                        split_inventory.append(shard)
            else:
                if timespan.minimum_duration:
                    if timespan.minimum_duration <= timespan.duration:
                        split_inventory.append(timespan)
                else:
                    split_inventory.append(timespan)
        split_inventory.sort()
        return split_inventory

    @staticmethod
    def subtract_timespan_inventories(inventory_one, inventory_two):
        r'''Subtracts `inventory_two` from `inventory_one`.

        ::

            >>> inventory_one = timespantools.TimespanInventory([
            ...     timespantools.Timespan(0, 10),
            ...     timespantools.Timespan(10, 20),
            ...     timespantools.Timespan(40, 80),
            ...     ])

        ::

            >>> inventory_two = timespantools.TimespanInventory([
            ...     timespantools.Timespan(5, 15),
            ...     timespantools.Timespan(25, 35),
            ...     timespantools.Timespan(35, 45),
            ...     timespantools.Timespan(55, 65),
            ...     timespantools.Timespan(85, 95),
            ...     ])

        ::

            >>> import consort
            >>> manager = consort.TimeManager
            >>> result = manager.subtract_timespan_inventories(
            ...      inventory_one,
            ...      inventory_two,
            ...      )
            >>> print(format(result))
            timespantools.TimespanInventory(
                [
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(5, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(15, 1),
                        stop_offset=durationtools.Offset(20, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(45, 1),
                        stop_offset=durationtools.Offset(55, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(65, 1),
                        stop_offset=durationtools.Offset(80, 1),
                        ),
                    ]
                )

        ::

            >>> result = manager.subtract_timespan_inventories(
            ...      inventory_two,
            ...      inventory_one,
            ...      )
            >>> print(format(result))
            timespantools.TimespanInventory(
                [
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(25, 1),
                        stop_offset=durationtools.Offset(35, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(35, 1),
                        stop_offset=durationtools.Offset(40, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(85, 1),
                        stop_offset=durationtools.Offset(95, 1),
                        ),
                    ]
                )

        '''
        import consort
        resulting_timespans = consort.TimespanCollection()
        if not inventory_two:
            return timespantools.TimespanInventory(inventory_one)
        elif not inventory_one:
            return timespantools.TimespanInventory()
        subtractee_index = 0
        subtractor_index = 0
        subtractee = None
        subtractor = None
        subtractee_is_modified = False
        while subtractee_index < len(inventory_one) and \
            subtractor_index < len(inventory_two):
            if subtractee is None:
                subtractee = inventory_one[subtractee_index]
                subtractee_is_modified = False
            if subtractor is None:
                subtractor = inventory_two[subtractor_index]
            if subtractee.intersects_timespan(subtractor):
                subtraction = subtractee - subtractor
                if len(subtraction) == 1:
                    subtractee = subtraction[0]
                    subtractee_is_modified = True
                elif len(subtraction) == 2:
                    resulting_timespans.insert(subtraction[0])
                    subtractee = subtraction[1]
                    subtractee_is_modified = True
                else:
                    subtractee = None
                    subtractee_index += 1
            else:
                if subtractee.stops_before_or_at_offset(
                    subtractor.start_offset):
                    resulting_timespans.insert(subtractee)
                    subtractee = None
                    subtractee_index += 1
                else:
                    subtractor = None
                    subtractor_index += 1
        if subtractee_is_modified:
            if subtractee:
                resulting_timespans.insert(subtractee)
            resulting_timespans.insert(inventory_one[subtractee_index + 1:])
        else:
            resulting_timespans.insert(inventory_one[subtractee_index:])
        resulting_timespans = timespantools.TimespanInventory(
            resulting_timespans[:])
        return resulting_timespans

    @staticmethod
    def validate_timespans(demultiplexed_timespans):
        durations = set()
        for voice_name, timespans in demultiplexed_timespans.items():
            timespans.sort()
            assert timespans.start_offset == 0
            assert timespans.all_are_contiguous
            assert timespans.all_are_well_formed
            assert timespans.all_are_nonoverlapping
            durations.add(timespans.stop_offset)
        assert len(tuple(durations)) == 1