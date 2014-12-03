# -*- encoding: utf-8 -*-
from __future__ import print_function
import abc
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import instrumenttools
from abjad.tools import pitchtools
from abjad.tools import systemtools
from abjad.tools.topleveltools import inspect_


class PitchHandler(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_chord_expressions',
        '_forbid_repetitions',
        '_hash',
        '_pitch_application_rate',
        '_transform_stack',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        forbid_repetitions=None,
        chord_expressions=None,
        pitch_application_rate=None,
        transform_stack=None,
        ):
        import consort
        if forbid_repetitions is not None:
            forbid_repetitions = bool(forbid_repetitions)
        self._forbid_repetitions = forbid_repetitions
        if chord_expressions is not None:
            prototype = (
                tools.ChordExpression,
                tools.KeyClusterExpression,
                )
            assert chord_expressions
            assert all(isinstance(x, prototype) for x in chord_expressions)
            chord_expressions = datastructuretools.CyclicTuple(
                chord_expressions,
                )
        self._chord_expressions = chord_expressions
        self._hash = None
        assert pitch_application_rate in (
            None, 'logical_tie', 'division', 'phrase',
            )
        self._pitch_application_rate = pitch_application_rate
        if transform_stack is not None:
            prototype = (
                pitchtools.Inversion,
                pitchtools.Multiplication,
                pitchtools.Transposition,
                )
            assert all(isinstance(_, prototype) for _ in transform_stack)
            transform_stack = tuple(transform_stack)
        self._transform_stack = transform_stack

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

    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            if format(self) == format(expr):
                return True
        return False

    def __hash__(self):
        if self._hash is None:
            hash_values = (type(self), format(self))
            self._hash = hash(hash_values)
        return self._hash

    ### PRIVATE METHODS ###

    def _apply_chord_expression(
        self,
        logical_tie,
        pitch_range=None,
        seed=0,
        ):
        if self.chord_expressions:
            chord_expression = self.chord_expressions[seed]
            chord_expression(
                logical_tie,
                pitch_range=pitch_range,
                )

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
                seeds_by_music_specifier[music_specifier] += 1
                seed = seeds_by_music_specifier[music_specifier]
                seeds_by_voice[voice] = seed
            else:
                seed = seeds_by_voice[voice]
        elif pitch_application_rate == 'division':
            if attack_point_signature.is_first_of_division:
                seeds_by_music_specifier[music_specifier] += 1
                seed = seeds_by_music_specifier[music_specifier]
                seeds_by_voice[voice] = seed
            else:
                seed = seeds_by_voice[voice]
        else:
            seeds_by_music_specifier[music_specifier] += 1
            seed = seeds_by_music_specifier[music_specifier]
        return seed

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
                consort.SegmentMaker._logical_tie_to_music_specifier(
                    logical_tie)
            if not music_specifier:
                continue
            pitch_handler = music_specifier.pitch_handler
            if not pitch_handler:
                continue
            voice = consort.SegmentMaker._logical_tie_to_voice(logical_tie)
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
    def chord_expressions(self):
        return self._chord_expressions

    @property
    def forbid_repetitions(self):
        return self._forbid_repetitions

    @property
    def pitch_application_rate(self):
        return self._pitch_application_rate

    @property
    def transform_stack(self):
        return self._transform_stack