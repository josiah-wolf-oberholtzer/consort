# -*- encoding: utf -*-
from abjad.tools import abctools
from abjad.tools import mathtools
from abjad.tools import timespantools


class RatioPartsExpression(abctools.AbjadObject):
    r'''Ratio parts expression.


    ..  container:: example

        ::

            >>> from consort import makers
            >>> expression = makers.RatioPartsExpression(
            ...     ratio=(1, 2, 1),
            ...     parts=(0, 2),
            ...     )
            >>> print(format(expression))
            consort.makers.RatioPartsExpression(
                parts=(0, 2),
                ratio=mathtools.Ratio(1, 2, 1),
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

    ..  container:: example

        ::

            >>> expression = makers.RatioPartsExpression(
            ...     ratio=(1, 2, 1),
            ...     parts=(0, 2),
            ...     timespan=timespantools.Timespan(
            ...          start_offset=(1, 4),
            ...          ),
            ...     )

        ::

            >>> timespan = timespantools.Timespan(0, 4)
            >>> for x in expression(timespan):
            ...     x
            ...
            Timespan(start_offset=Offset(1, 4), stop_offset=Offset(1, 1))
            Timespan(start_offset=Offset(3, 1), stop_offset=Offset(4, 1))

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_parts',
        '_ratio',
        '_timespan',
        )

    ### INITIALIZER ###

    def __init__(self,
        parts=0,
        ratio=(1, 1),
        timespan=None,
        ):
        if not isinstance(ratio, mathtools.Ratio):
            ratio = mathtools.Ratio(ratio)
        self._ratio = ratio
        if isinstance(parts, int):
            parts = (parts,)
        assert all(0 <= _ < len(ratio) for _ in parts)
        parts = tuple(parts)
        self._parts = parts
        if timespan is not None:
            assert isinstance(timespan, timespantools.Timespan)
        self._timespan = timespan


    ### SPECIAL METHODS ###

    def __call__(self, timespan):
        assert isinstance(timespan, timespantools.Timespan)
        divided_timespan = timespan.divide_by_ratio(self.ratio)
        timespans = timespantools.TimespanInventory()
        for part in self.parts:
            timespans.append(divided_timespan[part])
        if self.timespan is not None:
            timespans & self.timespan
        timespans.round_offsets((1, 16))
        return timespans

    ### PUBLIC PROPERTIES ###

    @property
    def parts(self):
        return self._parts

    @property
    def ratio(self):
        return self._ratio

    @property
    def timespan(self):
        return self._timespan