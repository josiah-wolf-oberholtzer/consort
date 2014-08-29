# -*- encoding: utf-8 -*-
import abc
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import timespantools


class TimespanMaker(abctools.AbjadValueObject):
    r'''Abstract base class for timespan makers.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_can_split',
        '_minimum_duration',
        '_reflect',
        '_seed',
        )

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(
        self,
        can_split=None,
        minimum_duration=None,
        reflect=None,
        seed=None,
        ):
        if can_split is not None:
            can_split = bool(can_split)
        self._can_split = can_split
        if minimum_duration is not None:
            minimum_duration = durationtools.Duration(minimum_duration)
        self._minimum_duration = minimum_duration
        if reflect is not None:
            reflect = bool(reflect)
        self._reflect = reflect
        if seed is not None:
            seed = int(seed)
        self._seed = seed

    ### SPECIAL METHODS ###

    def __call__(
        self,
        color=None,
        layer=None,
        music_specifiers=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        if target_timespan is None:
            raise TypeError
        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
        assert isinstance(timespan_inventory, timespantools.TimespanInventory)
        if not music_specifiers:
            return timespan_inventory
        self._make_timespans(
            color=color,
            layer=layer,
            music_specifiers=music_specifiers,
            target_timespan=target_timespan,
            timespan_inventory=timespan_inventory,
            )
        timespan_inventory.sort()
        return timespan_inventory


    ### PRIVATE METHODS ###

    def _make_performed_timespan(
        self,
        color=None,
        layer=None,
        music_specifier=None,
        start_offset=None,
        stop_offset=None,
        voice_name=None,
        ):
        from consort import makers
        timespan = makers.PerformedTimespan(
            can_split=self.can_split,
            color=color,
            layer=layer,
            minimum_duration=self.minimum_duration,
            music_specifier=music_specifier,
            original_start_offset=start_offset,
            original_stop_offset=stop_offset,
            start_offset=start_offset,
            stop_offset=stop_offset,
            voice_name=voice_name,
            )
        return timespan

    ### PUBLIC PROPERTIES ###

    @property
    def can_split(self):
        return self._can_split

    @property
    def is_dependent(self):
        return False

    @property
    def minimum_duration(self):
        return self._minimum_duration

    @property
    def reflect(self):
        return self._reflect

    @property
    def seed(self):
        return self._seed