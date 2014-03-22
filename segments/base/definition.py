# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import indicatortools
from consort import makers


segment_maker = makers.ConsortSegmentMaker(
    annotation_specifier=makers.AnnotationSpecifier(
        show_stage_1=True,
        show_stage_2=True,
        show_stage_3=True,
        show_stage_4=True,
        show_stage_5=True,
        show_stage_6=True,
        show_unannotated_result=True,
        ),
    is_final_segment=False,
    permitted_time_signatures=indicatortools.TimeSignatureInventory([
        (2, 4),
        (3, 4),
        (3, 8),
        (5, 8),
        (5, 16),
        (6, 8),
        (7, 8),
        (7, 16),
        ]),
    target_duration=durationtools.Duration(4),
    template=makers.ConsortScoreTemplate(
        violin_count=1,
        viola_count=1,
        cello_count=1,
        contrabass_count=0,
        split_hands=False,
        ),
    tempo=indicatortools.Tempo((1, 8), 72),
    )


__all__ = (
    'segment_maker',
    )
