# -*- encoding: utf-8 -*-
from abjad import durationtools
from abjad import indicatortools
from consort import makers
from consort import materials


red_voice_specifier = makers.VoiceSpecifier(
    color='red',
    music_specifier=makers.MusicSpecifier(
        rhythm_maker=materials.note_rhythm_maker,
        ),
    timespan_maker=makers.TimespanMaker(
        can_split=False,
        ),
    voice_identifiers='.*',
    )


segment_maker = makers.ConsortSegmentMaker(
    annotation_specifier=makers.AnnotationSpecifier(
        show_stage_6=True,
        show_unannotated_result=False,
        ),
    permitted_time_signatures=indicatortools.TimeSignatureInventory([
        (2, 4),
        (3, 8),
        (5, 16),
        (7, 16),
        ]),
    template=makers.ConsortScoreTemplate(
        violin_count=1,
        viola_count=1,
        cello_count=1,
        contrabass_count=0,
        split_hands=False,
        ),
    target_duration=durationtools.Duration(4),
    tempo=indicatortools.Tempo((1, 8), 72),
    voice_settings=(),
    voice_specifiers=(
        red_voice_specifier,
        ),
    )
