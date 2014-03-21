# -*- encoding: utf-8 -*-
from abjad import *
output_module_import_statements = [
    'from abjad.tools import rhythmmakertools',
    ]


incised_rhythm_maker = rhythmmakertools.IncisedRhythmMaker(
    beam_specifier=rhythmmakertools.BeamSpecifier(
        beam_each_division=False,
        beam_divisions_together=False,
        ),
    incise_specifier=rhythmmakertools.InciseSpecifier(
        incise_divisions=True,
        prefix_talea=(1,),
        prefix_lengths=(0,),
        suffix_talea=(1,),
        suffix_lengths=(1,),
        talea_denominator=32,
        )
    )
