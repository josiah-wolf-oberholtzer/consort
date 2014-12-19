# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from consort.tools.PitchHandler import PitchHandler


class AbsolutePitchHandler(PitchHandler):
    r'''Absolute pitch maker.

    ::

        >>> import consort
        >>> pitch_handler = consort.AbsolutePitchHandler(
        ...     pitches="c' d' e' f'",
        ...     )
        >>> print(format(pitch_handler))
        consort.tools.AbsolutePitchHandler(
            pitches=datastructuretools.CyclicTuple(
                [
                    pitchtools.NamedPitch("c'"),
                    pitchtools.NamedPitch("d'"),
                    pitchtools.NamedPitch("e'"),
                    pitchtools.NamedPitch("f'"),
                    ]
                ),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_pitches',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        forbid_repetitions=None,
        grace_expressions=None,
        logical_tie_expressions=None,
        pitch_application_rate=None,
        pitches=None,
        transform_stack=None,
        ):
        PitchHandler.__init__(
            self,
            forbid_repetitions=forbid_repetitions,
            grace_expressions=grace_expressions,
            logical_tie_expressions=logical_tie_expressions,
            pitch_application_rate=pitch_application_rate,
            transform_stack=transform_stack,
            )
        self._initialize_pitches(pitches)

    ### SPECIAL METHODS ###

    def __call__(
        self,
        attack_point_signature,
        logical_tie,
        phrase_seed,
        pitch_expr_timespans,
        pitch_range,
        previous_pitch,
        seed,
        transposition,
        ):
        pitch = self._get_pitch(previous_pitch, seed)
        self._process_logical_tie(logical_tie, pitch, pitch_range, seed)
        return pitch

    ### PRIVATE METHODS ###

    def _get_pitch(
        self,
        previous_pitch,
        seed,
        ):
        pitches = self.pitches
        if not pitches:
            pitch = pitchtools.NamedPitch("c'")
        else:
            pitch = pitches[seed]
        if self.transform_stack:
            for transform in self.transform_stack:
                pitch = transform(pitch)
        if self.pitches and 1 < len(set(pitches)) and self.forbid_repetitions:
            while pitch == previous_pitch:
                seed += 1
                pitch = pitches[seed]
                if self.transform_stack:
                    for transform in self.transform_stack:
                        pitch = transform(pitch)
        return pitch

    def _initialize_pitches(self, pitches):
        if pitches is not None:
            if not isinstance(pitches, collections.Sequence):
                pitches = (pitches,)
            pitches = pitchtools.PitchSegment(pitches)
            pitches = datastructuretools.CyclicTuple(pitches)
        self._pitches = pitches

    ### PUBLIC METHODS ###

    def get_pitch_expr_timespans(self, stop_offset):
        import consort
        transform_specifier = self._transform_specifier or \
            consort.TransformSpecifier
        pitch_expr = self._pitches
        pitch_expr_timespans = transform_specifier.get_pitch_expr_timespans(
            pitch_expr)
        return pitch_expr_timespans

    ### PUBLIC PROPERTIES ###

    @property
    def pitches(self):
        return self._pitches