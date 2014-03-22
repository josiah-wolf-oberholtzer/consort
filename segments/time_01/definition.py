# -*- encoding: utf-8 -*-
from abjad import *
from consort import makers
from consort import materials
from consort.segments import base


voice_specifier_one = makers.VoiceSpecifier(
    color='red',
    music_specifier=makers.MusicSpecifier(
        rhythm_maker=materials.note_rhythm_maker,
        ),
    timespan_maker=makers.TimespanMaker(
        can_split=False,
        ),
    voice_identifiers='.*',
    )


segment_maker = new(base.segment_maker,
    annotation_specifier__show_stage_4=False,
    annotation_specifier__show_stage_6=False,
    name='spans of time',
    permitted_time_signatures=indicatortools.TimeSignatureInventory([
        (2, 4),
        ]),
    rehearsal_mark='A1',
    voice_specifiers=(
        voice_specifier_one,
        ),
    )


__all__ = (
    'segment_maker',
    'voice_specifier_one',
    )
