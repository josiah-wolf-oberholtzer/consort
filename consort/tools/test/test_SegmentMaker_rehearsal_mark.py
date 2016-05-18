# -*- encoding: utf -*-
import collections
from abjad.tools import indicatortools
from abjad.tools import systemtools
from abjad.tools import templatetools
import consort


segment_metadata = collections.OrderedDict(
    segment_count=3,
    segment_number=2,
    )


def test_SegmentMaker_rehearsal_mark_01():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=4,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=None,
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker(
        segment_metadata=segment_metadata,
        )
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.41"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 4/4
                        \mark \markup {
                            \box
                                \pad-around
                                    #0.5
                                    \caps
                                        A
                            }
                        s1 * 1
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \bar "||"
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 1
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
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=None,
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((4, 4),),
        )
    lilypond_file, metadata = segment_maker(
        segment_metadata=segment_metadata,
        )
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.41"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 4/4
                        \mark \markup {
                            \concat
                                {
                                    \box
                                        \pad-around
                                            #0.5
                                            \caps
                                                A
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
                        \bar "||"
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 1
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
