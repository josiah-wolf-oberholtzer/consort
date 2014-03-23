# -*- encoding: utf-8 -*-
from abjad import durationtools
from abjad import indicatortools
from abjad import rhythmmakertools
from consort import makers


red_voice_specifier = makers.VoiceSpecifier(
    color='red',
    music_specifier=makers.MusicSpecifier(
        rhythm_maker=rhythmmakertools.TaleaRhythmMaker(
            beam_specifier=rhythmmakertools.BeamSpecifier(
                beam_divisions_together=True,
                ),
            #extra_counts_per_division=(1, 0, 2, 1, 0),
            talea=rhythmmakertools.Talea(
                counts=(1,),
                #counts=(1, 2, 1, 2, 3),
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


blue_voice_specifier = makers.VoiceSpecifier(
    color='blue',
    music_specifier=makers.MusicSpecifier(),
    timespan_maker=makers.TimespanMaker(
        can_split=False,
        initial_silence_durations=(
            durationtools.Duration(5, 16),
            ),
        playing_durations=(
            durationtools.Duration(1, 8),
            durationtools.Duration(3, 16),
            durationtools.Duration(1, 4),
            ),
        silence_durations=(
            durationtools.Duration(1, 2),
            durationtools.Duration(3, 4),
            ),
        synchronize_step=True,
        ),
    voice_identifiers=('Violin *', 'Viola *'),
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
    rehearsal_mark='C',
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
        blue_voice_specifier,
        ),
    )
