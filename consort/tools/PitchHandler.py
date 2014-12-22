# -*- encoding: utf-8 -*-
from __future__ import print_function
import abc
import collections
from abjad import datastructuretools
from abjad import durationtools
from abjad import inspect_
from abjad import iterate
from abjad import instrumenttools
from abjad import pitchtools
from abjad import sequencetools
from abjad import timespantools
from supriya import timetools
from consort.tools.HashCachingObject import HashCachingObject


class PitchHandler(HashCachingObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_deviations',
        '_forbid_repetitions',
        '_grace_expressions',
        '_logical_tie_expressions',
        '_pitch_application_rate',
        '_pitch_operation_specifier',
        '_pitch_specifier',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        deviations=None,
        forbid_repetitions=None,
        grace_expressions=None,
        logical_tie_expressions=None,
        pitch_application_rate=None,
        pitch_specifier=None,
        pitch_operation_specifier=None,
        ):
        HashCachingObject.__init__(self)
        self._initialize_deviations(deviations)
        self._initialize_forbid_repetitions(forbid_repetitions)
        self._initialize_grace_expressions(grace_expressions)
        self._initialize_logical_tie_expressions(logical_tie_expressions)
        self._initialize_pitch_application_rate(pitch_application_rate)
        self._initialize_pitch_specifier(pitch_specifier)
        self._initialize_pitch_operation_specifier(pitch_operation_specifier)

    ### SPECIAL METHODS ###

    @abc.abstractmethod
    def __call__(
        self,
        timewise_seed,
        logical_tie,
        attack_point_signature,
        phrase_seed,
        pitch_range,
        previous_pitch,
        seed,
        transposition,
        ):
        raise NotImplementedError

    ### PRIVATE METHODS ###

    def _apply_logical_tie_expression(
        self,
        logical_tie,
        pitch_range,
        seed,
        ):
        if self.logical_tie_expressions:
            logical_tie_expression = self.logical_tie_expressions[seed]
            logical_tie_expression(
                logical_tie,
                pitch_range=pitch_range,
                )

    def _apply_deviation(
        self,
        pitch,
        seed,
        ):
        print('SEED', seed)
        if self.deviations:
            deviation = self.deviations[seed]
            pitch = pitchtools.NumberedPitch(pitch)
            pitch = pitch.transpose(deviation)
            pitch = pitchtools.NamedPitch(pitch)
        return pitch

    @staticmethod
    def _get_timewise_seed(
        timewise_seeds_by_music_specifier,
        music_specifier,
        ):
        if music_specifier in timewise_seeds_by_music_specifier:
            timewise_seeds_by_music_specifier[music_specifier] += 1
        else:
            timewise_seeds_by_music_specifier[music_specifier] = 0
        return timewise_seeds_by_music_specifier[music_specifier]

    @staticmethod
    def _get_grace_logical_ties(logical_tie):
        logical_ties = []
        head = logical_tie.head
        previous_leaf = inspect_(head).get_leaf(-1)
        if previous_leaf is None:
            return logical_ties
        grace_containers = inspect_(previous_leaf).get_grace_containers(
            'after')
        if grace_containers:
            grace_container = grace_containers[0]
            for logical_tie in iterate(grace_container).by_logical_tie(
                pitched=True,
                ):
                logical_ties.append(logical_tie)
        return logical_ties

    @staticmethod
    def _get_instrument(logical_tie):
        component = logical_tie.head
        prototype = instrumenttools.Instrument
        instrument = inspect_(component).get_effective(prototype)
        return instrument

    @staticmethod
    def _get_phrase_seed(
        attack_point_signature,
        music_specifier,
        phrase_seeds,
        voice,
        ):
        if attack_point_signature.is_first_of_phrase:
            if (voice, music_specifier) not in phrase_seeds:
                phrase_seed = (music_specifier.seed or 0) - 1
                phrase_seeds[(voice, music_specifier)] = phrase_seed
            phrase_seeds[(voice, music_specifier)] += 1
        phrase_seed = phrase_seeds[(voice, music_specifier)]
        return phrase_seed

    def _get_pitch_choices(
        self,
        logical_tie,
        music_specifier,
        pitch_choice_timespans_by_music_specifier,
        segment_duration,
        ):
        if music_specifier not in pitch_choice_timespans_by_music_specifier:
            pitch_handler = music_specifier.pitch_handler
            pitch_specifier = pitch_handler.pitch_specifier
            operation_specifier = pitch_handler.pitch_operation_specifier
            pitch_choice_timespans = PitchHandler.get_pitch_choice_timespans(
                pitch_specifier=pitch_specifier,
                operation_specifier=operation_specifier,
                duration=segment_duration,
                )
            pitch_choice_timespans_by_music_specifier[music_specifier] = \
                pitch_choice_timespans
        timespans = pitch_choice_timespans_by_music_specifier[
            music_specifier]
        assert len(timespans)
        start_offset = logical_tie.get_timespan().start_offset
        # TODO: "overlapping" should include "starting at"
        found_timespans = \
            timespans.find_timespans_overlapping_offset(start_offset)
        found_timespans += \
            timespans.find_timespans_starting_at(start_offset)
        timespan = found_timespans[0]
        pitch_choices = timespan.annotation
        return pitch_choices

    @staticmethod
    def _get_pitch_range(
        instrument,
        logical_tie,
        ):
        prototype = pitchtools.PitchRange
        component = logical_tie.head
        pitch_range = inspect_(component).get_effective(prototype)
        if pitch_range is None and instrument is not None:
            pitch_range = instrument.pitch_range
        return pitch_range

    @staticmethod
    def _get_previous_pitch(
        music_specifier,
        previous_pitch_by_music_specifier,
        voice,
        ):
        key = (voice, music_specifier)
        if key not in previous_pitch_by_music_specifier:
            previous_pitch_by_music_specifier[key] = None
        previous_pitch = previous_pitch_by_music_specifier[key]
        return previous_pitch

    @staticmethod
    def _get_pitch_seed(
        attack_point_signature,
        music_specifier,
        pitch_application_rate,
        pitch_seeds_by_music_specifier,
        pitch_seeds_by_voice,
        voice,
        ):
        if music_specifier not in pitch_seeds_by_music_specifier:
            seed = (music_specifier.seed or 0) - 1
            pitch_seeds_by_music_specifier[music_specifier] = seed
            pitch_seeds_by_voice[voice] = seed
        if pitch_application_rate == 'phrase':
            if attack_point_signature.is_first_of_phrase:
                pitch_seeds_by_music_specifier[music_specifier] += 1
                seed = pitch_seeds_by_music_specifier[music_specifier]
                pitch_seeds_by_voice[voice] = seed
            else:
                seed = pitch_seeds_by_voice[voice]
        elif pitch_application_rate == 'division':
            if attack_point_signature.is_first_of_division:
                pitch_seeds_by_music_specifier[music_specifier] += 1
                seed = pitch_seeds_by_music_specifier[music_specifier]
                pitch_seeds_by_voice[voice] = seed
            else:
                seed = pitch_seeds_by_voice[voice]
        else:
            pitch_seeds_by_music_specifier[music_specifier] += 1
            seed = pitch_seeds_by_music_specifier[music_specifier]
        return seed

    @staticmethod
    def _get_transposition(
        instrument,
        music_specifier,
        ):
        transposition = pitchtools.NumberedInterval(0)
        if not music_specifier.pitches_are_nonsemantic and \
            instrument is not None:
            sounding_pitch = instrument.sounding_pitch_of_written_middle_c
            transposition = sounding_pitch - pitchtools.NamedPitch("c'")
            transposition = pitchtools.NumberedInterval(transposition)
        return transposition

    def _initialize_deviations(self, deviations):
        if deviations is not None:
            if not isinstance(deviations, collections.Sequence):
                deviations = (deviations,)
            assert len(deviations)
            deviations = (pitchtools.NumberedInterval(_) for _ in deviations)
            deviations = datastructuretools.CyclicTuple(deviations)
        self._deviations = deviations

    def _initialize_forbid_repetitions(self, forbid_repetitions):
        if forbid_repetitions is not None:
            forbid_repetitions = bool(forbid_repetitions)
        self._forbid_repetitions = forbid_repetitions

    def _initialize_grace_expressions(self, grace_expressions):
        import consort
        if grace_expressions is not None:
            prototype = consort.LogicalTieExpression
            assert grace_expressions, grace_expressions
            assert all(isinstance(_, prototype)
                for _ in grace_expressions), \
                grace_expressions
            grace_expressions = datastructuretools.CyclicTuple(
                grace_expressions,
                )
        self._grace_expressions = grace_expressions

    def _initialize_logical_tie_expressions(self, logical_tie_expressions):
        import consort
        if logical_tie_expressions is not None:
            prototype = consort.LogicalTieExpression
            assert logical_tie_expressions, logical_tie_expressions
            assert all(isinstance(_, prototype)
                for _ in logical_tie_expressions), \
                logical_tie_expressions
            logical_tie_expressions = datastructuretools.CyclicTuple(
                logical_tie_expressions,
                )
        self._logical_tie_expressions = logical_tie_expressions

    def _initialize_pitch_application_rate(self, pitch_application_rate):
        assert pitch_application_rate in (
            None, 'logical_tie', 'division', 'phrase',
            )
        self._pitch_application_rate = pitch_application_rate

    def _initialize_pitch_operation_specifier(self, pitch_operation_specifier):
        import consort
        if pitch_operation_specifier is not None:
            prototype = consort.PitchOperationSpecifier
            assert isinstance(pitch_operation_specifier, prototype)
        self._pitch_operation_specifier = pitch_operation_specifier

    def _initialize_pitch_specifier(self, pitch_specifier):
        import consort
        if pitch_specifier is not None:
            if not isinstance(pitch_specifier, consort.PitchSpecifier):
                pitch_specifier = consort.PitchSpecifier(pitch_specifier)
        self._pitch_specifier = pitch_specifier

    def _process_logical_tie(self, logical_tie, pitch, pitch_range, seed):
        for leaf in logical_tie:
            leaf.written_pitch = pitch
        grace_logical_ties = self._get_grace_logical_ties(logical_tie)
        if str(pitch.accidental) and grace_logical_ties:
            leaf.note_head.is_forced = True
        self._apply_logical_tie_expression(
            logical_tie,
            seed=seed,
            pitch_range=pitch_range,
            )
        for i, grace_logical_tie in enumerate(grace_logical_ties, seed):
            for leaf in grace_logical_tie:
                leaf.written_pitch = pitch
            if self.grace_expressions:
                grace_expression = self.grace_expressions[i]
                grace_expression(grace_logical_tie)

    @staticmethod
    def _process_session(segment_session):
        import consort
        maker = consort.SegmentMaker
        segment_duration = segment_session.measure_offsets[-1]
        attack_point_map = segment_session.attack_point_map
        pitch_choice_timespans_by_music_specifier = {}
        previous_pitch_by_music_specifier = {}
        seed_session = consort.SeedSession()
        for logical_tie in attack_point_map:
            music_specifier = maker.logical_tie_to_music_specifier(logical_tie)
            if not music_specifier or not music_specifier.pitch_handler:
                continue
            pitch_handler = music_specifier.pitch_handler
            attack_point_signature = attack_point_map[logical_tie]
            application_rate = pitch_handler.pitch_application_rate
            voice = consort.SegmentMaker.logical_tie_to_voice(logical_tie)
            seed_session(
                application_rate,
                attack_point_signature,
                music_specifier,
                voice,
                )
            previous_pitch = pitch_handler._get_previous_pitch(
                music_specifier,
                previous_pitch_by_music_specifier,
                voice,
                )
            pitch_choices = pitch_handler._get_pitch_choices(
                logical_tie,
                music_specifier,
                pitch_choice_timespans_by_music_specifier,
                segment_duration,
                )
#            instrument = PitchHandler._get_instrument(logical_tie)
#            transposition = PitchHandler._get_transposition(
#                instrument,
#                music_specifier,
#                )
            previous_pitch = pitch_handler(
                attack_point_signature,
                logical_tie,
                pitch_choices,
                previous_pitch,
                seed_session,
                )
            pitch_handler._set_previous_pitch(
                attack_point_signature,
                music_specifier,
                previous_pitch,
                pitch_handler.pitch_application_rate,
                previous_pitch_by_music_specifier,
                voice,
                )

    @staticmethod
    def _set_previous_pitch(
        attack_point_signature,
        music_specifier,
        pitch,
        pitch_application_rate,
        previous_pitch_by_music_specifier,
        voice,
        ):
        key = (voice, music_specifier)
        if pitch_application_rate == 'phrase':
            if attack_point_signature.is_first_of_phrase:
                previous_pitch_by_music_specifier[key] = pitch
        elif pitch_application_rate == 'division':
            if attack_point_signature.is_first_of_division:
                previous_pitch_by_music_specifier[key] = pitch
        else:
            previous_pitch_by_music_specifier[key] = pitch

    ### PUBLIC METHODS ###

    @staticmethod
    def get_pitch_choice_timespans(
        pitch_specifier=None,
        operation_specifier=None,
        duration=1,
        ):
        r'''Get pitch expression timespans.

        ::

            >>> import consort
            >>> pitch_specifier = consort.PitchSpecifier(
            ...     pitch_segments=(
            ...         "c' e' g'",
            ...         "fs' g' a'",
            ...         "b d",
            ...         ),
            ...     ratio=(1, 2, 3),
            ...     )
            >>> operation_specifier = consort.PitchOperationSpecifier(
            ...     pitch_operations=(
            ...         consort.PitchOperation((
            ...             pitchtools.Rotation(1),
            ...             pitchtools.Transposition(1),
            ...             )),
            ...         None,
            ...         consort.PitchOperation((
            ...             pitchtools.Rotation(-1),
            ...             pitchtools.Transposition(-1),
            ...             ))
            ...         ),
            ...     ratio=(1, 2, 1),
            ...     )
            >>> timespans = consort.PitchHandler.get_pitch_choice_timespans(
            ...     pitch_specifier=pitch_specifier,
            ...     operation_specifier=operation_specifier,
            ...     duration=12,
            ...     )
            >>> print(format(timespans))
            supriya.tools.timetools.TimespanCollection(
                [
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(2, 1),
                        annotation=datastructuretools.CyclicTuple(
                            [
                                pitchtools.NamedPitch("df'"),
                                pitchtools.NamedPitch('gf'),
                                pitchtools.NamedPitch('bf'),
                                ]
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(2, 1),
                        stop_offset=durationtools.Offset(3, 1),
                        annotation=datastructuretools.CyclicTuple(
                            [
                                pitchtools.NamedPitch("g'"),
                                pitchtools.NamedPitch("e'"),
                                pitchtools.NamedPitch("f'"),
                                ]
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(3, 1),
                        stop_offset=durationtools.Offset(6, 1),
                        annotation=datastructuretools.CyclicTuple(
                            [
                                pitchtools.NamedPitch("fs'"),
                                pitchtools.NamedPitch("g'"),
                                pitchtools.NamedPitch("a'"),
                                ]
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(6, 1),
                        stop_offset=durationtools.Offset(9, 1),
                        annotation=datastructuretools.CyclicTuple(
                            [
                                pitchtools.NamedPitch('b'),
                                pitchtools.NamedPitch('d'),
                                ]
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(9, 1),
                        stop_offset=durationtools.Offset(12, 1),
                        annotation=datastructuretools.CyclicTuple(
                            [
                                pitchtools.NamedPitch('as'),
                                pitchtools.NamedPitch("fss'"),
                                ]
                            ),
                        ),
                    ]
                )

        Returns timespans.
        '''
        import consort
        duration = durationtools.Duration(duration)
        pitch_specifier = pitch_specifier or consort.PitchSpecifier()
        operation_specifier = operation_specifier or \
            consort.PitchOperationSpecifier()
        pitch_choice_timespans = timetools.TimespanCollection()
        pitch_timespans = pitch_specifier.get_timespans(duration)
        operation_timespans = operation_specifier.get_timespans(duration)
        offsets = set()
        offsets.update(pitch_timespans.all_offsets)
        offsets.update(operation_timespans.all_offsets)
        offsets = tuple(sorted(offsets))
        for start_offset, stop_offset in sequencetools.iterate_sequence_nwise(
            offsets):
            timespan = timespantools.Timespan(
                start_offset=start_offset,
                stop_offset=stop_offset,
                )
            pitch_timespan = \
                pitch_timespans.find_timespans_intersecting_timespan(
                    timespan)[0]
            pitches = pitch_timespan.annotation
            operation_timespan = \
                operation_timespans.find_timespans_intersecting_timespan(
                    timespan)[0]
            operation = operation_timespan.annotation
            if operation is not None:
                pitches = operation(pitches)
            pitches = datastructuretools.CyclicTuple(pitches)
            pitch_choice_timespan = timespantools.AnnotatedTimespan(
                annotation=pitches,
                start_offset=start_offset,
                stop_offset=stop_offset,
                )
            pitch_choice_timespans.insert(pitch_choice_timespan)
        return pitch_choice_timespans

    ### PUBLIC PROPERTIES ###

    @property
    def deviations(self):
        return self._deviations

    @property
    def forbid_repetitions(self):
        return self._forbid_repetitions

    @property
    def grace_expressions(self):
        return self._grace_expressions

    @property
    def logical_tie_expressions(self):
        return self._logical_tie_expressions

    @property
    def pitch_application_rate(self):
        return self._pitch_application_rate

    @property
    def pitch_operation_specifier(self):
        return self._pitch_operation_specifier

    @property
    def pitch_specifier(self):
        return self._pitch_specifier