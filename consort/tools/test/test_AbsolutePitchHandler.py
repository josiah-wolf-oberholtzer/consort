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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 1/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 3/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
                                % [Voice 1] Measure 2
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
                                % [Voice 1] Measure 3
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
                pitchtools.CompoundOperator(
                    pitchtools.Transposition(1),
                    ),
                None,
                pitchtools.CompoundOperator(
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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 3/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
                                % [Voice 1] Measure 2
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
                                % [Voice 1] Measure 3
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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 3/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
                                % [Voice 1] Measure 2
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
                                % [Voice 1] Measure 3
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
                    \context Staff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
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
                                % [Voice 2] Measure 2
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
                                % [Voice 2] Measure 3
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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 3/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
                                % [Voice 1] Measure 2
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
                                % [Voice 1] Measure 3
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
                    \context Staff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
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
                                % [Voice 2] Measure 2
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
                                % [Voice 2] Measure 3
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
                pitchtools.CompoundOperator(pitchtools.Transposition(1)),
                None,
                ),
            ratio=(1, 2, 1),
            ),
        )
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=3,
        omit_stylesheets=True,
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 3/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
                                % [Voice 1] Measure 2
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
                                % [Voice 1] Measure 3
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
                    \context Staff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
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
                                % [Voice 2] Measure 2
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
                                % [Voice 2] Measure 3
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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 3/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
                                % [Voice 1] Measure 2
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
                                % [Voice 1] Measure 3
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
                    \context Staff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
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
                                % [Voice 2] Measure 2
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
                                % [Voice 2] Measure 3
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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 3/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
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
                                % [Voice 1] Measure 2
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
                                % [Voice 1] Measure 3
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
                    \context Staff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
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
                                % [Voice 2] Measure 2
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
                                % [Voice 2] Measure 3
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
        score_template=templatetools.GroupedStavesScoreTemplate(
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
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "Grouped Staves Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 1/4
                        s1 * 3/4
                    }
                }
                \context StaffGroup = "Grouped Staves Staff Group" <<
                    \context Staff = "Staff 1" {
                        \context Voice = "Voice 1" {
                            {
                                % [Voice 1] Measure 1
                                {
                                    c'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    cqs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bqs16
                                    \set stemLeftBeamCount = 2
                                    c'16 ]
                                }
                                % [Voice 1] Measure 2
                                {
                                    gqs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gqf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    gqs'16 ]
                                }
                                % [Voice 1] Measure 3
                                {
                                    eqf'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    eqs'16
                                    \set stemLeftBeamCount = 2
                                    eqf'16 ]
                                }
                            }
                        }
                    }
                    \context Staff = "Staff 2" {
                        \context Voice = "Voice 2" {
                            {
                                % [Voice 2] Measure 1
                                {
                                    e'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    eqs'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    eqf'16
                                    \set stemLeftBeamCount = 2
                                    e'16 ]
                                }
                                % [Voice 2] Measure 2
                                {
                                    cqs'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bqs16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    \set stemLeftBeamCount = 2
                                    cqs'16 ]
                                }
                                % [Voice 2] Measure 3
                                {
                                    gqf'16 [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    gqs'16
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
