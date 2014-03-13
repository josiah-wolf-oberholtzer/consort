# -*- encoding: utf-8 -*-
import os
import re
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondfiletools
from abjad.tools import markuptools
from abjad.tools import metertools
from abjad.tools import scoretools
from abjad.tools import timespantools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from experimental.tools.segmentmakertools import SegmentMaker


class ConsortSegmentMaker(SegmentMaker):
    r'''A Consort segment-maker.

    ::

        >>> from consort import makers
        >>> from consort import templates
        >>> template = templates.ConsortScoreTemplate(
        ...     violin_count=2,
        ...     viola_count=1,
        ...     cello_count=1,
        ...     contrabass_count=0,
        ...     )

    ::

        >>> segment_maker = makers.ConsortSegmentMaker(
        ...     permitted_time_signatures=(
        ...         (5, 8),
        ...         (7, 16),
        ...         ),
        ...     target_duration=2,
        ...     tempo=indicatortools.Tempo((1, 4), 72),
        ...     template=template,
        ...     voice_specifiers=(
        ...         makers.VoiceSpecifier(
        ...             music_specifier=makers.MusicSpecifier(),
        ...             timespan_maker=makers.TimespanMaker(),
        ...             voice_identifiers=('Violin \\d+ LH Voice',),
        ...             ),
        ...         ),
        ...     )
        >>> print format(segment_maker)
        makers.ConsortSegmentMaker(
            is_final_segment=False,
            permitted_time_signatures=indicatortools.TimeSignatureInventory(
                [
                    indicatortools.TimeSignature((5, 8)),
                    indicatortools.TimeSignature((7, 16)),
                    ]
                ),
            target_duration=durationtools.Duration(2, 1),
            template=templates.ConsortScoreTemplate(
                violin_count=2,
                viola_count=1,
                cello_count=1,
                contrabass_count=0,
                ),
            tempo=indicatortools.Tempo(durationtools.Duration(1, 4), 72),
            voice_specifiers=(
                makers.VoiceSpecifier(
                    music_specifier=makers.MusicSpecifier(),
                    timespan_maker=makers.TimespanMaker(
                        can_shift=False,
                        can_split=False,
                        initial_silence_durations=(),
                        minimum_duration=durationtools.Duration(1, 8),
                        playing_durations=(
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
                    voice_identifiers=('Violin \\d+ LH Voice',),
                    ),
                ),
            )

    ::

        >>> lilypond_file = segment_maker()

    '''

    ### CLASS VARIABLES ###

    class SegmentProduct(abctools.AbjadObject):
        r'''A segment segment_product.
        '''

        ### CLASS VARIABLES ###

        __slots__ = (
            'lilypond_file',
            'meters',
            'score',
            'segment_duration',
            'segment_maker',
            'timespan_inventory_mapping',
            )

        ### INITIALIZER ###

        def __init__(
            self,
            segment_maker=None,
            ):
            self.lilypond_file = None
            self.meters = None
            self.score = None
            self.segment_duration = None
            self.segment_maker = segment_maker
            self.timespan_inventory_mapping = None

        ### PUBLIC PROPERTIES ###

        @property
        def measure_offsets(self):
            measure_durations = [x.duration for x in self.time_signatures]
            measure_offsets = mathtools.cumulative_sums(measure_durations)
            return measure_offsets

        @property
        def time_signatures(self):
            return (
                meter.implied_time_signature
                for meter in self.meters
                )

    __slots__ = (
        '_is_final_segment',
        '_permitted_time_signatures',
        '_target_duration',
        '_template',
        '_tempo',
        '_voice_settings',
        '_voice_specifiers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        is_final_segment=False,
        name=None,
        permitted_time_signatures=None,
        target_duration=None,
        template=None,
        tempo=None,
        voice_settings=None,
        voice_specifiers=None,
        ):
        from consort import makers
        SegmentMaker.__init__(
            self,
            name=name,
            )
        if voice_settings is not None:
            assert all(isinstance(x, makers.VoiceSetting)
                for x in voice_settings)
            voice_settings = tuple(voice_settings)
        self._voice_settings = voice_settings
        if voice_specifiers is not None:
            voice_specifiers = tuple(voice_specifiers)
            assert len(voice_specifiers)
            assert all(isinstance(x, makers.VoiceSpecifier)
                for x in voice_specifiers)
        self._voice_specifiers = voice_specifiers
        self._is_final_segment = bool(is_final_segment)
        if permitted_time_signatures is not None:
            permitted_time_signatures = indicatortools.TimeSignatureInventory(
                items=permitted_time_signatures,
                )
        self._permitted_time_signatures = permitted_time_signatures
        if target_duration is not None:
            target_duration = durationtools.Duration(target_duration)
        self._target_duration = target_duration
        self._template = template
        if tempo is not None:
            tempo = indicatortools.Tempo(tempo)
        self._tempo = tempo

    ### SPECIAL METHODS ###

    def __call__(self):

        segment_product = self.SegmentProduct(segment_maker=self)
        segment_product.score = self.template()

        self._make_timespan_inventory_mapping(segment_product)
        self._find_meters(segment_product)
        self._cleanup_performed_timespans(segment_product)
        #self._create_dependent_timespans(segment_product)
        #self._remove_empty_trailing_measures(segment_product)
        #self._create_silent_timespans(segment_product)
        #self._apply_voice_settings(segment_product)

        #self._populate_time_signature_context(segment_product)
        #self._populate_rhythms(segment_product)
        #self._cleanup_silences(segment_product)

        #makers.GraceAgent.iterate_score(segment_product.score)
        #makers.PitchAgent.iterate_score(segment_product.score)
        #makers.AlterationAgent.iterate_score(segment_product.score)
        #makers.RegisterAgent.iterate_score(segment_product.score)
        #makers.ChordAgent.iterate_score(segment_product.score)
        #makers.AttachmentAgent.iterate_score(segment_product.score)

        #segment_product.lilypond_file = self._make_lilypond_file(
        #    segment_product.score)

        #return segment_product.lilypond_file

        return segment_product

    ### PRIVATE METHODS ###

    def _apply_voice_settings(self, segment_product):
        if self.voice_settings is not None:
            for context_setting in self.voice_settings:
                context_setting(segment_product)

    def _cleanup_performed_timespans(self, segment_product):
        measure_offsets = segment_product.measure_offsets
        timespan_inventory_mapping = segment_product.timespan_inventory_mapping
        for voice_name in timespan_inventory_mapping:
            timespan_inventory = timespan_inventory_mapping[voice_name]
            timespan_inventory.split_at_offsets(measure_offsets)
            for timespan in timespan_inventory[:]:
                timespan_maker = timespan.music_specifier.timespan_maker
                minimum_duration = timespan_maker.minimum_duration
                if timespan.duration < minimum_duration:
                    timespan_inventory.remove(timespan)

    def _find_meters(self, segment_product):
        offset_counter = datastructuretools.TypedCounter(
            item_class=durationtools.Offset,
            )
        for timespan_inventory in \
            segment_product.timespan_inventory_mapping.values():
            for timespan in timespan_inventory:
                offset_counter[timespan.start_offset] += 1
                offset_counter[timespan.stop_offset] += 1
        if not offset_counter:
            offset_counter[self.target_duration] += 1
        meters = metertools.Meter.fit_meters_to_expr(
            offset_counter,
            self.permitted_time_signatures,
            maximum_repetitions=2,
            )
        segment_product.meters = tuple(meters)
        segment_product.segment_duration = sum(
            x.duration for x in segment_product.time_signatures)

    def _make_lilypond_file(self, score):
        rehearsal_mark = indicatortools.LilyPondCommand(r'mark \default')
        attach(rehearsal_mark, score['TimeSignatureContext'][0],
            scope=scoretools.Context)
        attach(self.segment_tempo, score['TimeSignatureContext'][0])
        if self.is_final_segment:
            score.add_final_markup(self.final_markup)
            score.add_final_bar_line()
        else:
            score.add_final_bar_line('||')
        assert inspect_(score).is_well_formed()
        lilypond_file = lilypondfiletools.LilyPondFile()
        lilypond_file.use_relative_includes = True
        score_block = lilypondfiletools.Block(name='score')
        score_block.items.append(score)
        lilypond_file.items.append(score_block)
        for file_path in self.stylesheets_file_paths:
            lilypond_file.file_initial_user_includes.append(file_path)
        lilypond_file.file_initial_system_comments[:] = []
        return lilypond_file

    def _make_timespan_inventory_mapping(self, segment_product):
        timespan_inventory_mapping = {}
        segment_duration = durationtools.Duration(0)
        for layer, voice_specifier in enumerate(self.voice_specifiers):
            timespan_inventory, final_duration = voice_specifier(
                layer=layer,
                target_duration=self.target_duration,
                template=self.template,
                )
            if segment_duration < final_duration:
                segment_duration = final_duration
            for timespan in timespan_inventory:
                voice_name, layer = timespan.voice_name, timespan.layer
                if voice_name not in timespan_inventory_mapping:
                    timespan_inventory_mapping[voice_name] = []
                    for _ in range(len(self.voice_specifiers)):
                        timespan_inventory_mapping[voice_name].append(
                            timespantools.TimespanInventory())
                timespan_inventory_mapping[voice_name][layer].append(
                    timespan)
                timespan_inventory_mapping[voice_name][layer].sort()
        for voice_name in timespan_inventory_mapping:
            timespan_inventories = timespan_inventory_mapping[voice_name]
            timespan_inventory = self._resolve_timespan_inventories(
                timespan_inventories)
            timespan_inventory_mapping[voice_name] = timespan_inventory
        segment_product.segment_duration = segment_duration
        segment_product.timespan_inventory_mapping = timespan_inventory_mapping

    def _resolve_timespan_inventories(self, timespan_inventories):
        resolved_timespan_inventory = timespantools.TimespanInventory()
        resolved_timespan_inventory.extend(timespan_inventories[0])
        for timespan_inventory in timespan_inventories[1:]:
            for timespan in timespan_inventory:
                resolved_timespan_inventory -= timespan
        return resolved_timespan_inventory

    ### PUBLIC METHODS ###

    @staticmethod
    def find_voice_names(
        template=None,
        voice_identifiers=None,
        ):
        r'''Find voice names matching `voice_identifiers` in `template`:

        ::

            >>> from consort import makers
            >>> from consort import templates
            >>> template = templates.ConsortScoreTemplate(
            ...     violin_count=2,
            ...     viola_count=1,
            ...     cello_count=1,
            ...     contrabass_count=1,
            ...     )
            >>> voice_identifiers = (
            ...     'Violin \\d+ LH Voice',
            ...     'Viola LH Voice',
            ...     )
            >>> makers.ConsortSegmentMaker.find_voice_names(
            ...     template=template,
            ...     voice_identifiers=voice_identifiers,
            ...     )
            ('Violin 1 LH Voice', 'Violin 2 LH Voice', 'Viola LH Voice')

        '''
        score = template()
        all_voice_names = [voice.name for voice in
            iterate(score).by_class(scoretools.Voice)]
        matched_voice_names = set()
        for voice_identifier in voice_identifiers:
            pattern = re.compile(voice_identifier)
            for voice_name in all_voice_names:
                match = pattern.match(voice_name)
                if match:
                    matched_voice_names.add(voice_name)
        selected_voice_names = []
        for voice_name in all_voice_names:
            if voice_name in matched_voice_names:
                selected_voice_names.append(voice_name)
        selected_voice_names = tuple(selected_voice_names)
        return selected_voice_names

    ### PUBLIC PROPERTIES ###

    @property
    def final_markup(self):
        from consort.__metadata__ import metadata
        right_column = markuptools.MarkupCommand(
            'right-column', [
                ' ',
                ' ',
                ' ',
                metadata['locale'],
                '{} - {}'.format(
                    metadata['time_period'][0],
                    metadata['time_period'][1],
                    ),
                ],
            )
        italic = markuptools.MarkupCommand(
            'italic',
            right_column,
            )
        final_markup = markuptools.Markup(italic, 'down')
        return final_markup

    @property
    def is_final_segment(self):
        return self._is_final_segment

    @property
    def permitted_time_signatures(self):
        return self._permitted_time_signatures

    @property
    def template(self):
        return self._template

    @property
    def stylesheet_file_paths(self):
        import consort
        consort_path = consort.__path__[0]
        stylesheets_path = os.path.join(
            consort_path,
            'stylesheets',
            )
        stylesheet_file_names = [x for x in os.listdir(stylesheets_path)
            if os.path.splitext(x)[-1] == 'ily']
        stylesheet_file_paths = []
        for file_name in stylesheet_file_names:
            relative_file_path = os.path.join(
                '..', '..', 'stylesheets',
                file_name,
                )
            stylesheet_file_paths.append(relative_file_path)
        return stylesheet_file_paths

    @property
    def target_duration(self):
        return self._target_duration

    @property
    def tempo(self):
        return self._tempo

    @property
    def voice_settings(self):
        return self._voice_settings

    @property
    def voice_specifiers(self):
        return self._voice_specifiers
