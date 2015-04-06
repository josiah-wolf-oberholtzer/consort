# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from abjad.tools import mathtools
from abjad.tools import sequencetools
from abjad.tools import timespantools
from consort.tools.TimespanMaker import TimespanMaker


class DependentTimespanMaker(TimespanMaker):
    r'''A dependent timespan-maker.

    ::

        >>> import consort
        >>> timespan_maker = consort.DependentTimespanMaker(
        ...     include_inner_starts=True,
        ...     include_inner_stops=True,
        ...     voice_names=(
        ...         'Viola Voice',
        ...          ),
        ...     )
        >>> print(format(timespan_maker))
        consort.tools.DependentTimespanMaker(
            include_inner_starts=True,
            include_inner_stops=True,
            voice_names=('Viola Voice',),
            )

    ::

        >>> timespan_inventory = timespantools.TimespanInventory([
        ...     consort.tools.PerformedTimespan(
        ...         voice_name='Viola Voice',
        ...         start_offset=(1, 4),
        ...         stop_offset=(1, 1),
        ...         ),
        ...     consort.tools.PerformedTimespan(
        ...         voice_name='Viola Voice',
        ...         start_offset=(3, 4),
        ...         stop_offset=(3, 2),
        ...         ),
        ...     ])

    ::

        >>> music_specifiers = {
        ...     'Violin Voice': None,
        ...     'Cello Voice': None,
        ...     }
        >>> target_timespan = timespantools.Timespan((1, 2), (2, 1))
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     timespan_inventory=timespan_inventory,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Cello Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Violin Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Cello Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Viola Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Cello Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Violin Voice',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_include_inner_starts',
        '_include_inner_stops',
        '_labels',
        '_rotation_indices',
        '_voice_names',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        include_inner_starts=None,
        include_inner_stops=None,
        labels=None,
        output_masks=None,
        padding=None,
        rotation_indices=None,
        timespan_specifier=None,
        voice_names=None,
        ):
        TimespanMaker.__init__(
            self,
            output_masks=output_masks,
            padding=padding,
            timespan_specifier=timespan_specifier,
            )
        if include_inner_starts is not None:
            include_inner_starts = bool(include_inner_starts)
        self._include_inner_starts = include_inner_starts
        if include_inner_stops is not None:
            include_inner_stops = bool(include_inner_stops)
        self._include_inner_stops = include_inner_stops
        if rotation_indices is not None:
            if not isinstance(rotation_indices, collections.Sequence):
                rotation_indices = int(rotation_indices)
                rotation_indices = (rotation_indices,)
            rotation_indices = tuple(rotation_indices)
        self._rotation_indices = rotation_indices
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
        rotation_indices = self.rotation_indices or (0,)
        rotation_indices = datastructuretools.CyclicTuple(rotation_indices)
        context_counter = collections.Counter()
        preexisting_timespans = self._collect_preexisting_timespans(
            target_timespan=target_timespan,
            timespan_inventory=timespan_inventory,
            )
        for group_index, group in enumerate(
            preexisting_timespans.partition(True)
            ):
            rotation_index = rotation_indices[group_index]
            offsets = set()
            offsets.add(group.start_offset)
            offsets.add(group.stop_offset)
            for timespan in group:
                if self.include_inner_starts:
                    offsets.add(timespan.start_offset)
                if self.include_inner_stops:
                    offsets.add(timespan.stop_offset)
            offsets = tuple(sorted(offsets))
            durations = mathtools.difference_series(offsets)
            durations = sequencetools.rotate_sequence(
                durations, rotation_index)
            start_offset = offsets[0]
            for context_name, music_specifier in music_specifiers.items():
                context_seed = context_counter[context_name]
                timespans = music_specifier(
                    durations=durations,
                    layer=layer,
                    output_masks=self.output_masks,
                    padding=self.padding,
                    seed=context_seed,
                    start_offset=start_offset,
                    timespan_specifier=self.timespan_specifier,
                    voice_name=context_name,
                    )
                context_counter[context_name] += 1
                new_timespans.extend(timespans)
        return new_timespans

    ### PUBLIC PROPERTIES ###

    @property
    def include_inner_starts(self):
        return self._include_inner_starts

    @property
    def include_inner_stops(self):
        return self._include_inner_stops

    @property
    def is_dependent(self):
        return True

    @property
    def labels(self):
        return self._labels

    @property
    def rotation_indices(self):
        return self._rotation_indices

    @property
    def voice_names(self):
        return self._voice_names