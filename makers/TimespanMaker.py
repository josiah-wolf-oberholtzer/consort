# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import timespantools


class TimespanMaker(abctools.AbjadObject):
    r'''A timespan maker.

    ::

        >>> from consort import makers
        >>> timespan_maker = makers.TimespanMaker()
        >>> print format(timespan_maker)
        makers.TimespanMaker(
            can_shift=False,
            can_split=False,
            minimum_duration=durationtools.Duration(1, 8),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_can_shift',
        '_can_split',
        '_minimum_duration',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        can_shift=False,
        can_split=False,
        minimum_duration=durationtools.Duration(1, 8),
        ):
        self._can_shift = bool(can_shift)
        self._can_split = bool(can_split)
        self._minimum_duration = durationtools.Duration(minimum_duration)

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music_specifier=None,
        score_template=None,
        target_duration=None,
        voice_specifier=None,
        ):
        pass

    ### PUBLIC PROPERTIES ###

    @property
    def can_shift(self):
        return self._can_shift

    @property
    def can_split(self):
        return self._can_split

    @property
    def minimum_duration(self):
        return self._minimum_duration
