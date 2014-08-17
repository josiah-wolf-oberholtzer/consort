# -*- encoding: utf -*-
from abjad.tools import abctools
from abjad.tools import mathtools
from abjad.tools import timespantools


class RatioPartsExpression(abctools.AbjadObject):
    r'''Ratio parts expression.

    ::

        >>> from consort import makers
        >>> expression = makers.RatioPartsExpression(
        ...     ratio=(1, 2, 1),
        ...     parts=(0, 2),
        ...     )
        >>> print(format(expression))
        consort.makers.RatioPartsExpression(
            ratio=mathtools.Ratio(1, 2, 1),
            parts=(0, 2),
            )

    ::

        >>> timespan = timespantools.Timespan(
        ...     start_offset=Duration(1, 2),
        ...     stop_offset=Duration(3, 2),
        ...     )
        >>> for x in expression(timespan):
        ...     x
        ...
        Timespan(start_offset=Offset(1, 2), stop_offset=Offset(3, 4))
        Timespan(start_offset=Offset(5, 4), stop_offset=Offset(3, 2))


    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_parts',
        '_ratio',
        )

    ### INITIALIZER ###

    def __init__(self,
        ratio=(1, 1),
        parts=0,
        ):
        if not isinstance(ratio, mathtools.Ratio):
            ratio = mathtools.Ratio(ratio)
        self._ratio = ratio
        if isinstance(parts, int):
            parts = (parts,)
        assert all(0 <= _ < len(ratio) for _ in parts)
        parts = tuple(parts)
        self._parts = parts

    ### SPECIAL METHODS ###

    def __call__(self, timespan):
        assert isinstance(timespan, timespantools.Timespan)
        divided_timespan = timespan.divide_by_ratio(self.ratio)
        timespans = []
        for part in self.parts:
            timespans.append(divided_timespan[part])
        return tuple(timespans)

    ### PUBLIC PROPERTIES ###

    @property
    def parts(self):
        return self._parts

    @property
    def ratio(self):
        return self._ratio