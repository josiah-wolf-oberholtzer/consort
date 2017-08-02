import abjad
from abjad.tools import abctools
from abjad.tools import selectiontools


class AfterGraceSelectorCallback(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    def __call__(self, expr, rotation=None, start_offset=None):
        assert isinstance(expr, tuple), repr(tuple)
        result = []
        for subexpr in expr:
            subresult = []
            for x in subexpr:
                subresult.append(x)
                if abjad.inspect(x).get_after_grace_container():
                    subresult = selectiontools.Selection(subresult)
                    result.append(subresult)
                    subresult = []
            if subresult:
                subresult = selectiontools.Selection(subresult)
                result.append(subresult)
        return tuple(result)
