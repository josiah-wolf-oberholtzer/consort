# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import selectiontools


class PhrasedSelectorCallback(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    def __call__(self, expr):
        assert isinstance(expr, tuple), repr(tuple)
        result = []
        for subexpr in expr:
            subresult = []
            for division in subexpr[:-1]:
                leaf = division.select_leaves()[0]
                selection = selectiontools.Selection(leaf)
                subresult.append(selection)
            leaves = subexpr[-1].select_leaves()
            if leaves.get_duration() <= durationtools.Duration(1, 8):
                subresult.append(leaves[-1])
            elif 1 == len(leaves):
                subresult.append(leaves[0])
            else:
                subresult.append(leaves[0])
                subresult.append(leaves[1])
            subresult = selectiontools.Selection(subresult)
            result.append(subresult)
        result = tuple(result)
        return result