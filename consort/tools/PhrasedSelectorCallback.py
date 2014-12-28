# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import durationtools


class PhrasedSelectorCallback(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    def __call__(self, expr):
        assert isinstance(expr, tuple), repr(tuple)
        result = []
        for subexpr in expr:
            for division in subexpr[:-1]:
                result.append(division.select_leaves()[0])
            leaves = subexpr[-1].select_leaves()
            if leaves.get_duration() <= durationtools.Duration(1, 8):
                result.append(leaves[-1])
            elif 1 == len(leaves):
                result.append(leaves[0])
            else:
                result.append(leaves[0])
                result.append(leaves[1])
        result = tuple(result)
        print(result)
        return result