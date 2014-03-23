# -*- encoding: utf-8 -*-
from abjad import new
from abjad.tools import rhythmmakertools
from consort import materials
from consort.segments import time_05 as base


voice_specifier_one = new(base.voice_specifier_one,
    music_specifier__rhythm_maker=new(
        materials.talea_rhythm_maker,
        burnish_specifier=rhythmmakertools.BurnishSpecifier(
            burnish_output=True,
            lefts=(-1,),
            left_lengths=(1, 0),
            middles=(0,),
            right_lengths=(0,),
            ),
        extra_counts_per_division=(1, 0, 0, 0),
        talea__counts=(1, 2, 3),
        ).rotate(-2),
    )

segment_maker = new(base.segment_maker,
    annotation_specifier__show_stage_1=False,
    annotation_specifier__show_stage_2=False,
    annotation_specifier__show_stage_3=False,
    annotation_specifier__show_stage_4=True,
    annotation_specifier__show_stage_5=True,
    annotation_specifier__show_annotated_result=False,
    name='rotating rhythm patterns (2)',
    rehearsal_mark='B6b',
    voice_specifiers=(
        voice_specifier_one,
        ),
    )

__all__ = (
    'segment_maker',
    'voice_specifier_one',
    )
