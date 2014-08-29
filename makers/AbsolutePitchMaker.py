# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from consort.makers.PitchMaker import PitchMaker


class AbsolutePitchMaker(PitchMaker):
    r'''Absolute pitch maker.

    ::

        >>> from consort import makers
        >>> pitch_maker = makers.AbsolutePitchMaker(
        ...     pitches="c' d' e' f'",
        ...     )
        >>> print(format(pitch_maker))
        consort.makers.AbsolutePitchMaker(
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
        pitches=None,
        ):
        PitchMaker.__init__(
            self,
            allow_repetition=allow_repetition,
            chord_expressions=chord_expressions
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
        for i, leaf in enumerate(logical_tie):
            leaf.written_pitch = pitch
        self._apply_chord_expression(
            logical_tie,
            seed=seed,
            )
        return pitch

    ### PUBLIC PROPERTIES ###

    @property
    def pitches(self):
        return self._pitches