# -*- encoding: utf-8 -*-
from abjad import durationtools
from abjad import indicatortools
from abjad import rhythmmakertools
from consort import makers
from consort import materials


red_voice_specifier = makers.VoiceSpecifier(
    color='red',
    music_specifier=makers.MusicSpecifier(
#        rhythm_maker=materials.note_rhythm_maker,
        rhythm_maker=rhythmmakertools.TaleaRhythmMaker(
            beam_specifier=rhythmmakertools.BeamSpecifier(
                beam_divisions_together=True,
                ),
            extra_counts_per_division=(1, 0, 2, 1, 0),
            talea=rhythmmakertools.Talea(
                counts=(1, 2, 1, 2, 3),
                denominator=16,
                ),
            ),
        ),
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
        hide_inner_bracket=False,
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
