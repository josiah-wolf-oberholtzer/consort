import abjad
from abjad.tools import abctools


class RatioPartsExpression(abctools.AbjadObject):
    r'''Ratio parts expression.


    ..  container:: example

        ::

            >>> expression = consort.RatioPartsExpression(
            ...     ratio=(1, 2, 1),
            ...     parts=(0, 2),
            ...     )
            >>> print(format(expression))
            consort.tools.RatioPartsExpression(
                parts=(0, 2),
                ratio=abjad.Ratio((1, 2, 1)),
                )

        ::

            >>> timespan = abjad.Timespan(
            ...     start_offset=abjad.Duration(1, 2),
            ...     stop_offset=abjad.Duration(3, 2),
            ...     )
            >>> for x in expression(timespan):
            ...     x
            ...
            Timespan(start_offset=Offset(1, 2), stop_offset=Offset(3, 4))
            Timespan(start_offset=Offset(5, 4), stop_offset=Offset(3, 2))

    ..  container:: example

        ::

            >>> expression = consort.RatioPartsExpression(
            ...     ratio=(1, 2, 1),
            ...     parts=(0, 2),
            ...     mask_timespan=abjad.Timespan(
            ...          start_offset=(1, 4),
            ...          ),
            ...     )

        ::

            >>> timespan = abjad.Timespan(0, 4)
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
        '_mask_timespan',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        parts=0,
        ratio=(1, 1),
        mask_timespan=None,
        ):
        if not isinstance(ratio, abjad.Ratio):
            ratio = abjad.Ratio(ratio)
        self._ratio = ratio
        if isinstance(parts, int):
            parts = (parts,)
        assert all(0 <= _ < len(ratio) for _ in parts)
        parts = tuple(sorted(set(parts)))
        self._parts = parts
        if mask_timespan is not None:
            assert isinstance(mask_timespan, abjad.Timespan)
        self._mask_timespan = mask_timespan

    ### SPECIAL METHODS ###

    def __call__(self, timespan):
        assert isinstance(timespan, abjad.Timespan)
        divided_timespan = timespan.divide_by_ratio(self.ratio)
        timespans = abjad.TimespanList()
        for part in self.parts:
            timespans.append(divided_timespan[part])
        if self.mask_timespan is not None:
            timespans & self.mask_timespan
        return timespans

    ### PUBLIC METHODS ###

    @staticmethod
    def from_sequence(sequence):
        r'''Creates a ratio parts expression from `sequence`.

        ::

            >>> ratio = [-1, 2, -1, 1, -1]
            >>> expression = consort.RatioPartsExpression.from_sequence(ratio)
            >>> print(format(expression))
            consort.tools.RatioPartsExpression(
                parts=(1, 3),
                ratio=abjad.Ratio((1, 2, 1, 1, 1)),
                )

        Returns new ratio parts expression.
        '''
        assert all(sequence)
        assert len(sequence)
        ratio = []
        parts = []
        for i, x in enumerate(sequence):
            if 0 < x:
                parts.append(i)
            ratio.append(abs(x))
        result = RatioPartsExpression(
            parts=parts,
            ratio=ratio,
            )
        return result

    ### PUBLIC PROPERTIES ###

    @property
    def mask_timespan(self):
        return self._mask_timespan

    @property
    def parts(self):
        return self._parts

    @property
    def ratio(self):
        return self._ratio
