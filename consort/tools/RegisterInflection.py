import abjad
import bisect
from abjad.tools import abctools
from abjad.tools import mathtools


class RegisterInflection(abctools.AbjadValueObject):
    r'''A pitch curve.

    ::

        >>> register_inflection = consort.RegisterInflection(
        ...     inflections=(-6, 0, 9),
        ...     ratio=(2, 1),
        ...     )
        >>> print(format(register_inflection))
        consort.tools.RegisterInflection(
            inflections=abjad.IntervalSegment(
                (
                    abjad.NumberedInterval(-6),
                    abjad.NumberedInterval(0),
                    abjad.NumberedInterval(9),
                    ),
                item_class=abjad.NumberedInterval,
                ),
            ratio=abjad.Ratio((2, 1)),
            )

    ::

        >>> register_inflection(0)
        NumberedInterval(-6)

    ::

        >>> register_inflection((1, 3))
        NumberedInterval(-3)

    ::

        >>> register_inflection((1, 2))
        NumberedInterval(-1)

    ::

        >>> register_inflection((2, 3))
        NumberedInterval(0)

    ::

        >>> register_inflection(1)
        NumberedInterval(9)

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_inflections',
        '_ratio',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        inflections=(0, 0),
        ratio=(1,),
        ):
        if isinstance(inflections, type(self)):
            expr = inflections
            self._inflections = expr.inflections
            self._ratio = expr.ratio
            return
        ratio = abjad.Ratio([abs(x) for x in ratio])
        self._ratio = ratio
        inflections = abjad.IntervalSegment(
            inflections,
            item_class=abjad.NumberedInterval,
            )
        self._inflections = inflections
        assert len(inflections) == len(ratio) + 1

    ### SPECIAL METHODS ###

    def __call__(self, position):
        position = abjad.Offset(position)
        if position < 0:
            position = abjad.Offset(0)
        if 1 < position:
            position = abjad.Offset(1)
        if position == 0:
            return self.inflections[0]
        elif position == 1:
            return self.inflections[-1]
        ratio_sum = sum(list(self.ratio))
        positions = [abjad.Offset(x) / ratio_sum
            for x in mathtools.cumulative_sums(list(self.ratio))]
        index = bisect.bisect(positions, position)
        position = float(position)
        x0 = float(positions[index - 1])
        x1 = float(positions[index])
        y0 = float(self.inflections[index - 1])
        y1 = float(self.inflections[index])
        dx = x1 - x0
        dy = y1 - y0
        m = float(dy) / float(dx)
        b = y0 - (m * x0)
        result = (position * m) + b
        result = abjad.NumberedInterval(int(result))
        return result

    ### PUBLIC METHODS ###

    def align(self):
        r'''Aligns all inflections to a minimum interval of zero.

        ::

            >>> inflection = consort.RegisterInflection.zigzag().align()
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(0),
                        abjad.NumberedInterval(9),
                        abjad.NumberedInterval(3),
                        abjad.NumberedInterval(12),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1, 1, 1)),
                )

        Emits new register inflection.
        '''
        minimum = sorted(self.inflections, key=lambda x: x.semitones)[0]
        inflections = (_ - minimum for _ in self.inflections)
        return abjad.new(self, inflections=inflections)

    @staticmethod
    def ascending(width=12):
        r'''Creates an ascending register inflection.

        ::

            >>> inflection = consort.RegisterInflection.ascending()
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(-6),
                        abjad.NumberedInterval(6),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1,)),
                )

        Emits new register inflection.
        '''
        import consort
        half_width = abs(int(width / 2))
        return consort.RegisterInflection(
            inflections=(0 - half_width, half_width),
            ratio=(1,),
            )

    @staticmethod
    def descending(width=12):
        r'''Creates a descending register inflection.

        ::

            >>> inflection = consort.RegisterInflection.descending()
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(6),
                        abjad.NumberedInterval(-6),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1,)),
                )

        Emits new register inflection.
        '''
        import consort
        return consort.RegisterInflection.ascending(width=width).invert()

    def invert(self):
        r'''Inverts register inflection

        ::

            >>> inflection = consort.RegisterInflection.triangle().invert()
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(6),
                        abjad.NumberedInterval(-6),
                        abjad.NumberedInterval(6),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1, 1)),
                )

        Emits new register inflection.
        '''
        return abjad.new(self, inflections=(-x for x in self.inflections))

    def reverse(self):
        r'''Reverses register inflection.

        ::

            >>> inflection = consort.RegisterInflection.zigzag().reverse()
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(6),
                        abjad.NumberedInterval(-3),
                        abjad.NumberedInterval(3),
                        abjad.NumberedInterval(-6),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1, 1, 1)),
                )

        Emits new register inflection.
        '''
        return abjad.new(
            self,
            inflections=reversed(self.inflections),
            ratio=reversed(self.ratio),
            )

    def rotate(self, n=1):
        r'''Rotates register inflection by `n`.

        ::

            >>> inflection = consort.RegisterInflection.zigzag().rotate(1)
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(6),
                        abjad.NumberedInterval(-6),
                        abjad.NumberedInterval(3),
                        abjad.NumberedInterval(-3),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1, 1, 1)),
                )

        Emits new register inflection.
        '''
        import consort
        return abjad.new(
            self,
            inflections=consort.rotate(self.inflections, n),
            ratio=consort.rotate(self.ratio, n),
            )

    @staticmethod
    def triangle(width=12):
        r'''Creates a triangular register inflection.

        ::

            >>> inflection = consort.RegisterInflection.triangle()
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(-6),
                        abjad.NumberedInterval(6),
                        abjad.NumberedInterval(-6),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1, 1)),
                )

        ::

            >>> inflection = consort.RegisterInflection.triangle(width=6)
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(-3),
                        abjad.NumberedInterval(3),
                        abjad.NumberedInterval(-3),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1, 1)),
                )

        Emits new register inflection.
        '''
        import consort
        half_width = int(width / 2)
        return consort.RegisterInflection(
            inflections=(-half_width, half_width, -half_width),
            ratio=(1, 1),
            )

    @staticmethod
    def zigzag(width=12):
        r'''Creates a zigzag register inflection.

        ::

            >>> inflection = consort.RegisterInflection.zigzag()
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(-6),
                        abjad.NumberedInterval(3),
                        abjad.NumberedInterval(-3),
                        abjad.NumberedInterval(6),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1, 1, 1)),
                )

        ::

            >>> inflection = consort.RegisterInflection.zigzag(width=8)
            >>> print(format(inflection))
            consort.tools.RegisterInflection(
                inflections=abjad.IntervalSegment(
                    (
                        abjad.NumberedInterval(-4),
                        abjad.NumberedInterval(2),
                        abjad.NumberedInterval(-2),
                        abjad.NumberedInterval(4),
                        ),
                    item_class=abjad.NumberedInterval,
                    ),
                ratio=abjad.Ratio((1, 1, 1)),
                )

        Emits new register inflection.
        '''
        import consort
        half_width = int(width / 2)
        quarter_width = int(width / 4)
        return consort.RegisterInflection(
            inflections=(
                -half_width,
                quarter_width,
                -quarter_width,
                half_width,
                ),
            ratio=(1, 1, 1),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def inflections(self):
        return self._inflections

    @property
    def ratio(self):
        return self._ratio
