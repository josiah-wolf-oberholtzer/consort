# -*- encoding: utf-8 -*-
import os
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
from experimental.tools.segmentmakertools import SegmentMaker


class ConsortSegmentMaker(SegmentMaker):
    r'''A Consort segment-maker.

    ::

        >>> from consort import makers
        >>> segment_maker = makers.ConsortSegmentMaker()
        >>> print format(segment_maker)
        makers.ConsortSegmentMaker(
            is_final_segment=False,
            )

    '''

    ### CLASS VARIABLES ###

    class SegmentProduct(abctools.AbjadObject):
        r'''A segment product.
        '''

        ### CLASS VARIABLES ###

        __slots__ = (
            'lilypond_file',
            'meters',
            'score',
            'segment_duration',
            'segment_maker',
            'time_signatures',
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
            self.time_signatures = None
            self.timespan_inventory_mapping = None

    __slots__ = (
        '_context_map',
        '_context_settings',
        '_context_specifiers',
        '_is_final_segment',
        '_permitted_time_signatures',
        '_target_duration',
        '_tempo',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        context_map=None,
        context_settings=None,
        context_specifiers=None,
        is_final_segment=False,
        name=None,
        permitted_time_signatures=None,
        target_duration=None,
        tempo=None,
        ):
        from consort import makers
        SegmentMaker.__init__(
            self,
            name=name,
            )
        if context_map is not None:
            assert isinstance(context_map, datastructuretools.ContextMap)
            assert context_map.score_template == self.score_template
        self._context_map = context_map
        if context_settings is not None:
            assert all(isinstance(x, makers.ContextSetting)
                for x in context_settings)
            context_settings = tuple(context_settings)
        self._context_settings = context_settings
        if context_specifiers is not None:
            context_specifiers = tuple(context_specifiers)
            assert len(context_specifiers)
            assert all(isinstance(x, makers.ContextSpecifier)
                for x in context_specifiers)
        self._context_specifiers = context_specifiers
        self._is_final_segment = bool(is_final_segment)
        if permitted_time_signatures is not None:
            permitted_time_signatures = (
                indicatortools.TimeSignature(x)
                for x in permitted_time_signatures
                )
        self._permitted_time_signatures = permitted_time_signatures
        if target_duration is not None:
            target_duration = durationtools.Duration(target_duration)
        self._target_duration = target_duration
        if tempo is not None:
            tempo = indicatortools.Tempo(tempo)
        self._tempo = tempo

    ### SPECIAL METHODS ###

    def __call__(self):
        from consort import makers

        product = self.SegmentProduct(segment_maker=self)
        product.score = self.score_template()

        self._make_timespan_inventory_mapping(product)
        self._find_meters(product)
        self._cleanup_semantic_timespans(product)
        self._create_dependent_timespans(product)
        self._remove_empty_trailing_measures(product)
        self._create_silent_timespans(product)
        self._apply_context_settings(product)

        #self._populate_time_signature_context(product)
        #self._populate_rhythms(product)
        #self._cleanup_silences(product)

        makers.GraceAgent.iterate_score(product.score)
        makers.PitchAgent.iterate_score(product.score)
        makers.AlterationAgent.iterate_score(product.score)
        makers.RegisterAgent.iterate_score(product.score)
        makers.ChordAgent.iterate_score(product.score)
        makers.AttachmentAgent.iterate_score(product.score)

        product.lilypond_file = self._make_lilypond_file(product.score)

        return product.lilypond_file

    ### PRIVATE METHODS ###

    def _find_meters(self, product):
        offset_counter = datastructuretools.TypedCounter(
            item_class=durationtools.Offset,
            )
        for timespan_inventory in product.timespan_inventory_mapping.values():
            for timespan in timespan_inventory:
                offset_counter[timespan.start_offset] += 1
                offset_counter[timespan.stop_offset] += 1
        if not offset_counter:
            offset_counter[self.target_segment_duration] += 1
        meters = metertools.Meter.fit_meters_to_expr(
            offset_counter,
            self.permitted_time_signatures,
            maximum_repetitions=2,
            )
        product.meters = meters

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

    def _make_timespan_inventory_mapping(self, product):
        timespan_inventory = timespantools.TimespanInventory()
        for layer, context_specifier in enumerate(self.context_specifiers):
            result = context_specifier(
                layer=layer,
                template=self.score_template,
                )
            timespan_inventory.extend(result)
        timespan_inventory_mapping = {}
        for timespan in timespan_inventory:
            context_name, layer = timespan.context_name, timespan.layer
            if context_name not in timespan_inventory_mapping:
                timespan_inventory_mapping[context_name] = []
                for _ in range(len(self.context_specifiers)):
                    timespan_inventory_mapping[context_name].append(
                        timespantools.TimespanInventory())
            timespan_inventory_mapping[context_name][layer].append(timespan)
        for context_name in timespan_inventory_mapping:
            timespan_inventories = timespan_inventory_mapping[context_name]
            timespan_inventory = self._resolve_timespan_inventories(
                timespan_inventories)
            timespan_inventory_mapping[context_name] = timespan_inventory
        product.timespan_inventory_mapping = timespan_inventory_mapping

    def _resolve_timespan_inventories(self, timespan_inventories):
        pass

    ### PUBLIC PROPERTIES ###

    @property
    def context_specifiers(self):
        return self._context_specifiers

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
    def score_template(self):
        from consort import templates
        template = templates.ConsortScoreTemplate(
            violin_count=2,
            viola_count=1,
            cello_count=1,
            contrabass_count=0,
            )
        return template

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
