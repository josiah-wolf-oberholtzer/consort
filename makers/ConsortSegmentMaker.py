# -*- encoding: utf-8 -*-
import os
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondfiletools
from abjad.tools import markuptools
from abjad.tools import scoretools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from experimental.tools.segmentmakertools import SegmentMaker


class ConsortSegmentMaker(SegmentMaker):
    r'''A Consort segment-maker.

    ::

        >>> from consort import makers
        >>> segment_maker = makers.ConsortSegmentMaker()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_is_final_segment',
        '_permitted_time_signatures',
        '_target_duration',
        '_tempo',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        is_final_segment=False,
        name=None,
        permitted_time_signatures=None,
        target_duration=None,
        tempo=None,
        ):
        SegmentMaker.__init__(
            self,
            name=name,
            )
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

    def _configure_lilypond_file(self, score):
        import consort
        lilypond_file = lilypondfiletools.LilyPondFile()
        lilypond_file.use_relative_includes = True
        score_block = lilypondfiletools.Block(name='score')
        score_block.items.append(score)
        lilypond_file.items.append(score_block)
        consort_path = consort.__path__[0]
        stylesheets_path = os.path.join(
            consort_path,
            'stylesheets',
            )
        stylesheets_file_paths = [x for x in os.listdir(stylesheets_path)
            if os.path.splitext(x)[-1] == 'ily']
        for file_path in stylesheets_file_paths:
            file_name = os.path.split(file_path)[-1]
            relative_file_path = os.path.join(
                '..', '..', 'stylesheets',
                file_name,
                )
            lilypond_file.file_initial_user_includes.append(relative_file_path)
        lilypond_file.file_initial_system_comments[:] = []
        return lilypond_file

    def _configure_score(self, score):
        rehearsal_mark = indicatortools.LilyPondCommand(r'mark \default')
        attach(rehearsal_mark, score['TimeSignatureContext'][0],
            scope=scoretools.Context)
        attach(self.segment_tempo, score['TimeSignatureContext'][0])
        if self.is_final_segment:
            right_column = markuptools.MarkupCommand(
                'right-column', [
                    ' ',
                    ' ',
                    ' ',
                    'Jamaica Plain',
                    'February 2014 - April 2014',
                    ],
                )
            italic = markuptools.MarkupCommand(
                'italic',
                right_column,
                )
            final_markup = markuptools.Markup(italic, 'down')
            score.add_final_markup(final_markup)
            score.add_final_bar_line()
        else:
            score.add_final_bar_line('||')

    def _make_music(self):
        from consort import makers
        from consort import templates

        template = templates.ConsortScoreTemplate(
            violin_count=2,
            viola_count=1,
            cello_count=1,
            contrabass_count=0,
            )
        score = template()

        makers.GraceAgent.iterate_score(score)
        makers.PitchAgent.iterate_score(score)
        makers.AlterationAgent.iterate_score(score)
        makers.RegisterAgent.iterate_score(score)
        makers.ChordAgent.iterate_score(score)
        makers.AttachmentAgent.iterate_score(score)

        self._configure_score(score)
        assert inspect_(score).is_well_formed()
        lilypond_file = self._configure_lilypond_file(score)
        return lilypond_file

    ### PUBLIC PROPERTIES ###

    @property
    def permitted_time_signatures(self):
        return self._permitted_time_signatures

    @property
    def target_duration(self):
        return self._target_duration

    @property
    def tempo(self):
        return self._tempo
