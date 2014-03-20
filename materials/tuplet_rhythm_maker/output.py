# -*- encoding: utf-8 -*-
from abjad.tools import rhythmmakertools


tuplet_rhythm_maker = rhythmmakertools.TupletRhythmMaker(
    tuplet_ratios=(
        mathtools.Ratio(1, 1),
        mathtools.Ratio(1, 2),
        mathtools.Ratio(2, -1),
        mathtools.Ratio(-1, 1, 1),
        ),
    tie_specifier=rhythmmakertools.TieSpecifier(
        tie_across_divisions=True,
        tie_split_notes=True,
        ),
    tuplet_spelling_specifier=rhythmmakertools.TupletSpellingSpecifier(
        avoid_dots=True,
        is_diminution=True,
        ),
    )