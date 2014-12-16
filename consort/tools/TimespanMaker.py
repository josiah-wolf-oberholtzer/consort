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
        '_forbid_splitting',
        '_minimum_duration',
        '_seed',
        '_timespan_specifier',
        )

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(
        self,
        forbid_splitting=None,
        minimum_duration=None,
        seed=None,
        timespan_specifier=None,
        ):
        import consort
        if forbid_splitting is not None:
            forbid_splitting = bool(forbid_splitting)
        self._forbid_splitting = forbid_splitting
        if minimum_duration is not None:
            minimum_duration = durationtools.Duration(minimum_duration)
        self._minimum_duration = minimum_duration
        if seed is not None:
            seed = int(seed)
        self._seed = seed
        if timespan_specifier is not None:
            assert isinstance(timespan_specifier, consort.TimespanSpecifier)
        self._timespan_specifier = timespan_specifier

    ### SPECIAL METHODS ###

    def __call__(
        self,
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
        layer=None,
        music_specifier=None,
        start_offset=None,
        stop_offset=None,
        voice_name=None,
        ):
        import consort
        timespan = consort.PerformedTimespan(
            forbid_splitting=self.forbid_splitting,
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
    def forbid_splitting(self):
        return self._forbid_splitting

    @property
    def is_dependent(self):
        return False

    @property
    def minimum_duration(self):
        return self._minimum_duration

    @property
    def seed(self):
        return self._seed

    @property
    def timespan_specifier(self):
        return self._timespan_specifier