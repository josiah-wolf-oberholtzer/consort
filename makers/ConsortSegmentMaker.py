# -*- encoding: utf-8 -*-
import os
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondfiletools
from abjad.tools import markuptools
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

    __slots__ = (
        '_context_specifiers',
        '_is_final_segment',
        '_permitted_time_signatures',
        '_target_duration',
        '_tempo',
        )

    ### INITIALIZER ###

    def __init__(
        self,
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

    ### PRIVATE METHODS ###

    def _create_timespan_inventories(self):
        timespan_inventory = timespantools.TimespanInventory()
        for layer, context_specifier in enumerate(self.context_specifiers):
            result = context_specifier(
                layer=layer,
                template=self.score_template,
                )
            timespan_inventory.extend(result)

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

    def _make_music(self):
        from consort import makers

        score = self.score_template()

        #timespan_inventory = None
        #timespan_inventory_mapping = None

        makers.GraceAgent.iterate_score(score)
        makers.PitchAgent.iterate_score(score)
        makers.AlterationAgent.iterate_score(score)
        makers.RegisterAgent.iterate_score(score)
        makers.ChordAgent.iterate_score(score)
        makers.AttachmentAgent.iterate_score(score)

        lilypond_file = self._make_lilypond_file(score)

        return lilypond_file

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
