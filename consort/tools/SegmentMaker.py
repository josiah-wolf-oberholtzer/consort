# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
import importlib
import itertools
import os
from abjad import attach
from abjad import detach
from abjad import inspect_
from abjad import iterate
from abjad import mutate
from abjad import new
from abjad import set_
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondfiletools
from abjad.tools import markuptools
from abjad.tools import mathtools
from abjad.tools import metertools
from abjad.tools import rhythmmakertools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools import spannertools
from abjad.tools import systemtools
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

        >>> lilypond_file = segment_maker() # doctest: +SKIP
        Performing rhythmic interpretation:
            populating independent timespans:
                populated timespans: ...
                found meters: ...
                demultiplexed timespans: ...
                split timespans: ...
                pruned malformed timespans: ...
                consolidated timespans: ...
                inscribed timespans: ...
                multiplexed timespans: ...
                pruned short timespans: ...
                pruned meters: ...
                total: ...
            populating dependent timespans:
                populated timespans: ...
                demultiplexed timespans: ...
                split timespans: ...
                pruned short timespans: ...
                pruned malformed timespans: ...
                consolidated timespans: ...
                inscribed timespans: ...
                total: ...
            populated silent timespans: ...
            validated timespans: ...
            rewriting meters:
                rewriting Cello Bowing Voice: 2
                rewriting Cello Fingering Voice: 2
                rewriting Viola Bowing Voice: 2
                rewriting Viola Fingering Voice: 2
                rewriting Violin 1 Bowing Voice: 3
                rewriting Violin 1 Fingering Voice: 2
                rewriting Violin 2 Bowing Voice: 3
                rewriting Violin 2 Fingering Voice: 2
                total: 0.169489145279
            populated score: ...
            total: ...
        Performing non-rhythmic interpretation:
            collected attack points: ...
            handled graces: ...
            handled pitches: ...
            handled attachments: ...
            total: ...
        Checking for well-formedness violations:
            [] 24 check_beamed_quarter_notes
            [] 18 check_discontiguous_spanners
            [] 80 check_duplicate_ids
            [] 0 check_intermarked_hairpins
            [] 2 check_misdurated_measures
            [] 2 check_misfilled_measures
            [] 4 check_mispitched_ties
            [] 24 check_misrepresented_flags
            [] 80 check_missing_parents
            [] 2 check_nested_measures
            [] 0 check_overlapping_beams
            [] 0 check_overlapping_glissandi
            [] 0 check_overlapping_octavation_spanners
            [] 0 check_short_hairpins
            total: ...

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attack_point_map',
        '_desired_duration_in_seconds',
        '_discard_final_silence',
        '_is_annotated',
        '_lilypond_file',
        '_maximum_meter_run_length',
        '_meters',
        '_name',
        '_omit_stylesheets',
        '_permitted_time_signatures',
        '_previous_segment_metadata',
        '_repeat',
        '_score',
        '_score_template',
        '_segment_metadata',
        '_settings',
        '_tempo',
        '_timespan_quantization',
        '_voice_names',
        '_voicewise_timespans',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        desired_duration_in_seconds=None,
        discard_final_silence=None,
        is_annotated=None,
        maximum_meter_run_length=None,
        name=None,
        omit_stylesheets=None,
        permitted_time_signatures=None,
        repeat=None,
        score_template=None,
        settings=None,
        tempo=None,
        timespan_quantization=None,
        ):
        makertools.SegmentMaker.__init__(
            self,
            )
        self.name = name
        self.is_annotated = is_annotated
        self.discard_final_silence = discard_final_silence
        self.desired_duration_in_seconds = desired_duration_in_seconds
        self.maximum_meter_run_length = maximum_meter_run_length
        self.omit_stylesheets = omit_stylesheets
        self.permitted_time_signatures = permitted_time_signatures
        self.score_template = score_template
        self.tempo = tempo
        self.timespan_quantization = timespan_quantization
        self.settings = settings
        self.repeat = repeat
        self._reset()

    ### SPECIAL METHODS ###

    def __call__(
        self,
        annotate=None,
        verbose=True,
        segment_metadata=None,
        previous_segment_metadata=None,
        ):
        import consort
        self._reset()
        self._segment_metadata = segment_metadata or \
            datastructuretools.TypedOrderedDict()
        self._previous_segment_metadata = previous_segment_metadata or \
            datastructuretools.TypedOrderedDict()
        self._score = self.score_template()
        self._voice_names = tuple(
            voice.name for voice in
            iterate(self.score).by_class(scoretools.Voice)
            )

        with systemtools.Timer(
            '    total:',
            'Performing rhythmic interpretation:',
            verbose=verbose,
            ):
            self.interpret_rhythms(verbose=verbose)
        with systemtools.Timer(
            '    total:',
            'Performing non-rhythmic interpretation:',
            verbose=verbose,
            ):
            with systemtools.Timer(
                '    collected attack points:',
                verbose=verbose,
                ):
                attack_point_map = self.collect_attack_points(self.score)
            self._attack_point_map = attack_point_map
            with systemtools.ForbidUpdate(self.score, update_on_exit=True):
                with systemtools.Timer(
                    '    handled graces:',
                    verbose=verbose,
                    ):
                    consort.GraceHandler._process_session(self)
            with systemtools.ForbidUpdate(self.score, update_on_exit=True):
                with systemtools.Timer(
                    '    handled pitches:',
                    verbose=verbose,
                    ):
                    consort.PitchHandler._process_session(self)
            with systemtools.ForbidUpdate(self.score, update_on_exit=True):
                with systemtools.Timer(
                    '    handled attachments:',
                    verbose=verbose,
                    ):
                    consort.AttachmentHandler._process_session(self)
            self.configure_score()
            self.configure_lilypond_file()
        with systemtools.Timer(
            enter_message='Checking for well-formedness violations:',
            exit_message='    total:',
            verbose=verbose,
            ):
            self.validate_score(self.score, verbose=verbose)

        is_annotated = self.is_annotated
        if annotate is not None:
            is_annotated = annotate
        if is_annotated:
            consort.annotate(self.score)

        self.update_segment_metadata()

        return self.lilypond_file, self._segment_metadata

    ### PRIVATE METHODS ###

    def _reset(self):
        self._attack_point_map = None
        self._lilypond_file = None
        self._meters = None
        self._score = None
        self._voice_names = None
        self._voicewise_timespans = None
        self._segment_metadata = None
        self._previous_segment_metadata = None

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

    def get_end_tempo_indication(self):
        prototype = indicatortools.Tempo
        context = self._score['Time Signature Context']
        last_leaf = inspect_(context).get_leaf(-1)
        effective_tempo = inspect_(last_leaf).get_effective(prototype)
        if effective_tempo is not None:
            duration = effective_tempo.duration.pair
            units_per_minute = effective_tempo.units_per_minute
            effective_tempo = (duration, units_per_minute)
        return effective_tempo

    def get_end_time_signature(self):
        prototype = indicatortools.TimeSignature
        context = self._score['Time Signature Context']
        last_measure = context[-1]
        time_signature = inspect_(last_measure).get_effective(prototype)
        if not time_signature:
            return
        pair = time_signature.pair
        return pair

    def add_time_signature_context(self):
        import consort
        time_signatures = [_.implied_time_signature for _ in self.meters]
        measures = scoretools.make_spacer_skip_measures(time_signatures)
        if 'Time Signature Context' not in self.score:
            time_signature_context = \
                consort.ScoreTemplateManager.make_time_signature_context()
            self.score.insert(0, time_signature_context)
        self.score['Time Signature Context'].extend(measures)

    def add_setting(
        self,
        silenced_contexts=None,
        timespan_identifier=None,
        timespan_maker=None,
        **music_specifiers
        ):
        import consort
        setting = consort.MusicSetting(
            silenced_contexts=silenced_contexts,
            timespan_identifier=timespan_identifier,
            timespan_maker=timespan_maker,
            **music_specifiers
            )
        self._settings.append(setting)

    def attach_initial_bar_line(self):
        segment_number = self._segment_metadata.get('segment_number', 1)
        if self.repeat:
            return
        elif self._previous_segment_metadata.get('is_repeated'):
            return
        elif segment_number == 1:
            return
        bar_line = indicatortools.LilyPondCommand('bar "||"', 'before')
        for staff in iterate(self.score).by_class(scoretools.Staff):
            attach(bar_line, staff)

    def attach_final_bar_line(self):
        segment_number = self._segment_metadata.get('segment_number', 1)
        segment_count = self._segment_metadata.get('segment_count', 1)
        if self.repeat:
            repeat = indicatortools.Repeat()
            for staff in iterate(self.score).by_class(scoretools.Staff):
                attach(repeat, staff)
            attach(repeat, self.score['Time Signature Context'])
        elif segment_number == segment_count:
            self.score.add_final_bar_line(
                abbreviation='|.',
                to_each_voice=True,
                )
        if segment_number == segment_count:
            self.score.add_final_markup(self.final_markup)

    def get_rehearsal_letter(self):
        segment_number = self._segment_metadata.get('segment_number', 1)
        if segment_number == 1:
            return ''
        segment_index = segment_number - 1
        rehearsal_ordinal = ord('A') - 1 + segment_index
        rehearsal_letter = chr(rehearsal_ordinal)
        return rehearsal_letter

    def attach_rehearsal_mark(self):
        markup_a, markup_b = None, None
        first_leaf = self.score['Time Signature Context'].select_leaves()[0]
        rehearsal_letter = self.get_rehearsal_letter()
        if rehearsal_letter:
            markup_a = markuptools.Markup(rehearsal_letter)
            markup_a = markup_a.caps().pad_around(0.5).box()
        if self.name:
            markup_b = markuptools.Markup('"{}"'.format(self.name or ' '))
            markup_b = markup_b.fontsize(-3)
        if markup_a and markup_b:
            markup = markuptools.Markup.concat([markup_a, ' ', markup_b])
        else:
            markup = markup_a or markup_b
        if markup:
            rehearsal_mark = indicatortools.RehearsalMark(markup=markup)
            attach(rehearsal_mark, first_leaf)

    def attach_tempo(self):
        first_leaf = self.score['Time Signature Context'].select_leaves()[0]
        if self.tempo is not None:
            attach(self.tempo, first_leaf)

    def configure_lilypond_file(self):
        lilypond_file = lilypondfiletools.LilyPondFile()
        if not self.omit_stylesheets:
            lilypond_file.use_relative_includes = True
            path = os.path.join(
                '..',
                '..',
                'stylesheets',
                'stylesheet.ily',
                )
            lilypond_file.file_initial_user_includes.append(path)
            if 1 < self._segment_metadata.get('segment_number', 1):
                path = os.path.join(
                    '..',
                    '..',
                    'stylesheets',
                    'nonfirst-segment.ily',
                    )
                lilypond_file.file_initial_user_includes.append(path)
        lilypond_file.file_initial_system_comments[:] = []
        score_block = lilypondfiletools.Block(name='score')
        score_block.items.append(self.score)
        lilypond_file.items.append(score_block)
        lilypond_file.score = self.score
        self._lilypond_file = lilypond_file

    def configure_score(self):
        self.add_time_signature_context()
        self.attach_tempo()
        self.attach_rehearsal_mark()
        self.attach_initial_bar_line()
        self.attach_final_bar_line()
        self.set_bar_number()
        self.postprocess_grace_containers()
        self.postprocess_ties()
        self.attach_measure_number_comments()

    def attach_measure_number_comments(self):
        first_bar_number = self._segment_metadata.get('first_bar_number', 1)
        measure_offsets = self.measure_offsets
        for voice in iterate(self.score).by_class(scoretools.Voice):
            for phrase in voice:
                for division in phrase:
                    timespan = inspect_(division).get_timespan()
                    start_offset = timespan.start_offset
                    matched = False
                    for bar_number, measure_offset in enumerate(
                        measure_offsets, first_bar_number):
                        if measure_offset == start_offset:
                            matched = True
                            break
                    if not matched:
                        continue
                    string = 'Measure {}'.format(bar_number)
                    comment = indicatortools.LilyPondComment(string)
                    attach(comment, division)

    def postprocess_ties(self):
        for component in iterate(self.score).depth_first():
            if not inspect_(component).has_spanner(spannertools.Tie):
                continue
            tie = inspect_(component).get_spanner(spannertools.Tie)
            if component != tie[0]:
                continue
            components = tie.components
            detach(tie)
            tie = spannertools.Tie(use_messiaen_style_ties=True)
            attach(tie, components)

    def set_bar_number(self):
        first_bar_number = self._segment_metadata.get('first_bar_number')
        if first_bar_number is not None:
            set_(self.score).current_bar_number = first_bar_number
        #else:
        #    override(self.score).bar_number.transparent = True

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
    def logical_tie_to_division(logical_tie):
        import consort
        parentage = inspect_(logical_tie.head).get_parentage()
        prototype = consort.MusicSpecifier
        for i, parent in enumerate(parentage):
            if inspect_(parent).has_indicator(prototype):
                break
        return parentage[i - 1]

    @staticmethod
    def logical_tie_to_phrase(logical_tie):
        import consort
        parentage = inspect_(logical_tie.head).get_parentage()
        prototype = consort.MusicSpecifier
        for parent in parentage:
            if inspect_(parent).has_indicator(prototype):
                return parent

    @staticmethod
    def logical_tie_to_voice(logical_tie):
        parentage = inspect_(logical_tie.head).get_parentage()
        voice = None
        for parent in parentage:
            if isinstance(parent, scoretools.Voice):
                voice = parent
        return voice

    def postprocess_grace_containers(self):
        import consort
        score = self.score
        stop_trill_span = consort.StopTrillSpan()
        for leaf in iterate(score).by_class(scoretools.Leaf):
            agent = inspect_(leaf)
            spanners = agent.get_spanners(consort.ConsortTrillSpanner)
            if not spanners:
                continue
            after_graces = agent.get_grace_containers('after')
            if not after_graces:
                continue
            after_grace = after_graces[0]
            leaf = after_grace[0]
            attach(stop_trill_span, leaf)

    @staticmethod
    def validate_score(score, verbose=True):
        manager = systemtools.WellformednessManager(expr=score)
        triples = manager()
        for current_violators, current_total, current_check in triples:
            if verbose:
                print('    {} {} {}'.format(
                    current_violators,
                    current_total,
                    current_check,
                    ))
        if current_violators:
            raise AssertionError

    @staticmethod
    def can_rewrite_meter(inscribed_timespan):
        r'''Is true if containers to be inscribed into `inscribed_timespan` can
        undergo meter rewriting. Otherwise false.

        Returns boolean.
        '''
        import consort
        music_specifier = inscribed_timespan.music_specifier
        if music_specifier is None:
            return True
        rhythm_maker = music_specifier.rhythm_maker
        if rhythm_maker is None:
            return True
        if isinstance(rhythm_maker, consort.CompositeRhythmMaker):
            specifier = rhythm_maker.default.duration_spelling_specifier
        else:
            specifier = rhythm_maker.duration_spelling_specifier
        if specifier is None:
            return True
        if specifier.forbid_meter_rewriting:
            return False
        return True

    @staticmethod
    def cleanup_logical_ties(music):
        for logical_tie in iterate(music).by_logical_tie(
            nontrivial=True, pitched=True, reverse=True):
            if len(logical_tie) != 2:
                continue
            if not logical_tie.all_leaves_are_in_same_parent:
                continue
            if logical_tie.written_duration == \
                durationtools.Duration(1, 8):
                mutate(logical_tie).replace([scoretools.Note("c'8")])
            elif logical_tie.written_duration == \
                durationtools.Duration(1, 16):
                mutate(logical_tie).replace([scoretools.Note("c'16")])

    @staticmethod
    def collect_attack_points(score):
        import consort
        attack_point_map = collections.OrderedDict()
        iterator = iterate(score).by_timeline(component_class=scoretools.Note)
        for note in iterator:
            logical_tie = inspect_(note).get_logical_tie()
            if note is not logical_tie.head:
                continue
            attack_point_signature = \
                consort.AttackPointSignature.from_logical_tie(logical_tie)
            attack_point_map[logical_tie] = attack_point_signature
        return attack_point_map

    @staticmethod
    def consolidate_demultiplexed_timespans(demultiplexed_maquette):
        for voice_name in demultiplexed_maquette:
            timespans = demultiplexed_maquette[voice_name]
            consolidated_timespans = SegmentMaker.consolidate_timespans(
                timespans)
            demultiplexed_maquette[voice_name] = consolidated_timespans

    @staticmethod
    def consolidate_rests(music):
        r"""Consolidates non-tupleted rests into separate containers in
        `music`.

        ::

            >>> import consort

        ::

            >>> music = scoretools.Container(r'''
            ...     { r4 c'8 }
            ...     \times 2/3 { d'4 r8 }
            ...     { r4 e'4 f'4 r4 }
            ...     { r4 g8 r8 }
            ...     { r4 }
            ...     { r4 }
            ...     { a'4 \times 2/3 { b'4 r8 } }
            ...     { c''4 r8 }
            ...     ''')
            >>> print(format(music))
            {
                {
                    r4
                    c'8
                }
                \times 2/3 {
                    d'4
                    r8
                }
                {
                    r4
                    e'4
                    f'4
                    r4
                }
                {
                    r4
                    g8
                    r8
                }
                {
                    r4
                }
                {
                    r4
                }
                {
                    a'4
                    \times 2/3 {
                        b'4
                        r8
                    }
                }
                {
                    c''4
                    r8
                }
            }

        ::

            >>> music = consort.SegmentMaker.consolidate_rests(music)
            >>> print(format(music))
            {
                {
                    r4
                }
                {
                    c'8
                }
                \times 2/3 {
                    d'4
                    r8
                }
                {
                    r4
                }
                {
                    e'4
                    f'4
                }
                {
                    r4
                    r4
                }
                {
                    g8
                }
                {
                    r8
                    r4
                    r4
                }
                {
                    a'4
                    \times 2/3 {
                        b'4
                        r8
                    }
                }
                {
                    c''4
                }
                {
                    r8
                }
            }

        Returns `music`.
        """
        prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            )
        initial_music_duration = inspect_(music).get_duration()
        initial_leaves = music.select_leaves()
        if not isinstance(music[0], scoretools.Tuplet):
            leading_silence = scoretools.Container()
            while music[0] and isinstance(music[0][0], prototype):
                leading_silence.append(music[0].pop(0))
            if leading_silence:
                music.insert(0, leading_silence)
        if not isinstance(music[-1], scoretools.Tuplet):
            tailing_silence = scoretools.Container()
            while music[-1] and isinstance(music[-1][-1], prototype):
                tailing_silence.insert(0, music[-1].pop())
            if tailing_silence:
                music.append(tailing_silence)
        if len(music) < 2:
            return music
        indices = reversed(range(len(music) - 1))
        for index in indices:
            division = music[index]
            next_division = music[index + 1]
            silence = scoretools.Container()
            if not isinstance(division, scoretools.Tuplet):
                while division and isinstance(division[-1], prototype):
                    silence.insert(0, division.pop())
            if not isinstance(next_division, scoretools.Tuplet):
                while next_division and \
                    isinstance(next_division[0], prototype):
                    silence.append(next_division.pop(0))
            if silence:
                music.insert(index + 1, silence)
            if not division:
                music.remove(division)
            if not next_division:
                music.remove(next_division)
        for division in music[:]:
            if not division:
                music.remove(division)
        assert inspect_(music).get_duration() == initial_music_duration
        assert music.select_leaves() == initial_leaves
        return music

    @staticmethod
    def consolidate_timespans(timespans, allow_silences=False):
        r'''Consolidates contiguous performed timespans by music specifier.

        ::

            >>> import consort

        ::

            >>> timespans = timespantools.TimespanInventory([
            ...     consort.PerformedTimespan(
            ...         start_offset=0,
            ...         stop_offset=10,
            ...         music_specifier='foo',
            ...         ),
            ...     consort.PerformedTimespan(
            ...         start_offset=10,
            ...         stop_offset=20,
            ...         music_specifier='foo',
            ...         ),
            ...     consort.PerformedTimespan(
            ...         start_offset=20,
            ...         stop_offset=25,
            ...         music_specifier='bar',
            ...         ),
            ...     consort.PerformedTimespan(
            ...         start_offset=40,
            ...         stop_offset=50,
            ...         music_specifier='bar',
            ...         ),
            ...     consort.PerformedTimespan(
            ...         start_offset=50,
            ...         stop_offset=58,
            ...         music_specifier='bar',
            ...         ),
            ...     ])
            >>> print(format(timespans))
            timespantools.TimespanInventory(
                [
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(10, 1),
                        music_specifier='foo',
                        ),
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(10, 1),
                        stop_offset=durationtools.Offset(20, 1),
                        music_specifier='foo',
                        ),
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(20, 1),
                        stop_offset=durationtools.Offset(25, 1),
                        music_specifier='bar',
                        ),
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(40, 1),
                        stop_offset=durationtools.Offset(50, 1),
                        music_specifier='bar',
                        ),
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(50, 1),
                        stop_offset=durationtools.Offset(58, 1),
                        music_specifier='bar',
                        ),
                    ]
                )

        ::

            >>> timespans = consort.SegmentMaker.consolidate_timespans(
            ...     timespans)
            >>> print(format(timespans))
            timespantools.TimespanInventory(
                [
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(20, 1),
                        divisions=(
                            durationtools.Duration(10, 1),
                            durationtools.Duration(10, 1),
                            ),
                        music_specifier='foo',
                        ),
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(20, 1),
                        stop_offset=durationtools.Offset(25, 1),
                        divisions=(
                            durationtools.Duration(5, 1),
                            ),
                        music_specifier='bar',
                        ),
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(40, 1),
                        stop_offset=durationtools.Offset(58, 1),
                        divisions=(
                            durationtools.Duration(10, 1),
                            durationtools.Duration(8, 1),
                            ),
                        music_specifier='bar',
                        ),
                    ]
                )

        Returns new timespan inventory.
        '''
        consolidated_timespans = timespantools.TimespanInventory()
        for music_specifier, grouped_timespans in \
            SegmentMaker.group_timespans(timespans):
            if music_specifier is None and not allow_silences:
                continue
            if hasattr(music_specifier, 'minimum_phrase_duration'):
                duration = music_specifier.minimum_phrase_duration
                if duration and grouped_timespans.duration < duration:
                    continue
            divisions = tuple(_.duration for _ in grouped_timespans)
            first_timespan = grouped_timespans[0]
            last_timespan = grouped_timespans[-1]
            consolidated_timespan = new(
                first_timespan,
                divisions=divisions,
                stop_offset=last_timespan.stop_offset,
                original_stop_offset=last_timespan.original_stop_offset,
                )
            consolidated_timespans.append(consolidated_timespan)
        consolidated_timespans.sort()
        return consolidated_timespans

    @staticmethod
    def debug_timespans(timespans):
        import consort
        if not timespans:
            consort.debug('No timespans found.')
        else:
            consort.debug('DEBUG: Dumping timespans:')
        if isinstance(timespans, dict):
            for voice_name in timespans:
                consort.debug('\t' + voice_name)
                for timespan in timespans[voice_name]:
                    consort.debug('\t\t{}: {} to {}'.format(
                        type(timespan).__name__,
                        timespan.start_offset,
                        timespan.stop_offset,
                        ))
        else:
            for timespan in timespans:
                consort.debug('\t({}) {}: {} to {}'.format(
                    timespan.voice_name,
                    type(timespan).__name__,
                    timespan.start_offset,
                    timespan.stop_offset,
                    ))

    @staticmethod
    def resolve_maquette(multiplexed_timespans):
        import consort
        demultiplexed_maquette = consort.TimespanInventoryMapping()
        for timespan in multiplexed_timespans:
            voice_name, layer = timespan.voice_name, timespan.layer
            if voice_name not in demultiplexed_maquette:
                demultiplexed_maquette[voice_name] = {}
            if layer not in demultiplexed_maquette[voice_name]:
                demultiplexed_maquette[voice_name][layer] = \
                    timespantools.TimespanInventory()
            demultiplexed_maquette[voice_name][layer].append(
                timespan)
            demultiplexed_maquette[voice_name][layer]
        for voice_name in demultiplexed_maquette:
            timespan_inventories = demultiplexed_maquette[voice_name]
            timespan_inventory = \
                SegmentMaker.resolve_timespan_inventories(
                    timespan_inventories)
            demultiplexed_maquette[voice_name] = timespan_inventory
        return demultiplexed_maquette

    @staticmethod
    def division_is_silent(division):
        r'''Is true when division only contains rests, at any depth.

        ::

            >>> import consort

        ::

            >>> division = scoretools.Container("c'4 d'4 e'4 f'4")
            >>> consort.SegmentMaker.division_is_silent(division)
            False

        ::

            >>> division = scoretools.Container('r4 r8 r16 r32')
            >>> consort.SegmentMaker.division_is_silent(division)
            True

        ::

            >>> division = scoretools.Container(
            ...     r"c'4 \times 2/3 { d'8 r8 e'8 } f'4")
            >>> consort.SegmentMaker.division_is_silent(division)
            False

        ::

            >>> division = scoretools.Container(
            ...     r'\times 2/3 { r4 \times 2/3 { r8. } }')
            >>> consort.SegmentMaker.division_is_silent(division)
            True

        Returns boolean.
        '''
        rest_prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            )
        leaves = division.select_leaves()
        return all(isinstance(leaf, rest_prototype) for leaf in leaves)

    def interpret_rhythms(
        self,
        verbose=True,
        ):
        multiplexed_timespans = timespantools.TimespanInventory()

        with systemtools.Timer(
            enter_message='    populating independent timespans:',
            exit_message='        total:',
            verbose=verbose,
            ):
            meters, measure_offsets, multiplexed_timespans = \
                self.populate_independent_timespans(
                    self.discard_final_silence,
                    multiplexed_timespans,
                    self.permitted_time_signatures,
                    self.score,
                    self.score_template,
                    self.settings or (),
                    self.desired_duration,
                    self.timespan_quantization,
                    verbose=verbose,
                    )
            self._meters = meters

        with systemtools.Timer(
            enter_message='    populating dependent timespans:',
            exit_message='        total:',
            verbose=verbose,
            ):
            demultiplexed_maquette = \
                self.populate_dependent_timespans(
                    self.measure_offsets,
                    multiplexed_timespans,
                    self.score,
                    self.score_template,
                    self.settings or (),
                    self.desired_duration,
                    verbose=verbose,
                    )

        with systemtools.Timer(
            '    populated silent timespans:',
            verbose=verbose,
            ):
            demultiplexed_maquette = self.populate_silent_timespans(
                demultiplexed_maquette,
                self.measure_offsets,
                self.voice_names,
                )

        with systemtools.Timer(
            '    validated timespans:',
            verbose=verbose,
            ):
            self.validate_timespans(demultiplexed_maquette)

        with systemtools.Timer(
            enter_message='    rewriting meters:',
            exit_message='        total:',
            verbose=verbose,
            ):
            #expr = 'self.rewrite_meters(demultiplexed_maquette, self.meters)'
            #systemtools.IOManager.profile_expr(
            #    expr,
            #    global_context=globals(),
            #    local_context=locals(),
            #    )
            self.rewrite_meters(
                demultiplexed_maquette,
                self.meters,
                self.score,
                verbose=verbose,
                )

        with systemtools.Timer(
            '    populated score:',
            verbose=verbose,
            ):
            self.populate_score(
                demultiplexed_maquette,
                self.score,
                )

        self._voicewise_timespans = demultiplexed_maquette

    def find_meters(
        self,
        permitted_time_signatures=None,
        desired_duration=None,
        timespan_inventory=None,
        ):
        import consort
        offset_counter = metertools.OffsetCounter()
        for timespan in timespan_inventory:
            if isinstance(timespan, consort.SilentTimespan):
                continue
            offset_counter[timespan.start_offset] += 2
            offset_counter[timespan.stop_offset] += 1
        maximum = 1
        if offset_counter:
            maximum = int(max(offset_counter.values()))
        offset_counter[desired_duration] = maximum * 2
        maximum_meter_run_length = self.maximum_meter_run_length
        meters = metertools.Meter.fit_meters_to_expr(
            expr=offset_counter,
            meters=permitted_time_signatures,
            maximum_run_length=maximum_meter_run_length,
            )
        return tuple(meters)

    @staticmethod
    def get_rhythm_maker(music_specifier):
        import consort
        beam_specifier = rhythmmakertools.BeamSpecifier(
            beam_each_division=False,
            beam_divisions_together=False,
            )
        if music_specifier is None:
            rhythm_maker = rhythmmakertools.NoteRhythmMaker(
                beam_specifier=beam_specifier,
                output_masks=[rhythmmakertools.silence_all()],
                )
        elif music_specifier.rhythm_maker is None:
            rhythm_maker = rhythmmakertools.NoteRhythmMaker(
                beam_specifier=beam_specifier,
                tie_specifier=rhythmmakertools.TieSpecifier(
                    tie_across_divisions=True,
                    ),
                )
        elif isinstance(music_specifier.rhythm_maker,
            consort.CompositeRhythmMaker):
            rhythm_maker = music_specifier.rhythm_maker.new(
                beam_specifier=beam_specifier,
                )
        else:
            rhythm_maker = music_specifier.rhythm_maker
            rhythm_maker = new(
                rhythm_maker,
                beam_specifier=beam_specifier,
                )
        assert rhythm_maker is not None
        return rhythm_maker

    @staticmethod
    def group_nonsilent_divisions(music):
        r'''Groups non-silent divisions together.

        Yields groups in reverse order.

        ::

            >>> import consort

        ::

            >>> divisions = []
            >>> divisions.append(scoretools.Container('r4'))
            >>> divisions.append(scoretools.Container("c'4"))
            >>> divisions.append(scoretools.Container('r4 r4'))
            >>> divisions.append(scoretools.Container("d'4 d'4"))
            >>> divisions.append(scoretools.Container("e'4 e'4 e'4"))
            >>> divisions.append(scoretools.Container('r4 r4 r4'))
            >>> divisions.append(scoretools.Container("f'4 f'4 f'4 f'4"))

        ::

            >>> for group in consort.SegmentMaker.group_nonsilent_divisions(
            ...     divisions):
            ...     print(group)
            (Container("f'4 f'4 f'4 f'4"),)
            (Container("d'4 d'4"), Container("e'4 e'4 e'4"))
            (Container("c'4"),)

        Returns generator.
        '''
        group = []
        for division in tuple(reversed(music)):
            if SegmentMaker.division_is_silent(division):
                if group:
                    yield tuple(reversed(group))
                    group = []
            else:
                group.append(division)
        if group:
            yield tuple(reversed(group))

    @staticmethod
    def group_timespans(timespans):
        def grouper(timespan):
            music_specifier = None
            if isinstance(timespan, consort.PerformedTimespan):
                music_specifier = timespan.music_specifier
                if music_specifier is None:
                    music_specifier = consort.MusicSpecifier()
            forbid_fusing = timespan.forbid_fusing
            return music_specifier, forbid_fusing
        import consort
        for partitioned_timespans in timespans.partition(
            include_tangent_timespans=True):
            for key, grouped_timespans in itertools.groupby(
                partitioned_timespans, grouper):
                music_specifier, forbid_fusing = key
                if forbid_fusing:
                    for timespan in grouped_timespans:
                        group = timespantools.TimespanInventory([timespan])
                        yield music_specifier, group
                else:
                    group = timespantools.TimespanInventory(
                        grouped_timespans)
                    yield music_specifier, group

    @staticmethod
    def inscribe_demultiplexed_timespans(
        demultiplexed_maquette,
        score,
        ):
        counter = collections.Counter()
        voice_names = demultiplexed_maquette.keys()
        voice_names = SegmentMaker.sort_voice_names(score, voice_names)
        for voice_name in voice_names:
            inscribed_timespans = timespantools.TimespanInventory()
            uninscribed_timespans = demultiplexed_maquette[voice_name]
            for timespan in uninscribed_timespans:
                if timespan.music is None:
                    music_specifier = timespan.music_specifier
                    if music_specifier not in counter:
                        if music_specifier is None:
                            seed = 0
                        else:
                            seed = music_specifier.seed or 0
                        counter[music_specifier] = seed
                    seed = counter[music_specifier]
                    result = SegmentMaker.inscribe_timespan(
                        timespan,
                        seed=seed,
                        )
                    inscribed_timespans.extend(result)
                    # Negative rotation mimics advancing through a series.
                    counter[music_specifier] -= 1
                else:
                    inscribed_timespans.append(timespan)
            demultiplexed_maquette[voice_name] = inscribed_timespans

    @staticmethod
    def inscribe_timespan(timespan, seed=None):
        r'''Inscribes `timespan`.

        ::

            >>> import consort
            >>> music_specifier = consort.MusicSpecifier(
            ...     rhythm_maker=rhythmmakertools.NoteRhythmMaker(
            ...         output_masks=[
            ...             rhythmmakertools.SilenceMask(
            ...                 indices=[0],
            ...                 period=3,
            ...                 ),
            ...             ],
            ...         ),
            ...     )

        ::

            >>> timespan = consort.PerformedTimespan(
            ...     divisions=[durationtools.Duration(1, 4)] * 7,
            ...     start_offset=0,
            ...     stop_offset=(7, 4),
            ...     music_specifier=music_specifier,
            ...     )
            >>> print(format(timespan))
            consort.tools.PerformedTimespan(
                start_offset=durationtools.Offset(0, 1),
                stop_offset=durationtools.Offset(7, 4),
                divisions=(
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 4),
                    ),
                music_specifier=consort.tools.MusicSpecifier(
                    rhythm_maker=rhythmmakertools.NoteRhythmMaker(
                        output_masks=rhythmmakertools.BooleanPatternInventory(
                            (
                                rhythmmakertools.SilenceMask(
                                    indices=(0,),
                                    period=3,
                                    ),
                                )
                            ),
                        ),
                    ),
                )

        ::

            >>> result = consort.SegmentMaker.inscribe_timespan(timespan)
            >>> print(format(result))
            timespantools.TimespanInventory(
                [
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(1, 4),
                        stop_offset=durationtools.Offset(3, 4),
                        music=scoretools.Container(
                            "{   c'4 } {   c'4 }"
                            ),
                        music_specifier=consort.tools.MusicSpecifier(
                            rhythm_maker=rhythmmakertools.NoteRhythmMaker(
                                output_masks=rhythmmakertools.BooleanPatternInventory(
                                    (
                                        rhythmmakertools.SilenceMask(
                                            indices=(0,),
                                            period=3,
                                            ),
                                        )
                                    ),
                                ),
                            ),
                        original_start_offset=durationtools.Offset(0, 1),
                        original_stop_offset=durationtools.Offset(7, 4),
                        ),
                    consort.tools.PerformedTimespan(
                        start_offset=durationtools.Offset(1, 1),
                        stop_offset=durationtools.Offset(3, 2),
                        music=scoretools.Container(
                            "{   c'4 } {   c'4 }"
                            ),
                        music_specifier=consort.tools.MusicSpecifier(
                            rhythm_maker=rhythmmakertools.NoteRhythmMaker(
                                output_masks=rhythmmakertools.BooleanPatternInventory(
                                    (
                                        rhythmmakertools.SilenceMask(
                                            indices=(0,),
                                            period=3,
                                            ),
                                        )
                                    ),
                                ),
                            ),
                        original_start_offset=durationtools.Offset(0, 1),
                        original_stop_offset=durationtools.Offset(7, 4),
                        ),
                    ]
                )

        Returns timespan inventory.
        '''
        inscribed_timespans = timespantools.TimespanInventory()
        rhythm_maker = SegmentMaker.get_rhythm_maker(timespan.music_specifier)
        durations = timespan.divisions[:]
        music = SegmentMaker.make_music(
            rhythm_maker,
            durations,
            seed,
            )
        assert inspect_(music).get_duration() == timespan.duration
        for container, duration in zip(music, durations):
            assert inspect_(container).get_duration() == duration
        music = SegmentMaker.consolidate_rests(music)
        assert inspect_(music).get_duration() == timespan.duration
        for group in SegmentMaker.group_nonsilent_divisions(music):
            start_offset = inspect_(group[0]).get_timespan().start_offset
            stop_offset = inspect_(group[-1]).get_timespan().stop_offset
            start_offset += timespan.start_offset
            stop_offset += timespan.start_offset
            container = scoretools.Container()
            container.extend(group)
#            beam = spannertools.GeneralizedBeam(
#                durations=[division._get_duration() for division in music],
#                include_long_duration_notes=False,
#                include_long_duration_rests=False,
#                isolated_nib_direction=None,
#                use_stemlets=False,
#                )
#            attach(beam, container, name='beam')
            for division in container:
                durations = [division._get_duration()]
                beam = spannertools.GeneralizedBeam(
                    durations=durations,
                    include_long_duration_notes=False,
                    include_long_duration_rests=False,
                    isolated_nib_direction=None,
                    use_stemlets=True,
                    )
                attach(beam, division)
            attach(timespan.music_specifier, container, scope=scoretools.Voice)
            inscribed_timespan = new(
                timespan,
                divisions=None,
                music=container,
                start_offset=start_offset,
                stop_offset=stop_offset,
                )
            assert inspect_(container).get_duration() == \
                inscribed_timespan.duration
            assert inspect_(container).get_timespan().start_offset == 0
            assert inspect_(container[0]).get_timespan().start_offset == 0
            inscribed_timespans.append(inscribed_timespan)
        inscribed_timespans.sort()
        return inscribed_timespans

    @staticmethod
    def leaf_is_tied(leaf):
        prototype = spannertools.Tie
        leaf_tie = None
        if inspect_(leaf).get_spanners(prototype):
            leaf_tie = inspect_(leaf).get_spanner(prototype)
        else:
            return False
        next_leaf = inspect_(leaf).get_leaf(1)
        if next_leaf is not None:
            if inspect_(next_leaf).get_spanners(prototype):
                next_leaf_tie = inspect_(next_leaf).get_spanner(prototype)
                if leaf_tie is next_leaf_tie:
                    return True
        return False

    @staticmethod
    def make_music(rhythm_maker, durations, seed=0):
        music = rhythm_maker(durations, rotation=seed)
        for i, division in enumerate(music):
            if (
                len(division) == 1 and
                isinstance(division[0], scoretools.Tuplet)
                ):
                music[i] = division[0]
            else:
                music[i] = scoretools.Container(division)
        music = scoretools.Container(music)
        for division in music[:]:
            if (
                isinstance(division, scoretools.Tuplet) and
                division.multiplier == 1
                ):
                mutate(division).swap(scoretools.Container())
        return music

    @staticmethod
    def meters_to_offsets(meters):
        r'''Converts `meters` to offsets.

        ::

            >>> import consort

        ::

            >>> meters = [
            ...     metertools.Meter((3, 4)),
            ...     metertools.Meter((2, 4)),
            ...     metertools.Meter((6, 8)),
            ...     metertools.Meter((5, 16)),
            ...     ]

        ::

            >>> offsets = consort.SegmentMaker.meters_to_offsets(meters)
            >>> for x in offsets:
            ...     x
            ...
            Offset(0, 1)
            Offset(3, 4)
            Offset(5, 4)
            Offset(2, 1)
            Offset(37, 16)

        Returns tuple of offsets.
        '''
        durations = [_.duration for _ in meters]
        offsets = mathtools.cumulative_sums(durations)
        offsets = [durationtools.Offset(_) for _ in offsets]
        return tuple(offsets)

    @staticmethod
    def meters_to_timespans(meters):
        r'''Convert `meters` into a collection of annotated timespans.

        ::

            >>> import consort

        ::

            >>> meters = [
            ...     metertools.Meter((3, 4)),
            ...     metertools.Meter((2, 4)),
            ...     metertools.Meter((6, 8)),
            ...     metertools.Meter((5, 16)),
            ...     ]

        ::

            >>> timespans = consort.SegmentMaker.meters_to_timespans(meters)
            >>> print(format(timespans))
            consort.tools.TimespanCollection(
                [
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(3, 4),
                        annotation=metertools.Meter(
                            '(3/4 (1/4 1/4 1/4))'
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(3, 4),
                        stop_offset=durationtools.Offset(5, 4),
                        annotation=metertools.Meter(
                            '(2/4 (1/4 1/4))'
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(5, 4),
                        stop_offset=durationtools.Offset(2, 1),
                        annotation=metertools.Meter(
                            '(6/8 ((3/8 (1/8 1/8 1/8)) (3/8 (1/8 1/8 1/8))))'
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(2, 1),
                        stop_offset=durationtools.Offset(37, 16),
                        annotation=metertools.Meter(
                            '(5/16 ((3/16 (1/16 1/16 1/16)) (2/16 (1/16 1/16))))'
                            ),
                        ),
                    ]
                )

        Returns timespan collections.
        '''
        import consort
        timespans = consort.TimespanCollection()
        offsets = SegmentMaker.meters_to_offsets(meters)
        for i, meter in enumerate(meters):
            start_offset = offsets[i]
            stop_offset = offsets[i + 1]
            timespan = timespantools.AnnotatedTimespan(
                annotation=meter,
                start_offset=start_offset,
                stop_offset=stop_offset,
                )
            timespans.insert(timespan)
        return timespans

    @staticmethod
    def multiplex_timespans(demultiplexed_maquette):
        r'''Multiplexes `demultiplexed_maquette` into a single timespan
        inventory.

        ::

            >>> import consort

        ::

            >>> demultiplexed = {}
            >>> demultiplexed['foo'] = timespantools.TimespanInventory([
            ...     timespantools.Timespan(0, 10),
            ...     timespantools.Timespan(15, 30),
            ...     ])
            >>> demultiplexed['bar'] = timespantools.TimespanInventory([
            ...     timespantools.Timespan(5, 15),
            ...     timespantools.Timespan(20, 35),
            ...     ])
            >>> demultiplexed['baz'] = timespantools.TimespanInventory([
            ...     timespantools.Timespan(5, 40),
            ...     ])

        ::

            >>> multiplexed = consort.SegmentMaker.multiplex_timespans(
            ...     demultiplexed)
            >>> print(format(multiplexed))
            timespantools.TimespanInventory(
                [
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(10, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(5, 1),
                        stop_offset=durationtools.Offset(15, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(5, 1),
                        stop_offset=durationtools.Offset(40, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(15, 1),
                        stop_offset=durationtools.Offset(30, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(20, 1),
                        stop_offset=durationtools.Offset(35, 1),
                        ),
                    ]
                )

        Returns timespan inventory.
        '''
        multiplexed_timespans = timespantools.TimespanInventory()
        for timespans in demultiplexed_maquette.values():
            multiplexed_timespans.extend(timespans)
        multiplexed_timespans.sort()
        return multiplexed_timespans

    def populate_dependent_timespans(
        self,
        meter_offsets,
        multiplexed_timespans,
        score,
        score_template,
        settings,
        desired_duration,
        verbose=True,
        ):
        with systemtools.Timer(
            '        populated timespans:',
            verbose=verbose,
            ):
            self.populate_multiplexed_maquette(
                dependent=True,
                score=score,
                score_template=score_template,
                settings=settings,
                desired_duration=desired_duration,
                timespan_inventory=multiplexed_timespans,
                )
        with systemtools.Timer(
            '        demultiplexed timespans:',
            verbose=verbose,
            ):
            demultiplexed_maquette = self.resolve_maquette(
                multiplexed_timespans)
        with systemtools.Timer(
            '        split timespans:',
            verbose=verbose,
            ):
            self.split_demultiplexed_timespans(
                meter_offsets,
                demultiplexed_maquette,
                )
        with systemtools.Timer(
            '        pruned short timespans:',
            verbose=verbose,
            ):
            for voice_name, timespans in demultiplexed_maquette.items():
                self.prune_short_timespans(timespans)
        with systemtools.Timer(
            '        pruned malformed timespans:',
            verbose=verbose,
            ):
            for voice_name, timespans in demultiplexed_maquette.items():
                self.prune_malformed_timespans(timespans)
        with systemtools.Timer(
            '        consolidated timespans:',
            verbose=verbose,
            ):
            self.consolidate_demultiplexed_timespans(
                demultiplexed_maquette,
                )
        with systemtools.Timer(
            '        inscribed timespans:',
            verbose=verbose,
            ):
            self.inscribe_demultiplexed_timespans(
                demultiplexed_maquette,
                score,
                )
        return demultiplexed_maquette

    def populate_independent_timespans(
        self,
        discard_final_silence,
        multiplexed_timespans,
        permitted_time_signatures,
        score,
        score_template,
        settings,
        desired_duration,
        timespan_quantization,
        verbose=True,
        ):
        with systemtools.Timer(
            '        populated timespans:',
            verbose=verbose,
            ):
            SegmentMaker.populate_multiplexed_maquette(
                dependent=False,
                score=score,
                score_template=score_template,
                settings=settings,
                desired_duration=desired_duration,
                timespan_inventory=multiplexed_timespans,
                timespan_quantization=timespan_quantization,
                )
        with systemtools.Timer(
            '        found meters:',
            verbose=verbose,
            ):
            meters = self.find_meters(
                permitted_time_signatures=permitted_time_signatures,
                desired_duration=desired_duration,
                timespan_inventory=multiplexed_timespans,
                )
        meter_offsets = SegmentMaker.meters_to_offsets(meters)
        with systemtools.Timer(
            '        demultiplexed timespans:',
            verbose=verbose,
            ):
            demultiplexed_maquette = SegmentMaker.resolve_maquette(
                multiplexed_timespans)
        with systemtools.Timer(
            '        split timespans:',
            verbose=verbose,
            ):
            SegmentMaker.split_demultiplexed_timespans(
                meter_offsets,
                demultiplexed_maquette,
                )
        # TODO: Determine best place for malformed timespan pruning.
        with systemtools.Timer(
            '        pruned malformed timespans:',
            verbose=verbose,
            ):
            for voice_name, timespans in demultiplexed_maquette.items():
                SegmentMaker.prune_malformed_timespans(timespans)
        with systemtools.Timer(
            '        consolidated timespans:',
            verbose=verbose,
            ):
            SegmentMaker.consolidate_demultiplexed_timespans(
                demultiplexed_maquette,
                )
        with systemtools.Timer(
            '        inscribed timespans:',
            verbose=verbose,
            ):
            SegmentMaker.inscribe_demultiplexed_timespans(
                demultiplexed_maquette,
                score,
                )
        with systemtools.Timer(
            '        multiplexed timespans:',
            verbose=verbose,
            ):
            multiplexed_timespans = SegmentMaker.multiplex_timespans(
                demultiplexed_maquette)
        # TODO: Why prune after consolidation?
        with systemtools.Timer(
            '        pruned short timespans:',
            verbose=verbose,
            ):
            SegmentMaker.prune_short_timespans(multiplexed_timespans)
        with systemtools.Timer(
            '        pruned meters:',
            verbose=verbose,
            ):
            meters = SegmentMaker.prune_meters(
                discard_final_silence,
                meters,
                multiplexed_timespans.stop_offset,
                )
            meter_offsets = SegmentMaker.meters_to_offsets(meters)
        return meters, meter_offsets, multiplexed_timespans

    @staticmethod
    def populate_multiplexed_maquette(
        dependent=False,
        score=None,
        score_template=None,
        settings=None,
        desired_duration=None,
        timespan_inventory=None,
        timespan_quantization=None,
        ):
        segment_timespan = timespantools.Timespan(0, desired_duration)
        if timespan_quantization is None:
            timespan_quantization = durationtools.Duration(1, 16)
        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
        independent_settings = [setting for setting in settings
            if not setting.timespan_maker.is_dependent
            ]
        dependent_settings = [setting for setting in settings
            if setting.timespan_maker.is_dependent
            ]
        if dependent:
            settings = dependent_settings
            start_index = len(independent_settings)
        else:
            settings = independent_settings
            start_index = 0
        for layer, music_setting in enumerate(settings, start_index):
            music_setting(
                layer=layer,
                score=score,
                score_template=score_template,
                segment_timespan=segment_timespan,
                timespan_inventory=timespan_inventory,
                timespan_quantization=timespan_quantization,
                )

    @staticmethod
    def populate_score(
        demultiplexed_maquette,
        score,
        ):
        for voice_name, timespans in demultiplexed_maquette.items():
            voice = score[voice_name]
            for timespan in timespans:
                assert timespan.duration == \
                    inspect_(timespan.music).get_duration()
                voice.append(timespan.music)
        return score

    @staticmethod
    def populate_silent_timespans(
        demultiplexed_maquette,
        meter_offsets,
        voice_names=None,
        ):
        import consort
        silent_music_specifier = consort.MusicSpecifier()
        rhythm_maker = SegmentMaker.get_rhythm_maker(None)
        if voice_names is None:
            voice_names = demultiplexed_maquette.keys()
        else:
            voice_names = set(voice_names)
            voice_names.update(demultiplexed_maquette.keys())
        for voice_name in voice_names:
            if voice_name not in demultiplexed_maquette:
                demultiplexed_maquette[voice_name] = \
                    timespantools.TimespanInventory()
            timespans = demultiplexed_maquette[voice_name]
            silences = timespantools.TimespanInventory([
                consort.SilentTimespan(
                    start_offset=0,
                    stop_offset=meter_offsets[-1],
                    voice_name=voice_name,
                    )
                ])
            silences = SegmentMaker.subtract_timespan_inventories(
                silences, timespans)
            silences = SegmentMaker.split_timespans(meter_offsets, silences)
            for group in silences.partition(include_tangent_timespans=True):
                start_offset = group.start_offset,
                stop_offset = group.stop_offset,
                durations = [_.duration for _ in group]
                silence = SegmentMaker.make_music(
                    rhythm_maker,
                    durations,
                    )
                attach(silent_music_specifier, silence, scope=scoretools.Voice)
                silent_timespan = consort.PerformedTimespan(
                    music=silence,
                    start_offset=start_offset,
                    stop_offset=stop_offset,
                    voice_name=voice_name,
                    )
                timespans.append(silent_timespan)
            timespans.sort()
        return demultiplexed_maquette

    @staticmethod
    def prune_meters(
        discard_final_silence,
        meters,
        stop_offset,
        ):
        discard_final_silence = bool(discard_final_silence)
        if discard_final_silence and stop_offset:
            meters = list(meters)
            total_meter_durations = sum(_.duration for _ in meters[:-1])
            while stop_offset <= total_meter_durations:
                meters.pop()
                total_meter_durations = sum(_.duration for _ in meters[:-1])
        return tuple(meters)

    @staticmethod
    def prune_short_timespans(timespans):
        for timespan in timespans[:]:
            if timespan.minimum_duration and \
                timespan.duration < timespan.minimum_duration:
                timespans.remove(timespan)

    @staticmethod
    def prune_malformed_timespans(timespans):
        for timespan in timespans[:]:
            if not timespan.is_well_formed:
                timespans.remove(timespan)

    @staticmethod
    def report(timespan_inventory):
        print('REPORTING')
        for timespan in timespan_inventory:
            print(
                '\t',
                '{}:'.format(timespan.voice_name),
                '[{}]'.format(timespan.layer),
                type(timespan).__name__,
                float(timespan.start_offset),
                float(timespan.stop_offset),
                )
        print()

    @staticmethod
    def resolve_timespan_inventories(
        timespan_inventories=None,
        ):
        import consort
        timespan_inventories = [x[1] for x in
            sorted(timespan_inventories.items(),
                key=lambda item: item[0],
                )
            ]
        for timespan_inventory in timespan_inventories:
            assert timespan_inventory.all_are_nonoverlapping
        resolved_inventory = consort.TimespanCollection()
        for timespan in timespan_inventories[0]:
            if isinstance(timespan, consort.SilentTimespan):
                continue
            resolved_inventory.insert(timespan)
        for timespan_inventory in timespan_inventories[1:]:
            resolved_inventory = SegmentMaker.subtract_timespan_inventories(
                resolved_inventory,
                timespan_inventory,
                )
            for timespan in resolved_inventory[:]:
                if timespan.minimum_duration and \
                    timespan.duration < timespan.minimum_duration:
                    resolved_inventory.remove(timespan)
            for timespan in timespan_inventory:
                if isinstance(timespan, consort.SilentTimespan):
                    continue
                resolved_inventory.append(timespan)
            resolved_inventory.sort()
        resolved_inventory = timespantools.TimespanInventory(
            resolved_inventory[:],
            )
        return resolved_inventory

    @staticmethod
    def rewrite_container_meter(
        container,
        meter_timespans,
        forbid_staff_lines_spanner=None,
        ):
        assert meter_timespans
        assert meter_timespans[0].start_offset <= \
            inspect_(container).get_timespan().start_offset
        last_leaf = container.select_leaves()[-1]
        is_tied = SegmentMaker.leaf_is_tied(last_leaf)
        container_timespan = inspect_(container).get_timespan()
        if isinstance(container, scoretools.Tuplet):
            contents_duration = container._contents_duration
            meter = metertools.Meter(contents_duration)
            boundary_depth = 1
            if meter.numerator in (3, 4):
                boundary_depth = None
            mutate(container[:]).rewrite_meter(
                meter,
                boundary_depth=boundary_depth,
                maximum_dot_count=2,
                )
        elif len(meter_timespans) == 1:
            container_timespan = inspect_(container).get_timespan()
            container_start_offset = container_timespan.start_offset
            container_stop_offset = container_timespan.stop_offset
            meter_timespan = meter_timespans[0]
            relative_meter_start_offset = meter_timespan.start_offset
            assert relative_meter_start_offset <= container_start_offset
            absolute_meter_stop_offset = (
                relative_meter_start_offset +
                container_start_offset +
                meter_timespan.duration
                )
            assert container_stop_offset <= absolute_meter_stop_offset
            if meter_timespan.is_congruent_to_timespan(container_timespan) \
                and SegmentMaker.division_is_silent(container):
                multi_measure_rest = scoretools.MultimeasureRest(1)
                duration = inspect_(container).get_duration()
                multiplier = durationtools.Multiplier(duration)
                attach(multiplier, multi_measure_rest)
                container[:] = [multi_measure_rest]
                if not forbid_staff_lines_spanner:
                    staff_lines_spanner = spannertools.StaffLinesSpanner([0])
                    attach(
                        staff_lines_spanner,
                        container,
                        name='staff_lines_spanner',
                        )
            else:
                meter = meter_timespan.annotation
                meter_offset = meter_timespan.start_offset
                initial_offset = container_start_offset - meter_offset
                boundary_depth = 1
                if meter.numerator in (3, 4):
                    boundary_depth = None
                mutate(container[:]).rewrite_meter(
                    meter,
                    boundary_depth=boundary_depth,
                    initial_offset=initial_offset,
                    maximum_dot_count=2,
                    )
        else:
            # TODO: handle bar-line-crossing containers
            raise AssertionError('Bar-line-crossing containers not permitted.')
        if is_tied:
            last_leaf = container.select_leaves()[-1]
            next_leaf = inspect_(last_leaf).get_leaf(1)
            selection = selectiontools.ContiguousSelection((
                last_leaf, next_leaf))
            selection._attach_tie_spanner_to_leaf_pair()

    @staticmethod
    def rewrite_meters(
        demultiplexed_maquette,
        meters,
        score,
        verbose=True,
        ):
        import consort
        meter_timespans = SegmentMaker.meters_to_timespans(meters)
        cache = {}
        for context_name in sorted(demultiplexed_maquette):
            inscribed_timespans = demultiplexed_maquette[context_name]
            consort.debug('CONTEXT: {}'.format(context_name))
            context = score[context_name]
            forbid_staff_lines_spanner = context.context_name == 'Dynamics'
            progress_indicator = systemtools.ProgressIndicator(
                message='        rewriting {}'.format(context_name),
                verbose=verbose,
                )
            with progress_indicator:
                for inscribed_timespan in inscribed_timespans:
                    consort.debug('\t{!s} {!s} {!r}'.format(
                        inscribed_timespan.start_offset,
                        inscribed_timespan.stop_offset,
                        inscribed_timespan.music,
                        ))
                    if not SegmentMaker.can_rewrite_meter(inscribed_timespan):
                        continue
                    with systemtools.ForbidUpdate(
                        inscribed_timespan.music,
                        update_on_exit=True,
                        ):
                        for i, container in enumerate(inscribed_timespan.music):
                            container_timespan = inspect_(container).get_timespan()
                            container_timespan = container_timespan.translate(
                                inscribed_timespan.start_offset)
                            if i == 0:
                                assert container_timespan.start_offset == \
                                    inscribed_timespan.start_offset
                            if i == (len(inscribed_timespan.music) - 1):
                                assert container_timespan.stop_offset == \
                                    inscribed_timespan.stop_offset
                            if container_timespan in cache:
                                intersecting_meters = cache[container_timespan]
                            else:
                                intersecting_meters = \
                                    meter_timespans.find_timespans_intersecting_timespan(
                                        container_timespan)
                                cache[container_timespan] = intersecting_meters
                            shifted_intersecting_meters = [
                                _.translate(-1 * inscribed_timespan.start_offset)
                                for _ in intersecting_meters
                                ]
                            consort.debug('\t\t{!r} {!r}'.format(
                                container,
                                container_timespan,
                                ))
                            for intersecting_meter in intersecting_meters:
                                consort.debug('\t\t\t' + repr(intersecting_meter))
                            SegmentMaker.rewrite_container_meter(
                                container,
                                shifted_intersecting_meters,
                                forbid_staff_lines_spanner,
                                )
                            SegmentMaker.cleanup_logical_ties(container)
                            progress_indicator.advance()

    @staticmethod
    def sort_voice_names(score, voice_names):
        result = []
        for voice in iterate(score).by_class(scoretools.Voice):
            if voice.name in voice_names:
                result.append(voice.name)
        return tuple(result)

    @staticmethod
    def split_demultiplexed_timespans(
        meter_offsets=None,
        demultiplexed_maquette=None,
        ):
        for voice_name in demultiplexed_maquette:
            timespan_inventory = demultiplexed_maquette[voice_name]
            split_inventory = SegmentMaker.split_timespans(
                meter_offsets,
                timespan_inventory,
                )
            demultiplexed_maquette[voice_name] = split_inventory

    @staticmethod
    def split_timespans(offsets, timespan_inventory):
        offsets = list(offsets)
        timespan_inventory.sort()
        split_inventory = timespantools.TimespanInventory()
        for timespan in timespan_inventory:
            current_offsets = []
            while offsets and offsets[0] <= timespan.start_offset:
                offsets.pop(0)
            while offsets and offsets[0] < timespan.stop_offset:
                current_offsets.append(offsets.pop(0))
            if hasattr(timespan, 'music') and timespan.music:
                # We don't need to split already-inscribed timespans
                split_inventory.append(timespan)
                continue
            elif timespan.forbid_splitting:
                continue
            if current_offsets:
                shards = timespan.split_at_offsets(current_offsets)
                for shard in shards:
                    if shard.minimum_duration:
                        if shard.minimum_duration <= shard.duration:
                            split_inventory.append(shard)
                    else:
                        split_inventory.append(shard)
            else:
                if timespan.minimum_duration:
                    if timespan.minimum_duration <= timespan.duration:
                        split_inventory.append(timespan)
                else:
                    split_inventory.append(timespan)
        split_inventory.sort()
        return split_inventory

    @staticmethod
    def subtract_timespan_inventories(inventory_one, inventory_two):
        r'''Subtracts `inventory_two` from `inventory_one`.

        ::

            >>> inventory_one = timespantools.TimespanInventory([
            ...     timespantools.Timespan(0, 10),
            ...     timespantools.Timespan(10, 20),
            ...     timespantools.Timespan(40, 80),
            ...     ])

        ::

            >>> inventory_two = timespantools.TimespanInventory([
            ...     timespantools.Timespan(5, 15),
            ...     timespantools.Timespan(25, 35),
            ...     timespantools.Timespan(35, 45),
            ...     timespantools.Timespan(55, 65),
            ...     timespantools.Timespan(85, 95),
            ...     ])

        ::

            >>> import consort
            >>> manager = consort.SegmentMaker
            >>> result = manager.subtract_timespan_inventories(
            ...      inventory_one,
            ...      inventory_two,
            ...      )
            >>> print(format(result))
            timespantools.TimespanInventory(
                [
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(5, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(15, 1),
                        stop_offset=durationtools.Offset(20, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(45, 1),
                        stop_offset=durationtools.Offset(55, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(65, 1),
                        stop_offset=durationtools.Offset(80, 1),
                        ),
                    ]
                )

        ::

            >>> result = manager.subtract_timespan_inventories(
            ...      inventory_two,
            ...      inventory_one,
            ...      )
            >>> print(format(result))
            timespantools.TimespanInventory(
                [
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(25, 1),
                        stop_offset=durationtools.Offset(35, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(35, 1),
                        stop_offset=durationtools.Offset(40, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(85, 1),
                        stop_offset=durationtools.Offset(95, 1),
                        ),
                    ]
                )

        '''
        import consort
        resulting_timespans = consort.TimespanCollection()
        if not inventory_two:
            return timespantools.TimespanInventory(inventory_one)
        elif not inventory_one:
            return timespantools.TimespanInventory()
        subtractee_index = 0
        subtractor_index = 0
        subtractee = None
        subtractor = None
        subtractee_is_modified = False
        while subtractee_index < len(inventory_one) and \
            subtractor_index < len(inventory_two):
            if subtractee is None:
                subtractee = inventory_one[subtractee_index]
                subtractee_is_modified = False
            if subtractor is None:
                subtractor = inventory_two[subtractor_index]
            if subtractee.intersects_timespan(subtractor):
                subtraction = subtractee - subtractor
                if len(subtraction) == 1:
                    subtractee = subtraction[0]
                    subtractee_is_modified = True
                elif len(subtraction) == 2:
                    resulting_timespans.insert(subtraction[0])
                    subtractee = subtraction[1]
                    subtractee_is_modified = True
                else:
                    subtractee = None
                    subtractee_index += 1
            else:
                if subtractee.stops_before_or_at_offset(
                    subtractor.start_offset):
                    resulting_timespans.insert(subtractee)
                    subtractee = None
                    subtractee_index += 1
                else:
                    subtractor = None
                    subtractor_index += 1
        if subtractee_is_modified:
            if subtractee:
                resulting_timespans.insert(subtractee)
            resulting_timespans.insert(inventory_one[subtractee_index + 1:])
        else:
            resulting_timespans.insert(inventory_one[subtractee_index:])
        resulting_timespans = timespantools.TimespanInventory(
            resulting_timespans[:])
        return resulting_timespans

    @staticmethod
    def validate_timespans(demultiplexed_maquette):
        durations = set()
        for voice_name, timespans in demultiplexed_maquette.items():
            timespans.sort()
            assert timespans.start_offset == 0
            assert timespans.all_are_contiguous
            assert timespans.all_are_well_formed
            assert timespans.all_are_nonoverlapping
            durations.add(timespans.stop_offset)
        assert len(tuple(durations)) == 1

    def update_segment_metadata(self):
        self._segment_metadata.update(
            measure_count=len(self.meters),
            end_tempo=self.get_end_tempo_indication(),
            end_time_signature=self.get_end_time_signature(),
            is_repeated=self.repeat,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attack_point_map(self):
        return self._attack_point_map

    @property
    def meters(self):
        return self._meters

    @property
    def score(self):
        return self._score

    @property
    def voicewise_timespans(self):
        return self._voicewise_timespans

    @property
    def desired_duration(self):
        tempo = self.tempo
        tempo_desired_duration_in_seconds = durationtools.Duration(
            tempo.duration_to_milliseconds(tempo.duration),
            1000,
            )
        desired_duration = durationtools.Duration((
            self.desired_duration_in_seconds /
            tempo_desired_duration_in_seconds
            ).limit_denominator(8))
        desired_duration *= tempo.duration
        count = desired_duration // durationtools.Duration(1, 8)
        desired_duration = durationtools.Duration(count, 8)
        assert 0 < desired_duration
        return desired_duration

    @property
    def desired_duration_in_seconds(self):
        return self._desired_duration_in_seconds

    @desired_duration_in_seconds.setter
    def desired_duration_in_seconds(self, desired_duration_in_seconds):
        if desired_duration_in_seconds is not None:
            desired_duration_in_seconds = durationtools.Duration(
                desired_duration_in_seconds,
                )
        self._desired_duration_in_seconds = desired_duration_in_seconds

    @property
    def discard_final_silence(self):
        return self._discard_final_silence

    @discard_final_silence.setter
    def discard_final_silence(self, discard_final_silence):
        if discard_final_silence is not None:
            discard_final_silence = bool(discard_final_silence)
        self._discard_final_silence = discard_final_silence

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
    def is_annotated(self):
        return self._is_annotated

    @is_annotated.setter
    def is_annotated(self, expr):
        if expr is not None:
            expr = bool(expr)
        self._is_annotated = expr

    @property
    def lilypond_file(self):
        return self._lilypond_file

    @property
    def maximum_meter_run_length(self):
        return self._maximum_meter_run_length

    @maximum_meter_run_length.setter
    def maximum_meter_run_length(self, expr):
        if expr is not None:
            expr = int(expr)
            assert 0 < expr
        self._maximum_meter_run_length = expr

    @property
    def measure_offsets(self):
        measure_durations = [x.duration for x in self.time_signatures]
        measure_offsets = mathtools.cumulative_sums(measure_durations)
        return measure_offsets

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, expr):
        if expr is not None:
            expr = str(expr)
        self._name = expr

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
    def segment_duration(self):
        return sum(x.duration for x in self.time_signatures)

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
        if self._tempo is None:
            if self._previous_segment_metadata is not None:
                tempo = self._previous_segment_metadata.get('end_tempo')
                tempo = indicatortools.Tempo(*tempo)
                return tempo
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        if tempo is not None:
            if not isinstance(tempo, indicatortools.Tempo):
                tempo = indicatortools.Tempo(tempo)
        self._tempo = tempo

    @property
    def time_signatures(self):
        return tuple(
            meter.implied_time_signature
            for meter in self.meters
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

    @property
    def voice_names(self):
        return self._voice_names

    @property
    def repeat(self):
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        if repeat is not None:
            repeat = bool(repeat)
        self._repeat = repeat