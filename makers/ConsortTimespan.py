# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import timespantools
from abjad.tools import mathtools


class ConsortTimespan(timespantools.Timespan):
    r'''A Consort timespan.

    ::

        >>> from consort import makers
        >>> timespan = makers.ConsortTimespan()
        >>> print format(timespan)
        makers.ConsortTimespan(
            start_offset=NegativeInfinity,
            stop_offset=Infinity,
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_context_name',
        '_music_specifier',
        '_original_start_offset',
        '_original_stop_offset',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        context_name=None,
        music_specifier=None,
        original_start_offset=None,
        original_stop_offset=None,
        start_offset=mathtools.NegativeInfinity(),
        stop_offset=mathtools.Infinity(),
        ):
        timespantools.Timespan.__init__(
            self,
            start_offset=start_offset,
            stop_offset=stop_offset,
            )
        self._context_name = context_name
        self._music_specifier = music_specifier
        if original_start_offset is not None:
            original_start_offset = durationtools.Offset(original_start_offset)
        self._original_start_offset = original_start_offset
        if original_stop_offset is not None:
            original_stop_offset = durationtools.Offset(original_stop_offset)
        self._original_stop_offset = original_stop_offset

    ### PUBLIC PROPERTIES ###

    @property
    def context_name(self):
        return self._context_name

    @property
    def music_specifier(self):
        return self._music_specifier

    @property
    def original_start_offset(self):
        return self._original_start_offset

    @property
    def original_stop_offset(self):
        return self._original_stop_offset
