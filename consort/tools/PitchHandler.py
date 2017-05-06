# -*- encoding: utf-8 -*-
from __future__ import print_function
import abc
import collections
from abjad import attach
from abjad import inspect_
from abjad import iterate
from abjad import new
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import instrumenttools
from abjad.tools import indicatortools
from abjad.tools import pitchtools
from abjad.tools import timespantools
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
        '_pitches_are_nonsemantic',
        '_use_self_as_seed_key',
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
        pitches_are_nonsemantic=None,
        use_self_as_seed_key=None,
        ):
        HashCachingObject.__init__(self)
        self._initialize_deviations(deviations)
        self._initialize_forbid_repetitions(forbid_repetitions)
        self._initialize_grace_expressions(grace_expressions)
        self._initialize_logical_tie_expressions(logical_tie_expressions)
        self._initialize_pitch_application_rate(pitch_application_rate)
        self._initialize_pitch_specifier(pitch_specifier)
        self._initialize_pitch_operation_specifier(pitch_operation_specifier)
        if pitches_are_nonsemantic is not None:
            pitches_are_nonsemantic = bool(pitches_are_nonsemantic)
        self._pitches_are_nonsemantic = pitches_are_nonsemantic
        if use_self_as_seed_key is not None:
            use_self_as_seed_key = bool(use_self_as_seed_key)
        self._use_self_as_seed_key = use_self_as_seed_key

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
            if logical_tie_expression is not None:
                logical_tie_expression(
                    logical_tie,
                    pitch_range=pitch_range,
                    )

    def _apply_deviation(
        self,
        pitch,
        seed,
        ):
        if self.deviations:
            deviation = self.deviations[seed]
            if isinstance(deviation, pitchtools.NumberedInterval):
                if deviation != 0:
                    pitch = pitchtools.NumberedPitch(pitch)
                    pitch = pitch.transpose(deviation)
                    pitch = pitchtools.NamedPitch(pitch)
            elif isinstance(deviation, pitchtools.NamedInterval):
                pitch = pitch.transpose(deviation)
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
    def _get_instrument(logical_tie, music_specifier):
        if music_specifier.instrument is not None:
            return music_specifier.instrument
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
    def _get_sounding_pitch(
        instrument,
        pitch_handler,
        ):
        if not instrument:
            return pitchtools.NamedPitch("c'")
        sounding_pitch = instrument.sounding_pitch_of_written_middle_c
        transposition_is_non_octave = sounding_pitch.named_pitch_class != \
            pitchtools.NamedPitchClass('c')
        if transposition_is_non_octave:
            if pitch_handler.pitches_are_nonsemantic:
                return pitchtools.NamedPitch("c'")
            return sounding_pitch
        return None

    def _initialize_deviations(self, deviations):
        if deviations is not None:
            if not isinstance(deviations, collections.Sequence):
                deviations = (deviations,)
            assert len(deviations)
            intervals = []
            for interval in deviations:
                if isinstance(interval, (int, float)):
                    interval = pitchtools.NumberedInterval(interval)
                elif isinstance(interval, str):
                    interval = pitchtools.NamedInterval(interval)
                elif isinstance(interval, pitchtools.Interval):
                    pass
                else:
                    interval = pitchtools.NumberedInterval(interval)
                intervals.append(interval)
            deviations = datastructuretools.CyclicTuple(intervals)
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
        if logical_tie_expressions:
            prototype = (consort.LogicalTieExpression, type(None))
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
            if not isinstance(pitch_operation_specifier, prototype):
                pitch_operation_specifier = consort.PitchOperationSpecifier(
                    pitch_operations=pitch_operation_specifier,
                    )
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
    def _process_session(segment_maker):
        import consort
        maker = consort.SegmentMaker
        segment_duration = segment_maker.measure_offsets[-1]
        attack_point_map = segment_maker.attack_point_map
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
            seed_key = music_specifier
            if pitch_handler.use_self_as_seed_key:
                seed_key = pitch_handler
            seed_session(
                application_rate,
                attack_point_signature,
                seed_key,
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
            pitch = pitch_handler(
                attack_point_signature,
                logical_tie,
                music_specifier,
                pitch_choices,
                previous_pitch,
                seed_session,
                )
            if pitch.accidental.abbreviation in ('ss', 'ff'):
                pitch = pitchtools.NamedPitch(float(pitch))
            pitch_handler._set_previous_pitch(
                attack_point_signature,
                music_specifier,
                pitch,
                pitch_handler.pitch_application_rate,
                previous_pitch_by_music_specifier,
                voice,
                )
            pitch_handler._apply_transposition(
                attack_point_signature,
                logical_tie,
                music_specifier,
                pitch_handler,
                )
            instrument = pitch_handler._get_instrument(
                logical_tie,
                music_specifier,
                )
            pitch_range = pitch_handler._get_pitch_range(
                instrument,
                logical_tie,
                )
            pitch_handler._process_logical_tie(
                logical_tie,
                pitch,
                pitch_range,
                seed_session.current_unphrased_voicewise_logical_tie_seed,
                )

    @staticmethod
    def _apply_transposition(
        attack_point_signature,
        logical_tie,
        music_specifier,
        pitch_handler,
        ):
        import consort
        if not attack_point_signature.is_first_of_phrase:
            return
        voice = consort.SegmentMaker.logical_tie_to_voice(logical_tie)
        instrument = PitchHandler._get_instrument(
            logical_tie, music_specifier)
        sounding_pitch = PitchHandler._get_sounding_pitch(
            instrument, pitch_handler)
        if pitch_handler and pitch_handler.pitches_are_nonsemantic:
            sounding_pitch = pitchtools.NamedPitch('C4')
        if sounding_pitch is None:
            sounding_pitch = pitchtools.NamedPitch('C4')
        if sounding_pitch == pitchtools.NamedPitch('C4'):
            return
        phrase = consort.SegmentMaker.logical_tie_to_phrase(logical_tie)
        transposition_command = indicatortools.LilyPondCommand(
            "transpose {!s} c'".format(sounding_pitch),
            format_slot='before',
            )
        print(
            '        transposing',
            voice.name,
            voice.index(phrase),
            sounding_pitch,
            )
        attach(transposition_command, phrase)

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
            ...         pitchtools.CompoundOperator((
            ...             pitchtools.Rotation(1, stravinsky=True),
            ...             pitchtools.Transposition(1),
            ...             )),
            ...         None,
            ...         pitchtools.CompoundOperator((
            ...             pitchtools.Rotation(-1, stravinsky=True),
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
            consort.tools.TimespanCollection(
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
        pitch_choice_timespans = consort.TimespanCollection()
        pitch_timespans = pitch_specifier.get_timespans(duration)
        operation_timespans = operation_specifier.get_timespans(duration)
        offsets = set()
        offsets.update(pitch_timespans.all_offsets)
        offsets.update(operation_timespans.all_offsets)
        offsets = tuple(sorted(offsets))
        for start_offset, stop_offset in consort.iterate_nwise(offsets):
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

    def transpose(self, expr):
        import consort
        pitch_specifier = self.pitch_specifier or consort.PitchSpecifier(
            pitch_segments='C4',
            )
        pitch_specifier = pitch_specifier.transpose(expr)
        return new(self, pitch_specifier=pitch_specifier)

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

    @property
    def pitches_are_nonsemantic(self):
        return self._pitches_are_nonsemantic

    @property
    def use_self_as_seed_key(self):
        return self._use_self_as_seed_key
