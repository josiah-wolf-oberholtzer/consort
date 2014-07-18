# -*- encoding: utf-8 -*-
from consort.makers.MusicSetting import MusicSetting


class MusicConstruct(MusicSetting):
    r'''A music construct.

    ::

        >>> from consort import makers
        >>> red_setting = makers.MusicConstruct(
        ...     color='red',
        ...     music_specifier=makers.MusicSpecifier(),
        ...     timespan_maker=makers.TimespanMaker(
        ...         initial_silence_durations=(
        ...             durationtools.Duration(0, 1),
        ...             durationtools.Duration(1, 4),
        ...             ),
        ...         playing_durations=(
        ...             durationtools.Duration(1, 4),
        ...             durationtools.Duration(1, 2),
        ...             durationtools.Duration(1, 4),
        ...             ),
        ...         ),
        ...     voice_identifier=(
        ...         'Violin \\d+ Bowing Voice',
        ...         'Viola Bowing Voice',
        ...         ),
        ...     )
        >>> print(format(red_setting))
        makers.MusicConstruct(
            color='red',
            music_specifier=makers.MusicSpecifier(),
            timespan_maker=makers.TimespanMaker(
                initial_silence_durations=(
                    durationtools.Duration(0, 1),
                    durationtools.Duration(1, 4),
                    ),
                minimum_duration=durationtools.Duration(1, 8),
                playing_durations=(
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 2),
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
                ),
            voice_identifier=(
                'Violin \\d+ Bowing Voice',
                'Viola Bowing Voice',
                ),
            )

    ::

        >>> layer = 1
        >>> target_timespan = timespantools.Timespan(1, 2)
        >>> score_template = makers.StringOrchestraScoreTemplate(
        ...     violin_count=2,
        ...     viola_count=1,
        ...     cello_count=1,
        ...     contrabass_count=1,
        ...     )
        >>> timespan_inventory = red_setting(
        ...     layer=layer,
        ...     score_template=score_template,
        ...     target_timespan=target_timespan,
        ...     )

    ::

        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(5, 4),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(5, 4),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )


    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_music_specifier',
        '_timespan_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        color=None,
        music_specifier=None,
        timespan_identifier=None,
        timespan_maker=None,
        voice_identifier=None,
        ):
        from consort import makers
        MusicSetting.__init__(
            self,
            color=color,
            timespan_identifier=timespan_identifier,
            voice_identifier=voice_identifier,
            )
        assert isinstance(music_specifier, makers.MusicSpecifier)
        self._music_specifier = music_specifier
        assert isinstance(timespan_maker, makers.TimespanMaker)
        self._timespan_maker = timespan_maker

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer,
        score_template,
        target_timespan,
        timespan_inventory=None,
        ):
        target_timespans, voice_names, timespan_inventory = \
            MusicSetting.__call__(
                self,
                layer,
                score_template,
                target_timespan,
                timespan_inventory,
                )
        for target_timespan in target_timespans:
            timespan_inventory = self.timespan_maker(
                color=self.color,
                layer=layer,
                music_specifier=self.music_specifier,
                target_timespan=target_timespan,
                timespan_inventory=timespan_inventory,
                voice_names=voice_names,
                )
        return timespan_inventory

    ### PUBLIC PROPERTIES ###

    @property
    def music_specifier(self):
        return self._music_specifier

    @property
    def timespan_maker(self):
        return self._timespan_maker