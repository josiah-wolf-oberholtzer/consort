# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import detach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import mutate
from consort.makers.PitchMaker import PitchMaker


class NonsemanticPitchMaker(PitchMaker):

    ### CLASS VARIABLES ###

    __slots__ = (
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
        indices = range(grouping, seed)
        pitches = [self.pitches[x] for x in indices]
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