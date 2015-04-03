# -*- encoding: utf -*-
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import templatetools
import consort



def test_SegmentMaker_01():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=2,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=None,
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((5, 8), (7, 16)),
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
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
                                    \stopStaff
                                    \startStaff
                                }
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
                                    \bar "||"
                                    \stopStaff
                                    \startStaff
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
                                    \stopStaff
                                    \startStaff
                                }
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
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


def test_SegmentMaker_02():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=2,
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
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    r16
                                    r8
                                    \bar "||"
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    r16
                                    r8
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_SegmentMaker_03():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=False,
        desired_duration_in_seconds=2,
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
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    r16
                                    r8
                                }
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
                                    \bar "||"
                                    \stopStaff
                                    \startStaff
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    r16
                                    r8
                                }
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
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


def test_SegmentMaker_04():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=2,
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
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    c'8 ~
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    c'8 ~
                                }
                                {
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    r8
                                    r4
                                    \bar "||"
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    c'8 ~
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    c'8 ~
                                }
                                {
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    r8
                                    r4
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_SegmentMaker_05():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=2,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.FloodedTimespanMaker(
                    timespan_specifier=consort.TimespanSpecifier(
                        minimum_duration=durationtools.Duration(1, 8),
                        ),
                    ),
                v1=consort.MusicSpecifier(),
                v2=consort.MusicSpecifier(),
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((5, 8), (7, 16)),
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
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    c'8 ~
                                    \set stemLeftBeamCount = 1
                                    c'8 ]
                                    \bar "||"
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    c'8 ~
                                    \set stemLeftBeamCount = 1
                                    c'8 ]
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_SegmentMaker_06():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(
                    initial_silence_talea=rhythmmakertools.Talea(
                        counts=(0, 3),
                        denominator=16,
                        ),
                    silence_talea=rhythmmakertools.Talea(
                        counts=(1,),
                        denominator=8,
                        ),
                    timespan_specifier=consort.TimespanSpecifier(
                        minimum_duration=durationtools.Duration(1, 8),
                        ),
                    ),
                v1=consort.MusicSpecifier(),
                v2=consort.MusicSpecifier(),
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((5, 8), (7, 16)),
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
                                    c'8. ~ [
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    r16
                                    r8
                                }
                            }
                            {
                                {
                                    c'8.
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
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    r8.
                                }
                            }
                            {
                                {
                                    c'4
                                }
                            }
                            {
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
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


def test_SegmentMaker_07():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=3,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.TaleaTimespanMaker(
                    initial_silence_talea=rhythmmakertools.Talea(
                        counts=(0, 3),
                        denominator=16,
                        ),
                    silence_talea=rhythmmakertools.Talea(
                        counts=(1,),
                        denominator=8,
                        ),
                    timespan_specifier=consort.TimespanSpecifier(
                        minimum_duration=durationtools.Duration(1, 8),
                        ),
                    ),
                v1=consort.MusicSpecifier(
                    rhythm_maker=rhythmmakertools.TaleaRhythmMaker(
                        talea=rhythmmakertools.Talea(
                            counts=(1, 2),
                            denominator=16,
                            ),
                        ),
                    ),
                v2=consort.MusicSpecifier(
                    rhythm_maker=rhythmmakertools.TaleaRhythmMaker(
                        talea=rhythmmakertools.Talea(
                            counts=(2, 1),
                            denominator=16,
                            ),
                        ),
                    ),
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((5, 8), (7, 16)),
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
                                    c'16 [
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    c'8
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    r16
                                    r8
                                }
                            }
                            {
                                {
                                    c'8 [
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
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
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    r8.
                                }
                            }
                            {
                                {
                                    c'8 [
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                            {
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
                                    \bar "||"
                                    \stopStaff
                                    \startStaff
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 3" {
                        \context Voice = "Voice 3" {
                            {
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
                                    \stopStaff
                                    \startStaff
                                }
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 7/16
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