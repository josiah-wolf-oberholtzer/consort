# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from abjad.tools import sequencetools
from abjad.tools import timespantools
from consort.makers.TimespanMaker import TimespanMaker


class DependentTimespanMaker(TimespanMaker):
    r'''A dependent timespan maker.

    ::

        >>> from consort import makers
        >>> timespan_maker = makers.DependentTimespanMaker(
        ...     voice_names=(
        ...         'Viola Voice',
        ...          ),
        ...     )
        >>> print(format(timespan_maker))
        consort.makers.DependentTimespanMaker(
            voice_names=('Viola Voice',),
            )

    ::

        >>> timespan_inventory = timespantools.TimespanInventory([
        ...     makers.PerformedTimespan(
        ...         voice_name='Viola Voice',
        ...         start_offset=(1, 4),
        ...         stop_offset=(1, 1),
        ...         ),
        ...     makers.PerformedTimespan(
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
                consort.makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Voice',
                    ),
                consort.makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Violin Voice',
                    ),
                consort.makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Cello Voice',
                    ),
                consort.makers.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin Voice',
                    ),
                consort.makers.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Cello Voice',
                    ),
                consort.makers.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Viola Voice',
                    ),
                consort.makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Violin Voice',
                    ),
                consort.makers.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Cello Voice',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_voice_names',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        can_split=None,
        minimum_duration=None,
        voice_names=None,
        ):
        TimespanMaker.__init__(
            self,
            can_split=can_split,
            minimum_duration=minimum_duration,
            )
        if voice_names is not None:
            voice_names = tuple(voice_names)
        self._voice_names = voice_names

    ### PRIVATE METHODS ###

    def _make_timespans(
        self,
        color=None,
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
                preexisting_timespans.append(timespan)
        #preexisting_timespans.compute_logical_or()
        preexisting_timespans & target_timespan
        counter = collections.Counter()
        for voice_name, music_specifier in music_specifiers.items():
            for group in preexisting_timespans.partition(
                include_tangent_timespans=True):
                offsets = set()
                for timespan in group:
                    offsets.add(timespan.start_offset)
                    offsets.add(timespan.stop_offset)
                offsets = tuple(sorted(offsets))
                for start_offset, stop_offset in \
                    sequencetools.iterate_sequence_nwise(offsets, 2):

                    if not isinstance(music_specifier, tuple):
                        music_specifier = datastructuretools.CyclicTuple(
                            [music_specifier])
                    if voice_name not in counter:
                        counter[voice_name] = 0
                    music_specifier_index = counter[voice_name]
                    current_music_specifier = \
                        music_specifier[music_specifier_index]

                    timespan = self._make_performed_timespan(
                        color=color,
                        layer=layer,
                        music_specifier=current_music_specifier,
                        start_offset=start_offset,
                        stop_offset=stop_offset,
                        voice_name=voice_name,
                        )
                    timespan_inventory.append(timespan)

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        from scoremanager import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='can_split',
                display_string='can split',
                command='cp',
                editor=idetools.getters.get_boolean,
                ),
            systemtools.AttributeDetail(
                name='voice_names',
                display_string='voice names',
                command='vn',
                editor=idetools.getters.get_strings,
                ),
            systemtools.AttributeDetail(
                name='minimum_duration',
                display_string='minimum duration',
                command='md',
                editor=idetools.getters.get_duration,
                ),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def is_dependent(self):
        return True

    @property
    def voice_names(self):
        return self._voice_names