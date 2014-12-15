# -*- encoding: utf-8 -*-
from __future__ import print_function
import abc
from abjad import datastructuretools
from abjad import inspect_
from abjad import iterate
from abjad import instrumenttools
from abjad import pitchtools
from consort.tools.HashCachingObject import HashCachingObject


class PitchHandler(HashCachingObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_forbid_repetitions',
        '_grace_logical_tie_expressions',
        '_logical_tie_expressions',
        '_pitch_application_rate',
        '_transform_stack',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        forbid_repetitions=None,
        grace_logical_tie_expressions=None,
        logical_tie_expressions=None,
        pitch_application_rate=None,
        transform_stack=None,
        ):
        HashCachingObject.__init__(self)
        self._initialize_forbid_repetitions(forbid_repetitions)
        self._initialize_grace_logical_tie_expressions(
            grace_logical_tie_expressions)
        self._initialize_logical_tie_expressions(logical_tie_expressions)
        self._initialize_pitch_application_rate(pitch_application_rate)
        self._initialize_transform_stack(transform_stack)

    ### SPECIAL METHODS ###

    @abc.abstractmethod
    def __call__(
        self,
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
        pitch_range=None,
        seed=0,
        ):
        if self.logical_tie_expressions:
            logical_tie_expression = self.logical_tie_expressions[seed]
            logical_tie_expression(
                logical_tie,
                pitch_range=pitch_range,
                )

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

    @staticmethod
    def _get_pitch_range(
        instrument,
        logical_tie,
        ):
        prototype = pitchtools.PitchRange
        component = logical_tie.head
        pitch_range = inspect_(component).get_effective(prototype)
        if pitch_range is None:
            pitch_range = instrument.pitch_range
        return pitch_range

    @staticmethod
    def _get_seed(
        attack_point_signature,
        music_specifier,
        pitch_application_rate,
        seeds_by_music_specifier,
        seeds_by_voice,
        voice,
        ):
        if music_specifier not in seeds_by_music_specifier:
            seed = (music_specifier.seed or 0) - 1
            seeds_by_music_specifier[music_specifier] = seed
            seeds_by_voice[voice] = seed
        if pitch_application_rate == 'phrase':
            if attack_point_signature.is_first_of_phrase:
                seeds_by_music_specifier[music_specifier] -= 1
                seed = seeds_by_music_specifier[music_specifier]
                seeds_by_voice[voice] = seed
            else:
                seed = seeds_by_voice[voice]
        elif pitch_application_rate == 'division':
            if attack_point_signature.is_first_of_division:
                seeds_by_music_specifier[music_specifier] -= 1
                seed = seeds_by_music_specifier[music_specifier]
                seeds_by_voice[voice] = seed
            else:
                seed = seeds_by_voice[voice]
        else:
            seeds_by_music_specifier[music_specifier] -= 1
            seed = seeds_by_music_specifier[music_specifier]
        return seed

    @staticmethod
    def _get_transposition(
        instrument,
        music_specifier,
        ):
        transposition = pitchtools.NumberedInterval(0)
        if not music_specifier.pitches_are_nonsemantic:
            sounding_pitch = instrument.sounding_pitch_of_written_middle_c
            transposition = sounding_pitch - pitchtools.NamedPitch("c'")
            transposition = pitchtools.NumberedInterval(transposition)
        return transposition

    def _initialize_forbid_repetitions(self, forbid_repetitions):
        if forbid_repetitions is not None:
            forbid_repetitions = bool(forbid_repetitions)
        self._forbid_repetitions = forbid_repetitions

    def _initialize_grace_logical_tie_expressions(self,
        grace_logical_tie_expressions):
        import consort
        if grace_logical_tie_expressions is not None:
            prototype = consort.LogicalTieExpression
            assert grace_logical_tie_expressions, grace_logical_tie_expressions
            assert all(isinstance(_, prototype)
                for _ in grace_logical_tie_expressions), \
                grace_logical_tie_expressions
            grace_logical_tie_expressions = datastructuretools.CyclicTuple(
                grace_logical_tie_expressions,
                )
        self._grace_logical_tie_expressions = grace_logical_tie_expressions

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

    def _initialize_transform_stack(self, transform_stack):
        if transform_stack is not None:
            prototype = (
                pitchtools.Inversion,
                pitchtools.Multiplication,
                pitchtools.Transposition,
                )
            assert all(isinstance(_, prototype) for _ in transform_stack), \
                transform_stack
            transform_stack = tuple(transform_stack)
        self._transform_stack = transform_stack

    @staticmethod
    def _process_session(segment_session):
        import consort
        attack_point_map = segment_session.attack_point_map
        previous_pitch_by_music_specifier = {}
        seeds_by_music_specifier = {}
        seeds_by_voice = {}
        phrase_seeds = {}
        for logical_tie in attack_point_map:
            attack_point_signature = attack_point_map[logical_tie]
            music_specifier = \
                consort.SegmentMaker.logical_tie_to_music_specifier(
                    logical_tie)
            if not music_specifier:
                continue
            pitch_handler = music_specifier.pitch_handler
            if not pitch_handler:
                continue
            voice = consort.SegmentMaker.logical_tie_to_voice(logical_tie)
            phrase_seed = PitchHandler._get_phrase_seed(
                attack_point_signature,
                music_specifier,
                phrase_seeds,
                voice,
                )
            seed = PitchHandler._get_seed(
                attack_point_signature,
                music_specifier,
                pitch_handler.pitch_application_rate,
                seeds_by_music_specifier,
                seeds_by_voice,
                voice,
                )
            instrument = PitchHandler._get_instrument(logical_tie)
            transposition = PitchHandler._get_transposition(
                instrument,
                music_specifier,
                )
            pitch_range = PitchHandler._get_pitch_range(
                instrument,
                logical_tie,
                )
            if music_specifier not in previous_pitch_by_music_specifier:
                previous_pitch_by_music_specifier[music_specifier] = None
            previous_pitch = previous_pitch_by_music_specifier[music_specifier]
            previous_pitch_by_music_specifier[music_specifier] = pitch_handler(
                attack_point_signature,
                logical_tie,
                phrase_seed,
                pitch_range,
                previous_pitch,
                seed,
                transposition,
                )

    ### PUBLIC PROPERTIES ###

    @property
    def forbid_repetitions(self):
        return self._forbid_repetitions

    @property
    def grace_logical_tie_expressions(self):
        return self._grace_logical_tie_expressions

    @property
    def logical_tie_expressions(self):
        return self._logical_tie_expressions

    @property
    def pitch_application_rate(self):
        return self._pitch_application_rate

    @property
    def transform_stack(self):
        return self._transform_stack