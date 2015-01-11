# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import instrumenttools
from abjad.tools import markuptools
from abjad.tools import scoretools
from consort.tools.ScoreTemplate import ScoreTemplate


class StringQuartetScoreTemplate(ScoreTemplate):
    r'''A string quartet score template.

    ::

        >>> import consort
        >>> template = consort.StringQuartetScoreTemplate()
        >>> score = template()
        >>> print(format(score))
        \context Score = "String Quartet Score" <<
            \tag #'time
            \context TimeSignatureContext = "TimeSignatureContext" {
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
                \context BowingStaff = "Violin 1 Bowing Staff" {
                    \clef "percussion"
                    \context Voice = "Violin 1 Bowing Voice" {
                    }
                }
                \context FingeringStaff = "Violin 1 Fingering Staff" {
                    \clef "treble"
                    \context Voice = "Violin 1 Fingering Voice" {
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
                \context BowingStaff = "Violin 2 Bowing Staff" {
                    \clef "percussion"
                    \context Voice = "Violin 2 Bowing Voice" {
                    }
                }
                \context FingeringStaff = "Violin 2 Fingering Staff" {
                    \clef "treble"
                    \context Voice = "Violin 2 Fingering Voice" {
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
                \context BowingStaff = "Viola Bowing Staff" {
                    \clef "percussion"
                    \context Voice = "Viola Bowing Voice" {
                    }
                }
                \context FingeringStaff = "Viola Fingering Staff" {
                    \clef "alto"
                    \context Voice = "Viola Fingering Voice" {
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
                \context BowingStaff = "Cello Bowing Staff" {
                    \clef "percussion"
                    \context Voice = "Cello Bowing Voice" {
                    }
                }
                \context FingeringStaff = "Cello Fingering Staff" {
                    \clef "bass"
                    \context Voice = "Cello Fingering Voice" {
                    }
                }
            >>
        >>

    ::

        >>> for item in template.context_name_abbreviations.items():
        ...     item
        ...
        ('violin_1', 'Violin 1 Performer Group')
        ('violin_1_rh', 'Violin 1 Bowing Voice')
        ('violin_1_lh', 'Violin 1 Fingering Voice')
        ('violin_2', 'Violin 2 Performer Group')
        ('violin_2_rh', 'Violin 2 Bowing Voice')
        ('violin_2_lh', 'Violin 2 Fingering Voice')
        ('viola', 'Viola Performer Group')
        ('viola_rh', 'Viola Bowing Voice')
        ('viola_lh', 'Viola Fingering Voice')
        ('cello', 'Cello Performer Group')
        ('cello_rh', 'Cello Bowing Voice')
        ('cello_lh', 'Cello Fingering Voice')

    ::

        >>> for item in template.composite_context_pairs.items():
        ...     item
        ...
        ('violin_1', ('violin_1_rh', 'violin_1_lh'))
        ('violin_2', ('violin_2_rh', 'violin_2_lh'))
        ('viola', ('viola_rh', 'viola_lh'))
        ('cello', ('cello_rh', 'cello_lh'))

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    def __call__(self):
        import consort

        manager = consort.ScoreTemplateManager

        time_signature_context = manager.make_time_signature_context()

        violin_one = manager.make_single_string_performer(
            clef=indicatortools.Clef('treble'),
            instrument=instrumenttools.Violin(
                instrument_name='violin 1',
                instrument_name_markup=markuptools.Markup(
                    'Violin 1').hcenter_in(10),
                short_instrument_name='vln. 1',
                short_instrument_name_markup=markuptools.Markup(
                    'Vln. 1').hcenter_in(10)
                ),
            split=True,
            score_template=self,
            )

        violin_two = manager.make_single_string_performer(
            clef=indicatortools.Clef('treble'),
            instrument=instrumenttools.Violin(
                instrument_name='violin 2',
                instrument_name_markup=markuptools.Markup(
                    'Violin 2').hcenter_in(10),
                short_instrument_name='vln. 2',
                short_instrument_name_markup=markuptools.Markup(
                    'Vln. 2').hcenter_in(10)
                ),
            split=True,
            score_template=self,
            )

        viola = manager.make_single_string_performer(
            clef=indicatortools.Clef('alto'),
            instrument=instrumenttools.Viola(
                instrument_name='viola',
                instrument_name_markup=markuptools.Markup(
                    'Viola').hcenter_in(10),
                short_instrument_name='va.',
                short_instrument_name_markup=markuptools.Markup(
                    'Va.').hcenter_in(10)
                ),
            split=True,
            score_template=self,
            )

        cello = manager.make_single_string_performer(
            clef=indicatortools.Clef('bass'),
            instrument=instrumenttools.Cello(
                instrument_name='cello',
                instrument_name_markup=markuptools.Markup(
                    'Cello').hcenter_in(10),
                short_instrument_name='vc.',
                short_instrument_name_markup=markuptools.Markup(
                    'Vc.').hcenter_in(10)
                ),
            split=True,
            score_template=self,
            )

        score = scoretools.Score(
            [
                time_signature_context,
                violin_one,
                violin_two,
                viola,
                cello,
                ],
            name='String Quartet Score',
            )

        return score