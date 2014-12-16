# -*- encoding: utf-8 -*-
from abjad.tools import mathtools
from abjad.tools import timespantools


class SilentTimespan(timespantools.Timespan):
    r'''A silent timespan.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_layer',
        '_voice_name',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        layer=None,
        start_offset=mathtools.NegativeInfinity(),
        stop_offset=mathtools.Infinity(),
        voice_name=None,
        ):
        timespantools.Timespan.__init__(
            self,
            start_offset=start_offset,
            stop_offset=stop_offset,
            )
        if layer is not None:
            layer = int(layer)
        self._layer = layer
        self._voice_name = voice_name

    ### PUBLIC PROPERTIES ###

    @property
    def forbid_fusing(self):
        return False

    @property
    def forbid_splitting(self):
        return False

    @property
    def is_left_broken(self):
        return False

    @property
    def is_right_broken(self):
        return False

    @property
    def layer(self):
        return self._layer

    @property
    def minimum_duration(self):
        return 0

    @property
    def voice_name(self):
        return self._voice_name