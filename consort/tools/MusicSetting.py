# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad import inspect_
from abjad import new
from abjad.tools import abctools
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
        ...     viola_rh=consort.tools.MusicSpecifier(),
        ...     violin_1_rh=consort.tools.MusicSpecifier(),
        ...     violin_2_rh=consort.tools.MusicSpecifier(),
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
            viola_rh=consort.tools.MusicSpecifier(),
            violin_1_rh=consort.tools.MusicSpecifier(),
            violin_2_rh=consort.tools.MusicSpecifier(),
            )

    ::

        >>> layer = 1
        >>> segment_timespan = timespantools.Timespan(1, 2)
        >>> from abjad.tools import templatetools
        >>> score_template = consort.StringQuartetScoreTemplate()
        >>> timespan_inventory = red_setting(
        ...     layer=layer,
        ...     score_template=score_template,
        ...     segment_timespan=segment_timespan,
        ...     )

    ::

        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(5, 4),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(5, 4),
                    stop_offset=durationtools.Offset(3, 2),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                ]
            )

    ::

        >>> red_setting = new(
        ...     red_setting,
        ...     silenced_contexts=[
        ...         'viola_lh',
        ...         'cello',
        ...         ],
        ...     )
        >>> timespan_inventory = red_setting(
        ...     layer=layer,
        ...     score_template=score_template,
        ...     segment_timespan=segment_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(5, 4),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(3, 2),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    voice_name='Cello Bowing Voice',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    voice_name='Cello Fingering Voice',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    voice_name='Viola Fingering Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(5, 4),
                    stop_offset=durationtools.Offset(3, 2),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(3, 2),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(7, 4),
                    stop_offset=durationtools.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_music_specifiers',
        '_silenced_contexts',
        '_timespan_identifier',
        '_timespan_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        timespan_identifier=None,
        timespan_maker=None,
        silenced_contexts=None,
        **music_specifiers
        ):
        import consort
        prototype = (
            consort.CompositeMusicSpecifier,
            consort.MusicSpecifier,
            consort.MusicSpecifierSequence,
            str,  # for demonstration purposes only
            type(None),
            )
        for abbreviation, music_specifier in sorted(music_specifiers.items()):
            if isinstance(music_specifier, prototype):
                continue
            elif isinstance(music_specifier, collections.Sequence) and \
                all(isinstance(x, prototype) for x in music_specifier):
                music_specifier = consort.MusicSpecifierSequence(
                    music_specifiers=music_specifier,
                    )
                music_specifiers[abbreviation] = music_specifier
            else:
                raise ValueError(music_specifier)
        self._music_specifiers = music_specifiers
        if silenced_contexts is not None:
            silenced_contexts = (str(_) for _ in silenced_contexts)
            silenced_contexts = set(silenced_contexts)
        self._silenced_contexts = silenced_contexts
        if timespan_identifier is not None:
            prototype = (
                timespantools.Timespan,
                timespantools.TimespanInventory,
                consort.RatioPartsExpression,
                )
            if not isinstance(timespan_identifier, prototype):
                timespan_identifier = \
                    consort.RatioPartsExpression.from_sequence(
                        timespan_identifier)
            assert isinstance(timespan_identifier, prototype)
        self._timespan_identifier = timespan_identifier
        if timespan_maker is not None:
            assert isinstance(timespan_maker,
                consort.TimespanMaker), \
                timespan_maker
        else:
            timespan_maker = consort.FloodedTimespanMaker()
        self._timespan_maker = timespan_maker

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer=None,
        score=None,
        score_template=None,
        segment_timespan=None,
        timespan_inventory=None,
        timespan_quantization=None,
        ):
        if score is None:
            score = score_template()
        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
        if not self.music_specifiers:
            return timespan_inventory
        music_specifiers = self.resolve_music_specifiers(
            score_template,
            score=score,
            )
        silenced_context_names = self.resolve_silenced_contexts(
            score_template,
            score=score,
            )
        target_timespans = self.resolve_target_timespans(
            segment_timespan,
            timespan_quantization,
            )
        for i, target_timespan in enumerate(target_timespans):
            timespan_maker = self.timespan_maker.rotate(i)
            timespan_inventory = timespan_maker(
                layer=layer,
                music_specifiers=music_specifiers,
                silenced_context_names=silenced_context_names,
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
        manager = systemtools.StorageFormatManager
        keyword_argument_names = manager.get_keyword_argument_names(self)
        keyword_argument_names = list(keyword_argument_names)
        keyword_argument_names.extend(sorted(self.music_specifiers))
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=keyword_argument_names
            )

    ### PUBLIC METHODS ###

    def resolve_music_specifiers(
        self,
        score_template,
        score=None,
        ):
        import consort
        assert score_template is not None
        if score is None:
            score = score_template()
        all_abbreviations = score_template.context_name_abbreviations
        prototype = (
            consort.CompositeMusicSpecifier,
            consort.MusicSpecifierSequence,
            )
        triples = []
        for abbreviation, music_specifier in self.music_specifiers.items():
            if not isinstance(music_specifier, prototype):
                music_specifier = consort.MusicSpecifierSequence(
                    music_specifiers=music_specifier,
                    )
            context_name = all_abbreviations[abbreviation]
            context = score[context_name]
            context_index = inspect_(context).get_parentage().score_index
            context_name = context.name
            if isinstance(music_specifier, consort.CompositeMusicSpecifier):
                composite_pairs = score_template.composite_context_pairs
                one, two = composite_pairs[abbreviation]
                primary_voice_name = all_abbreviations[one]
                secondary_voice_name = all_abbreviations[two]
                music_specifier = new(
                    music_specifier,
                    primary_voice_name=primary_voice_name,
                    secondary_voice_name=secondary_voice_name,
                    )
            triple = (
                context_index,
                context_name,
                music_specifier,
                )
            triples.append(triple)
        triples.sort(key=lambda x: x[0])
        music_specifiers = collections.OrderedDict()
        for context_index, context_name, music_specifier in triples:
            music_specifiers[context_name] = music_specifier
        return music_specifiers

    def resolve_silenced_contexts(
        self,
        score_template,
        score=None,
        ):
        assert score_template is not None
        if score is None:
            score = score_template()
        all_abbreviations = score_template.context_name_abbreviations
        composite_pairs = getattr(
            score_template,
            'composite_context_pairs',
            {},
            )
        silenced_context_names = set()
        silenced_contexts = self.silenced_contexts or ()
        for abbreviation in silenced_contexts:
            if abbreviation in composite_pairs:
                one, two = composite_pairs[abbreviation]
                primary_voice_name = all_abbreviations[one]
                secondary_voice_name = all_abbreviations[two]
                silenced_context_names.add(primary_voice_name)
                silenced_context_names.add(secondary_voice_name)
            elif abbreviation in all_abbreviations:
                context_name = all_abbreviations[abbreviation]
                silenced_context_names.add(context_name)
            else:
                message = 'Unresolvable context abbreviation: {}'
                message = message.format(abbreviation)
                raise Exception(message)
        return silenced_context_names

    def resolve_target_timespans(
        self,
        segment_timespan,
        timespan_quantization=None,
        ):
        import consort
        assert isinstance(segment_timespan, timespantools.Timespan)
        if self.timespan_identifier is None:
            target_timespans = timespantools.TimespanInventory([
                segment_timespan,
                ])
        elif isinstance(self.timespan_identifier, timespantools.Timespan):
            target_timespans = segment_timespan & self.timespan_identifier
        else:
            if isinstance(self.timespan_identifier, consort.RatioPartsExpression):
                mask_timespans = self.timespan_identifier(segment_timespan)
            else:
                mask_timespans = self.timespan_identifier
            target_timespans = timespantools.TimespanInventory()
            for mask_timespan in mask_timespans:
                available_timespans = segment_timespan & mask_timespan
                target_timespans.extend(available_timespans)
        if timespan_quantization is not None:
            target_timespans.round_offsets(
                timespan_quantization,
                must_be_well_formed=True,
                )
        return target_timespans

    ### PUBLIC PROPERTIES ###

    @property
    def music_specifiers(self):
        return self._music_specifiers

    @property
    def silenced_contexts(self):
        return self._silenced_contexts

    @property
    def timespan_identifier(self):
        return self._timespan_identifier

    @property
    def timespan_maker(self):
        return self._timespan_maker