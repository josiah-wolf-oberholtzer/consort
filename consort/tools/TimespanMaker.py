# -*- encoding: utf-8 -*-
from __future__ import print_function
import abc
import collections
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import rhythmmakertools
from abjad.tools import timespantools


class TimespanMaker(abctools.AbjadValueObject):
    r'''Abstract base class for timespan makers.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_output_masks',
        '_padding',
        '_seed',
        '_timespan_specifier',
        )

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(
        self,
        output_masks=None,
        padding=None,
        seed=None,
        timespan_specifier=None,
        ):
        import consort
        if output_masks is not None:
            if isinstance(output_masks, rhythmmakertools.BooleanPattern):
                output_masks = (output_masks,)
            output_masks = rhythmmakertools.BooleanPatternInventory(
                items=output_masks,
                )
        self._output_masks = output_masks
        if padding is not None:
            padding = durationtools.Duration(padding)
        self._padding = padding
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
        silenced_context_names=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        if not isinstance(timespan_inventory, timespantools.TimespanInventory):
            timespan_inventory = timespantools.TimespanInventory(
                timespan_inventory,
                )
        if target_timespan is None:
            if timespan_inventory:
                target_timespan = timespan_inventory.timespan
            else:
                raise TypeError
        assert isinstance(timespan_inventory, timespantools.TimespanInventory)
        if not music_specifiers:
            return timespan_inventory
        music_specifiers = self._coerce_music_specifiers(music_specifiers)
        new_timespans = self._make_timespans(
            layer=layer,
            music_specifiers=music_specifiers,
            target_timespan=target_timespan,
            timespan_inventory=timespan_inventory,
            )
        self._make_silent_timespans(
            layer=layer,
            silenced_context_names=silenced_context_names,
            timespans=new_timespans,
            )
        timespan_inventory.extend(new_timespans)
        timespan_inventory.sort()
        return timespan_inventory

    ### PRIVATE METHODS ###

    @staticmethod
    def _coerce_music_specifiers(music_specifiers):
        import consort
        result = collections.OrderedDict()
        prototype = (
            consort.MusicSpecifierSequence,
            consort.CompositeMusicSpecifier,
            )
        for context_name, music_specifier in music_specifiers.items():
            if music_specifier is None:
                music_specifier = [None]
            if not isinstance(music_specifier, prototype):
                music_specifier = consort.MusicSpecifierSequence(
                    music_specifiers=music_specifier,
                    )
            result[context_name] = music_specifier
        return result

    def _make_silent_timespans(
        self,
        layer,
        silenced_context_names,
        timespans,
        ):
        import consort
        if not silenced_context_names or not timespans:
            return

        sounding_timespans_by_context = {}
        sounding_timespans = timespantools.TimespanInventory()
        for timespan in timespans:
            if not isinstance(timespan, consort.PerformedTimespan):
                continue
            voice_name = timespan.voice_name
            if voice_name not in sounding_timespans_by_context:
                sounding_timespans_by_context[voice_name] = \
                    timespantools.TimespanInventory()
            sounding_timespans_by_context[voice_name].append(timespan)
            sounding_timespans.append(timespan)
        sounding_timespans.sort()
        sounding_timespans.compute_logical_or()

        silent_timespans_by_context = {}
        for context_name in silenced_context_names:
            silent_timespans_by_context[context_name] = \
                timespantools.TimespanInventory()
        for shard in sounding_timespans.partition(True):
            for context_name in silenced_context_names:
                timespan = consort.SilentTimespan(
                    layer=layer,
                    voice_name=context_name,
                    start_offset=shard.start_offset,
                    stop_offset=shard.stop_offset,
                    )
                silent_timespans_by_context[context_name].append(timespan)

        # Remove any overlap between performed and silent timespans.
        # Then add the silent timespans into the original timespan inventory.
        for context_name, silent_timespans in \
            sorted(silent_timespans_by_context.items()):
            if context_name in sounding_timespans_by_context:
                for timespan in sounding_timespans_by_context[context_name]:
                    silent_timespans - timespan
            timespans.extend(silent_timespans)

    ### PUBLIC PROPERTIES ###

    @property
    def is_dependent(self):
        return False

    @property
    def output_masks(self):
        return self._output_masks

    @property
    def padding(self):
        return self._padding

    @property
    def seed(self):
        return self._seed

    @property
    def timespan_specifier(self):
        return self._timespan_specifier