# -*- encoding: utf-8 -*-
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
        ...     'Violin Voice': 'violin music',
        ...     'Cello Voice': 'cello music',
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
                    music_specifier='cello music',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Cello Voice',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier='violin music',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Violin Voice',
                    ),
                ]
            )

    ::

        >>> music_specifier = consort.CompositeMusicSpecifier(
        ...     primary_music_specifier='one',
        ...     primary_voice_name='Viola 1 RH',
        ...     rotation_indices=(0, 1, -1),
        ...     secondary_voice_name='Viola 1 LH',
        ...     secondary_music_specifier=consort.MusicSpecifierSequence(
        ...         application_rate='phrase',
        ...         music_specifiers=['two', 'three', 'four'],
        ...         ),
        ...     )
        >>> music_specifiers = {
        ...     'Viola 1 Performer Group': music_specifier,
        ...     }
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    music_specifier='two',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola 1 LH',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier='one',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola 1 RH',
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
        music_specifiers = self._coerce_music_specifiers(music_specifiers)
        start_offset = target_timespan.start_offset
        durations = [target_timespan.duration]
        for context_name, music_specifier in music_specifiers.items():
            timespans = music_specifier(
                durations=durations,
                layer=layer,
                padding=self.padding,
                seed=self.seed,
                start_offset=start_offset,
                timespan_specifier=self.timespan_specifier,
                voice_name=context_name,
                )
            timespan_inventory.extend(timespans)