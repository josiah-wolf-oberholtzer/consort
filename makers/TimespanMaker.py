# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import timespantools
from abjad.tools import abctools
import collections
from scoremanager import idetools


class TimespanMaker(abctools.AbjadValueObject):
    r'''A timespan maker.

    ::

        >>> from consort import makers
        >>> timespan_maker = makers.TimespanMaker(
        ...     initial_silence_durations=(
        ...         durationtools.Duration(0),
        ...         durationtools.Duration(1, 4),
        ...         )
        ...     )
        >>> print(format(timespan_maker))
        makers.TimespanMaker(
            initial_silence_durations=(
                durationtools.Duration(0, 1),
                durationtools.Duration(1, 4),
                ),
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

    ::

        >>> voice_names = ('Violin', 'Viola')
        >>> target_timespan = timespantools.Timespan(0, 1)
        >>> timespan_inventory = timespan_maker(
        ...     target_timespan=target_timespan,
        ...     voice_names=voice_names,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Violin',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Viola',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Violin',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
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
        can_split=None,
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
        if can_split is not None:
            can_split = bool(can_split)
        self._can_split = can_split

        if not isinstance(initial_silence_durations, collections.Sequence):
            initial_silence_durations = (initial_silence_durations,)
        initial_silence_durations = tuple(durationtools.Duration(x)
            for x in initial_silence_durations)
        assert all(0 <= x for x in initial_silence_durations)
        self._initial_silence_durations = initial_silence_durations

        self._minimum_duration = durationtools.Duration(minimum_duration)

        if not isinstance(playing_durations, collections.Sequence):
            playing_durations = (playing_durations,)
        playing_durations = tuple(durationtools.Duration(x)
            for x in playing_durations)
        assert len(playing_durations)
        assert all(0 < x for x in playing_durations)
        self._playing_durations = playing_durations

        if not isinstance(playing_groupings, collections.Sequence):
            playing_groupings = (playing_groupings,)
        playing_groupings = tuple(int(x) for x in playing_groupings)
        assert len(playing_groupings)
        assert all(0 < x for x in playing_groupings)
        self._playing_groupings = playing_groupings

        self._repeat = bool(repeat)

        if silence_durations is not None:
            if not isinstance(silence_durations, collections.Sequence):
                silence_durations = (silence_durations,)
            silence_durations = tuple(durationtools.Duration(x)
                for x in silence_durations)
            assert len(silence_durations)
            #assert all(0 < x for x in silence_durations)
        self._silence_durations = silence_durations

        assert step_anchor in (Left, Right)
        self._step_anchor = step_anchor
        self._synchronize_groupings = bool(synchronize_groupings)
        self._synchronize_step = bool(synchronize_step)

    ### SPECIAL METHODS ###

    def __call__(
        self,
        color=None,
        layer=None,
        music_specifier=None,
        target_timespan=None,
        timespan_inventory=None,
        voice_names=None,
        ):

        if target_timespan is None:
            raise TypeError

        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
        assert isinstance(timespan_inventory, timespantools.TimespanInventory)

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
        if silence_durations is None:
            silence_durations = (durationtools.Duration(0),)
        if len(silence_durations) < 2:
            silence_durations *= 2
        silence_durations = datastructuretools.StatalServer(
            silence_durations)()

        if self.synchronize_step:
            procedure = self._make_with_synchronized_step
        else:
            procedure = self._make_without_synchronized_step

        #print(format(initial_silence_durations))
        #print(format(playing_durations))
        #print(format(playing_groupings))
        #print(format(silence_durations))

        new_timespan_inventory, final_offset = procedure(
            color=color,
            initial_silence_durations=initial_silence_durations,
            layer=layer,
            music_specifier=music_specifier,
            playing_durations=playing_durations,
            playing_groupings=playing_groupings,
            silence_durations=silence_durations,
            target_timespan=target_timespan,
            voice_names=voice_names,
            )

        timespan_inventory.extend(new_timespan_inventory)
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

    def _make_with_synchronized_step(
        self,
        color=None,
        initial_silence_durations=None,
        layer=None,
        music_specifier=None,
        playing_durations=None,
        playing_groupings=None,
        silence_durations=None,
        target_timespan=None,
        voice_names=None,
        ):
        timespan_inventory = timespantools.TimespanInventory()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        if initial_silence_durations:
            start_offset += initial_silence_durations()[0]
        can_continue = True
        while start_offset < stop_offset and can_continue:
            if self.synchronize_groupings:
                grouping = playing_groupings()[0]
                durations = playing_durations(grouping)
            silence_duration = silence_durations()[0]
            for voice_name in voice_names:
                if not self.synchronize_groupings:
                    grouping = playing_groupings()[0]
                    durations = playing_durations(grouping)
                maximum_offset = start_offset + sum(durations) + \
                    silence_duration
                maximum_offset = min(maximum_offset, stop_offset)
                if self.step_anchor is Left:
                    maximum_offset = min(maximum_offset,
                        start_offset + silence_duration)
                current_offset = start_offset
                for duration in durations:
                    if maximum_offset < (current_offset + duration):
                        can_continue = False
                        break
                    timespan = self._make_performed_timespan(
                        color=color,
                        layer=layer,
                        music_specifier=music_specifier,
                        start_offset=current_offset,
                        stop_offset=current_offset + duration,
                        voice_name=voice_name,
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
        color=None,
        initial_silence_durations=None,
        layer=None,
        music_specifier=None,
        playing_durations=None,
        playing_groupings=None,
        silence_durations=None,
        target_timespan=None,
        voice_names=None,
        ):
        timespan_inventory = timespantools.TimespanInventory()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        final_offset = durationtools.Offset(0)
        for voice_name in voice_names:
            start_offset = target_timespan.start_offset
            if initial_silence_durations:
                start_offset += initial_silence_durations()[0]
            can_continue = True
            while start_offset < stop_offset and can_continue:
                silence_duration = silence_durations()[0]
                grouping = playing_groupings()[0]
                durations = playing_durations(grouping)
                maximum_offset = start_offset + sum(durations) + \
                    silence_duration
                maximum_offset = min(maximum_offset, stop_offset)
                if self.step_anchor is Left:
                    maximum_offset = min(maximum_offset,
                        start_offset + silence_duration)
                current_offset = start_offset
                for duration in durations:
                    if maximum_offset < (current_offset + duration):
                        can_continue = False
                        break
                    timespan = self._make_performed_timespan(
                        color=color,
                        layer=layer,
                        music_specifier=music_specifier,
                        start_offset=current_offset,
                        stop_offset=current_offset + duration,
                        voice_name=voice_name,
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

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='can_split',
                display_string='can split',
                command='cp',
                editor=idetools.getters.get_boolean,
                ),
            systemtools.AttributeDetail(
                name='initial_silence_durations',
                display_string='initial silence durations',
                command='is',
                editor=idetools.getters.get_durations,
                ),
            systemtools.AttributeDetail(
                name='minimum_duration',
                display_string='minimum duration',
                command='md',
                editor=idetools.getters.get_duration,
                ),
            systemtools.AttributeDetail(
                name='playing_durations',
                display_string='playing durations',
                command='pd',
                editor=idetools.getters.get_durations,
                ),
            systemtools.AttributeDetail(
                name='playing_groupings',
                display_string='playing groupings',
                command='pg',
                editor=idetools.getters.get_nonnegative_integers,
                ),
            systemtools.AttributeDetail(
                name='repeat',
                display_string='repeat',
                command='rp',
                editor=idetools.getters.get_boolean,
                ),
            systemtools.AttributeDetail(
                name='silence_durations',
                display_string='silence durations',
                command='sd',
                editor=idetools.getters.get_durations,
                ),
            systemtools.AttributeDetail(
                name='step_anchor',
                display_string='step anchor',
                command='sa',
                editor=idetools.getters.get_durations,
                ),
            systemtools.AttributeDetail(
                name='synchronize_groupings',
                display_string='synchonize groupings',
                command='sg',
                editor=idetools.getters.get_boolean,
                ),
            systemtools.AttributeDetail(
                name='synchronize_step',
                display_string='synchonize step',
                command='sy',
                editor=idetools.getters.get_boolean,
                ),
            )

    ### PUBLIC PROPERTIES ###

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