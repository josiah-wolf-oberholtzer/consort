# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from consort.tools.pitchtools.PitchHandler import PitchHandler


class AbsolutePitchHandler(PitchHandler):
    r'''Absolute pitch maker.

    ::

        >>> from consort.tools import pitchtools
        >>> pitch_handler = pitchtools.AbsolutePitchHandler(
        ...     pitches="c' d' e' f'",
        ...     )
        >>> print(format(pitch_handler))
        consort.tools.pitchtools.AbsolutePitchHandler(
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
        chord_expressions=None,
        pitch_application_rate=None,
        pitches=None,
        transform_stack=None,
        ):
        PitchHandler.__init__(
            self,
            forbid_repetitions=forbid_repetitions,
            chord_expressions=chord_expressions,
            pitch_application_rate=pitch_application_rate,
            transform_stack=transform_stack,
            )
        if pitches is not None:
            if not isinstance(pitches, collections.Sequence):
                pitches = (pitches,)
            pitches = pitchtools.PitchSegment(pitches)
            pitches = datastructuretools.CyclicTuple(pitches)
        self._pitches = pitches

    ### SPECIAL METHODS ###

    def __call__(
        self,
        attack_point_signature,
        logical_tie,
        phrase_seed,
        pitch_range,
        previous_pitch,
        seed,
        transposition,
        ):
        pitch = self._get_pitch(
            previous_pitch,
            seed,
            )
        for i, leaf in enumerate(logical_tie):
            leaf.written_pitch = pitch
        self._apply_chord_expression(
            logical_tie,
            seed=seed,
            pitch_range=pitch_range,
            )
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

    ### PUBLIC PROPERTIES ###

    @property
    def pitches(self):
        return self._pitches