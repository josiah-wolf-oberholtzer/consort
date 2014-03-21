# -*- encoding: utf-8 -*-
from abjad import new
from abjad.tools import rhythmmakertools
from consort import materials
from consort.segments import time_08 as base


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
        ).rotate(-4),
    )

voice_specifier_two = new(base.voice_specifier_two,
    )

segment_maker = new(base.segment_maker,
    rehearsal_mark='B7',
    voice_specifiers=(
        voice_specifier_one,
        voice_specifier_two,
        ),
    )

__all__ = (
    'segment_maker',
    'voice_specifier_one',
    'voice_specifier_two',
    )
