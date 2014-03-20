# -*- encoding: utf-8 -*-
from abjad import *
output_module_import_statements = [
    'from abjad.tools import rhythmmakertools',
    ]


talea_rhythm_maker = rhythmmakertools.TaleaRhythmMaker(
    extra_counts_per_division=(0, 0, 1),
    talea=rhythmmakertools.Talea(
        counts=(1, 2, 3),
        denominator=16,
        ),
    tie_specifier=rhythmmakertools.TieSpecifier(
        tie_split_notes=False,
        ),
    )
