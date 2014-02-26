# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class GraceAgent(abctools.AbjadObject):
    r'''A grace agent.
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
            grace_agent = music_specifier.grace_agent
            if grace_agent is None:
                continue
            seed = counter[grace_agent]
            grace_agent(logical_tie, seed=seed)
            counter[grace_agent] += 1
