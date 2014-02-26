# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class PitchAgent(abctools.AbjadObject):
    r'''A pitch agent.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(
        self,
        ):
        pass

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        seed=0,
        ):
        assert isinstance(logical_tie, selectiontools.LogicalTie)

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
            pitch_agent = music_specifier.pitch_agent
            if pitch_agent is None:
                continue
            seed = counter[pitch_agent]
            pitch_agent(logical_tie, seed=seed)
            counter[pitch_agent] += 1
