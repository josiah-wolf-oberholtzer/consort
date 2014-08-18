# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import detach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import mutate
from consort.makers.PitchMaker import PitchMaker


class AbsolutePitchMaker(PitchMaker):
    r'''Absolute pitch maker.

    ::

        >>> from consort import makers
        >>> pitch_maker = makers.AbsolutePitchMaker(
        ...     groupings=(2, 1, 1, 1),
        ...     pitches="c' d' e' f'",
        ...     )
        >>> print(format(pitch_maker))
        consort.makers.AbsolutePitchMaker(
            allow_repetition=False,
            groupings=(2, 1, 1, 1),
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
        '_groupings',
        '_pitches',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        allow_repetition=None,
        groupings=None,
        pitches=None,
        ):
        PitchMaker.__init__(
            self,
            allow_repetition=allow_repetition,
            )
        groupings = groupings or (1,)
        groupings = tuple(int(x) for x in groupings)
        assert all(0 < x for x in groupings)
        self._groupings = groupings
        pitches = pitchtools.PitchSegment(pitches)
        assert pitches
        pitches = datastructuretools.CyclicTuple(pitches)
        self._pitches = pitches

    ### PRIVATE METHODS ###

    def _process_logical_tie(
        self,
        logical_tie,
        seed=0,
        ):
        grouping = self._groupings[seed]
        pitches = self.pitches[seed:seed + grouping]
        pitches = pitchtools.PitchSet(pitches)
        for i, leaf in enumerate(logical_tie):
            chord = scoretools.Chord(leaf)
            chord.written_pitches = pitches
            grace_containers = inspect_(leaf).get_grace_containers('after')
            if grace_containers:
                old_grace_container = grace_containers[0]
                grace_notes = old_grace_container.select_leaves()
                detach(scoretools.GraceContainer, leaf)
            mutate(leaf).replace(chord)
            if grace_containers:
                new_grace_container = scoretools.GraceContainer(
                    grace_notes,
                    kind='after',
                    )
                attach(new_grace_container, chord)

    ### PUBLIC PROPERTIES ###

    @property
    def groupings(self):
        return self._groupings

    @property
    def pitches(self):
        return self._pitches