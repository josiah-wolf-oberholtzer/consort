# -*- encoding: utf-8 -*-
import itertools
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import schemetools
from abjad.tools import systemtools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import mutate
from abjad.tools.topleveltools import override
from abjad.tools import abctools


class AnnotationManager(abctools.AbjadValueObject):
    r'''An editorial manager.
    '''

    ### PUBLIC PROPERTIES ###

    @staticmethod
    def _annotate_stage_1(
        segment_session=None,
        ):
        from consort import makers
        rewritten_score = segment_session.score
        score_copy = mutate(rewritten_score).copy()
        annotated_score = makers.AnnotationManager.annotate(
            score=score_copy,
            segment_session=segment_session,
            )
        manager = override(annotated_score)
        manager.bar_line.transparent = True
        manager.beam.transparent = True
        manager.dots.transparent = True
        manager.flag.transparent = True
        manager.note_head.transparent = True
        manager.rest.transparent = True
        manager.span_bar.transparent = True
        manager.stem.transparent = True
        manager.tie.transparent = True
        manager.tuplet_bracket.transparent = True
        manager.tuplet_number.transparent = True
        prototype = scoretools.Voice
        for voice in iterate(annotated_score).by_class(prototype):
            if voice.context_name != 'LHVoice':
                continue
            override(voice).tuplet_bracket.transparent = True
        segment_session.scores.append(annotated_score)

    @staticmethod
    def _annotate_stage_2(
        segment_session=None,
        ):
        from consort import makers
        rewritten_score = segment_session.score
        score_copy = mutate(rewritten_score).copy()
        annotated_score = makers.AnnotationManager.annotate(
            score=score_copy,
            segment_session=segment_session,
            )
        manager = override(annotated_score)
        manager.bar_line.transparent = True
        manager.beam.transparent = True
        manager.dots.transparent = True
        manager.flag.transparent = True
        manager.note_head.transparent = True
        manager.rest.transparent = True
        manager.span_bar.transparent = True
        manager.stem.transparent = True
        manager.tie.transparent = True
        manager.tuplet_number.transparent = True
        prototype = scoretools.Voice
        for voice in iterate(annotated_score).by_class(prototype):
            if voice.context_name != 'LHVoice':
                continue
            override(voice).tuplet_bracket.transparent = True
        segment_session.scores.append(annotated_score)

    @staticmethod
    def _annotate_stage_3(
        segment_session=None,
        ):
        from consort import makers
        rewritten_score = segment_session.score
        score_copy = mutate(rewritten_score).copy()
        annotated_score = makers.AnnotationManager.annotate(
            score=score_copy,
            segment_session=segment_session,
            )
        manager = override(annotated_score)
        manager.beam.transparent = True
        manager.dots.transparent = True
        manager.flag.transparent = True
        manager.note_head.transparent = True
        manager.rest.transparent = True
        manager.stem.transparent = True
        manager.tie.transparent = True
        manager.tuplet_number.transparent = True
        prototype = scoretools.Voice
        for voice in iterate(annotated_score).by_class(prototype):
            if voice.context_name != 'LHVoice':
                continue
            override(voice).tuplet_bracket.transparent = True
        segment_session.scores.append(annotated_score)

    @staticmethod
    def _annotate_stage_4(
        segment_session=None,
        ):
        from consort import makers
        unrewritten_score = segment_session.unrewritten_score
        score_copy = mutate(unrewritten_score).copy()
        annotated_score = makers.AnnotationManager.annotate(
            score=score_copy,
            segment_session=segment_session,
            )
        segment_session.scores.append(annotated_score)

    @staticmethod
    def _annotate_stage_5(
        segment_session=None,
        ):
        from consort import makers
        score_copy = mutate(segment_session.score).copy()
        annotated_score = makers.AnnotationManager.annotate(
            score=score_copy,
            segment_session=segment_session,
            )
        segment_session.scores.append(annotated_score)

    @staticmethod
    def _annotate_stage_6(
        segment_session=None,
        should_copy=True,
        ):
        from consort import makers
        score = segment_session.score
        if should_copy:
            score = mutate(score).copy()
        annotated_score = makers.AnnotationManager.annotate(
            score=score,
            segment_session=segment_session,
            )
        segment_session.scores.append(annotated_score)

    @staticmethod
    def _create_all_annotation_voices(
        hide_brackets=None,
        score=None,
        segment_session=None,
        ):
        from consort import makers
        voicewise_timespans = segment_session.voicewise_timespans
        voice_names = voicewise_timespans.keys()
        voice_names = makers.RhythmManager._sort_voice_names(
            template=segment_session.segment_maker.template,
            voice_names=voice_names,
            )
        annotation_specifier = \
            segment_session.segment_maker.annotation_specifier
        hide_inner_bracket = \
            annotation_specifier.hide_inner_bracket
        with systemtools.ForbidUpdate(score):
            for voice_name in voice_names:
                timespan_inventory = voicewise_timespans[voice_name]
                inner_annotation, outer_annotation = \
                    AnnotationManager._create_annotation_voices(
                        hide_brackets=hide_brackets,
                        hide_inner_bracket=hide_inner_bracket,
                        timespan_inventory=timespan_inventory,
                        voice_name=voice_name,
                        )
                voice = score[voice_name]
                parentage = inspect_(voice).get_parentage(
                    include_self=False)
                parent = parentage[0]
                parent.append(inner_annotation)
                parent.append(outer_annotation)
        return score

    @staticmethod
    def _create_annotation_voices(
        hide_brackets=None,
        hide_inner_bracket=None,
        timespan_inventory=None,
        voice_name=None,
        ):
        def grouper(timespan):
            color = None
            music_specifier = None
            if isinstance(timespan, makers.PerformedTimespan):
                color = timespan.color
                music_specifier = timespan.music_specifier
            return color, music_specifier
        from consort import makers
        inner_annotation_items = []
        outer_annotation_items = []
        for key, timespans in itertools.groupby(
            timespan_inventory, grouper):
            color, music_specifier = key
            timespans = tuple(timespans)
            inner_durations = [x.duration for x in timespans]
            outer_duration = sum(inner_durations)
            is_left_broken = timespans[0].is_left_broken
            is_right_broken = timespans[-1].is_right_broken
            if music_specifier is None or music_specifier.is_sentinel:
                outer_note = scoretools.Note("c'1")
                outer_multiplier = durationtools.Multiplier(outer_duration)
                attach(outer_multiplier, outer_note)
                outer_annotation_items.append(outer_note)
                inner_note = mutate(outer_note).copy()
                inner_annotation_items.append(inner_note)
                continue
            note = scoretools.Note(0, 1)
            outer_tuplet = scoretools.Tuplet(outer_duration, (note,))
            override(outer_tuplet).tuplet_bracket.color = color
            AnnotationManager._override_tuplet_edge_height(
                is_left_broken=is_left_broken,
                is_right_broken=is_right_broken,
                tuplet=outer_tuplet,
                )
            outer_annotation_items.append(outer_tuplet)
            if not hide_inner_bracket:
                inner_tuplets = []
                for inner_duration in inner_durations:
                    note = scoretools.Note(0, 1)
                    inner_tuplet = scoretools.Tuplet(
                        inner_duration, (note,))
                    override(inner_tuplet).tuplet_bracket.color = color
                    inner_tuplets.append(inner_tuplet)
                if len(inner_tuplets) == 1:
                    AnnotationManager._override_tuplet_edge_height(
                        is_left_broken=is_left_broken,
                        is_right_broken=is_right_broken,
                        tuplet=inner_tuplets[0],
                        )
                else:
                    if is_left_broken:
                        manager = override(inner_tuplets[0])
                        manager.tuplet_bracket.edge_height = \
                            schemetools.SchemePair(0, 0.7)
                    if is_right_broken:
                        manager = override(inner_tuplets[-1])
                        manager.tuplet_bracket.edge_height = \
                            schemetools.SchemePair(0.7, 0)
                inner_annotation_items.extend(inner_tuplets)
            else:
                inner_note = scoretools.Note(0, 1)
                inner_multiplier = durationtools.Multiplier(outer_duration)
                attach(inner_multiplier, inner_note)
                inner_annotation_items.append(inner_note)

        inner_annotation = scoretools.Context(
            inner_annotation_items,
            name='{} Inner Annotation'.format(voice_name),
            context_name='InnerAnnotation',
            )
        outer_annotation = scoretools.Context(
            outer_annotation_items,
            name='{} Outer Annotation'.format(voice_name),
            context_name='OuterAnnotation',
            )
        if hide_brackets:
            override(inner_annotation).tuplet_bracket.transparent = True
            override(outer_annotation).tuplet_bracket.transparent = True
        return inner_annotation, outer_annotation

    @staticmethod
    def _override_tuplet_edge_height(
        is_left_broken=None,
        is_right_broken=None,
        tuplet=None,
        ):
        if is_left_broken:
            if is_right_broken:
                override(tuplet).tuplet_bracket.edge_height = \
                    schemetools.SchemePair(0, 0)
            else:
                override(tuplet).tuplet_bracket.edge_height = \
                    schemetools.SchemePair(0, 0.7)
        elif is_right_broken:
            override(tuplet).tuplet_bracket.edge_height = \
                schemetools.SchemePair(0.7, 0)

    ### PUBLIC METHODS ###

    @staticmethod
    def annotate(
        hide_brackets=None,
        score=None,
        segment_session=None,
        ):
        annotated_score = AnnotationManager._create_all_annotation_voices(
            hide_brackets=hide_brackets,
            score=score,
            segment_session=segment_session,
            )
        return annotated_score
