# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from consort.makers.PitchHandler import PitchHandler


class AbsolutePitchHandler(PitchHandler):
    r'''Absolute pitch maker.

    ::

        >>> from consort import makers
        >>> pitch_handler = makers.AbsolutePitchHandler(
        ...     pitches="c' d' e' f'",
        ...     )
        >>> print(format(pitch_handler))
        consort.makers.AbsolutePitchHandler(
            allow_repetition=False,
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
        allow_repetition=None,
        chord_expressions=None,
        pitch_application_rate=None,
        pitches=None,
        transform_stack=None,
        ):
        PitchHandler.__init__(
            self,
            allow_repetition=allow_repetition,
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

    ### PRIVATE METHODS ###

    def _process_logical_tie(
        self,
        logical_tie,
        pitch_range=None,
        previous_pitch=None,
        music_index=0,
        logical_tie_index=0,
        ):
        seed = music_index + logical_tie_index
        pitches = self.pitches
        if not pitches:
            pitch = pitchtools.NamedPitch("c'")
        else:
            pitch = pitches[seed]
        if self.transform_stack:
            for transform in self.transform_stack:
                pitch = transform(pitch)
        for i, leaf in enumerate(logical_tie):
            leaf.written_pitch = pitch
        self._apply_chord_expression(
            logical_tie,
            seed=seed,
            pitch_range=pitch_range,
            )
        return pitch

    ### PUBLIC PROPERTIES ###

    @property
    def pitches(self):
        return self._pitches