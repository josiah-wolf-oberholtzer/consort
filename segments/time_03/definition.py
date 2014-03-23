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
        minimum_duration=Duration(1, 8),
        playing_durations=(
            Duration(1, 4),
            Duration(3, 16),
            Duration(1, 8),
            ),
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
    annotation_specifier__show_stage_1=False,
    annotation_specifier__show_stage_2=False,
    annotation_specifier__show_stage_4=False,
    annotation_specifier__show_annotated_result=False,
    name='different silences: 1/4 and 1/8',
    rehearsal_mark='A3',
    voice_specifiers=(
        voice_specifier_one,
        ),
    )


__all__ = (
    'segment_maker',
    'voice_specifier_one',
    )
