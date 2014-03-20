# -*- encoding: utf-8 -*-
from abjad import *
output_module_import_statements = [
    'from abjad.tools import *',
    ]


tuplet_rhythm_maker = rhythmmakertools.TupletRhythmMaker(
    tie_specifier=rhythmmakertools.TieSpecifier(
        tie_across_divisions=True,
        ),
    tuplet_ratios=(
        (1, 1),
        (1, 2),
        (2, -1),
        (-1, 1, 1),
        ),
    tuplet_spelling_specifier=rhythmmakertools.TupletSpellingSpecifier(
        avoid_dots=True,
        ),
    )
