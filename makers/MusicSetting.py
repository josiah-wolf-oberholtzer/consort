# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import rhythmmakertools
from abjad.tools import timespantools
from abjad.tools.topleveltools import inspect_


class MusicSetting(abctools.AbjadValueObject):
    r'''A music setting.

    ::

        >>> from consort import makers
        >>> red_setting = makers.MusicSetting(
        ...     color='red',
        ...     timespan_maker=makers.TaleaTimespanMaker(
        ...         initial_silence_talea=rhythmmakertools.Talea(
        ...             counts=(0, 4),
        ...             denominator=16,
        ...             ),
        ...         playing_talea=rhythmmakertools.Talea(
        ...             counts=(4, 8, 4),
        ...             denominator=16,
        ...             ),
        ...         ),
        ...     viola_bowing_voice=makers.MusicSpecifier(),
        ...     violin_1_bowing_voice=makers.MusicSpecifier(),
        ...     violin_2_bowing_voice=makers.MusicSpecifier(),
        ...     )
        >>> print(format(red_setting))
        makers.MusicSetting(
            color='red',
            timespan_maker=makers.TaleaTimespanMaker(
                initial_silence_talea=rhythmmakertools.Talea(
                    counts=(0, 4),
                    denominator=16,
                    ),
                playing_talea=rhythmmakertools.Talea(
                    counts=(4, 8, 4),
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
                ),
            viola_bowing_voice=makers.MusicSpecifier(),
            violin_1_bowing_voice=makers.MusicSpecifier(),
            violin_2_bowing_voice=makers.MusicSpecifier(),
            )

    ::

        >>> layer = 1
        >>> target_timespan = timespantools.Timespan(1, 2)
        >>> score_template = templatetools.StringOrchestraScoreTemplate(
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
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(5, 4),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(5, 4),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
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
            assert isinstance(timespan_maker, makers.TimespanMaker), \
                timespan_maker
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
        score = score_template()
        voice_pairs = []
        for name, music_specifier in self.music_specifiers.items():
            voice_name = score_template.voice_name_abbreviations[name]
            voice = score[voice_name]
            voice_pair = (voice, music_specifier)
            voice_pairs.append(voice_pair)
        voice_pairs.sort(
            key=lambda x: inspect_(x[0]).get_parentage().score_index,
            )
        music_specifiers = collections.OrderedDict()
        for voice, music_specifier in voice_pairs:
            music_specifiers[voice.name] = music_specifier
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
                music_specifiers=music_specifiers,
                target_timespan=target_timespan,
                timespan_inventory=timespan_inventory,
                )
        return timespan_inventory

    def __getattr__(self, item):
        if item in self.music_specifiers:
            return self.music_specifiers[item]
        return object.__getattribute__(self, item)

    ### PRIVATE PROPERTIES ###

    @property
    def _storage_format_specification(self):
        from abjad.tools import systemtools
        manager = systemtools.StorageFormatManager
        keyword_argument_names = manager.get_keyword_argument_names(self)
        keyword_argument_names = list(keyword_argument_names)
        keyword_argument_names.extend(sorted(self.music_specifiers))
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=keyword_argument_names
            )

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