# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from abjad.tools import mathtools
from abjad.tools import sequencetools
from abjad.tools import timespantools
from consort.tools.TimespanMaker import TimespanMaker


class DependentTimespanMaker(TimespanMaker):
    r'''A dependent timespan maker.

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
        can_split=None,
        include_inner_starts=None,
        include_inner_stops=None,
        labels=None,
        minimum_duration=None,
        rotation_indices=None,
        voice_names=None,
        ):
        TimespanMaker.__init__(
            self,
            can_split=can_split,
            minimum_duration=minimum_duration,
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

    def _make_timespans(
        self,
        layer=None,
        music_specifiers=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        if not self.voice_names:
            return
        preexisting_timespans = timespantools.TimespanInventory()
        for timespan in timespan_inventory:
            if timespan.voice_name in self.voice_names:
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
        rotation_indices = self.rotation_indices or (0,)
        rotation_indices = datastructuretools.CyclicTuple(rotation_indices)
        voice_counter = collections.Counter()
        groups = preexisting_timespans.partition(
            include_tangent_timespans=True,
            )
        for group_index, group in enumerate(groups):
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
            offsets = [_ + offsets[0]
                for _ in mathtools.cumulative_sums(durations)]
            for start_offset, stop_offset in \
                sequencetools.iterate_sequence_nwise(offsets, 2):
                for voice_name, music_specifier in music_specifiers.items():
                    if not isinstance(music_specifier, tuple):
                        music_specifier = datastructuretools.CyclicTuple(
                            [music_specifier])
                    if voice_name not in voice_counter:
                        voice_counter[voice_name] = 0
                    music_specifier_index = voice_counter[voice_name]
                    current_music_specifier = \
                        music_specifier[music_specifier_index]
                    timespan = self._make_performed_timespan(
                        layer=layer,
                        music_specifier=current_music_specifier,
                        start_offset=start_offset,
                        stop_offset=stop_offset,
                        voice_name=voice_name,
                        )
                    timespan_inventory.append(timespan)
                    voice_counter[voice_name] += 1

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        from ide import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='can_split',
                display_string='can split',
                command='cp',
                editor=idetools.getters.get_boolean,
                ),
            systemtools.AttributeDetail(
                name='minimum_duration',
                display_string='minimum duration',
                command='md',
                editor=idetools.getters.get_duration,
                ),
            systemtools.AttributeDetail(
                name='labels',
                display_string='labels',
                command='l',
                editor=idetools.getters.get_strings,
                ),
            systemtools.AttributeDetail(
                name='voice_names',
                display_string='voice names',
                command='vn',
                editor=idetools.getters.get_strings,
                ),
            )

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