# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from consort.tools.TimespanMaker import TimespanMaker


class FloodedTimespanMaker(TimespanMaker):
    r'''A flooded timespan maker.

    ::

        >>> import consort
        >>> timespan_maker = consort.FloodedTimespanMaker()
        >>> print(format(timespan_maker))
        consort.tools.FloodedTimespanMaker()

    ::

        >>> music_specifiers = {
        ...     'Violin Voice': None,
        ...     'Cello Voice': None,
        ...     }
        >>> target_timespan = timespantools.Timespan((1, 2), (2, 1))
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Cello Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Violin Voice',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        padding=None,
        timespan_specifier=None,
        ):
        TimespanMaker.__init__(
            self,
            padding=padding,
            timespan_specifier=timespan_specifier,
            )

    ### PRIVATE METHODS ###

    def _make_timespans(
        self,
        layer=None,
        music_specifiers=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        import consort
        counter = collections.Counter()
        for voice_name, music_specifier in music_specifiers.items():
            if not isinstance(music_specifier, tuple):
                music_specifier = datastructuretools.CyclicTuple(
                    [music_specifier])
            if voice_name not in counter:
                counter[voice_name] = 0
            music_specifier_index = counter[voice_name]
            current_music_specifier = \
                music_specifier[music_specifier_index]
            timespan = self._make_performed_timespan(
                layer=layer,
                music_specifier=current_music_specifier,
                start_offset=target_timespan.start_offset,
                stop_offset=target_timespan.stop_offset,
                voice_name=voice_name,
                )
            timespan_inventory.append(timespan)
            if self.padding:
                left_padding = consort.SilentTimespan(
                    start_offset=timespan.start_offset - self.padding,
                    stop_offset=timespan.start_offset,
                    voice_name=voice_name,
                    )
                timespan_inventory.append(left_padding)
                right_padding = consort.SilentTimespan(
                    start_offset=timespan.stop_offset,
                    stop_offset=timespan.stop_offset + self.padding,
                    voice_name=voice_name,
                    )
                timespan_inventory.append(right_padding)