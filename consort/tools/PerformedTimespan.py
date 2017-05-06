# -*- encoding: utf-8 -*-
from abjad import new
from abjad.tools import durationtools
from abjad.tools import markuptools
from abjad.tools import mathtools
from abjad.tools import sequencetools
from abjad.tools import systemtools
from abjad.tools import timespantools


class PerformedTimespan(timespantools.Timespan):
    r'''A Consort timespan.

    ::

        >>> import consort
        >>> timespan = consort.PerformedTimespan()
        >>> print(format(timespan))
        consort.tools.PerformedTimespan(
            start_offset=NegativeInfinity,
            stop_offset=Infinity,
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_forbid_fusing',
        '_forbid_splitting',
        '_divisions',
        '_layer',
        '_minimum_duration',
        '_music',
        '_music_specifier',
        '_original_start_offset',
        '_original_stop_offset',
        '_voice_name',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        start_offset=mathtools.NegativeInfinity(),
        stop_offset=mathtools.Infinity(),
        divisions=None,
        forbid_fusing=None,
        forbid_splitting=None,
        layer=None,
        minimum_duration=None,
        music=None,
        music_specifier=None,
        original_start_offset=None,
        original_stop_offset=None,
        voice_name=None,
        ):
        timespantools.Timespan.__init__(
            self,
            start_offset=start_offset,
            stop_offset=stop_offset,
            )
        if divisions is not None:
            divisions = tuple(durationtools.Duration(_) for _ in divisions)
            assert sum(divisions) == self.duration
        self._divisions = divisions
        if forbid_fusing is not None:
            forbid_fusing = bool(forbid_fusing)
        self._forbid_fusing = forbid_fusing
        if forbid_splitting is not None:
            forbid_splitting = bool(forbid_splitting)
        self._forbid_splitting = forbid_splitting
        if layer is not None:
            layer = int(layer)
        self._layer = layer
        if minimum_duration is not None:
            minimum_duration = durationtools.Duration(minimum_duration)
        self._minimum_duration = minimum_duration
        #if music is not None:
        #    assert inspect_(music).get_duration() == self.duration
        self._music = music
        #if music_specifier is not None:
        #    assert isinstance(music_specifier, consort.MusicSpecifier), \
        #        music_specifier
        self._music_specifier = music_specifier
        if original_start_offset is not None:
            original_start_offset = durationtools.Offset(original_start_offset)
        else:
            original_start_offset = self.start_offset
        self._original_start_offset = original_start_offset
        if original_stop_offset is not None:
            original_stop_offset = durationtools.Offset(original_stop_offset)
        else:
            original_stop_offset = self.stop_offset
        self._original_stop_offset = original_stop_offset
        self._voice_name = voice_name

    ### SPECIAL METHODS ###

    def __lt__(self, expr):
        if timespantools.Timespan.__lt__(self, expr):
            return True
        if not timespantools.Timespan.__gt__(self, expr):
            if hasattr(expr, 'voice_name'):
                return self.voice_name < expr.voice_name
        return False

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
        ps = ps.lineto(stop, postscript_y_offset)
        ps = ps.stroke()
        ps = ps.moveto(start, postscript_y_offset + 0.75)
        ps = ps.lineto(start, postscript_y_offset - 0.75)
        ps = ps.stroke()
        ps = ps.moveto(stop, postscript_y_offset + 0.75)
        ps = ps.lineto(stop, postscript_y_offset - 0.75)
        ps = ps.stroke()
        if self.layer is not None:
            ps = ps.moveto(start, postscript_y_offset)
            ps = ps.rmoveto(0.25, 0.5)
            ps = ps.show(str(self.layer))
        return ps

    def _get_format_specification(self):
        agent = systemtools.StorageFormatAgent(self)
        names = agent.signature_keyword_names
        if self.original_start_offset == self.start_offset:
            names.remove('original_start_offset')
        if self.original_stop_offset == self.stop_offset:
            names.remove('original_stop_offset')
        return systemtools.FormatSpecification(
            storage_format_kwargs_names=names,
            )

    ### PUBLIC METHODS ###

    def split_at_offset(self, offset):
        from abjad.tools import timespantools
        offset = durationtools.Offset(offset)
        result = timespantools.TimespanList()
        if self._start_offset < offset < self._stop_offset:
            left_divisions, right_divisions = None, None
            if self.divisions is not None:
                left_divisions, right_divisions = sequencetools.split_sequence(
                    self.divisions,
                    [offset - self.start_offset],
                    overhang=True,
                    )
            left = new(
                self,
                start_offset=self._start_offset,
                stop_offset=offset,
                divisions=left_divisions,
                )
            right = new(
                self,
                start_offset=offset,
                stop_offset=self._stop_offset,
                divisions=right_divisions,
                )
            if left.duration:
                result.append(left)
            if right.duration:
                result.append(right)
        else:
            result.append(new(self))
        return result

    ### PUBLIC PROPERTIES ###

    @property
    def divisions(self):
        return self._divisions

    @property
    def forbid_fusing(self):
        return self._forbid_fusing

    @property
    def forbid_splitting(self):
        return self._forbid_splitting

    @property
    def is_left_broken(self):
        if self.original_start_offset is not None:
            if self.original_start_offset != self.start_offset:
                return True
        return False

    @property
    def is_right_broken(self):
        if self.original_stop_offset is not None:
            if self.original_stop_offset != self.stop_offset:
                return True
        return False

    @property
    def layer(self):
        return self._layer

    @property
    def minimum_duration(self):
        return self._minimum_duration

    @property
    def music(self):
        return self._music

    @property
    def music_specifier(self):
        return self._music_specifier

    @property
    def original_start_offset(self):
        return self._original_start_offset

    @property
    def original_stop_offset(self):
        return self._original_stop_offset

    @property
    def voice_name(self):
        return self._voice_name
