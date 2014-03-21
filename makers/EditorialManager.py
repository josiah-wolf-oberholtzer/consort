# -*- encoding: utf-8 -*-
import itertools
from abjad.tools import durationtools
from abjad.tools import scoretools
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
        annotation_specification = \
            segment_product.segment_maker.annotation_specification
        show_inner_bracket = \
            annotation_specification.show_inner_bracket
        for voice_name in voice_names:
            timespan_inventory = timespan_inventory_mapping[voice_name]
            inner_annotation, outer_annotation = \
                EditorialManager._create_annotation_voices(
                    hide_brackets=hide_brackets,
                    show_inner_bracket=show_inner_bracket,
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
        show_inner_bracket=None,
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
            if music_specifier is None or music_specifier.is_sentinel:
                outer_note = scoretools.Note("c'1")
                outer_multiplier = durationtools.Multiplier(outer_duration)
                attach(outer_multiplier, outer_note)
                outer_annotation.append(outer_note)
                inner_note = mutate(outer_note).copy()
                inner_annotation.append(inner_note)
                continue
            outer_tuplet = scoretools.Tuplet(outer_duration, "c'1")
            outer_annotation.append(outer_tuplet)
            if show_inner_bracket:
                inner_tuplets = [scoretools.Tuplet(inner_duration, "c'1")
                    for inner_duration in inner_durations]
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
