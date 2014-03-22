# -*- encoding: utf-8 -*-
from abjad import new
from consort import materials
from consort.segments import time_05 as base


voice_specifier_one = new(base.voice_specifier_one,
    music_specifier__rhythm_maker=new(
        materials.talea_rhythm_maker,
        extra_counts_per_division=(0,),
        talea__counts=(1,),
        ),
    )

segment_maker = new(base.segment_maker,
    annotation_specifier__show_stage_1=False,
    annotation_specifier__show_stage_2=False,
    annotation_specifier__show_stage_3=True,
    annotation_specifier__show_stage_4=False,
    annotation_specifier__show_stage_5=True,
    annotation_specifier__show_stage_6=False,
    name='inscribing a rhythm',
    rehearsal_mark='B1',
    voice_specifiers=(
        voice_specifier_one,
        ),
    )

__all__ = (
    'segment_maker',
    'voice_specifier_one',
    )
