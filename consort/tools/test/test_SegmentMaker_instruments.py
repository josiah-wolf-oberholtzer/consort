# -*- encoding: utf -*-
from abjad.tools import indicatortools
from abjad.tools import rhythmmakertools
from abjad.tools import stringtools
from abjad.tools import templatetools
import consort


def test_SegmentMaker_instruments_01():
    segment_maker = consort.SegmentMaker(
        discard_final_silence=True,
        desired_duration_in_seconds=8,
        omit_stylesheets=True,
        score_template=templatetools.StringQuartetScoreTemplate(),
        settings=None,
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=[(4, 4)],
        )
    instrument = consort.Instrument(
        instrument_name_markup='Foo',
        short_instrument_name_markup='F.',
        instrument_change_markup='F!',
        )
    segment_maker.add_setting(
        timespan_identifier=[1, -1],
        vn1=consort.MusicSpecifier(
            instrument=instrument,
            rhythm_maker=rhythmmakertools.NoteRhythmMaker(),
            ),
        va=consort.MusicSpecifier(
            instrument=instrument,
            rhythm_maker=rhythmmakertools.NoteRhythmMaker(),
            ),
        )
    segment_maker.add_setting(
        timespan_identifier=[-1, 1],
        vn2=consort.MusicSpecifier(
            instrument=instrument,
            rhythm_maker=rhythmmakertools.NoteRhythmMaker(),
            ),
        va=consort.MusicSpecifier(
            instrument=instrument,
            rhythm_maker=rhythmmakertools.NoteRhythmMaker(),
            ),
        )
    lilypond_file, metadata = segment_maker(segment_metadata=None)
    assert format(lilypond_file) == stringtools.normalize(
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
                        s1 * 2
                    }
                }
                \context StaffGroup = "String Quartet Staff Group" <<
                    \tag #'first-violin
                    \context Staff = "First Violin Staff" {
                        \clef "treble"
                        \set Staff.instrumentName = \markup { Violin }
                        \set Staff.shortInstrumentName = \markup { Vn. }
                        \context Voice = "First Violin Voice" {
                            {
                                % [First Violin Voice] Measure 1
                                {
                                    \set Staff.instrumentName = \markup { Foo }
                                    \set Staff.shortInstrumentName = \markup { F. }
                                    c'1
                                }
                            }
                            {
                                % [First Violin Voice] Measure 2
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 1
                                    \bar "|."
                                }
                            }
                        }
                    }
                    \tag #'second-violin
                    \context Staff = "Second Violin Staff" {
                        \clef "treble"
                        \set Staff.instrumentName = \markup { Violin }
                        \set Staff.shortInstrumentName = \markup { Vn. }
                        \context Voice = "Second Violin Voice" {
                            {
                                % [Second Violin Voice] Measure 1
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 1
                                    \stopStaff
                                    \startStaff
                                }
                            }
                            {
                                % [Second Violin Voice] Measure 2
                                {
                                    \set Staff.instrumentName = \markup { Foo }
                                    \set Staff.shortInstrumentName = \markup { F. }
                                    c'1 ^ \markup { F! }
                                    \bar "|."
                                }
                            }
                        }
                    }
                    \tag #'viola
                    \context Staff = "Viola Staff" {
                        \clef "alto"
                        \set Staff.instrumentName = \markup { Viola }
                        \set Staff.shortInstrumentName = \markup { Va. }
                        \context Voice = "Viola Voice" {
                            {
                                % [Viola Voice] Measure 1
                                {
                                    \set Staff.instrumentName = \markup { Foo }
                                    \set Staff.shortInstrumentName = \markup { F. }
                                    c'1
                                }
                                % [Viola Voice] Measure 2
                                {
                                    c'1
                                    \bar "|."
                                }
                            }
                        }
                    }
                    \tag #'cello
                    \context Staff = "Cello Staff" {
                        \clef "bass"
                        \set Staff.instrumentName = \markup { Cello }
                        \set Staff.shortInstrumentName = \markup { Vc. }
                        \context Voice = "Cello Voice" {
                            {
                                % [Cello Voice] Measure 1
                                {
                                    \stopStaff
                                    \once \override Staff.StaffSymbol.line-positions = #'(0)
                                    \startStaff
                                    R1 * 2
                                    \bar "|."
                                }
                            }
                        }
                    }
                >>
            >>
        }
        ''',
        )
