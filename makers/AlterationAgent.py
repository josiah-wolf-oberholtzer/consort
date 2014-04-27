# -*- encoding: utf-8 -*-
import collections
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import mathtools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools import sequencetools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import new


class AlterationAgent(ConsortObject):
    r'''An alteration agent.

    ::

        >>> from consort import makers
        >>> alteration_agent = makers.AlterationAgent()
        >>> print(format(alteration_agent))
        makers.AlterationAgent()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_alterations',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        alterations=None,
        ):
        if alterations is not None:
            assert len(alterations)
            assert mathtools.all_are_nonnegative_integer_equivalent_numbers(
                alterations)
            alterations = tuple(int(x) for x in alterations)
            alterations = sequencetools.Sequence(*alterations)
        self._alterations = alterations

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        seed=0,
        ):
        assert isinstance(logical_tie, selectiontools.LogicalTie)
        if self.alterations is None:
            return
        alterations = self.alterations.rotate(seed)
        alteration = alterations[0]
        if alteration != 0:
            alteration = alteration / 2.
        for leaf in logical_tie:
            if isinstance(leaf, scoretools.Note):
                pitch = float(leaf.written_pitch) + alteration
                leaf.written_pitch = pitch
            elif isinstance(leaf, scoretools.Chord):
                pitches = []
                for written_pitch in leaf.written_pitches:
                    pitch = float(written_pitch) + alteration
                    pitches.append(pitch)
                leaf.written_pitches = pitches

    ### PUBLIC METHODS ###

    @staticmethod
    def iterate_score(
        score,
        ):
        from consort import makers
        counter = collections.Counter()
        for leaf in iterate(score).by_timeline(scoretools.Note):
            logical_tie = inspect_(leaf).get_logical_tie()
            if leaf is not logical_tie.head:
                continue
            prototype = makers.MusicSpecifier
            music_specifier = inspect_(leaf).get_effective(prototype)
            alteration_agent = music_specifier.alteration_agent
            if alteration_agent is None:
                continue
            seed = counter[alteration_agent]
            alteration_agent(
                logical_tie,
                seed=seed,
                )
            counter[alteration_agent] += 1

    def reverse(self):
        alterations = self.alterations
        if alterations is not None:
            alterations = alterations.reverse()
        return new(self,
            alterations=alterations,
            )

    def rotate(self, n=0):
        alterations = self.alterations
        if alterations is not None:
            alterations = alterations.rotate(n)
        return new(self,
            alterations=alterations,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def alterations(self):
        return self._alterations
