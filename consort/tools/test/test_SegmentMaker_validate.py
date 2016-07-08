import collections
import consort
from abjad.tools import indicatortools
from abjad.tools import systemtools


def test_SegmentMaker_validate_01():

    segment_metadata = collections.OrderedDict(
        segment_count=2,
        segment_number=1,
        )

    music_specifier = consort.MusicSpecifier(
        pitch_handler=consort.AbsolutePitchHandler(
            pitch_specifier=consort.PitchSpecifier(
                pitch_segments=['C2'],
                ),
            )
        )

    segment_maker = consort.SegmentMaker(
        desired_duration_in_seconds=4,
        omit_stylesheets=True,
        permitted_time_signatures=[(4, 4)],
        score_template=consort.StringQuartetScoreTemplate(split=False),
        tempo=indicatortools.Tempo((1, 4), 60),
        )

    segment_maker.add_setting(
        violin_1=music_specifier,
        violin_2=music_specifier,
        viola=music_specifier,
        cello=music_specifier,
        )

    lilypond_file, metadata = segment_maker(segment_metadata=segment_metadata)
    assert format(lilypond_file) == systemtools.TestManager.clean_string(
        r'''
        \version "2.19.44"
        \language "english"

        #(ly:set-option 'relative-includes #t)

        \score {
            \context Score = "String Quartet Score" <<
                \tag #'time
                \context TimeSignatureContext = "Time Signature Context" {
                    {
                        \tempo 4=60
                        \time 4/4
                        s1 * 1
                    }
                }
                \tag #'violin-1
                \context StringPerformerGroup = "Violin 1 Performer Group" \with {
                    instrumentName = \markup {
                        \hcenter-in
                            #10
                            "Violin 1"
                        }
                    shortInstrumentName = \markup {
                        \hcenter-in
                            #10
                            "Vln. 1"
                        }
                } <<
                    \context StringStaff = "Violin 1 Staff" {
                        \context Voice = "Violin 1 Voice" {
                            \clef "treble"
                            {
                                % [Violin 1 Voice] Measure 1
                                {
                                    \once \override NoteHead.color = #red
                                    c,1
                                }
                            }
                        }
                    }
                >>
                \tag #'violin-2
                \context StringPerformerGroup = "Violin 2 Performer Group" \with {
                    instrumentName = \markup {
                        \hcenter-in
                            #10
                            "Violin 2"
                        }
                    shortInstrumentName = \markup {
                        \hcenter-in
                            #10
                            "Vln. 2"
                        }
                } <<
                    \context StringStaff = "Violin 2 Staff" {
                        \context Voice = "Violin 2 Voice" {
                            \clef "treble"
                            {
                                % [Violin 2 Voice] Measure 1
                                {
                                    \once \override NoteHead.color = #red
                                    c,1
                                }
                            }
                        }
                    }
                >>
                \tag #'viola
                \context StringPerformerGroup = "Viola Performer Group" \with {
                    instrumentName = \markup {
                        \hcenter-in
                            #10
                            Viola
                        }
                    shortInstrumentName = \markup {
                        \hcenter-in
                            #10
                            Va.
                        }
                } <<
                    \context StringStaff = "Viola Staff" {
                        \context Voice = "Viola Voice" {
                            \clef "alto"
                            {
                                % [Viola Voice] Measure 1
                                {
                                    \once \override NoteHead.color = #red
                                    c,1
                                }
                            }
                        }
                    }
                >>
                \tag #'cello
                \context StringPerformerGroup = "Cello Performer Group" \with {
                    instrumentName = \markup {
                        \hcenter-in
                            #10
                            Cello
                        }
                    shortInstrumentName = \markup {
                        \hcenter-in
                            #10
                            Vc.
                        }
                } <<
                    \context StringStaff = "Cello Staff" {
                        \context Voice = "Cello Voice" {
                            \clef "bass"
                            {
                                % [Cello Voice] Measure 1
                                {
                                    c,1
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''')
