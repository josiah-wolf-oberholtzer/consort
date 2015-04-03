# -*- encoding: utf -*-
from abjad.tools import indicatortools
from abjad.tools import systemtools
from abjad.tools import templatetools
import consort


def test_SegmentMaker_rehearsal_mark_01():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=4,
        omit_stylesheets=True,
        rehearsal_mark='A',
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=None,
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker()
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 4/4
                        \tempo 4=60
                        \mark \markup {
                            \concat
                                {
                                    \override
                                        #'(box-padding . 0.5)
                                        \box
                                            \caps
                                                A
                                    " "
                                    \fontsize
                                        #-3
                                        " "
                                }
                            }
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 1
                                    \bar "||"
                                    \stopStaff
                                    \startStaff
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_SegmentMaker_rehearsal_mark_02():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=4,
        name='A transitional segment',
        omit_stylesheets=True,
        rehearsal_mark='A Part 1',
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=None,
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker()
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 4/4
                        \tempo 4=60
                        \mark \markup {
                            \concat
                                {
                                    \override
                                        #'(box-padding . 0.5)
                                        \box
                                            \caps
                                                "A Part 1"
                                    " "
                                    \fontsize
                                        #-3
                                        "A transitional segment"
                                }
                            }
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 1
                                    \bar "||"
                                    \stopStaff
                                    \startStaff
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')