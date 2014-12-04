# -*- encoding: utf -*-
from abjad.tools import indicatortools
from abjad.tools import systemtools
from abjad.tools import templatetools
import consort


def test_SegmentMaker___call___01():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        duration_in_seconds=2,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(),
                v1=consort.MusicSpecifier(),
                v2=consort.MusicSpecifier(),
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((5, 8), (7, 16)),
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
                        \time 7/16
                        \tempo 4=60
                        s1 * 7/16
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    r8.
                                    \bar "||"
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    r8.
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        '''), format(lilypond_file)


def test_SegmentMaker___call___02():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=False,
        duration_in_seconds=2,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(),
                v1=consort.MusicSpecifier(),
                v2=consort.MusicSpecifier(),
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((5, 8), (7, 16)),
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
                        \time 7/16
                        \tempo 4=60
                        s1 * 7/16
                    }
                    {
                        s1 * 7/16
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    r8.
                                }
                                {
                                    r4..
                                    \bar "||"
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    r8.
                                }
                                {
                                    r4..
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        '''), format(lilypond_file)


def test_SegmentMaker___call___03():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        duration_in_seconds=2,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.FloodedTimespanMaker(),
                v1=consort.MusicSpecifier(),
                v2=consort.MusicSpecifier(),
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((5, 8), (7, 16)),
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
                        \time 7/16
                        \tempo 4=60
                        s1 * 7/16
                    }
                    {
                        s1 * 7/16
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'4.. ~
                                }
                                {
                                    \set stemLeftBeamCount = 2
                                    c'16
                                }
                            }
                            {
                                {
                                    r4.
                                    \bar "||"
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    c'4.. ~
                                }
                                {
                                    \set stemLeftBeamCount = 2
                                    c'16
                                }
                            }
                            {
                                {
                                    r4.
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        '''), format(lilypond_file)