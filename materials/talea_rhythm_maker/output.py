# -*- encoding: utf-8 -*-
from abjad.tools import rhythmmakertools


talea_rhythm_maker = rhythmmakertools.TaleaRhythmMaker(
    talea=rhythmmakertools.Talea(
        counts=(1, 2, 3),
        denominator=16,
        ),
    extra_counts_per_division=(0, 0, 1),
    tie_specifier=rhythmmakertools.TieSpecifier(
        tie_across_divisions=False,
        tie_split_notes=False,
        ),
    )