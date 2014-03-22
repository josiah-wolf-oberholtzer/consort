# -*- encoding: utf-8 -*-
import itertools
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import schemetools
from abjad.tools import timespantools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import mutate
from abjad.tools.topleveltools import override
from consort.makers.ConsortObject import ConsortObject


class EditorialManager(ConsortObject):
    r'''An editorial manager.
    '''

    ### PUBLIC PROPERTIES ###

    @staticmethod
    def _create_all_annotation_voices(
        hide_brackets=None,
        score=None,
        segment_product=None,
        ):
        from consort import makers
        timespan_inventory_mapping = segment_product.timespan_inventory_mapping
        voice_names = timespan_inventory_mapping.keys()
        voice_names = makers.RhythmManager._sort_voice_names(
            template=segment_product.segment_maker.template,
            voice_names=voice_names,
            )
        annotation_specifier = \
            segment_product.segment_maker.annotation_specifier
        hide_inner_bracket = \
            annotation_specifier.hide_inner_bracket
        for voice_name in voice_names:
            timespan_inventory = timespan_inventory_mapping[voice_name]
            inner_annotation, outer_annotation = \
                EditorialManager._create_annotation_voices(
                    hide_brackets=hide_brackets,
                    hide_inner_bracket=hide_inner_bracket,
                    timespan_inventory=timespan_inventory,
                    voice_name=voice_name,
                    )
            voice = score[voice_name]
            parentage = inspect_(voice).get_parentage(include_self=False)
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
            music_specifier = None
            if isinstance(timespan, makers.PerformedTimespan):
                music_specifier = timespan.music_specifier
                if music_specifier is None:
                    music_specifier = makers.MusicSpecifier()
            return music_specifier
        from consort import makers
        inner_annotation = scoretools.Context(
            name='{} Inner Annotation'.format(voice_name),
            context_name='InnerAnnotation',
            )
        outer_annotation = scoretools.Context(
            name='{} Outer Annotation'.format(voice_name),
            context_name='OuterAnnotation',
            )
        for music_specifier, timespans in itertools.groupby(
            timespan_inventory, grouper):
            timespans = timespantools.TimespanInventory(timespans)
            outer_duration = timespans.duration
            inner_durations = [x.duration for x in timespans]
            colors = tuple(set([timespan.color for timespan in timespans]))
            assert len(colors) == 1
            color = colors[0]
            is_left_broken = timespans[0].is_left_broken
            is_right_broken = timespans[-1].is_right_broken
            if music_specifier is None or music_specifier.is_sentinel:
                outer_note = scoretools.Note("c'1")
                outer_multiplier = durationtools.Multiplier(outer_duration)
                attach(outer_multiplier, outer_note)
                outer_annotation.append(outer_note)
                inner_note = mutate(outer_note).copy()
                inner_annotation.append(inner_note)
                continue
            outer_tuplet = scoretools.Tuplet(outer_duration, "c'1")
            override(outer_tuplet).tuplet_bracket.color = color
            EditorialManager._override_tuplet_edge_height(
                is_left_broken=is_left_broken,
                is_right_broken=is_right_broken,
                tuplet=outer_tuplet,
                )
            outer_annotation.append(outer_tuplet)
            if not hide_inner_bracket:
                inner_tuplets = []
                for inner_duration in inner_durations:
                    inner_tuplet = scoretools.Tuplet(inner_duration, "c'1")
                    override(inner_tuplet).tuplet_bracket.color = color
                    inner_tuplets.append(inner_tuplet)
                if len(inner_tuplets) == 1:
                    EditorialManager._override_tuplet_edge_height(
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
                inner_annotation.extend(inner_tuplets)
            else:
                inner_note = scoretools.Note("c'1")
                inner_multiplier = durationtools.Multiplier(outer_duration)
                attach(inner_multiplier, inner_note)
                inner_annotation.append(inner_note)
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
        segment_product=None,
        ):
        annotated_score = EditorialManager._create_all_annotation_voices(
            hide_brackets=hide_brackets,
            score=score,
            segment_product=segment_product,
            )
        return annotated_score
