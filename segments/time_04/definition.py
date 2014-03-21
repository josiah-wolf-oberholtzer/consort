# -*- encoding: utf-8 -*-
from abjad import *
from consort import makers
from consort import materials
from consort.segments import base


voice_specifier_one = makers.VoiceSpecifier(
    music_specifier=makers.MusicSpecifier(
        rhythm_maker=materials.note_rhythm_maker,
        ),
    timespan_maker=makers.TimespanMaker(
        can_split=False,
        minimum_duration=Duration(1, 8),
        playing_durations=(
            Duration(1, 4),
            Duration(3, 16),
            Duration(1, 8),
            ),
        playing_groupings=(2, 2, 1, 1),
        silence_durations=(
            Duration(1, 4),
            Duration(1, 8),
            ),
        synchronize_groupings=True,
        synchronize_step=True,
        ),
    voice_identifiers='.*',
    )


segment_maker = new(base.segment_maker,
    rehearsal_mark='A4',
    voice_specifiers=(
        voice_specifier_one,
        ),
    )


__all__ = (
    'segment_maker',
    'voice_specifier_one',
    )
