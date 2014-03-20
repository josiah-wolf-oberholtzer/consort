# -*- encoding: utf-8 -*-
from abjad import *
from consort.segments import time_05 as base


voice_specifier_one = new(base.voice_specifier_one,
    music_specifier__rhythm_maker=rhythmmakertools.TaleaRhythmMaker(
        talea=rhythmmakertools.Talea(
            counts=(1, 1),
            denominator=16,
            ),
        tie_specifier=rhythmmakertools.TieSpecifier(
            tie_split_notes=False,
            ),
        ),
    )

#voice_specifier_two = new(base.voice_specifier_two,
#    music_specifier__rhythm_maker=rhythmmakertools.TupletRhythmMaker(
#        tuplet_ratios=(
#            (1, 1),
#            ),
#        tuplet_spelling_specifier=rhythmmakertools.TupletSpellingSpecifier(
#            avoid_dots=True,
#            ),
#        ),
#    )

segment_maker = new(base.segment_maker,
    rehearsal_mark='B1',
    voice_specifiers=(
        voice_specifier_one,
#        voice_specifier_two,
        ),
    )
