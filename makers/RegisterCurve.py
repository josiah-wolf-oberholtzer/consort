# -*- encoding: utf-8 -*-
import bisect
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import pitchtools
from abjad.tools.topleveltools import new


class RegisterCurve(abctools.AbjadObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_ratio',
        '_registers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        ratio=None,
        registers=None,
        ):
        ratio = mathtools.Ratio([abs(x) for x in ratio])
        self._ratio = ratio
        assert len(registers) == len(ratio) + 1
        registers = pitchtools.PitchSegment(
            registers,
            item_class=pitchtools.NamedPitch,
            )
        self._registers = registers

    ### SPECIAL METHODS ###

    def __call__(self, position):
        position = durationtools.Offset(position)
        if position < 0:
            position = durationtools.Offset(0)
        if 1 < position:
            position = durationtools.Offset(1)
        if position == 0:
            return self.registers[0]
        elif position == 1:
            return self.registers[-1]
        ratio_sum = sum(self.ratio)
        positions = [durationtools.Offset(x) / ratio_sum
            for x in mathtools.cumulative_sums(self.ratio)]
        index = bisect.bisect(positions, position)
        position = float(position)
        x0 = float(positions[index - 1])
        x1 = float(positions[index])
        y0 = float(self.registers[index - 1])
        y1 = float(self.registers[index])
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
            registers=self.registers.transpose(expr),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def ratio(self):
        return self._ratio

    @property
    def registers(self):
        return self._registers
