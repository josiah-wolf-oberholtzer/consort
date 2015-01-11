# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad import new
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import rhythmmakertools
from abjad.tools import timespantools
from consort.tools.TimespanMaker import TimespanMaker


class TaleaTimespanMaker(TimespanMaker):
    r'''A talea timespan maker.

    ::

        >>> import consort
        >>> timespan_maker = consort.TaleaTimespanMaker(
        ...     initial_silence_talea=rhythmmakertools.Talea(
        ...         counts=(0, 4),
        ...         denominator=16,
        ...         )
        ...     )
        >>> print(format(timespan_maker))
        consort.tools.TaleaTimespanMaker(
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

        >>> import collections
        >>> music_specifiers = collections.OrderedDict([
        ...     ('Violin', None),
        ...     ('Viola', None),
        ...     ])
        >>> target_timespan = timespantools.Timespan(0, 1)
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Violin',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Viola',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Violin',
                    ),
                consort.tools.PerformedTimespan(
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
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Viola',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Violin',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Viola',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Violin',
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
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Viola',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 8),
                    stop_offset=durationtools.Offset(3, 8),
                    voice_name='Violin',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(5, 8),
                    stop_offset=durationtools.Offset(7, 8),
                    voice_name='Viola',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_fuse_groups',
        '_initial_silence_talea',
        '_padding',
        '_playing_talea',
        '_playing_groupings',
        '_reflect',
        '_repeat',
        '_silence_talea',
        '_step_anchor',
        '_synchronize_groupings',
        '_synchronize_step',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        fuse_groups=None,
        initial_silence_talea=None,
        padding=None,
        playing_talea=rhythmmakertools.Talea(
            counts=[4],
            denominator=16,
            ),
        playing_groupings=(1,),
        reflect=None,
        repeat=True,
        seed=None,
        silence_talea=rhythmmakertools.Talea(
            counts=[4],
            denominator=16,
            ),
        step_anchor=Right,
        synchronize_groupings=False,
        synchronize_step=False,
        timespan_specifier=None,
        ):
        TimespanMaker.__init__(
            self,
            padding=padding,
            seed=seed,
            timespan_specifier=timespan_specifier,
            )

        if fuse_groups is not None:
            fuse_groups = bool(fuse_groups)
        self._fuse_groups = fuse_groups

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

        if reflect is not None:
            reflect = bool(reflect)
        self._reflect = reflect

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

    def _fuse_timespans(self, timespans):
        import consort
        if not timespans:
            return timespans
        if not self.padding:
            fused_timespan = new(
                timespans[0],
                stop_offset=timespans[-1].stop_offset,
                )
            timespans[:] = [fused_timespan]
            return timespans
        if len(timespans) == 1:
            pass
        elif len(timespans) == 2:
            pass
        elif isinstance(timespans[-1], consort.PerformedTimespan):
            fused_timespan = new(
                timespans[1],
                stop_offset=timespans[-1].stop_offset,
                )
            timespans[1:] = [fused_timespan]
        else:
            fused_timespan = new(
                timespans[1],
                stop_offset=timespans[-2].stop_offset,
                )
            timespans[1:-1] = [fused_timespan]
        return timespans

    def _make_infinite_iterator(self, sequence):
        index = 0
        sequence = datastructuretools.CyclicTuple(sequence)
        while True:
            yield sequence[index]
            index += 1

    def _make_timespans(
        self,
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

        if self.seed is not None and 0 < self.seed:
            for _ in range(self.seed):
                next(initial_silence_talea)
                next(playing_talea)
                next(playing_groupings)
                next(silence_talea)

        if self.synchronize_step:
            procedure = self._make_with_synchronized_step
        else:
            procedure = self._make_without_synchronized_step
        new_timespan_inventory, final_offset = procedure(
            initial_silence_talea=initial_silence_talea,
            layer=layer,
            playing_talea=playing_talea,
            playing_groupings=playing_groupings,
            music_specifiers=music_specifiers,
            silence_talea=silence_talea,
            target_timespan=target_timespan,
            )
        
        if self.reflect:
            new_timespan_inventory = new_timespan_inventory.reflect(
                axis=target_timespan.axis,
                )

        timespan_inventory.extend(new_timespan_inventory)
        return timespan_inventory

    def _make_with_synchronized_step(
        self,
        initial_silence_talea=None,
        layer=None,
        playing_talea=None,
        playing_groupings=None,
        music_specifiers=None,
        silence_talea=None,
        target_timespan=None,
        ):
        import consort
        counter = collections.Counter()
        timespan_inventory = timespantools.TimespanInventory()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        start_offset += next(initial_silence_talea)
        can_continue = True
        while start_offset < stop_offset and can_continue:
            silence_duration = next(silence_talea)
            durations = []
            if self.synchronize_groupings:
                grouping = next(playing_groupings)
                durations = [next(playing_talea) for _ in range(grouping)]
            for context_name, music_specifier in music_specifiers.items():
                if context_name not in counter:
                    counter[context_name] = 0
                seed = counter[context_name]
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
                if self.padding:
                    maximum_offset += (self.padding * 2)
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
                if self.padding:
                    current_offset += self.padding
                    maximum_offset -= self.padding
                group_offset = current_offset

                valid_durations = []
                for duration in durations:
                    if maximum_offset < (current_offset + duration):
                        can_continue = False
                        break
                    valid_durations.append(duration)
                if self.fuse_groups:
                    valid_durations = [sum(valid_durations)]

                new_timespans = music_specifier(
                    durations=valid_durations,
                    layer=layer,
                    padding=self.padding,
                    seed=seed,
                    start_offset=group_offset,
                    timespan_specifier=self.timespan_specifier,
                    voice_name=context_name,
                    )

#                new_timespans = []
#                for i, duration in enumerate(durations):
#                    if maximum_offset < (current_offset + duration):
#                        can_continue = False
#                        if self.padding:
#                            timespan = consort.SilentTimespan(
#                                layer=layer,
#                                start_offset=current_offset,
#                                stop_offset=current_offset + self.padding,
#                                voice_name=context_name,
#                                )
#                            new_timespans.append(timespan)
#                        break
#                    if self.padding:
#                        if i == 0:
#                            timespan = consort.SilentTimespan(
#                                layer=layer,
#                                start_offset=current_offset,
#                                stop_offset=current_offset + duration,
#                                voice_name=context_name,
#                                )
#                        elif i == len(durations) - 1:
#                            timespan = consort.SilentTimespan(
#                                layer=layer,
#                                start_offset=current_offset,
#                                stop_offset=current_offset + duration,
#                                voice_name=context_name,
#                                )
#                        else:
#                            timespan = self._make_performed_timespan(
#                                layer=layer,
#                                music_specifier=current_music_specifier,
#                                start_offset=current_offset,
#                                stop_offset=current_offset + duration,
#                                voice_name=context_name,
#                                )
#                    else:
#                        timespan = self._make_performed_timespan(
#                            layer=layer,
#                            music_specifier=current_music_specifier,
#                            start_offset=current_offset,
#                            stop_offset=current_offset + duration,
#                            voice_name=context_name,
#                            )
#                    new_timespans.append(timespan)
#                    current_offset += duration
#                if new_timespans and self.fuse_groups:
#                    new_timespans = self._fuse_timespans(new_timespans)

                if all(isinstance(_, consort.SilentTimespan)
                    for _ in new_timespans):
                    new_timespans[:] = []
                timespan_inventory.extend(new_timespans)
                counter[context_name] += 1
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
        initial_silence_talea=None,
        layer=None,
        playing_talea=None,
        playing_groupings=None,
        music_specifiers=None,
        silence_talea=None,
        target_timespan=None,
        ):
        import consort
        counter = collections.Counter()
        timespan_inventory = timespantools.TimespanInventory()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        final_offset = durationtools.Offset(0)
        for context_name, music_specifier in music_specifiers.items():

            if context_name not in counter:
                counter[context_name] = 0

            start_offset = target_timespan.start_offset
            start_offset += next(initial_silence_talea)
            can_continue = True

            while start_offset < stop_offset and can_continue:

                seed = counter[context_name]

                silence_duration = next(silence_talea)
                grouping = next(playing_groupings)
                durations = [next(playing_talea) for _ in range(grouping)]
                if self.padding:
                    start_offset += self.padding
                maximum_offset = start_offset + sum(durations) + \
                    silence_duration
                maximum_offset = min(maximum_offset, stop_offset)
                if self.step_anchor is Left:
                    maximum_offset = min(maximum_offset,
                        start_offset + silence_duration)
                if self.padding:
                    maximum_offset -= self.padding
                current_offset = start_offset
                group_offset = start_offset

                valid_durations = []
                for duration in durations:
                    if maximum_offset < (current_offset + duration):
                        can_continue = False
                        break
                    valid_durations.append(duration)
                    current_offset += duration
                if self.fuse_groups:
                    valid_durations = [sum(valid_durations)]

                new_timespans = music_specifier(
                    durations=valid_durations,
                    layer=layer,
                    padding=self.padding,
                    seed=seed,
                    start_offset=group_offset,
                    timespan_specifier=self.timespan_specifier,
                    voice_name=context_name,
                    )

#                new_timespans = []
#                for i, duration in enumerate(durations):
#                    if maximum_offset < (current_offset + duration):
#                        can_continue = False
#                        if self.padding:
#                            timespan = consort.SilentTimespan(
#                                layer=layer,
#                                start_offset=current_offset,
#                                stop_offset=current_offset + self.padding,
#                                voice_name=context_name,
#                                )
#                            new_timespans.append(timespan)
#                        break
#                    if self.padding:
#                        if i == 0:
#                            timespan = consort.SilentTimespan(
#                                layer=layer,
#                                start_offset=current_offset,
#                                stop_offset=current_offset + duration,
#                                voice_name=context_name,
#                                )
#                        elif i == len(durations) - 1:
#                            timespan = consort.SilentTimespan(
#                                layer=layer,
#                                start_offset=current_offset,
#                                stop_offset=current_offset + duration,
#                                voice_name=context_name,
#                                )
#                        else:
#                            timespan = self._make_performed_timespan(
#                                layer=layer,
#                                music_specifier=current_music_specifier,
#                                start_offset=current_offset,
#                                stop_offset=current_offset + duration,
#                                voice_name=context_name,
#                                )
#                    else:
#                        timespan = self._make_performed_timespan(
#                            layer=layer,
#                            music_specifier=current_music_specifier,
#                            start_offset=current_offset,
#                            stop_offset=current_offset + duration,
#                            voice_name=context_name,
#                            )
#                    new_timespans.append(timespan)
#                    current_offset += duration
#                if new_timespans and self.fuse_groups:
#                    new_timespans = self._fuse_timespans(new_timespans)

                if all(isinstance(_, consort.SilentTimespan)
                    for _ in new_timespans):
                    new_timespans = []
                timespan_inventory.extend(new_timespans)
                if self.step_anchor is Left:
                    start_offset += silence_duration
                else:
                    start_offset = current_offset + silence_duration
                if not self.repeat:
                    break
                counter[context_name] += 1
            if final_offset < start_offset:
                final_offset = start_offset
        return timespan_inventory, final_offset

    ### PUBLIC PROPERTIES ###

    @property
    def fuse_groups(self):
        return self._fuse_groups

    @property
    def initial_silence_talea(self):
        return self._initial_silence_talea

    @property
    def playing_groupings(self):
        return self._playing_groupings

    @property
    def playing_talea(self):
        return self._playing_talea

    @property
    def reflect(self):
        return self._reflect

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