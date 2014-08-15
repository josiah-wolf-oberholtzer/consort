# -*- encoding: utf-8 -*-
from abjad import *


tuplet_rhythm_maker = rhythmmakertools.TupletRhythmMaker(
    tuplet_ratios=(
        mathtools.Ratio(1, 1),
        mathtools.Ratio(1, 2),
        mathtools.Ratio(2, -1),
        mathtools.Ratio(-1, 1, 1),
        ),
    beam_specifier=rhythmmakertools.BeamSpecifier(
        beam_each_division=False,
        beam_divisions_together=False,
        ),
    tie_specifier=rhythmmakertools.TieSpecifier(
        tie_across_divisions=True,
        ),
    tuplet_spelling_specifier=rhythmmakertools.TupletSpellingSpecifier(
        avoid_dots=True,
        is_diminution=True,
        simplify_tuplets=False,
        ),
    )