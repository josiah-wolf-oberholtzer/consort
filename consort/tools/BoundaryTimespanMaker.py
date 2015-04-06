# -*- encoding: utf-8 -*-
import collections
from abjad.tools import durationtools
from abjad.tools import timespantools
from consort.tools.TimespanMaker import TimespanMaker


class BoundaryTimespanMaker(TimespanMaker):
    r'''A boundary timespan-maker.

    ::

        >>> import consort
        >>> timespan_maker = consort.BoundaryTimespanMaker(
        ...     start_duration=(1, 2),
        ...     stop_duration=(1, 4),
        ...     voice_names=('Violin 1 Voice', 'Violin 2 Voice'),
        ...     )
        >>> print(format(timespan_maker))
        consort.tools.BoundaryTimespanMaker(
            start_duration=durationtools.Duration(1, 2),
            stop_duration=durationtools.Duration(1, 4),
            voice_names=('Violin 1 Voice', 'Violin 2 Voice'),
            )

    ::

        >>> timespan_inventory = timespantools.TimespanInventory([
        ...     consort.PerformedTimespan(
        ...         start_offset=0,
        ...         stop_offset=1,
        ...         voice_name='Violin 1 Voice',
        ...         ),
        ...     consort.PerformedTimespan(
        ...         start_offset=(1, 2),
        ...         stop_offset=(3, 2),
        ...         voice_name='Violin 2 Voice',
        ...         ),
        ...     consort.PerformedTimespan(
        ...         start_offset=3,
        ...         stop_offset=4,
        ...         voice_name='Violin 2 Voice',
        ...         ),
        ...     ])

    ::

        >>> music_specifiers = {'Cello Voice': None}
        >>> target_timespan = timespantools.Timespan(0, 10)
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     timespan_inventory=timespan_inventory,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Cello Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin 1 Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Violin 2 Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 2),
                    stop_offset=durationtools.Offset(7, 4),
                    voice_name='Cello Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 1),
                    stop_offset=durationtools.Offset(7, 2),
                    voice_name='Cello Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 1),
                    stop_offset=durationtools.Offset(4, 1),
                    voice_name='Violin 2 Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(4, 1),
                    stop_offset=durationtools.Offset(17, 4),
                    voice_name='Cello Voice',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_labels',
        '_start_duration',
        '_stop_duration',
        '_voice_names',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        start_duration=None,
        stop_duration=None,
        labels=None,
        output_masks=None,
        padding=None,
        timespan_specifier=None,
        voice_names=None,
        ):
        TimespanMaker.__init__(
            self,
            output_masks=output_masks,
            padding=padding,
            timespan_specifier=timespan_specifier,
            )
        if start_duration is not None:
            start_duration = durationtools.Duration(start_duration)
            assert 0 < start_duration
        self._start_duration = start_duration
        if stop_duration is not None:
            stop_duration = durationtools.Duration(stop_duration)
            assert 0 < stop_duration
        self._stop_duration = stop_duration
        if labels is not None:
            if isinstance(labels, str):
                labels = (labels,)
            labels = tuple(str(_) for _ in labels)
        self._labels = labels
        if voice_names is not None:
            voice_names = tuple(voice_names)
        self._voice_names = voice_names

    ### PRIVATE METHODS ###

    def _collect_preexisting_timespans(
        self,
        target_timespan=None,
        timespan_inventory=None,
        ):
        import consort
        preexisting_timespans = timespantools.TimespanInventory()
        for timespan in timespan_inventory:
            if not isinstance(timespan, consort.PerformedTimespan):
                continue
            if timespan.voice_name not in self.voice_names:
                continue
            if not self.labels:
                preexisting_timespans.append(timespan)
            elif not hasattr(timespan, 'music_specifier') or \
                not timespan.music_specifier or \
                not timespan.music_specifier.labels:
                continue
            elif any(label in timespan.music_specifier.labels
                for label in self.labels):
                preexisting_timespans.append(timespan)
        preexisting_timespans & target_timespan
        return preexisting_timespans

    def _make_timespans(
        self,
        layer=None,
        music_specifiers=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        new_timespans = timespantools.TimespanInventory()
        if not self.voice_names:
            return new_timespans
        context_counter = collections.Counter()
        preexisting_timespans = self._collect_preexisting_timespans(
            target_timespan=target_timespan,
            timespan_inventory=timespan_inventory,
            )
        for group_index, group in enumerate(
            preexisting_timespans.partition(True)
            ):
            for context_name, music_specifier in music_specifiers.items():
                context_seed = context_counter[context_name]
                if self.start_duration:
                    timespans = music_specifier(
                        durations=[self.start_duration],
                        layer=layer,
                        output_masks=self.output_masks,
                        padding=self.padding,
                        seed=context_seed,
                        start_offset=group.start_offset,
                        timespan_specifier=self.timespan_specifier,
                        voice_name=context_name,
                        )
                    context_counter[context_name] += 1
                    new_timespans.extend(timespans)
                if self.stop_duration:
                    timespans = music_specifier(
                        durations=[self.stop_duration],
                        layer=layer,
                        output_masks=self.output_masks,
                        padding=self.padding,
                        seed=context_seed,
                        start_offset=group.stop_offset,
                        timespan_specifier=self.timespan_specifier,
                        voice_name=context_name,
                        )
                    context_counter[context_name] += 1
                    new_timespans.extend(timespans)
        return new_timespans

    ### PUBLIC PROPERTIES ###

    @property
    def labels(self):
        return self._labels

    @property
    def start_duration(self):
        return self._start_duration

    @property
    def stop_duration(self):
        return self._stop_duration

    @property
    def voice_names(self):
        return self._voice_names