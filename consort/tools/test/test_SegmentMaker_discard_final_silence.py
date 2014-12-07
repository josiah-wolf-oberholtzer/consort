# -*- encoding: utf -*-
from abjad.tools import indicatortools
from abjad.tools import systemtools
from abjad.tools import templatetools
from abjad.tools import timespantools
import consort


def test_SegmentMaker_discard_final_silence_01():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=False,
        desired_duration_in_seconds=16,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.FloodedTimespanMaker(),
                timespan_identifier=timespantools.Timespan(0, (1, 4)),
                v1=consort.MusicSpecifier(),
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
                    {
                        s1 * 1
                    }
                    {
                        s1 * 1
                    }
                    {
                        s1 * 1
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
                                    r2.
                                }
                                {
                                    R1 * 1
                                }
                                {
                                    R1 * 1
                                }
                                {
                                    R1 * 1
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        '''), format(lilypond_file)


def test_SegmentMaker_discard_final_silence_02():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=16,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=(
            consort.MusicSetting(
                timespan_maker=consort.FloodedTimespanMaker(),
                timespan_identifier=timespantools.Timespan(0, (1, 4)),
                v1=consort.MusicSpecifier(),
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
                                    c'4
                                }
                            }
                            {
                                {
                                    r2.
                                    \bar "||"
                                }
                            }
                        }
                    }
                >>
            >>
        }
        '''), format(lilypond_file)