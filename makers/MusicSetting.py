# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import timespantools


class MusicSetting(abctools.AbjadValueObject):
    r'''A music setting.

    ::

        >>> from consort import makers
        >>> red_setting = makers.MusicSetting(
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
        makers.MusicSetting(
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
        '_color',
        '_music_specifiers',
        '_timespan_identifier',
        '_timespan_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        color=None,
        timespan_identifier=None,
        timespan_maker=None,
        **music_specifiers
        ):
        from consort import makers
        if color is not None:
            color = str(color)
        self._color = color
        if timespan_identifier is not None:
            prototype = (
                timespantools.Timespan,
                timespantools.TimespanInventory,
                makers.RatioPartsExpression,
                )
            assert isinstance(timespan_identifier, prototype)
        self._timespan_identifier = timespan_identifier
        prototype = (type(None), makers.MusicSpecifier)
        for music_specifier in music_specifiers.values():
            assert isinstance(music_specifier, prototype)
        self._music_specifiers = music_specifiers
        if timespan_maker is not None:
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
        from consort import makers
        assert score_template is not None
        voice_names = makers.SegmentMaker._find_voice_names(
            score_template=score_template,
            voice_identifier=self.voice_identifier,
            )
        assert voice_names, voice_names
        assert isinstance(target_timespan, timespantools.Timespan)
        if self.timespan_identifier is None:
            target_timespans = timespantools.TimespanInventory([
                target_timespan,
                ])
        elif isinstance(self.timespan_identifier, timespantools.Timespan):
            target_timespans = target_timespan & self.timespan_identifier
        else:
            if isinstance(self.timespan_identifier, makers.RatioPartsExpression):
                mask_timespans = self.timespan_identifier(target_timespan)
            else:
                mask_timespans = self.timespan_identifier
            target_timespans = timespantools.TimespanInventory()
            for mask_timespan in mask_timespans:
                available_timespans = target_timespan & mask_timespan
                target_timespans.extend(available_timespans)
        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
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
    def color(self):
        return self._color

    @property
    def music_specifiers(self):
        return self._music_specifiers

    @property
    def timespan_identifier(self):
        return self._timespan_identifier

    @property
    def timespan_maker(self):
        return self._timespan_maker

    @property
    def voice_identifier(self):
        return self._voice_identifier