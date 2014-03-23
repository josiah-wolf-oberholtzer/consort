# -*- encoding: utf-8 -*-
from abjad import durationtools
from abjad import indicatortools
from consort import makers


red_voice_specifier = makers.VoiceSpecifier(
    color='red',
    music_specifier=makers.MusicSpecifier(),
    timespan_maker=makers.TimespanMaker(
        can_split=False,
        initial_silence_durations=(
            durationtools.Duration(0),
            durationtools.Duration(1, 8),
            durationtools.Duration(1, 4),
            ),
        minimum_duration=durationtools.Duration(1, 8),
        playing_durations=(
            durationtools.Duration(1, 4),
            durationtools.Duration(3, 16),
            durationtools.Duration(1, 8),
            ),
        playing_groupings=(2, 2, 1, 1),
        silence_durations=(
            durationtools.Duration(1, 4),
            durationtools.Duration(1, 8),
            ),
        synchronize_step=False,
        ),
    voice_identifiers='.*',
    )


segment_maker = makers.ConsortSegmentMaker(
    annotation_specifier=makers.AnnotationSpecifier(
        show_annotated_result=True,
        show_unannotated_result=False,
        ),
    name='a string trio',
    permitted_time_signatures=indicatortools.TimeSignatureInventory([
        (2, 4),
        (3, 8),
        (5, 16),
        (7, 16),
        ]),
    rehearsal_mark='A',
    target_duration=durationtools.Duration(4),
    template=makers.ConsortScoreTemplate(
        violin_count=1,
        viola_count=1,
        cello_count=1,
        contrabass_count=0,
        split_hands=False,
        ),
    tempo=indicatortools.Tempo((1, 8), 72),
    voice_specifiers=(
        red_voice_specifier,
        ),
    )
