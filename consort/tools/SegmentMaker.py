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
from abjad.tools import templatetools
from abjad.tools import timespantools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from experimental.tools import makertools


class SegmentMaker(makertools.SegmentMaker):
    r'''A Consort segment-maker.

    ::

        >>> import consort
        >>> score_template = templatetools.StringOrchestraScoreTemplate(
        ...     violin_count=2,
        ...     viola_count=1,
        ...     cello_count=1,
        ...     contrabass_count=0,
        ...     )

    ::

        >>> segment_maker = consort.SegmentMaker(
        ...     score_template=score_template,
        ...     settings=(
        ...         consort.MusicSetting(
        ...             timespan_maker=consort.TaleaTimespanMaker(),
        ...             violin_1_bowing_voice=consort.MusicSpecifier(),
        ...             violin_2_bowing_voice=consort.MusicSpecifier(),
        ...             ),
        ...         ),
        ...     duration_in_seconds=2,
        ...     tempo=indicatortools.Tempo((1, 4), 72),
        ...     permitted_time_signatures=(
        ...         (5, 8),
        ...         (7, 16),
        ...         ),
        ...     )
        >>> print(format(segment_maker))
        consort.SegmentMaker(
            duration_in_seconds=durationtools.Duration(2, 1),
            permitted_time_signatures=indicatortools.TimeSignatureInventory(
                [
                    indicatortools.TimeSignature((5, 8)),
                    indicatortools.TimeSignature((7, 16)),
                    ]
                ),
            score_template=templatetools.StringOrchestraScoreTemplate(
                violin_count=2,
                viola_count=1,
                cello_count=1,
                contrabass_count=0,
                split_hands=True,
                use_percussion_clefs=False,
                ),
            settings=(
                consort.MusicSetting(
                    timespan_maker=consort.TaleaTimespanMaker(
                        can_split=True,
                        playing_talea=rhythmmakertools.Talea(
                            counts=(4,),
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
                    violin_1_bowing_voice=consort.MusicSpecifier(),
                    violin_2_bowing_voice=consort.MusicSpecifier(),
                    ),
                ),
            tempo=indicatortools.Tempo(
                duration=durationtools.Duration(1, 4),
                units_per_minute=72,
                ),
            )

    ::

        >>> lilypond_file = segment_maker()
        TimespanManager:
            made independent timespans: ...
            found meters: ...
            made voicewise timespans (1/2): ...
            cleaned-up performed timespans: ...
            made dependent timespans: ...
            made voicewise timespans (2/2): ...
            made silent timespans: ...
            total: ...
        RhythmManager:
            populated time signature context: ...
            populated rhythms: ...
            consolidated silences: ...
            rewrote meters: ...
            cleaned up silences: ...
            cleaned up logical ties: ...
            collected attack points: ...
            total: ...
        AnnotationManager (1):
            total: ...
        GraceHandler:
            total: ...
        PitchHandler:
            total: ...
        AttachmentHandler:
            total: ...
        AnnotationManager (2):
            total: ...

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_annotation_specifier',
        '_discard_final_silence',
        '_duration_in_seconds',
        '_is_final_segment',
        '_permitted_time_signatures',
        '_rehearsal_mark',
        '_score_template',
        '_settings',
        '_tempo',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        annotation_specifier=None,
        discard_final_silence=None,
        duration_in_seconds=None,
        is_final_segment=None,
        name=None,
        permitted_time_signatures=None,
        rehearsal_mark=None,
        score_template=None,
        settings=None,
        tempo=None,
        ):
        import consort
        makertools.SegmentMaker.__init__(
            self,
            name=name,
            )
        if discard_final_silence is not None:
            discard_final_silence = bool(discard_final_silence)
        self._discard_final_silence = discard_final_silence
        self.set_annotation_specifier(annotation_specifier)
        self.set_duration_in_seconds(duration_in_seconds)
        self.set_is_final_segment(is_final_segment)
        self.set_rehearsal_mark(rehearsal_mark)
        self.set_score_template(score_template)
        self.set_tempo(tempo)
        self.set_permitted_time_signatures(permitted_time_signatures)
        if settings is not None:
            assert isinstance(settings, collections.Sequence)
            prototype = consort.MusicSetting
            assert all(isinstance(x, prototype) for x in settings)
            settings = list(settings)
        self._settings = settings or []

    ### SPECIAL METHODS ###

    def __call__(self):
        import consort

        segment_session = consort.SegmentSession(segment_maker=self)
        segment_session.score = self.score_template()
        assert isinstance(segment_session.score, scoretools.Score)
        timer = systemtools.Timer()

        with timer:
            print('TimespanManager:')
            segment_session = consort.TimespanManager.execute(
                discard_final_silence=self.discard_final_silence,
                permitted_time_signatures=self.permitted_time_signatures,
                score_template=self.score_template,
                segment_session=segment_session,
                settings=self.settings or (),
                target_duration=self.target_duration,
                )
            print('\ttotal:', timer.elapsed_time)

        with timer:
            print('RhythmManager:')
            segment_session = consort.RhythmManager.execute(
                annotation_specifier=self.annotation_specifier,
                segment_session=segment_session,
                )
            print('\ttotal:', timer.elapsed_time)

        with timer:
            print('AnnotationManager (1):')
            if self.annotation_specifier is not None:
                if self.annotation_specifier.show_stage_1:
                    consort.AnnotationManager._annotate_stage_1(segment_session)
                if self.annotation_specifier.show_stage_2:
                    consort.AnnotationManager._annotate_stage_2(segment_session)
                if self.annotation_specifier.show_stage_3:
                    consort.AnnotationManager._annotate_stage_3(segment_session)
                if self.annotation_specifier.show_stage_4:
                    consort.AnnotationManager._annotate_stage_4(segment_session)
                if self.annotation_specifier.show_stage_5:
                    consort.AnnotationManager._annotate_stage_5(segment_session)
            print('\ttotal:', timer.elapsed_time)

        with systemtools.ForbidUpdate(segment_session.score):

            with timer:
                print('GraceHandler:')
                consort.GraceHandler._process_session(
                    segment_session,
                    )
                print('\ttotal:', timer.elapsed_time)

            with timer:
                print('PitchHandler:')
                consort.PitchHandler._process_session(
                    segment_session,
                    )
                print('\ttotal:', timer.elapsed_time)

            with timer:
                print('AttachmentHandler:')
                consort.AttachmentHandler._process_session(
                    segment_session,
                    )
                print('\ttotal:', timer.elapsed_time)

        with timer:
            print('AnnotationManager (2):')
            if self.annotation_specifier is not None:
                if self.annotation_specifier.show_annotated_result:
                    should_copy = True
                    if not self.annotation_specifier.show_unannotated_result:
                        should_copy = False
                    consort.AnnotationManager._annotate_stage_6(
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

    @staticmethod
    def _logical_tie_to_voice(logical_tie):
        parentage = inspect_(logical_tie.head).get_parentage()
        voice = None
        for parent in parentage:
            if isinstance(parent, scoretools.Voice):
                voice = parent
        return voice

    @staticmethod
    def _logical_tie_to_music_specifier(logical_tie):
        import consort
        parentage = inspect_(logical_tie.head).get_parentage()
        music_specifier = None
        prototype = consort.MusicSpecifier
        for parent in parentage:
            if not inspect_(parent).has_indicator(prototype):
                continue
            music_specifier = inspect_(parent).get_indicator(prototype)
        return music_specifier

    def _configure_score(self, score):
        if self.rehearsal_mark is not None:
            markup = markuptools.Markup(r'''
                \override #'(box-padding . 0.5)
                    \box "{}"
                " "
                \fontsize #-3
                    "{}"
                '''.format(str(self.rehearsal_mark), self.name or ' '),
                )
            rehearsal_mark = indicatortools.RehearsalMark(
                markup=markup,
                )
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
            score.add_final_bar_line(
                to_each_voice=True,
                )
        else:
            score.add_final_bar_line(
                abbreviation='||',
                to_each_voice=True,
                )
        assert inspect_(score).is_well_formed()
        return score

    @staticmethod
    def _find_voice_names(
        score_template=None,
        voice_identifier=None,
        ):
        r'''Find voice names matching `voice_identifier` in `score_template`:

        ::

            >>> import consort
            >>> score_template = templatetools.StringOrchestraScoreTemplate(
            ...     violin_count=2,
            ...     viola_count=1,
            ...     cello_count=1,
            ...     contrabass_count=1,
            ...     )
            >>> voice_identifier = (
            ...     'Violin \\d+ Bowing Voice',
            ...     'Viola Bowing Voice',
            ...     )
            >>> consort.SegmentMaker._find_voice_names(
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

    ### PRIVATE PROPERTIES ###

    @property
    def _storage_format_specification(self):
        from abjad.tools import systemtools
        manager = systemtools.StorageFormatManager
        keyword_argument_names = manager.get_keyword_argument_names(self)
        keyword_argument_names = list(keyword_argument_names)
        if not self.settings:
            keyword_argument_names.remove('settings')
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=keyword_argument_names
            )

    ### PUBLIC METHODS ###

    def add_setting(
        self,
        color=None,
        timespan_identifier=None,
        timespan_maker=None,
        **music_specifiers
        ):
        import consort
        setting = tools.MusicSetting(
            color=color,
            timespan_identifier=timespan_identifier,
            timespan_maker=timespan_maker,
            **music_specifiers
            )
        self._settings.append(setting)

    def set_annotation_specifier(self, annotation_specifier=None):
        import consort
        prototype = (tools.AnnotationSpecifier, type(None))
        assert isinstance(annotation_specifier, prototype)
        self._annotation_specifier = annotation_specifier

    def set_duration_in_seconds(self, duration_in_seconds=None):
        if duration_in_seconds is not None:
            duration_in_seconds = durationtools.Duration(duration_in_seconds)
        self._duration_in_seconds = duration_in_seconds

    def set_rehearsal_mark(self, rehearsal_mark=None):
        self._rehearsal_mark = rehearsal_mark

    def set_is_final_segment(self, is_final_segment=None):
        r'''

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> segment_maker.set_is_final_segment(True)
            >>> print(format(segment_maker))
            consort.SegmentMaker(
                is_final_segment=True,
                )

        '''
        if not is_final_segment:
            is_final_segment = None
        else:
            is_final_segment = True
        self._is_final_segment = is_final_segment

    def set_score_template(self, score_template=None):
        r'''

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> score_template = templatetools.StringOrchestraScoreTemplate(
            ...     violin_count=2,
            ...     viola_count=1,
            ...     cello_count=1,
            ...     contrabass_count=0,
            ...     )
            >>> segment_maker.set_score_template(score_template)
            >>> print(format(segment_maker))
            consort.SegmentMaker(
                score_template=templatetools.StringOrchestraScoreTemplate(
                    violin_count=2,
                    viola_count=1,
                    cello_count=1,
                    contrabass_count=0,
                    split_hands=True,
                    use_percussion_clefs=False,
                    ),
                )

        '''
        self._score_template = score_template

    def set_tempo(self, tempo=None):
        r'''

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> tempo = indicatortools.Tempo((1, 4), 52)
            >>> segment_maker.set_tempo(tempo)
            >>> print(format(segment_maker))
            consort.SegmentMaker(
                tempo=indicatortools.Tempo(
                    duration=durationtools.Duration(1, 4),
                    units_per_minute=52,
                    ),
                )

        '''
        if tempo is not None and not isinstance(tempo, indicatortools.Tempo):
            tempo = indicatortools.Tempo(tempo)
        self._tempo = tempo

    def set_permitted_time_signatures(self, permitted_time_signatures=None):
        r'''

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> time_signatures = [(3, 4), (2, 4), (5, 8)]
            >>> segment_maker.set_permitted_time_signatures(time_signatures)
            >>> print(format(segment_maker))
            consort.SegmentMaker(
                permitted_time_signatures=indicatortools.TimeSignatureInventory(
                    [
                        indicatortools.TimeSignature((3, 4)),
                        indicatortools.TimeSignature((2, 4)),
                        indicatortools.TimeSignature((5, 8)),
                        ]
                    ),
                )

        '''
        if permitted_time_signatures is not None:
            permitted_time_signatures = indicatortools.TimeSignatureInventory(
                items=permitted_time_signatures,
                )
        self._permitted_time_signatures = permitted_time_signatures

    ### PUBLIC PROPERTIES ###

    @property
    def annotation_specifier(self):
        return self._annotation_specifier

    @property
    def discard_final_silence(self):
        return self._discard_final_silence

    @property
    def duration_in_seconds(self):
        return self._duration_in_seconds

    @property
    def final_markup(self):
        metadata = self.score_package_metadata
        contents = [' ', ' ', ' ']
        locale = metadata['locale']
        if isinstance(locale, str):
            contents.append(locale)
        else:
            contents.extend(locale)
        time_period = '{} - {}'.format(
            metadata['time_period'][0],
            metadata['time_period'][1],
            )
        contents.append(time_period)
        
        column = markuptools.MarkupCommand(
            'center-column', contents
            )
        italic = markuptools.MarkupCommand(
            'italic',
            column,
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
    def rehearsal_mark(self):
        return self._rehearsal_mark

    @property
    def score_package_metadata(self):
        module_name = '{}.__metadata__'.format(self.score_package_name)
        module = importlib.import_module(module_name)
        metadata = getattr(module, 'metadata')
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
            ).limit_denominator(8))
        target_duration *= tempo.duration
        count = target_duration // durationtools.Duration(1, 8)
        target_duration = durationtools.Duration(count, 8)
        assert 0 < target_duration
        return target_duration

    @property
    def tempo(self):
        return self._tempo

    @property
    def timespan(self):
        return timespantools.Timespan(
            start_offset=0,
            stop_offset=self.target_duration,
            )