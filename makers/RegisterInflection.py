# -*- encoding: utf-8 -*-
import bisect
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import pitchtools
from abjad.tools.topleveltools import new


class RegisterInflection(abctools.AbjadValueObject):
    r'''A pitch curve.

    ::

        >>> from consort import makers
        >>> register_inflection = makers.RegisterInflection(
        ...     inflections=(-6, 0, 9),
        ...     ratio=(2, 1),
        ...     )
        >>> print(format(register_inflection))
        makers.RegisterInflection(
            inflections=pitchtools.IntervalSegment(
                (
                    pitchtools.NumberedInterval(-6),
                    pitchtools.NumberedInterval(0),
                    pitchtools.NumberedInterval(9),
                    ),
                item_class=pitchtools.NumberedInterval,
                ),
            ratio=mathtools.Ratio(2, 1),
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
        ratio = mathtools.Ratio([abs(x) for x in ratio])
        self._ratio = ratio
        assert len(inflections) == len(ratio) + 1
        inflections = pitchtools.IntervalSegment(
            inflections,
            item_class=pitchtools.NumberedInterval,
            )
        self._inflections = inflections

    ### SPECIAL METHODS ###

    def __call__(self, position):
        position = durationtools.Offset(position)
        if position < 0:
            position = durationtools.Offset(0)
        if 1 < position:
            position = durationtools.Offset(1)
        if position == 0:
            return self.inflections[0]
        elif position == 1:
            return self.inflections[-1]
        ratio_sum = sum(self.ratio)
        positions = [durationtools.Offset(x) / ratio_sum
            for x in mathtools.cumulative_sums(self.ratio)]
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
        result = pitchtools.NumberedInterval(int(result))
        return result

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        r'''Attribute manifest.

        ::

            >>> from consort import makers
            >>> register_inflection = makers.RegisterInflection()
            >>> attribute_manifest = register_inflection._attribute_manifest

        '''
        from abjad.tools import systemtools
        from scoremanager import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='inflections',
                display_string='inflections',
                command='i',
                editor=idetools.getters.get_integers,
                ),
            systemtools.AttributeDetail(
                name='ratio',
                display_string='ratio',
                command='r',
                editor=idetools.getters.get_nonnegative_integers,
                ),
            )

    ### PUBLIC METHODS ###

    @staticmethod
    def ascending():
        from consort import makers
        return makers.RegisterInflection(
            inflections=(-6, 6),
            ratio=(1,),
            )

    @staticmethod
    def descending():
        from consort import makers
        return makers.RegisterInflection.ascending().invert()

    def invert(self):
        return new(self,
            inflections=(-x for x in self.inflections),
            )

    def reverse(self):
        return new(self,
            inflections=reversed(self.inflections),
            ratio=reversed(self.ratio),
            )

    @staticmethod
    def triangle():
        from consort import makers
        return makers.RegisterInflection(
            inflections=(-6, 6, -6),
            ratio=(1, 1),
            )

    @staticmethod
    def zigzag():
        from consort import makers
        return makers.RegisterInflection(
            inflections=(-12, 6, -6, 12),
            ratio=(1, 1, 1),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def inflections(self):
        return self._inflections

    @property
    def ratio(self):
        return self._ratio