# -*- encoding: utf-8 -*-
from abjad import *
from consort import makers
from consort.segments import base


voice_specifier = makers.VoiceSpecifier(
    music_specifier=makers.MusicSpecifier(
        rhythm_maker=rhythmmakertools.NoteRhythmMaker(
            tie_specifier=rhythmmakertools.TieSpecifier(
                tie_across_divisions=False,
                ),
            ),
        ),
    timespan_maker=makers.TimespanMaker(
        can_split=False,
        ),
    voice_identifiers='.*',
    )


segment_maker = new(base.segment_maker,
    rehearsal_mark=1,
    voice_specifiers=(
        voice_specifier,
        ),
    )


__all__ = (
    'segment_maker',
    )


if __name__ == '__main__':
    segment_maker.build_and_persist(__file__)
