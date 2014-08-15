# -*- encoding: utf-8 -*-
from abjad import *


note_rhythm_maker = rhythmmakertools.NoteRhythmMaker(
    beam_specifier=rhythmmakertools.BeamSpecifier(
        beam_each_division=False,
        beam_divisions_together=False,
        ),
    tie_specifier=rhythmmakertools.TieSpecifier(
        tie_across_divisions=False,
        ),
    )