# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import rhythmmakertools
from abjad.tools import timespantools
from consort.makers.TimespanMaker import TimespanMaker
from scoremanager import idetools
import collections


class TaleaTimespanMaker(TimespanMaker):
    r'''A talea timespan maker.

    ::

        >>> from consort import makers
        >>> timespan_maker = makers.TaleaTimespanMaker(
        ...     initial_silence_talea=rhythmmakertools.Talea(
        ...         counts=(0, 4),
        ...         denominator=16,
        ...         )
        ...     )
        >>> print(format(timespan_maker))
        makers.TaleaTimespanMaker(
            initial_silence_talea=rhythmmakertools.Talea(
                counts=(0, 4),
                denominator=16,
                ),
            playing_talea=rhythmmakertools.Talea(
                counts=(4,),
                denominator=16,
                ),
            playing_groupings=(1,),
            repeat=True,
            silence_talea=rhythmmakertools.Talea(
                counts=(4,),
                denominator=16,
                ),
            step_anchor=Right,
            synchronize_groupings=False,
            synchronize_step=False,
            )

    ::

        >>> music_specifiers = {
        ...     'Violin': None,
        ...     'Viola': None,
        ...     }
        >>> target_timespan = timespantools.Timespan(0, 1)
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Violin',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Viola',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Violin',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola',
                    ),
                ]
            )

    ::

        >>> timespan_maker = new(timespan_maker,
        ...     initial_silence_talea=None,
        ...     synchronize_step=True,
        ...     )
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Violin',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Viola',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Violin',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Viola',
                    ),
                ]
            )

    ::

        >>> timespan_maker = new(timespan_maker,
        ...     initial_silence_talea=rhythmmakertools.Talea(
        ...         counts=(0, 2),
        ...         denominator=16,
        ...         ),
        ...     )
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Viola',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 8),
                    stop_offset=durationtools.Offset(3, 8),
                    voice_name='Violin',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(5, 8),
                    stop_offset=durationtools.Offset(7, 8),
                    voice_name='Viola',
                    ),
                makers.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_initial_silence_talea',
        '_playing_talea',
        '_playing_groupings',
        '_repeat',
        '_silence_talea',
        '_step_anchor',
        '_synchronize_groupings',
        '_synchronize_step',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        can_split=None,
        initial_silence_talea=None,
        minimum_duration=None,
        playing_talea=rhythmmakertools.Talea(
            counts=[4],
            denominator=16,
            ),
        playing_groupings=(1,),
        repeat=True,
        silence_talea=rhythmmakertools.Talea(
            counts=[4],
            denominator=16,
            ),
        step_anchor=Right,
        synchronize_groupings=False,
        synchronize_step=False,
        ):
        TimespanMaker.__init__(
            self,
            can_split=can_split,
            minimum_duration=minimum_duration,
            )

        if initial_silence_talea is not None:
            assert isinstance(initial_silence_talea, rhythmmakertools.Talea)
            assert initial_silence_talea.counts
            assert all(0 <= x for x in initial_silence_talea.counts)
        self._initial_silence_talea = initial_silence_talea

        assert isinstance(playing_talea, rhythmmakertools.Talea)
        assert playing_talea.counts
        assert all(0 < x for x in playing_talea.counts)
        self._playing_talea = playing_talea

        if not isinstance(playing_groupings, collections.Sequence):
            playing_groupings = (playing_groupings,)
        playing_groupings = tuple(int(x) for x in playing_groupings)
        assert len(playing_groupings)
        assert all(0 < x for x in playing_groupings)
        self._playing_groupings = playing_groupings

        self._repeat = bool(repeat)

        if silence_talea is not None:
            assert isinstance(silence_talea, rhythmmakertools.Talea)
            assert silence_talea.counts
            assert all(0 <= x for x in silence_talea.counts)
        self._silence_talea = silence_talea

        assert step_anchor in (Left, Right)
        self._step_anchor = step_anchor
        self._synchronize_groupings = bool(synchronize_groupings)
        self._synchronize_step = bool(synchronize_step)

    ### PRIVATE METHODS ###

    def _make_infinite_iterator(self, sequence):
        index = 0
        sequence = datastructuretools.CyclicTuple(sequence)
        while True:
            yield sequence[index]
            index += 1

    def _make_timespans(
        self,
        color=None,
        layer=None,
        music_specifiers=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        initial_silence_talea = self.initial_silence_talea
        if not initial_silence_talea:
            initial_silence_talea = rhythmmakertools.Talea((0,), 1)
        initial_silence_talea = iter(initial_silence_talea)
        playing_talea = iter(self.playing_talea)
        playing_groupings = self._make_infinite_iterator(
            self.playing_groupings,
            )
        silence_talea = self.silence_talea
        if silence_talea is None:
            silence_talea = rhythmmakertools.Talea((0,), 1)
        silence_talea = iter(silence_talea)
        if self.synchronize_step:
            procedure = self._make_with_synchronized_step
        else:
            procedure = self._make_without_synchronized_step
        new_timespan_inventory, final_offset = procedure(
            color=color,
            initial_silence_talea=initial_silence_talea,
            layer=layer,
            playing_talea=playing_talea,
            playing_groupings=playing_groupings,
            music_specifiers=music_specifiers,
            silence_talea=silence_talea,
            target_timespan=target_timespan,
            )
        timespan_inventory.extend(new_timespan_inventory)
        return timespan_inventory

    def _make_with_synchronized_step(
        self,
        color=None,
        initial_silence_talea=None,
        layer=None,
        playing_talea=None,
        playing_groupings=None,
        music_specifiers=None,
        silence_talea=None,
        target_timespan=None,
        ):
        timespan_inventory = timespantools.TimespanInventory()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        start_offset += next(initial_silence_talea)
        can_continue = True
        while start_offset < stop_offset and can_continue:
            if self.synchronize_groupings:
                grouping = next(playing_groupings)
                durations = [next(playing_talea) for _ in range(grouping)]
            silence_duration = next(silence_talea)
            for voice_name, music_specifier in music_specifiers.items():
                initial_silence_duration = next(initial_silence_talea)
                if not self.synchronize_groupings:
                    grouping = next(playing_groupings)
                    durations = [next(playing_talea) for _ in range(grouping)]
                maximum_offset = (
                    start_offset +
                    sum(durations) +
                    silence_duration +
                    initial_silence_duration
                    )
                maximum_offset = min(maximum_offset, stop_offset)
                if self.step_anchor is Left:
                    maximum_offset = min(
                        maximum_offset,
                        (
                            initial_silence_duration +
                            start_offset +
                            silence_duration
                            ),
                        )
                current_offset = start_offset + initial_silence_duration
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
        initial_silence_talea=None,
        layer=None,
        playing_talea=None,
        playing_groupings=None,
        music_specifiers=None,
        silence_talea=None,
        target_timespan=None,
        ):
        timespan_inventory = timespantools.TimespanInventory()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        final_offset = durationtools.Offset(0)
        for voice_name, music_specifier in music_specifiers.items():
            start_offset = target_timespan.start_offset
            start_offset += next(initial_silence_talea)
            can_continue = True
            while start_offset < stop_offset and can_continue:
                silence_duration = next(silence_talea)
                grouping = next(playing_groupings)
                durations = [next(playing_talea) for _ in range(grouping)]
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
                name='initial_silence_talea',
                display_string='initial silence talea',
                command='it',
                editor=rhythmmakertools.Talea,
                ),
            systemtools.AttributeDetail(
                name='minimum_duration',
                display_string='minimum duration',
                command='md',
                editor=idetools.getters.get_duration,
                ),
            systemtools.AttributeDetail(
                name='playing_talea',
                display_string='playing talea',
                command='pt',
                editor=rhythmmakertools.Talea,
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
                name='silence_talea',
                display_string='silence talea',
                command='st',
                editor=rhythmmakertools.Talea,
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
    def initial_silence_talea(self):
        return self._initial_silence_talea

    @property
    def playing_talea(self):
        return self._playing_talea

    @property
    def playing_groupings(self):
        return self._playing_groupings

    @property
    def repeat(self):
        return self._repeat

    @property
    def silence_talea(self):
        return self._silence_talea

    @property
    def step_anchor(self):
        return self._step_anchor

    @property
    def synchronize_groupings(self):
        return self._synchronize_groupings

    @property
    def synchronize_step(self):
        return self._synchronize_step