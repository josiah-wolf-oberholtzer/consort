# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import indicatortools
from abjad.tools import instrumenttools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class PitchHandler(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_allow_repetition',
        '_chord_expressions',
        '_pitch_application_rate',
        '_transform_stack',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        allow_repetition=False,
        chord_expressions=None,
        pitch_application_rate=None,
        transform_stack=None,
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

    def __call__(
        self,
        music,
        music_index=0,
        ):
        from consort import makers
        music_specifier = inspect_(music).get_indicator(makers.MusicSpecifier)
        instrument = inspect_(music).get_effective(instrumenttools.Instrument)
        if not music_specifier.pitches_are_nonsemantic:
            pitch = instrument.sounding_pitch_of_written_middle_c
            if pitch != pitchtools.NamedPitch("c'"):
                command = indicatortools.LilyPondCommand(
                    r"transpose {} c'".format(pitch),
                    'before',
                    )
                attach(command, music)
        pitch_range = inspect_(music).get_effective(pitchtools.PitchRange)
        if pitch_range is None:
            pitch_range = instrument.pitch_range
        divisions = [_ for _ in music]
        division_index = 0
        previous_pitch = None
        iterator = iterate(music).by_logical_tie(pitched=True)
        for logical_tie_index, logical_tie in enumerate(iterator):
            parentage = inspect_(logical_tie.head).get_parentage()
            for x in parentage:
                if x in divisions:
                    division_index = divisions.index(x)
                    break
            if self.pitch_application_rate == 'division':
                logical_tie_index = division_index
            elif self.pitch_application_rate == 'phrase':
                logical_tie_index = 0
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

    @staticmethod
    def _process_session(score):
        from consort import makers
        counter = collections.Counter()
        for voice in iterate(score).by_class(scoretools.Voice):
            for container in voice:
                prototype = makers.MusicSpecifier
                music_specifier = inspect_(container).get_effective(prototype)
                maker = music_specifier.pitch_handler
                if maker is None:
                    continue
                if music_specifier not in counter:
                    seed = music_specifier.seed or 0
                    counter[music_specifier] = seed
                seed = counter[music_specifier]
                maker(container, music_index=seed)
                counter[music_specifier] += 1

    ### PUBLIC PROPERTIES ###

    @property
    def allow_repetition(self):
        return self._allow_repetition

    @property
    def chord_expressions(self):
        return self._chord_expressions

    @property
    def pitch_application_rate(self):
        return self._pitch_application_rate

    @property
    def transform_stack(self):
        return self._transform_stack