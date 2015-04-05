# -*- encoding: utf -*-
import collections
from abjad import new
from abjad.tools import indicatortools
from abjad.tools import pitchtools
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import templatetools
import consort


music_specifier = consort.MusicSpecifier(
    rhythm_maker=rhythmmakertools.EvenDivisionRhythmMaker(
        denominators=[16],
        ),
    )

segment_metadata = collections.OrderedDict(
    segment_count=2,
    segment_number=1,
    )


def test_AbsolutePitchHandler_01():
    pitch_handler = consort.AbsolutePitchHandler()
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=1,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_02():
    pitch_handler = consort.AbsolutePitchHandler(
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments=(
                "c' e' g'",
                ),
            ratio=(1,),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=1,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_03():
    pitch_handler = consort.AbsolutePitchHandler(
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments=(
                "c' e' g'",
                "fs' gs'",
                "b",
                ),
            ratio=(1, 1, 1),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    fs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs'16
                                    \set stemLeftBeamCount = 2
                                    gs'16 ]
                                }
                                {
                                    b16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    b16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    b16
                                    \set stemLeftBeamCount = 2
                                    b16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_04():
    pitch_handler = consort.AbsolutePitchHandler(
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments=(
                "c' e' g'",
                "fs' gs'",
                "b",
                ),
            ratio=(3, 2, 1),
            ),
        pitch_operation_specifier=consort.PitchOperationSpecifier(
            pitch_operations=(
                pitchtools.PitchOperation(
                    pitchtools.Transposition(1),
                    ),
                None,
                pitchtools.PitchOperation(
                    pitchtools.Transposition(1),
                    ),
                ),
            ratio=(1, 2, 1),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=1,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    df'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    f'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs'16
                                    \set stemLeftBeamCount = 2
                                    gs'16 ]
                                }
                                {
                                    fs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_05():
    pitch_handler = consort.AbsolutePitchHandler(
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments=(
                "c' e' g'",
                "fs' gs'",
                "b",
                ),
            ratio=(3, 2, 1),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            v2=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    g'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs'16
                                    \set stemLeftBeamCount = 2
                                    fs'16 ]
                                }
                                {
                                    fs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    b16
                                    \set stemLeftBeamCount = 2
                                    b16 ]
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    e'16 ]
                                }
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gs'16
                                    \set stemLeftBeamCount = 2
                                    gs'16 ]
                                }
                                {
                                    gs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    b16
                                    \set stemLeftBeamCount = 2
                                    b16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_06():
    pitch_handler = consort.AbsolutePitchHandler(
        forbid_repetitions=True,
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments=(
                "c' e' g'",
                "fs' gs'",
                "b",
                ),
            ratio=(3, 2, 1),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            v2=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    g'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs'16
                                    \set stemLeftBeamCount = 2
                                    gs'16 ]
                                }
                                {
                                    fs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    b16
                                    \set stemLeftBeamCount = 2
                                    b16 ]
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    e'16 ]
                                }
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gs'16
                                    \set stemLeftBeamCount = 2
                                    fs'16 ]
                                }
                                {
                                    gs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    b16
                                    \set stemLeftBeamCount = 2
                                    b16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_07():
    pitch_handler = consort.AbsolutePitchHandler(
        forbid_repetitions=True,
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments=(
                "c' e' g'",
                "fs' gs'",
                "b",
                ),
            ratio=(3, 2, 1),
            ),
        pitch_operation_specifier=consort.PitchOperationSpecifier(
            pitch_operations=(
                None,
                pitchtools.PitchOperation(pitchtools.Transposition(1)),
                None,
                ),
            ratio=(1, 2, 1),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            v2=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    df'16 ]
                                }
                                {
                                    af'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    f'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    a'16 ]
                                }
                                {
                                    g'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    b16
                                    \set stemLeftBeamCount = 2
                                    b16 ]
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    f'16 ]
                                }
                                {
                                    df'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    \set stemLeftBeamCount = 2
                                    g'16 ]
                                }
                                {
                                    a'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    b16
                                    \set stemLeftBeamCount = 2
                                    b16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_08():
    pitch_handler = consort.AbsolutePitchHandler(
        forbid_repetitions=True,
        pitch_application_rate='division',
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments="c' e' g'",
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            v2=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    g'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    g'16 ]
                                }
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    e'16 ]
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    e'16 ]
                                }
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    g'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    g'16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_09():
    pitch_handler = consort.AbsolutePitchHandler(
        forbid_repetitions=True,
        pitch_application_rate='phrase',
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments="c' e' g'",
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            v2=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    e'16 ]
                                }
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    e'16 ]
                                }
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    e'16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')


def test_AbsolutePitchHandler_10():
    pitch_handler = consort.AbsolutePitchHandler(
        deviations=(0, 0.5, -0.5),
        forbid_repetitions=True,
        pitch_application_rate='division',
        pitch_specifier=consort.PitchSpecifier(
            pitch_segments="c' e' g'",
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(
            staff_count=2,
            ),
        settings=consort.MusicSetting(
            timespan_maker=consort.FloodedTimespanMaker(),
            v1=new(music_specifier, pitch_handler=pitch_handler),
            v2=new(music_specifier, pitch_handler=pitch_handler),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=((1, 4),),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.17"
        \language "english"

        \score {
            \context Score = "Grouped Rhythmic Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "TimeSignatureContext" {
                    {
                        \time 1/4
                        \tempo 4=60
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                    {
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                    \context RhythmicStaff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bqs16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    cqs'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    gqf'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gqs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    gqf'16 ]
                                }
                                {
                                    eqs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    eqf'16
                                    \set stemLeftBeamCount = 2
                                    eqs'16 ]
                                }
                            }
                        }
                    }
                    \context RhythmicStaff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                {
                                    eqs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    eqf'16
                                    \set stemLeftBeamCount = 2
                                    eqs'16 ]
                                }
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bqs16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    cqs'16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                {
                                    gqf'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gqs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    gqf'16 ]
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')