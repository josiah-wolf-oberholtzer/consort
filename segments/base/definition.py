# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import indicatortools
from consort import makers


segment_maker = makers.ConsortSegmentMaker(
    is_final_segment=False,
    permitted_time_signatures=indicatortools.TimeSignatureInventory([
        (2, 4),
        (3, 4),
        (3, 8),
        (5, 8),
        (6, 8),
        (7, 8),
        (7, 16),
        ]),
    target_duration=durationtools.Duration(9, 2),
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
