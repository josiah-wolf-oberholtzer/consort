# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
import importlib
import os
import re
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondfiletools
from abjad.tools import markuptools
from abjad.tools import scoretools
from abjad.tools import systemtools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from experimental.tools import segmentmakertools


class ConsortSegmentMaker(segmentmakertools.SegmentMaker):
    r'''A Consort segment-maker.

    ::

        >>> from consort import makers
        >>> score_template = makers.ConsortScoreTemplate(
        ...     violin_count=2,
        ...     viola_count=1,
        ...     cello_count=1,
        ...     contrabass_count=0,
        ...     )

    ::

        >>> segment_maker = makers.ConsortSegmentMaker(
        ...     score_template=score_template,
        ...     settings=(
        ...         makers.SegmentSetting(
        ...             music_specifier=makers.MusicSpecifier(),
        ...             timespan_maker=makers.TimespanMaker(),
        ...             voice_identifier=('Violin \\d+ Bowing Voice',),
        ...             ),
        ...         ),
        ...     duration_in_seconds=2,
        ...     tempo=indicatortools.Tempo((1, 4), 72),
        ...     time_signatures=(
        ...         (5, 8),
        ...         (7, 16),
        ...         ),
        ...     )
        >>> print(format(segment_maker))
        makers.ConsortSegmentMaker(
            is_final_segment=False,
            score_template=makers.ConsortScoreTemplate(
                violin_count=2,
                viola_count=1,
                cello_count=1,
                contrabass_count=0,
                split_hands=True,
                use_percussion_clefs=False,
                ),
            settings=(
                makers.SegmentSetting(
                    music_specifier=makers.MusicSpecifier(),
                    timespan_maker=makers.TimespanMaker(
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
                    voice_identifier=('Violin \\d+ Bowing Voice',),
                    ),
                ),
            duration_in_seconds=durationtools.Duration(2, 1),
            tempo=indicatortools.Tempo(
                duration=durationtools.Duration(1, 4),
                units_per_minute=72,
                ),
            time_signatures=indicatortools.TimeSignatureInventory(
                [
                    indicatortools.TimeSignature((5, 8)),
                    indicatortools.TimeSignature((7, 16)),
                    ]
                ),
            )

    ::

        >>> lilypond_file = segment_maker()
        TimespanManager:
            total: ...
        RhythmManager:
            populating time signature context: ...
            populating rhythms: ...
            rewriting meters: ...
            cleaning up silences: ...
            total: ...
        AnnotationManager (1):
            total: ...
        GraceAgent:
            total: ...
        PitchAgent:
            total: ...
        RegisterAgent:
            total: ...
        AttachmentAgent:
            total: ...
        AnnotationManager (2):
            total: ...

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_annotation_specifier',
        '_is_final_segment',
        '_time_signatures',
        '_rehearsal_mark',
        '_settings',
        '_duration_in_seconds',
        '_score_template',
        '_tempo',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        annotation_specifier=None,
        is_final_segment=False,
        name=None,
        rehearsal_mark=None,
        score_template=None,
        settings=None,
        duration_in_seconds=None,
        tempo=None,
        time_signatures=None,
        ):
        from consort import makers
        segmentmakertools.SegmentMaker.__init__(
            self,
            name=name,
            )
        self.set_annotation_specifier(annotation_specifier)
        self.set_duration_in_seconds(duration_in_seconds)
        self.set_is_final_segment(is_final_segment) 
        self.set_rehearsal_mark(rehearsal_mark)
        self.set_score_template(score_template)
        self.set_tempo(tempo)
        self.set_time_signatures(time_signatures)
        if settings is not None:
            assert isinstance(settings, collections.Sequence)
            prototype = (makers.VoiceSetting, makers.SegmentSetting)
            assert all(isinstance(x, prototype) for x in settings)
            settings = list(settings)
        self._settings = settings

    ### SPECIAL METHODS ###

    def __call__(self):
        from consort import makers

        segment_session = makers.SegmentSession(segment_maker=self)
        segment_session.score = self.score_template()
        assert isinstance(segment_session.score, scoretools.Score)
        timer = systemtools.Timer()

        with timer:
            print('TimespanManager:')
            segment_session = makers.TimespanManager.execute(
                score_template=self.score_template,
                segment_session=segment_session,
                settings=self.settings or (),
                target_duration=self.target_duration,
                time_signatures=self.time_signatures,
                )
            print('\ttotal:', timer.elapsed_time)

        with timer:
            print('RhythmManager:')
            segment_session = makers.RhythmManager.execute(
                annotation_specifier=self.annotation_specifier,
                segment_session=segment_session,
                )
            print('\ttotal:', timer.elapsed_time)

        with timer:
            print('AnnotationManager (1):')
            if self.annotation_specifier is not None:
                if self.annotation_specifier.show_stage_1:
                    makers.AnnotationManager._annotate_stage_1(segment_session)
                if self.annotation_specifier.show_stage_2:
                    makers.AnnotationManager._annotate_stage_2(segment_session)
                if self.annotation_specifier.show_stage_3:
                    makers.AnnotationManager._annotate_stage_3(segment_session)
                if self.annotation_specifier.show_stage_4:
                    makers.AnnotationManager._annotate_stage_4(segment_session)
                if self.annotation_specifier.show_stage_5:
                    makers.AnnotationManager._annotate_stage_5(segment_session)
            print('\ttotal:', timer.elapsed_time)

        with timer:
            print('GraceAgent:')
            makers.GraceAgent.iterate_score(segment_session.score)
            print('\ttotal:', timer.elapsed_time)

        with timer:
            print('PitchAgent:')
            makers.PitchAgent.iterate_score(segment_session.score)
            print('\ttotal:', timer.elapsed_time)

        #makers.AlterationAgent.iterate_score(segment_session.score)

        with timer:
            print('RegisterAgent:')
            makers.RegisterAgent.iterate_score(segment_session.score)
            print('\ttotal:', timer.elapsed_time)

        #makers.ChordAgent.iterate_score(segment_session.score)

        with timer:
            print('AttachmentAgent:')
            makers.AttachmentAgent.iterate_score(segment_session.score)
            print('\ttotal:', timer.elapsed_time)

        with timer:
            print('AnnotationManager (2):')
            if self.annotation_specifier is not None:
                if self.annotation_specifier.show_annotated_result:
                    should_copy = True
                    if not self.annotation_specifier.show_unannotated_result:
                        should_copy = False
                    makers.AnnotationManager._annotate_stage_6(
                        segment_session=segment_session,
                        should_copy=should_copy,
                        )
                if self.annotation_specifier.show_unannotated_result:
                    segment_session.scores.append(segment_session.score)
            else:
                segment_session.scores.append(segment_session.score)
            print('\ttotal:', timer.elapsed_time)

        lilypond_file = self._make_lilypond_file()
        for score in segment_session.scores:
            score = self._configure_score(score)
            score_block = lilypondfiletools.Block(name='score')
            score_block.items.append(score)
            lilypond_file.items.append(score_block)

        return lilypond_file

    def __illustrate__(self):
        return self()

    ### PRIVATE METHODS ###

    def _configure_score(self, score):
        if self.rehearsal_mark is not None:
            rehearsal_mark_text = 'mark \\markup {{ ' \
                "\\override #'(box-padding . 0.5) " \
                '\\box "{}" " " \\fontsize #-3 "{}" }}'
            rehearsal_mark_text = rehearsal_mark_text.format(
                str(self.rehearsal_mark),
                self.name or '',
                )
            rehearsal_mark = indicatortools.LilyPondCommand(
                rehearsal_mark_text)
            attach(
                rehearsal_mark,
                score['TimeSignatureContext'].select_leaves()[0],
                )
        if self.tempo is not None:
            attach(
                self.tempo,
                score['TimeSignatureContext'].select_leaves()[0],
                )
        if self.is_final_segment:
            score.add_final_markup(self.final_markup)
            score.add_final_bar_line()
        else:
            score.add_final_bar_line('||')
        assert inspect_(score).is_well_formed()
        return score

    @staticmethod
    def _find_voice_names(
        score_template=None,
        voice_identifier=None,
        ):
        r'''Find voice names matching `voice_identifier` in `score_template`:

        ::

            >>> from consort import makers
            >>> score_template = makers.ConsortScoreTemplate(
            ...     violin_count=2,
            ...     viola_count=1,
            ...     cello_count=1,
            ...     contrabass_count=1,
            ...     )
            >>> voice_identifier = (
            ...     'Violin \\d+ Bowing Voice',
            ...     'Viola Bowing Voice',
            ...     )
            >>> makers.ConsortSegmentMaker._find_voice_names(
            ...     score_template=score_template,
            ...     voice_identifier=voice_identifier,
            ...     )
            ('Violin 1 Bowing Voice', 'Violin 2 Bowing Voice', 'Viola Bowing Voice')

        '''
        score = score_template()
        all_voice_names = [voice.name for voice in
            iterate(score).by_class(scoretools.Voice)]
        matched_voice_names = set()
        for voice_identifier in voice_identifier:
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

    def _make_lilypond_file(self):
        lilypond_file = lilypondfiletools.LilyPondFile()
        lilypond_file.use_relative_includes = True
        for file_path in self.stylesheet_file_paths:
            lilypond_file.file_initial_user_includes.append(file_path)
        lilypond_file.file_initial_system_comments[:] = []
        return lilypond_file

    ### PUBLIC METHODS ###

    def add_settings(self, setting):
        from consort import makers
        prototype = (makers.VoiceSetting, makers.SegmentSetting)
        assert isinstance(setting, prototype)
        self._settings.append(setting)

    def set_annotation_specifier(self, annotation_specifier=None):
        from consort import makers
        prototype = (makers.AnnotationSpecifier, type(None))
        assert isinstance(annotation_specifier, prototype)
        self._annotation_specifier = annotation_specifier

    def set_duration_in_seconds(self, duration_in_seconds=None):
        if duration_in_seconds is not None:
            duration_in_seconds = durationtools.Duration(duration_in_seconds)
        self._duration_in_seconds = duration_in_seconds

    def set_rehearsal_mark(self, rehearsal_mark=None):
        self._rehearsal_mark = rehearsal_mark

    def set_is_final_segment(self, is_final_segment=False):
        self._is_final_segment = bool(is_final_segment)

    def set_score_template(self, score_template=None):
        self._score_template = score_template

    def set_tempo(self, tempo=None):
        if tempo is not None and not isinstance(tempo, indicatortools.Tempo):
            tempo = indicatortools.Tempo(tempo)
        self._tempo = tempo

    def set_time_signatures(self, time_signatures=None):
        if time_signatures is not None:
            time_signatures = indicatortools.TimeSignatureInventory(
                items=time_signatures,
                )
        self._time_signatures = time_signatures

    ### PUBLIC PROPERTIES ###

    @property
    def annotation_specifier(self):
        return self._annotation_specifier

    @property
    def duration_in_seconds(self):
        return self._duration_in_seconds

    @property
    def final_markup(self):
        metadata = self.score_package_metadata
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
    def rehearsal_mark(self):
        return self._rehearsal_mark

    @property
    def score_package_metadata(self):
        command = 'from {}.__metadata__ import metadata'
        namespace = {}
        exec(command, namespace, namespace)
        metadata = namespace['metadata']
        return metadata

    @property
    def score_package_module(self):
        module = importlib.import_module(self.score_package_name)
        return module

    @property
    def score_package_name(self):
        return 'consort'

    @property
    def score_package_path(self):
        return self.score_package_module.__path__[0]

    @property
    def score_template(self):
        return self._score_template

    @property
    def settings(self):
        if self._settings is None:
            return None
        return tuple(self._settings)

    @property
    def stylesheet_file_paths(self):
        stylesheets_path = os.path.join(
            self.score_package_path,
            'stylesheets',
            )
        stylesheet_file_names = os.listdir(stylesheets_path)
        stylesheet_file_paths = []
        for file_name in stylesheet_file_names:
            if not file_name.endswith('.ily'):
                continue
            full_path = os.path.join(
                stylesheets_path,
                file_name,
                )
            stylesheet_file_paths.append(full_path)
        return stylesheet_file_paths

    @property
    def target_duration(self):
        tempo = self.tempo
        tempo_duration_in_seconds = durationtools.Duration(
            tempo.duration_to_milliseconds(tempo.duration),
            1000,
            )
        target_duration = durationtools.Duration((
            self.duration_in_seconds / tempo_duration_in_seconds
            ).limit_denominator(16))
        target_duration *= tempo.duration
        return target_duration

    @property
    def tempo(self):
        return self._tempo

    @property
    def time_signatures(self):
        return self._time_signatures
