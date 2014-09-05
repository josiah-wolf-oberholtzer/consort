# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import instrumenttools
from abjad.tools import pitchtools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class PitchMaker(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_allow_repetition',
        '_chord_expressions',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        allow_repetition=False,
        chord_expressions=None,
        ):
        from consort import makers
        self._allow_repetition = bool(allow_repetition)
        if chord_expressions is not None:
            prototype = (
                makers.ChordExpression,
                makers.KeyClusterExpression,
                )
            assert chord_expressions
            assert all(isinstance(x, prototype) for x in chord_expressions)
            chord_expressions = datastructuretools.CyclicTuple(
                chord_expressions,
                )
        self._chord_expressions = chord_expressions

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        music_index=0,
        ):
        pitch_range = inspect_(music).get_effective(pitchtools.PitchRange)
        if pitch_range is None:
            instrument = inspect_(music).get_effective(
                instrumenttools.Instrument)
            if instrument is not None:
                pitch_range = instrument.pitch_range
        previous_pitch = None
        iterator = iterate(music).by_logical_tie(pitched=True)
        for logical_tie_index, logical_tie in enumerate(iterator):
            previous_pitch = self._process_logical_tie(
                logical_tie,
                previous_pitch=previous_pitch,
                pitch_range=pitch_range,
                music_index=music_index,
                logical_tie_index=logical_tie_index,
                )

    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            if format(self) == format(expr):
                return True
        return False

    def __hash__(self):
        hash_values = (type(self), format(self))
        return hash(hash_values)

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

    ### PUBLIC PROPERTIES ###

    @property
    def allow_repetition(self):
        return self._allow_repetition

    @property
    def chord_expressions(self):
        return self._chord_expressions