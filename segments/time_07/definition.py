# -*- encoding: utf-8 -*-
from abjad import *
from experimental.tools import selectortools
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
        initial_silence_durations=(
            Duration(0),
            Duration(1, 8),
            Duration(1, 4),
            ),
        minimum_duration=Duration(0, 8),
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
        synchronize_step=False,
        ),
    voice_identifiers='.*',
    )


voice_specifier_two = makers.VoiceSpecifier(
    color='blue',
    music_specifier=makers.MusicSpecifier(
        attachment_agent=makers.AttachmentAgent(
            attachment_specifiers=(
                makers.AttachmentSpecifier(
                    attachments=(
                        indicatortools.Articulation('>'),
                        ),
                    selector=selectortools.Selector().by_leaves()[0],
                    ),
                ),
            ),
        rhythm_maker=materials.note_rhythm_maker,
        ),
    timespan_maker=makers.TimespanMaker(
        can_split=False,
        initial_silence_durations=(
            #Duration(5, 16),
            ),
        minimum_duration=Duration(0, 8),
        playing_durations=(
            Duration(3, 16),
            Duration(1, 8),
            Duration(3, 32),
            Duration(1, 8),
            ),
        silence_durations=(
            Duration(3, 4),
            ),
        step_anchor=Left,
        synchronize_step=True,
        ),
    voice_identifiers='.*',
    )


segment_maker = new(base.segment_maker,
    annotation_specifier__show_stage_1=False,
    annotation_specifier__show_stage_2=False,
    annotation_specifier__show_stage_4=False,
    annotation_specifier__show_annotated_result=False,
    name='desynchronizing blue timespan releases',
    rehearsal_mark='A7',
    voice_specifiers=(
        voice_specifier_one,
        voice_specifier_two,
        ),
    )


__all__ = (
    'segment_maker',
    'voice_specifier_one',
    'voice_specifier_two',
    )
