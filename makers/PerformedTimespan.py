# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import timespantools
from abjad.tools import mathtools


class PerformedTimespan(timespantools.Timespan):
    r'''A Consort timespan.

    ::

        >>> from consort import makers
        >>> timespan = makers.PerformedTimespan()
        >>> print format(timespan)
        makers.PerformedTimespan(
            start_offset=NegativeInfinity,
            stop_offset=Infinity,
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_context_name',
        '_layer',
        '_music_specifier',
        '_original_start_offset',
        '_original_stop_offset',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        context_name=None,
        layer=None,
        music_specifier=None,
        original_start_offset=None,
        original_stop_offset=None,
        start_offset=mathtools.NegativeInfinity(),
        stop_offset=mathtools.Infinity(),
        ):
        from consort import makers
        timespantools.Timespan.__init__(
            self,
            start_offset=start_offset,
            stop_offset=stop_offset,
            )
        self._context_name = context_name
        if layer is not None:
            layer = int(layer)
        self._layer = layer
        if music_specifier is not None:
            assert isinstance(music_specifier, makers.MusicSpecifier)
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

    ### PUBLIC PROPERTIES ###

    @property
    def context_name(self):
        return self._context_name

    @property
    def layer(self):
        return self._layer

    @property
    def music_specifier(self):
        return self._music_specifier

    @property
    def original_start_offset(self):
        return self._original_start_offset

    @property
    def original_stop_offset(self):
        return self._original_stop_offset
