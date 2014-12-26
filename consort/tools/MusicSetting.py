# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad import inspect_
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import timespantools


class MusicSetting(abctools.AbjadValueObject):
    r'''A music setting.

    ::

        >>> import consort
        >>> red_setting = consort.MusicSetting(
        ...     timespan_maker=consort.TaleaTimespanMaker(
        ...         initial_silence_talea=rhythmmakertools.Talea(
        ...             counts=(0, 4),
        ...             denominator=16,
        ...             ),
        ...         playing_talea=rhythmmakertools.Talea(
        ...             counts=(4, 8, 4),
        ...             denominator=16,
        ...             ),
        ...         ),
        ...     viola_bowing_voice=consort.tools.MusicSpecifier(),
        ...     violin_1_bowing_voice=consort.tools.MusicSpecifier(),
        ...     violin_2_bowing_voice=consort.tools.MusicSpecifier(),
        ...     )
        >>> print(format(red_setting))
        consort.tools.MusicSetting(
            timespan_maker=consort.tools.TaleaTimespanMaker(
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
            viola_bowing_voice=consort.tools.MusicSpecifier(),
            violin_1_bowing_voice=consort.tools.MusicSpecifier(),
            violin_2_bowing_voice=consort.tools.MusicSpecifier(),
            )

    ::

        >>> layer = 1
        >>> target_timespan = timespantools.Timespan(1, 2)
        >>> from abjad.tools import templatetools
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
                consort.tools.PerformedTimespan(
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(5, 4),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    start_offset=durationtools.Offset(5, 4),
                    stop_offset=durationtools.Offset(3, 2),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_music_specifiers',
        '_timespan_identifier',
        '_timespan_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        timespan_identifier=None,
        timespan_maker=None,
        **music_specifiers
        ):
        import consort
        if timespan_identifier is not None:
            prototype = (
                timespantools.Timespan,
                timespantools.TimespanInventory,
                consort.RatioPartsExpression,
                )
            assert isinstance(timespan_identifier, prototype)
        self._timespan_identifier = timespan_identifier
        prototype = (type(None), consort.tools.MusicSpecifier)
        for music_specifier in music_specifiers.values():
            if music_specifier is None:
                continue
            elif isinstance(music_specifier, prototype):
                continue
            elif isinstance(music_specifier, tuple) and \
                all(isinstance(x, prototype) for x in music_specifier):
                continue
            raise ValueError(music_specifier)
        self._music_specifiers = music_specifiers
        if timespan_maker is not None:
            assert isinstance(timespan_maker,
                consort.TimespanMaker), \
                timespan_maker
        self._timespan_maker = timespan_maker

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer=None,
        score=None,
        score_template=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        if score is None:
            score = score_template()
        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
        if not self.music_specifiers:
            return timespan_inventory
        music_specifiers = self._get_music_specifiers(score, score_template)
        target_timespans = self._get_target_timespans(target_timespan)
        for target_timespan in target_timespans:
            timespan_inventory = self.timespan_maker(
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

    ### PRIVATE METHODS ###

    def _get_music_specifiers(self, score, score_template):
        import consort
        assert score_template is not None
        voice_triples = []
        for name, music_specifier in self.music_specifiers.items():
            if music_specifier is None:
                music_specifier = (None,)
            elif isinstance(music_specifier, consort.MusicSpecifier):
                music_specifier = (music_specifier,)
            music_specifier = datastructuretools.CyclicTuple(music_specifier)
            voice_name = score_template.context_name_abbreviations[name]
            voice = score[voice_name]
            voice_index = inspect_(voice).get_parentage().score_index
            voice_name = voice.name
            voice_triple = (
                voice_index,
                voice_name,
                music_specifier,
                )
            voice_triples.append(voice_triple)
        voice_triples.sort(key=lambda x: x[0])
        music_specifiers = collections.OrderedDict()
        for voice_index, voice_name, music_specifier in voice_triples:
            music_specifiers[voice_name] = music_specifier
        return music_specifiers

    def _get_target_timespans(self, target_timespan):
        import consort
        assert isinstance(target_timespan, timespantools.Timespan)
        if self.timespan_identifier is None:
            target_timespans = timespantools.TimespanInventory([
                target_timespan,
                ])
        elif isinstance(self.timespan_identifier, timespantools.Timespan):
            target_timespans = target_timespan & self.timespan_identifier
        else:
            if isinstance(self.timespan_identifier, consort.RatioPartsExpression):
                mask_timespans = self.timespan_identifier(target_timespan)
            else:
                mask_timespans = self.timespan_identifier
            target_timespans = timespantools.TimespanInventory()
            for mask_timespan in mask_timespans:
                available_timespans = target_timespan & mask_timespan
                target_timespans.extend(available_timespans)
        return target_timespans

    ### PRIVATE PROPERTIES ###

    @property
    def _storage_format_specification(self):
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
    def music_specifiers(self):
        return self._music_specifiers

    @property
    def timespan_identifier(self):
        return self._timespan_identifier

    @property
    def timespan_maker(self):
        return self._timespan_maker