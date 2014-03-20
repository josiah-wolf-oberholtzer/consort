# -*- encoding: utf-8 -*-
from abjad.tools import rhythmmakertools


incised_rhythm_maker = rhythmmakertools.IncisedRhythmMaker(
    incise_specifier=rhythmmakertools.InciseSpecifier(
        incise_divisions=True,
        incise_output=False,
        prefix_talea=(1,),
        prefix_lengths=(0,),
        suffix_talea=(1,),
        suffix_lengths=(1,),
        talea_denominator=32,
        fill_with_notes=True,
        ),
    )