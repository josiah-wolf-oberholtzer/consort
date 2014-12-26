# -*- encoding: utf-8 -*-
from abjad import abctools
from abjad import inspect_
from abjad import selectiontools


class AfterGraceSelectorCallback(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    def __call__(self, expr):
        assert isinstance(expr, tuple), repr(tuple)
        result = []
        for subexpr in expr:
            subresult = []
            for x in subexpr:
                subresult.append(x)
                if inspect_(x).get_grace_containers('after'):
                    subresult = selectiontools.Selection(subresult)
                    result.append(subresult)
                    subresult = []
            if subresult:
                subresult = selectiontools.Selection(subresult)
                result.append(subresult)
        return tuple(result)