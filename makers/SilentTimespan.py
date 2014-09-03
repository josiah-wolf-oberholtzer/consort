# -*- encoding: utf-8 -*-
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
        start_offset=None,
        stop_offset=None,
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
        if voice_name is not None:
            voice_name = int(voice_name)
        self._voice_name = voice_name

    ### PUBLIC PROPERTIES ###

    @property
    def color(self):
        return None

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
    def voice_name(self):
        return self._voice_name