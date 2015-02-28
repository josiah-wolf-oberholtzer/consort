# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
import importlib
import os
from abjad import attach
from abjad import inspect_
from abjad import iterate
from abjad import mutate
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondfiletools
from abjad.tools import markuptools
from abjad.tools import scoretools
from abjad.tools import spannertools
from abjad.tools import systemtools
from abjad.tools import templatetools
from abjad.tools import timespantools
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
        ...     desired_duration_in_seconds=2,
        ...     tempo=indicatortools.Tempo((1, 4), 72),
        ...     permitted_time_signatures=(
        ...         (5, 8),
        ...         (7, 16),
        ...         ),
        ...     )
        >>> print(format(segment_maker))
        consort.tools.SegmentMaker(
            desired_duration_in_seconds=durationtools.Duration(2, 1),
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
                consort.tools.MusicSetting(
                    timespan_maker=consort.tools.TaleaTimespanMaker(
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
                    violin_1_bowing_voice=consort.tools.MusicSpecifier(),
                    violin_2_bowing_voice=consort.tools.MusicSpecifier(),
                    ),
                ),
            tempo=indicatortools.Tempo(
                duration=durationtools.Duration(1, 4),
                units_per_minute=72,
                ),
            )

    ::

        >>> lilypond_file = segment_maker()
        TimeManager:
            populating independent timespans:
                populated timespans: ...
                found meters: ...
                demultiplexed timespans: ...
                split timespans: ...
                consolidated timespans: ...
                inscribed timespans: ...
                multiplexed timespans: ...
                total: ...
            populating dependent timespans:
                populated timespans: ...
                demultiplexed timespans: ...
                split timespans: ...
                consolidated timespans: ...
                inscribed timespans: ...
                total: ...
            populated silent timespans: ...
            populated score: ...
            collected attack points: ...
            total: ...
        GraceHandler:
            total: ...
        PitchHandler:
            total: ...
        AttachmentHandler:
            total: ...

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_discard_final_silence',
        '_desired_duration_in_seconds',
        '_omit_stylesheets',
        '_is_final_segment',
        '_permitted_time_signatures',
        '_rehearsal_mark',
        '_score_template',
        '_settings',
        '_tempo',
        '_timespan_quantization',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        discard_final_silence=None,
        desired_duration_in_seconds=None,
        omit_stylesheets=None,
        is_final_segment=None,
        name=None,
        permitted_time_signatures=None,
        rehearsal_mark=None,
        score_template=None,
        settings=None,
        tempo=None,
        timespan_quantization=None,
        ):
        makertools.SegmentMaker.__init__(
            self,
            name=name,
            )
        self.discard_final_silence = discard_final_silence
        self.desired_duration_in_seconds = desired_duration_in_seconds
        self.is_final_segment = is_final_segment
        self.omit_stylesheets = omit_stylesheets
        self.permitted_time_signatures = permitted_time_signatures
        self.rehearsal_mark = rehearsal_mark
        self.score_template = score_template
        self.tempo = tempo
        self.timespan_quantization = timespan_quantization
        self.settings = settings

    ### SPECIAL METHODS ###

    def __call__(self, score_context_name=None, verbose=True):
        import consort
        segment_session = consort.SegmentSession(segment_maker=self)
        with systemtools.Timer('\ttotal:', 'TimeManager:', verbose=verbose):
            segment_session = consort.TimeManager.execute(
                discard_final_silence=self.discard_final_silence,
                permitted_time_signatures=self.permitted_time_signatures,
                score_template=self.score_template,
                segment_session=segment_session,
                settings=self.settings or (),
                desired_duration=self.desired_duration,
                timespan_quantization=self.timespan_quantization,
                verbose=verbose,
                )
        with systemtools.ForbidUpdate(segment_session.score):
            with systemtools.Timer(
                enter_message='GraceHandler:',
                exit_message='\ttotal:',
                verbose=verbose,
                ):
                consort.GraceHandler._process_session(
                    segment_session,
                    )
            with systemtools.Timer(
                enter_message='PitchHandler:',
                exit_message='\ttotal:',
                verbose=verbose,
                ):
                consort.PitchHandler._process_session(segment_session)
            with systemtools.Timer(
                enter_message='AttachmentHandler:',
                exit_message='\ttotal:',
                verbose=verbose,
                ):
                consort.AttachmentHandler._process_session(segment_session)
        lilypond_file = self.make_lilypond_file()
        score = self.configure_score(segment_session.score)
        if score_context_name:
            score.context_name = score_context_name
        score_block = lilypondfiletools.Block(name='score')
        score_block.items.append(score)
        lilypond_file.items.append(score_block)
        lilypond_file.score = score
        with systemtools.Timer(
            enter_message='Checking for wellformedness violations:',
            exit_message='\ttotal:',
            verbose=verbose,
            ):
            self.validate_score(score, verbose=verbose)
        return lilypond_file

    def __illustrate__(self):
        return self()

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
        timespan_identifier=None,
        timespan_maker=None,
        **music_specifiers
        ):
        import consort
        setting = consort.MusicSetting(
            timespan_identifier=timespan_identifier,
            timespan_maker=timespan_maker,
            **music_specifiers
            )
        self._settings.append(setting)

    def attach_final_bar_line(self, score):
        if self.is_final_segment:
            score.add_final_markup(self.final_markup)
            score.add_final_bar_line(abbreviation='|.', to_each_voice=True)
        else:
            score.add_final_bar_line(abbreviation='||', to_each_voice=True)

    def attach_rehearsal_mark(self, score):
        first_leaf = score['TimeSignatureContext'].select_leaves()[0]
        if self.rehearsal_mark is not None:
            markup_a = markuptools.Markup(str(self.rehearsal_mark))
            markup_a = markup_a.caps()
            markup_a = markup_a.box()
            markup_a = markup_a.override(('box-padding', 0.5))
            markup_b = markuptools.Markup('"{}"'.format(self.name or ' '))
            markup_b = markup_b.fontsize(-3)
            markup = markuptools.Markup.concat([markup_a, ' ', markup_b])
            rehearsal_mark = indicatortools.RehearsalMark(markup=markup)
            attach(rehearsal_mark, first_leaf)

    def attach_tempo(self, score):
        first_leaf = score['TimeSignatureContext'].select_leaves()[0]
        if self.tempo is not None:
            attach(self.tempo, first_leaf)

    def configure_score(self, score):
        self.attach_tempo(score)
        self.attach_rehearsal_mark(score)
        self.attach_final_bar_line(score)
        return score

    def copy_voice(
        self,
        voice,
        attachment_names=None,
        new_voice_name=None,
        new_context_name=None,
        remove_grace_containers=False,
        remove_ties=False,
        replace_rests_with_skips=False,
        ):
        new_voice = mutate(voice).copy()
        if new_voice_name:
            new_voice.name = new_voice_name
        if new_context_name:
            new_voice.context_name = new_context_name
        rests = []
        for component in iterate(new_voice).depth_first(capped=True):
            agent = inspect_(component)
            indicators = agent.get_indicators(unwrap=False)
            spanners = agent.get_spanners()
            for x in indicators:
                if not x.name:
                    continue
                if attachment_names and \
                    not any(x.name.startswith(_) for _ in attachment_names):
                    x._detach()
            for x in spanners:
                if remove_ties and isinstance(x, spannertools.Tie):
                    x._detach()
                if not x.name:
                    continue
                elif attachment_names and \
                    not any(x.name.startswith(_) for _ in attachment_names):
                    x._detach()
            if replace_rests_with_skips and \
                isinstance(component, scoretools.Rest):
                rests.append(component)
            grace_containers = agent.get_grace_containers()
            if grace_containers and remove_grace_containers:
                for grace_container in grace_containers:
                    grace_container._detach()
        if replace_rests_with_skips:
            for rest in rests:
                indicators = inspect_(rest).get_indicators(
                    durationtools.Multiplier,
                    )
                skip = scoretools.Skip(rest)
                if indicators:
                    attach(indicators[0], skip)
                mutate(rest).replace(skip)
        return new_voice

    @staticmethod
    def logical_tie_to_music_specifier(logical_tie):
        import consort
        parentage = inspect_(logical_tie.head).get_parentage()
        music_specifier = None
        prototype = consort.MusicSpecifier
        for parent in parentage:
            if not inspect_(parent).has_indicator(prototype):
                continue
            music_specifier = inspect_(parent).get_indicator(prototype)
        return music_specifier

    @staticmethod
    def logical_tie_to_voice(logical_tie):
        parentage = inspect_(logical_tie.head).get_parentage()
        voice = None
        for parent in parentage:
            if isinstance(parent, scoretools.Voice):
                voice = parent
        return voice

    def make_lilypond_file(self):
        lilypond_file = lilypondfiletools.LilyPondFile()
        if not self.omit_stylesheets:
            lilypond_file.use_relative_includes = True
            for file_path in self.stylesheet_file_paths:
                lilypond_file.file_initial_user_includes.append(file_path)
        lilypond_file.file_initial_system_comments[:] = []
        return lilypond_file

    @staticmethod
    def validate_score(score, verbose=True):
        manager = systemtools.WellformednessManager(expr=score)
        triples = manager()
        for current_violators, current_total, current_check in triples:
            if verbose:
                print('\t', current_violators, current_total, current_check)
        if current_violators:
            raise AssertionError

    ### PUBLIC PROPERTIES ###

    @property
    def discard_final_silence(self):
        return self._discard_final_silence

    @discard_final_silence.setter
    def discard_final_silence(self, discard_final_silence):
        if discard_final_silence is not None:
            discard_final_silence = bool(discard_final_silence)
        self._discard_final_silence = discard_final_silence

    @property
    def desired_duration_in_seconds(self):
        return self._desired_duration_in_seconds

    @desired_duration_in_seconds.setter
    def desired_duration_in_seconds(self, desired_duration_in_seconds):
        if desired_duration_in_seconds is not None:
            desired_duration_in_seconds = durationtools.Duration(desired_duration_in_seconds)
        self._desired_duration_in_seconds = desired_duration_in_seconds

    @property
    def final_markup(self):
        metadata = self.score_package_metadata
        contents = [' ', ' ', ' ']
        locale = metadata.get('locale', 'Nowhere')
        if isinstance(locale, str):
            contents.append(locale)
        else:
            contents.extend(locale)
        time_period_default = ('2001', '3001')
        time_period = metadata.get('time_period', time_period_default)
        time_period = '{} - {}'.format(time_period[0], time_period[1])
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
        r'''Gets and sets if segment maker's segment is final.

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> segment_maker.is_final_segment = True
            >>> print(format(segment_maker))
            consort.tools.SegmentMaker(
                is_final_segment=True,
                )

        '''
        return self._is_final_segment

    @is_final_segment.setter
    def is_final_segment(self, is_final_segment):
        if is_final_segment is not None:
            is_final_segment = bool(is_final_segment)
        self._is_final_segment = is_final_segment

    @property
    def omit_stylesheets(self):
        return self._omit_stylesheets

    @omit_stylesheets.setter
    def omit_stylesheets(self, omit_stylesheets):
        if omit_stylesheets is not None:
            omit_stylesheets = bool(omit_stylesheets)
        self._omit_stylesheets = omit_stylesheets

    @property
    def permitted_time_signatures(self):
        r'''Gets and sets segment maker's permitted time signatures.

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> time_signatures = [(3, 4), (2, 4), (5, 8)]
            >>> segment_maker.permitted_time_signatures = time_signatures
            >>> print(format(segment_maker))
            consort.tools.SegmentMaker(
                permitted_time_signatures=indicatortools.TimeSignatureInventory(
                    [
                        indicatortools.TimeSignature((3, 4)),
                        indicatortools.TimeSignature((2, 4)),
                        indicatortools.TimeSignature((5, 8)),
                        ]
                    ),
                )

        '''
        return self._permitted_time_signatures

    @permitted_time_signatures.setter
    def permitted_time_signatures(self, permitted_time_signatures):
        if permitted_time_signatures is not None:
            permitted_time_signatures = indicatortools.TimeSignatureInventory(
                items=permitted_time_signatures,
                )
        self._permitted_time_signatures = permitted_time_signatures

    @property
    def rehearsal_mark(self):
        return self._rehearsal_mark

    @rehearsal_mark.setter
    def rehearsal_mark(self, rehearsal_mark):
        self._rehearsal_mark = rehearsal_mark

    @property
    def score_package_metadata(self):
        module_name = '{}.__metadata__'.format(self.score_package_name)
        try:
            module = importlib.import_module(module_name)
            metadata = getattr(module, 'metadata')
        except ImportError:
            metadata = {}
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
        r'''Gets and sets segment maker's score template.

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> score_template = templatetools.StringOrchestraScoreTemplate(
            ...     violin_count=2,
            ...     viola_count=1,
            ...     cello_count=1,
            ...     contrabass_count=0,
            ...     )
            >>> segment_maker.score_template = score_template
            >>> print(format(segment_maker))
            consort.tools.SegmentMaker(
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
        return self._score_template

    @score_template.setter
    def score_template(self, score_template):
        self._score_template = score_template

    @property
    def settings(self):
        return tuple(self._settings)

    @settings.setter
    def settings(self, settings):
        import consort
        if settings is not None:
            if not isinstance(settings, collections.Sequence):
                settings = (settings,)
            assert all(isinstance(_, consort.MusicSetting) for _ in settings)
            settings = list(settings)
        self._settings = settings or []

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
    def desired_duration(self):
        tempo = self.tempo
        tempo_desired_duration_in_seconds = durationtools.Duration(
            tempo.duration_to_milliseconds(tempo.duration),
            1000,
            )
        desired_duration = durationtools.Duration((
            self.desired_duration_in_seconds / tempo_desired_duration_in_seconds
            ).limit_denominator(8))
        desired_duration *= tempo.duration
        count = desired_duration // durationtools.Duration(1, 8)
        desired_duration = durationtools.Duration(count, 8)
        assert 0 < desired_duration
        return desired_duration

    @property
    def tempo(self):
        r'''Gets and sets segment maker tempo.

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> tempo = indicatortools.Tempo((1, 4), 52)
            >>> segment_maker.tempo = tempo
            >>> print(format(segment_maker))
            consort.tools.SegmentMaker(
                tempo=indicatortools.Tempo(
                    duration=durationtools.Duration(1, 4),
                    units_per_minute=52,
                    ),
                )

        '''
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        if tempo is not None:
            if not isinstance(tempo, indicatortools.Tempo):
                tempo = indicatortools.Tempo(tempo)
        self._tempo = tempo

    @property
    def timespan(self):
        return timespantools.Timespan(
            start_offset=0,
            stop_offset=self.desired_duration,
            )

    @property
    def timespan_quantization(self):
        r'''Gets and sets segment maker timespan quantization.

        ::

            >>> import consort
            >>> segment_maker = consort.SegmentMaker()
            >>> timespan_quantization = (1, 8)
            >>> segment_maker.timespan_quantization = timespan_quantization
            >>> print(format(segment_maker))
            consort.tools.SegmentMaker(
                timespan_quantization=durationtools.Duration(1, 8),
                )

        '''
        return self._timespan_quantization

    @timespan_quantization.setter
    def timespan_quantization(self, timespan_quantization):
        if timespan_quantization is not None:
            timespan_quantization = \
                durationtools.Duration(timespan_quantization)
        self._timespan_quantization = timespan_quantization