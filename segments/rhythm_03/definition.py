# -*- encoding: utf-8 -*-
from abjad import new
from consort import materials
from consort.segments import time_05 as base


voice_specifier_one = new(base.voice_specifier_one,
    music_specifier__rhythm_maker=new(
        materials.talea_rhythm_maker,
        extra_counts_per_division=(0,),
        talea__counts=(1, 2, 3),
        ),
    )

segment_maker = new(base.segment_maker,
    rehearsal_mark='B3',
    voice_specifiers=(
        voice_specifier_one,
        ),
    )

__all__ = (
    'segment_maker',
    'voice_specifier_one',
    )
