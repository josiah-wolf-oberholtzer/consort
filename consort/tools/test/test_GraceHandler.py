# -*- encoding: utf -*-
from abjad.tools import indicatortools
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import templatetools
import consort


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
        duration_in_seconds=4,
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
    lilypond_file = segment_maker()
    assert systemtools.TestManager.compare(
        format(lilypond_file),
        r'''
        \version "2.19.15"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 4/4
                        \tempo 4=60
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
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
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                            }
                            {
                                {
                                    c'4
                                    \bar "||"
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    r4
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        '''), format(lilypond_file)


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
        duration_in_seconds=4,
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
    lilypond_file = segment_maker()
    assert systemtools.TestManager.compare(
        format(lilypond_file),
        r'''
        \version "2.19.15"
        \language "english"
        
        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 4/4
                        \tempo 4=60
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        c'16
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                                {
                                    c'4
                                    \bar "||"
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    \afterGrace
                                    r4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                            }
                            {
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                                {
                                    \afterGrace
                                    c'4
                                    {
                                        \override Flag #'stroke-style = #"grace"
                                        \override Script #'font-size = #0.5
                                        \override Stem #'length = #8
                                        c'16
                                        c'16
                                        c'16
                                        \revert Flag #'stroke-style
                                        \revert Script #'font-size
                                        \revert Stem #'length
                                    }
                                }
                                {
                                    c'4
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        '''), format(lilypond_file)