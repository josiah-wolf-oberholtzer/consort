# -*- encoding: utf -*-
import collections
from abjad.tools import indicatortools
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import templatetools
import consort


segment_metadata = collections.OrderedDict(
    segment_count=2,
    segment_number=1,
    )


def test_GraceHandler_01():
    music_specifier = consort.MusicSpecifier(
        grace_handler=consort.GraceHandler(
            counts=(1,),
            ),
        rhythm_maker=rhythmmakertools.NoteRhythmMaker(
            tie_specifier=rhythmmakertools.TieSpecifier(
                tie_across_divisions=False,
                ),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=4,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(
                    initial_silence_talea=rhythmmakertools.Talea(
                        counts=(0, 1),
                        denominator=4,
                        ),
                    playing_groupings=(2,),
                    ),
                v1=music_specifier,
                v2=music_specifier,
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 4/4
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                            }
                            {
                                {
                                    c'4
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    r4
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_GraceHandler_02():
    music_specifier = consort.MusicSpecifier(
        grace_handler=consort.GraceHandler(
            counts=(1, 2, 3),
            ),
        rhythm_maker=rhythmmakertools.NoteRhythmMaker(
            tie_specifier=rhythmmakertools.TieSpecifier(
                tie_across_divisions=False,
                ),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=4,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(
                    initial_silence_talea=rhythmmakertools.Talea(
                        counts=(1,),
                        denominator=4,
                        ),
                    playing_groupings=(3,),
                    ),
                v1=music_specifier,
                v2=music_specifier,
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 4/4
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        c'16
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    c'4
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        c'16
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    c'4
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_GraceHandler_03():
    music_specifier = consort.MusicSpecifier(
        grace_handler=consort.GraceHandler(
            counts=(0, 2, 4),
            ),
        rhythm_maker=rhythmmakertools.NoteRhythmMaker(
            tie_specifier=rhythmmakertools.TieSpecifier(
                tie_across_divisions=False,
                ),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=4,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(
                    initial_silence_talea=rhythmmakertools.Talea(
                        counts=(1,),
                        denominator=4,
                        ),
                    playing_groupings=(3,),
                    ),
                v1=music_specifier,
                v2=music_specifier,
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 4/4
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
                                {
                                    r4
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        c'16
                                        c'16
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    c'4
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                            }
                            {
                                {
                                    c'4
                                }
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        c'16
                                        c'16
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    c'4
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')

def test_GraceHandler_04():
    music_specifier = consort.MusicSpecifier(
        grace_handler=consort.GraceHandler(
            only_if_preceded_by_silence=True,
            ),
        rhythm_maker=rhythmmakertools.NoteRhythmMaker(
            tie_specifier=rhythmmakertools.TieSpecifier(
                tie_across_divisions=False,
                ),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=4,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(
                    initial_silence_talea=rhythmmakertools.Talea(
                        counts=(1,),
                        denominator=4,
                        ),
                    playing_groupings=(2,),
                    ),
                v1=music_specifier,
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 4/4
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                            }
                            {
                                {
                                    c'4
                                }
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    r4
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_GraceHandler_05():
    music_specifier = consort.MusicSpecifier(
        grace_handler=consort.GraceHandler(
            only_if_preceded_by_nonsilence=True,
            ),
        rhythm_maker=rhythmmakertools.NoteRhythmMaker(
            tie_specifier=rhythmmakertools.TieSpecifier(
                tie_across_divisions=False,
                ),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=4,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(
                    initial_silence_talea=rhythmmakertools.Talea(
                        counts=(1,),
                        denominator=4,
                        ),
                    playing_groupings=(2,),
                    ),
                v1=music_specifier,
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 4/4
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
                                {
                                    r4
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag.stroke-style = #"grace"
                                        \override Script.font-size = #0.5
                                        c'16
                                        \revert Flag.stroke-style
                                        \revert Script.font-size
                                    }
                                }
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    r4
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')
