# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import timespantools
from abjad.tools import mathtools


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
        divisions=None,
        forbid_fusing=None,
        forbid_splitting=None,
        layer=None,
        minimum_duration=None,
        music=None,
        music_specifier=None,
        original_start_offset=None,
        original_stop_offset=None,
        start_offset=mathtools.NegativeInfinity(),
        stop_offset=mathtools.Infinity(),
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

    ### PRIVATE PROPERTIES ###

    @property
    def _storage_format_specification(self):
        from abjad.tools import systemtools
        manager = systemtools.StorageFormatManager
        keyword_argument_names = list(manager.get_keyword_argument_names(self))
        if self.original_start_offset == self.start_offset:
            keyword_argument_names.remove('original_start_offset')
        if self.original_stop_offset == self.stop_offset:
            keyword_argument_names.remove('original_stop_offset')
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=keyword_argument_names,
            )

    ### SPECIAL METHODS ###

    def __lt__(self, expr):
        if timespantools.Timespan.__lt__(self, expr):
            return True
        if not timespantools.Timespan.__gt__(self, expr):
            if hasattr(expr, 'voice_name'):
                return self.voice_name < expr.voice_name
        return False

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