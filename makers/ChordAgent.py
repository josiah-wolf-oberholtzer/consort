# -*- encoding: utf-8 -*-
import collections
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import sequencetools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import new


class ChordAgent(ConsortObject):
    r'''A chord agent.

    ::

        >>> from consort import makers
        >>> chord_agent = makers.ChordAgent()
        >>> print format(chord_agent)
        makers.ChordAgent()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_expressions',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        expressions=None,
        ):
        if expressions is not None:
            assert len(expressions)
            expressions = tuple(expressions)
        self._expressions = expressions

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        seed=0,
        ):
        assert isinstance(logical_tie, selectiontools.LogicalTie)
        expressions = sequencetools.Sequence(*self.expressions)
        expressions = expressions.rotate(seed)
        expression = expressions[0]
        if expression is None:
            return
        expression(logical_tie)

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
            chord_agent = music_specifier.chord_agent
            if chord_agent is None:
                continue
            seed = counter[chord_agent]
            chord_agent(logical_tie, seed=seed)
            counter[chord_agent] += 1

    def reverse(self):
        expressions = self.expressions
        if expressions is not None:
            expressions = sequencetools.Sequence(*expressions)
        return new(self,
            expressions=expressions.reverse(),
            )

    def rotate(self, n=0):
        expressions = self.expressions
        if expressions is not None:
            expressions = sequencetools.Sequence(*expressions)
        return new(self,
            expressions=expressions.rotate(n),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def expressions(self):
        return self._expressions
