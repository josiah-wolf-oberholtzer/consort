# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools import abctools
from abjad.tools import datastructuretools
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
            initial_silence_durations=(),
            minimum_duration=durationtools.Duration(1, 8),
            playing_durations=(
                durationtools.Duration(1, 4),
                ),
            playing_groupings=(1,),
            repeat=True,
            silence_durations=(
                durationtools.Duration(1, 4),
                ),
            step_anchor=Right,
            synchronize_groupings=False,
            synchronize_step=False,
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_can_shift',
        '_can_split',
        '_initial_silence_durations',
        '_minimum_duration',
        '_playing_durations',
        '_playing_groupings',
        '_repeat',
        '_silence_durations',
        '_step_anchor',
        '_synchronize_groupings',
        '_synchronize_step',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        can_shift=False,
        can_split=False,
        initial_silence_durations=(),
        minimum_duration=durationtools.Duration(1, 8),
        playing_durations=(
            durationtools.Duration(1, 4),
            ),
        playing_groupings=(1,),
        repeat=True,
        silence_durations=(
            durationtools.Duration(1, 4),
            ),
        step_anchor=Right,
        synchronize_groupings=False,
        synchronize_step=False,
        ):
        self._can_shift = bool(can_shift)
        self._can_split = bool(can_split)
        initial_silence_durations = tuple(durationtools.Duration(x)
            for x in initial_silence_durations)
        assert all(0 <= x for x in initial_silence_durations)
        self._initial_silence_durations = initial_silence_durations
        self._minimum_duration = durationtools.Duration(minimum_duration)
        playing_durations = tuple(durationtools.Duration(x)
            for x in playing_durations)
        assert len(playing_durations)
        assert all(0 < x for x in playing_durations)
        self._playing_durations = playing_durations
        playing_groupings = tuple(int(x) for x in playing_groupings)
        assert len(playing_groupings)
        assert all(0 < x for x in playing_groupings)
        self._playing_groupings = playing_groupings
        self._repeat = bool(repeat)
        silence_durations = tuple(durationtools.Duration(x)
            for x in silence_durations)
        assert len(silence_durations)
        assert all(0 < x for x in silence_durations)
        self._silence_durations = silence_durations
        assert step_anchor in (Left, Right)
        self._step_anchor = step_anchor
        self._synchronize_groupings = bool(synchronize_groupings)
        self._synchronize_step = bool(synchronize_step)

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer=None,
        music_specifier=None,
        target_duration=None,
        voice_specifier=None,
        ):

        initial_silence_durations = self.initial_silence_durations
        if len(initial_silence_durations) < 2:
            initial_silence_durations *= 2
        if initial_silence_durations:
            initial_silence_durations = datastructuretools.StatalServer(
                initial_silence_durations)()

        playing_durations = self.playing_durations
        if len(playing_durations) < 2:
            playing_durations *= 2
        playing_durations = datastructuretools.StatalServer(
            playing_durations)()

        playing_groupings = self.playing_groupings
        if len(playing_groupings) < 2:
            playing_groupings *= 2
        playing_groupings = datastructuretools.StatalServer(
            playing_groupings)()

        silence_durations = self.silence_durations
        if len(silence_durations) < 2:
            silence_durations *= 2
        silence_durations = datastructuretools.StatalServer(
            silence_durations)()

        if self.synchronize_step:
            procedure = self._make_with_synchronized_step
        else:
            procedure = self._make_without_synchronized_step

        timespan_inventory, final_offset = procedure(
            initial_silence_durations=initial_silence_durations,
            layer=layer,
            music_specifier=music_specifier,
            playing_durations=playing_durations,
            playing_groupings=playing_groupings,
            silence_durations=silence_durations,
            target_duration=target_duration,
            voice_specifier=voice_specifier,
            )

        if target_duration < final_offset:
            final_offset = durationtools.Offset(target_duration)

        timespan_inventory.sort()

        return timespan_inventory, final_offset

    ### PRIVATE METHODS ###

    def _make_with_synchronized_step(
        self,
        initial_silence_durations=None,
        layer=None,
        music_specifier=None,
        playing_durations=None,
        playing_groupings=None,
        silence_durations=None,
        target_duration=None,
        voice_specifier=None,
        ):
        from consort import makers
        timespan_inventory = timespantools.TimespanInventory()
        start_offset = durationtools.Offset(0)
        if initial_silence_durations:
            start_offset += initial_silence_durations()[0]
        while start_offset < target_duration:
            if self.synchronize_groupings:
                grouping = playing_groupings()[0]
                durations = playing_durations(grouping)
            silence_duration = silence_durations()[0]
            for voice_name in voice_specifier:
                if not self.synchronize_groupings:
                    grouping = playing_groupings()[0]
                    durations = playing_durations(grouping)
                maximum_offset = start_offset + sum(durations) + \
                    silence_duration
                maximum_offset = min(maximum_offset, target_duration)
                if self.step_anchor is Left:
                    maximum_offset = min(maximum_offset,
                        start_offset + silence_duration)
                current_offset = start_offset
                for duration in durations:
                    if maximum_offset < (current_offset + duration):
                        break
                    timespan = makers.PerformedTimespan(
                        context_name=voice_name,
                        layer=layer,
                        music_specifier=music_specifier,
                        start_offset=current_offset,
                        stop_offset=current_offset + duration,
                        )
                    timespan_inventory.append(timespan)
                    current_offset += duration
            timespan_inventory.sort()
            if self.step_anchor is Left:
                start_offset += silence_duration
            else:
                start_offset = timespan_inventory.stop_offset + \
                    silence_duration
            if not self.repeat:
                break
        return timespan_inventory, start_offset

    def _make_without_synchronized_step(
        self,
        initial_silence_durations=None,
        layer=None,
        music_specifier=None,
        playing_durations=None,
        playing_groupings=None,
        silence_durations=None,
        target_duration=None,
        voice_specifier=None,
        ):
        from consort import makers
        timespan_inventory = timespantools.TimespanInventory()
        final_offset = durationtools.Offset(0)
        for voice_name in voice_specifier:
            start_offset = durationtools.Offset(0)
            if initial_silence_durations:
                start_offset += initial_silence_durations()[0]
            while start_offset < target_duration:
                silence_duration = silence_durations()[0]
                grouping = playing_groupings()[0]
                durations = playing_durations(grouping)
                maximum_offset = start_offset + sum(durations) + \
                    silence_duration
                maximum_offset = min(maximum_offset, target_duration)
                if self.step_anchor is Left:
                    maximum_offset = min(maximum_offset,
                        start_offset + silence_duration)
                current_offset = start_offset
                for duration in durations:
                    if maximum_offset < (current_offset + duration):
                        break
                    timespan = makers.PerformedTimespan(
                        context_name=voice_name,
                        layer=layer,
                        music_specifier=music_specifier,
                        start_offset=current_offset,
                        stop_offset=current_offset + duration,
                        )
                    timespan_inventory.append(timespan)
                    current_offset += duration
                if self.step_anchor is Left:
                    start_offset += silence_duration
                else:
                    start_offset = current_offset + silence_duration
                if not self.repeat:
                    break
            if final_offset < start_offset:
                final_offset = start_offset
        return timespan_inventory, final_offset

    ### PUBLIC PROPERTIES ###

    @property
    def can_shift(self):
        return self._can_shift

    @property
    def can_split(self):
        return self._can_split

    @property
    def initial_silence_durations(self):
        return self._initial_silence_durations

    @property
    def minimum_duration(self):
        return self._minimum_duration

    @property
    def playing_durations(self):
        return self._playing_durations

    @property
    def playing_groupings(self):
        return self._playing_groupings

    @property
    def repeat(self):
        return self._repeat

    @property
    def silence_durations(self):
        return self._silence_durations

    @property
    def step_anchor(self):
        return self._step_anchor

    @property
    def synchronize_groupings(self):
        return self._synchronize_groupings

    @property
    def synchronize_step(self):
        return self._synchronize_step
