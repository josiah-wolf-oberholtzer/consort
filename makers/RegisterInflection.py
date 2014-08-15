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
        ...     pitches=(-6, 0, 9),
        ...     ratio=(2, 1),
        ...     )
        >>> print(format(register_inflection))
        makers.RegisterInflection(
            pitches=pitchtools.PitchSegment(
                (
                    pitchtools.NamedPitch('fs'),
                    pitchtools.NamedPitch("c'"),
                    pitchtools.NamedPitch("a'"),
                    ),
                item_class=pitchtools.NamedPitch,
                ),
            ratio=mathtools.Ratio(2, 1),
            )

    ::

        >>> register_inflection(0)
        NamedPitch('fs')

    ::

        >>> register_inflection((1, 3))
        NamedPitch('a')

    ::

        >>> register_inflection((1, 2))
        NamedPitch('b')

    ::

        >>> register_inflection((2, 3))
        NamedPitch("c'")

    ::

        >>> register_inflection(1)
        NamedPitch("a'")

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_pitches',
        '_ratio',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pitches=(0, 0),
        ratio=(1,),
        ):
        ratio = mathtools.Ratio([abs(x) for x in ratio])
        self._ratio = ratio
        assert len(pitches) == len(ratio) + 1
        pitches = pitchtools.PitchSegment(
            pitches,
            item_class=pitchtools.NamedPitch,
            )
        self._pitches = pitches

    ### SPECIAL METHODS ###

    def __call__(self, position):
        position = durationtools.Offset(position)
        if position < 0:
            position = durationtools.Offset(0)
        if 1 < position:
            position = durationtools.Offset(1)
        if position == 0:
            return self.pitches[0]
        elif position == 1:
            return self.pitches[-1]
        ratio_sum = sum(self.ratio)
        positions = [durationtools.Offset(x) / ratio_sum
            for x in mathtools.cumulative_sums(self.ratio)]
        index = bisect.bisect(positions, position)
        position = float(position)
        x0 = float(positions[index - 1])
        x1 = float(positions[index])
        y0 = float(self.pitches[index - 1])
        y1 = float(self.pitches[index])
        dx = x1 - x0
        dy = y1 - y0
        m = float(dy) / float(dx)
        b = y0 - (m * x0)
        result = (position * m) + b
        result = pitchtools.NamedPitch(int(result))
        return result

    ### PUBLIC METHODS ###

    def transpose(self, expr):
        return new(
            self,
            pitches=self.pitches.transpose(expr),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def pitches(self):
        return self._pitches

    @property
    def ratio(self):
        return self._ratio