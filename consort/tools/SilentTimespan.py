# -*- encoding: utf-8 -*-
from abjad.tools import markuptools
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
        start_offset=mathtools.NegativeInfinity(),
        stop_offset=mathtools.Infinity(),
        layer=None,
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

    ### PRIVATE METHODS ###

    def _as_postscript(
        self,
        postscript_x_offset,
        postscript_y_offset,
        postscript_scale,
        ):
        start = (float(self.start_offset) * postscript_scale)
        start -= postscript_x_offset
        stop = (float(self.stop_offset) * postscript_scale)
        stop -= postscript_x_offset
        ps = markuptools.Postscript()
        ps = ps.moveto(start, postscript_y_offset)
        ps = ps.setdash([0.5])
        ps = ps.lineto(stop, postscript_y_offset)
        ps = ps.stroke()
        ps = ps.moveto(start, postscript_y_offset + 0.75)
        ps = ps.setdash()
        ps = ps.lineto(start, postscript_y_offset - 0.75)
        ps = ps.stroke()
        ps = ps.moveto(stop, postscript_y_offset + 0.75)
        ps = ps.lineto(stop, postscript_y_offset - 0.75)
        ps = ps.stroke()
        if self.layer is not None:
            ps = ps.moveto(start, postscript_y_offset)
            ps = ps.rmoveto(0.25, 0.5)
            #ps = ps.scale(0.8, 0.8)
            ps = ps.show(str(self.layer))
            #ps = ps.scale(1.25, 1.25)
        return ps

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