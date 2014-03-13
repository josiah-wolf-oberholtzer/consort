# -*- encoding: utf-8 -*-
from abjad import attach
from abjad.tools import abctools
from abjad.tools import indicatortools
from abjad.tools import instrumenttools
from abjad.tools import scoretools


class ConsortScoreTemplate(abctools.AbjadObject):
    r'''String orchestra score template.

    ::

        >>> from consort import makers
        >>> template = makers.ConsortScoreTemplate()
        >>> score = template()
        >>> print format(score)
        \context Score = "Score" <<
            \tag #'(Violin1 Violin2 Violin3 Violin4 Violin5 Violin6 Viola1 Viola2 Viola3 Viola4 Cello1 Cello2 Cello3 Contrabass1 Contrabass2)
            \context TimeSignatureContext = "TimeSignatureContext" {
            }
            \context ViolinStaffGroup = "Violin Staff Group" <<
                \tag #'Violin1
                \context PerformerStaffGroup = "Violin 1 Staff Group" <<
                    \context RHStaff = "Violin 1 RH Staff" {
                        \context RHVoice = "Violin 1 RH Voice" {
                        }
                    }
                    \context LHStaff = "Violin 1 LH Staff" {
                        \context LHVoice = "Violin 1 LH Voice" {
                        }
                    }
                    \context Dynamics = "Violin 1 Dynamics" {
                    }
                >>
                \tag #'Violin2
                \context PerformerStaffGroup = "Violin 2 Staff Group" <<
                    \context RHStaff = "Violin 2 RH Staff" {
                        \context RHVoice = "Violin 2 RH Voice" {
                        }
                    }
                    \context LHStaff = "Violin 2 LH Staff" {
                        \context LHVoice = "Violin 2 LH Voice" {
                        }
                    }
                    \context Dynamics = "Violin 2 Dynamics" {
                    }
                >>
                \tag #'Violin3
                \context PerformerStaffGroup = "Violin 3 Staff Group" <<
                    \context RHStaff = "Violin 3 RH Staff" {
                        \context RHVoice = "Violin 3 RH Voice" {
                        }
                    }
                    \context LHStaff = "Violin 3 LH Staff" {
                        \context LHVoice = "Violin 3 LH Voice" {
                        }
                    }
                    \context Dynamics = "Violin 3 Dynamics" {
                    }
                >>
                \tag #'Violin4
                \context PerformerStaffGroup = "Violin 4 Staff Group" <<
                    \context RHStaff = "Violin 4 RH Staff" {
                        \context RHVoice = "Violin 4 RH Voice" {
                        }
                    }
                    \context LHStaff = "Violin 4 LH Staff" {
                        \context LHVoice = "Violin 4 LH Voice" {
                        }
                    }
                    \context Dynamics = "Violin 4 Dynamics" {
                    }
                >>
                \tag #'Violin5
                \context PerformerStaffGroup = "Violin 5 Staff Group" <<
                    \context RHStaff = "Violin 5 RH Staff" {
                        \context RHVoice = "Violin 5 RH Voice" {
                        }
                    }
                    \context LHStaff = "Violin 5 LH Staff" {
                        \context LHVoice = "Violin 5 LH Voice" {
                        }
                    }
                    \context Dynamics = "Violin 5 Dynamics" {
                    }
                >>
                \tag #'Violin6
                \context PerformerStaffGroup = "Violin 6 Staff Group" <<
                    \context RHStaff = "Violin 6 RH Staff" {
                        \context RHVoice = "Violin 6 RH Voice" {
                        }
                    }
                    \context LHStaff = "Violin 6 LH Staff" {
                        \context LHVoice = "Violin 6 LH Voice" {
                        }
                    }
                    \context Dynamics = "Violin 6 Dynamics" {
                    }
                >>
            >>
            \context ViolaStaffGroup = "Viola Staff Group" <<
                \tag #'Viola1
                \context PerformerStaffGroup = "Viola 1 Staff Group" <<
                    \context RHStaff = "Viola 1 RH Staff" {
                        \context RHVoice = "Viola 1 RH Voice" {
                        }
                    }
                    \context LHStaff = "Viola 1 LH Staff" {
                        \context LHVoice = "Viola 1 LH Voice" {
                        }
                    }
                    \context Dynamics = "Viola 1 Dynamics" {
                    }
                >>
                \tag #'Viola2
                \context PerformerStaffGroup = "Viola 2 Staff Group" <<
                    \context RHStaff = "Viola 2 RH Staff" {
                        \context RHVoice = "Viola 2 RH Voice" {
                        }
                    }
                    \context LHStaff = "Viola 2 LH Staff" {
                        \context LHVoice = "Viola 2 LH Voice" {
                        }
                    }
                    \context Dynamics = "Viola 2 Dynamics" {
                    }
                >>
                \tag #'Viola3
                \context PerformerStaffGroup = "Viola 3 Staff Group" <<
                    \context RHStaff = "Viola 3 RH Staff" {
                        \context RHVoice = "Viola 3 RH Voice" {
                        }
                    }
                    \context LHStaff = "Viola 3 LH Staff" {
                        \context LHVoice = "Viola 3 LH Voice" {
                        }
                    }
                    \context Dynamics = "Viola 3 Dynamics" {
                    }
                >>
                \tag #'Viola4
                \context PerformerStaffGroup = "Viola 4 Staff Group" <<
                    \context RHStaff = "Viola 4 RH Staff" {
                        \context RHVoice = "Viola 4 RH Voice" {
                        }
                    }
                    \context LHStaff = "Viola 4 LH Staff" {
                        \context LHVoice = "Viola 4 LH Voice" {
                        }
                    }
                    \context Dynamics = "Viola 4 Dynamics" {
                    }
                >>
            >>
            \context CelloStaffGroup = "Cello Staff Group" <<
                \tag #'Cello1
                \context PerformerStaffGroup = "Cello 1 Staff Group" <<
                    \context RHStaff = "Cello 1 RH Staff" {
                        \context RHVoice = "Cello 1 RH Voice" {
                        }
                    }
                    \context LHStaff = "Cello 1 LH Staff" {
                        \context LHVoice = "Cello 1 LH Voice" {
                        }
                    }
                    \context Dynamics = "Cello 1 Dynamics" {
                    }
                >>
                \tag #'Cello2
                \context PerformerStaffGroup = "Cello 2 Staff Group" <<
                    \context RHStaff = "Cello 2 RH Staff" {
                        \context RHVoice = "Cello 2 RH Voice" {
                        }
                    }
                    \context LHStaff = "Cello 2 LH Staff" {
                        \context LHVoice = "Cello 2 LH Voice" {
                        }
                    }
                    \context Dynamics = "Cello 2 Dynamics" {
                    }
                >>
                \tag #'Cello3
                \context PerformerStaffGroup = "Cello 3 Staff Group" <<
                    \context RHStaff = "Cello 3 RH Staff" {
                        \context RHVoice = "Cello 3 RH Voice" {
                        }
                    }
                    \context LHStaff = "Cello 3 LH Staff" {
                        \context LHVoice = "Cello 3 LH Voice" {
                        }
                    }
                    \context Dynamics = "Cello 3 Dynamics" {
                    }
                >>
            >>
            \context ContrabassStaffGroup = "Contrabass Staff Group" <<
                \tag #'Contrabass1
                \context PerformerStaffGroup = "Contrabass 1 Staff Group" <<
                    \context RHStaff = "Contrabass 1 RH Staff" {
                        \context RHVoice = "Contrabass 1 RH Voice" {
                        }
                    }
                    \context LHStaff = "Contrabass 1 LH Staff" {
                        \context LHVoice = "Contrabass 1 LH Voice" {
                        }
                    }
                    \context Dynamics = "Contrabass 1 Dynamics" {
                    }
                >>
                \tag #'Contrabass2
                \context PerformerStaffGroup = "Contrabass 2 Staff Group" <<
                    \context RHStaff = "Contrabass 2 RH Staff" {
                        \context RHVoice = "Contrabass 2 RH Voice" {
                        }
                    }
                    \context LHStaff = "Contrabass 2 LH Staff" {
                        \context LHVoice = "Contrabass 2 LH Voice" {
                        }
                    }
                    \context Dynamics = "Contrabass 2 Dynamics" {
                    }
                >>
            >>
        >>

    As a string quartet:

    ::

        >>> template = makers.ConsortScoreTemplate(
        ...     violin_count=2,
        ...     viola_count=1,
        ...     cello_count=1,
        ...     contrabass_count=0,
        ...     )
        >>> score = template()
        >>> print format(score)
        \context Score = "Score" <<
            \tag #'(Violin1 Violin2 Viola Cello)
            \context TimeSignatureContext = "TimeSignatureContext" {
            }
            \context ViolinStaffGroup = "Violin Staff Group" <<
                \tag #'Violin1
                \context PerformerStaffGroup = "Violin 1 Staff Group" <<
                    \context RHStaff = "Violin 1 RH Staff" {
                        \context RHVoice = "Violin 1 RH Voice" {
                        }
                    }
                    \context LHStaff = "Violin 1 LH Staff" {
                        \context LHVoice = "Violin 1 LH Voice" {
                        }
                    }
                    \context Dynamics = "Violin 1 Dynamics" {
                    }
                >>
                \tag #'Violin2
                \context PerformerStaffGroup = "Violin 2 Staff Group" <<
                    \context RHStaff = "Violin 2 RH Staff" {
                        \context RHVoice = "Violin 2 RH Voice" {
                        }
                    }
                    \context LHStaff = "Violin 2 LH Staff" {
                        \context LHVoice = "Violin 2 LH Voice" {
                        }
                    }
                    \context Dynamics = "Violin 2 Dynamics" {
                    }
                >>
            >>
            \context ViolaStaffGroup = "Viola Staff Group" <<
                \tag #'Viola
                \context PerformerStaffGroup = "Viola Staff Group" <<
                    \context RHStaff = "Viola RH Staff" {
                        \context RHVoice = "Viola RH Voice" {
                        }
                    }
                    \context LHStaff = "Viola LH Staff" {
                        \context LHVoice = "Viola LH Voice" {
                        }
                    }
                    \context Dynamics = "Viola Dynamics" {
                    }
                >>
            >>
            \context CelloStaffGroup = "Cello Staff Group" <<
                \tag #'Cello
                \context PerformerStaffGroup = "Cello Staff Group" <<
                    \context RHStaff = "Cello RH Staff" {
                        \context RHVoice = "Cello RH Voice" {
                        }
                    }
                    \context LHStaff = "Cello LH Staff" {
                        \context LHVoice = "Cello LH Voice" {
                        }
                    }
                    \context Dynamics = "Cello Dynamics" {
                    }
                >>
            >>
        >>

    As a cello solo:

    ::

        >>> template = makers.ConsortScoreTemplate(
        ...     violin_count=0,
        ...     viola_count=0,
        ...     cello_count=1,
        ...     contrabass_count=0,
        ...     )
        >>> score = template()
        >>> print format(score)
        \context Score = "Score" <<
            \tag #'(Cello)
            \context TimeSignatureContext = "TimeSignatureContext" {
            }
            \context CelloStaffGroup = "Cello Staff Group" <<
                \tag #'Cello
                \context PerformerStaffGroup = "Cello Staff Group" <<
                    \context RHStaff = "Cello RH Staff" {
                        \context RHVoice = "Cello RH Voice" {
                        }
                    }
                    \context LHStaff = "Cello LH Staff" {
                        \context LHVoice = "Cello LH Voice" {
                        }
                    }
                    \context Dynamics = "Cello Dynamics" {
                    }
                >>
            >>
        >>

    '''

    ### INITIALIZER ###

    def __init__(
        self,
        violin_count=6,
        viola_count=4,
        cello_count=3,
        contrabass_count=2,
        ):
        assert 0 <= violin_count
        assert 0 <= viola_count
        assert 0 <= cello_count
        assert 0 <= contrabass_count
        self._violin_count = int(violin_count)
        self._viola_count = int(viola_count)
        self._cello_count = int(cello_count)
        self._contrabass_count = int(contrabass_count)

    ### PRIVATE METHODS ###

    def _make_instrument_staff_group(
        self,
        count=None,
        instrument=None,
        ):
        instrument_name = instrument.instrument_name.title()
        instrument_staff_group = scoretools.StaffGroup(
            context_name='{}StaffGroup'.format(instrument_name),
            name='{} Staff Group'.format(instrument_name),
            )
        tag_names = []
        if count == 1:
            performer_staff_group, tag_name = \
                self._make_performer_staff_group(instrument, None)
            instrument_staff_group.append(performer_staff_group)
            tag_names.append(tag_name)
        else:
            for i in range(1, count + 1):
                performer_staff_group, tag_name = \
                    self._make_performer_staff_group(instrument, i)
                instrument_staff_group.append(performer_staff_group)
                tag_names.append(tag_name)
        return instrument_staff_group, tag_names

    def _make_performer_staff_group(
        self,
        instrument=None,
        number=None,
        ):
        if number is not None:
            name = '{} {}'.format(
                instrument.instrument_name.title(),
                number,
                )
        else:
            name = instrument.instrument_name.title()
        pitch_range = instrument.pitch_range

        lh_voice = scoretools.Voice(
            context_name='LHVoice',
            name='{} LH Voice'.format(name),
            )
        lh_staff = scoretools.Staff(
            [
                lh_voice
                ],
            context_name='LHStaff',
            name='{} LH Staff'.format(name),
            )
        attach(pitch_range, lh_staff)

        rh_voice = scoretools.Voice(
            context_name='RHVoice',
            name='{} RH Voice'.format(name),
            )
        rh_staff = scoretools.Staff(
            [
                rh_voice
                ],
            context_name='RHStaff',
            name='{} RH Staff'.format(name),
            )
        dynamics = scoretools.Voice(
            context_name='Dynamics',
            name='{} Dynamics'.format(name),
            )

        staff_group = scoretools.StaffGroup(
            [
                rh_staff,
                lh_staff,
                dynamics,
                ],
            context_name='PerformerStaffGroup',
            name='{} Staff Group'.format(name),
            )

        tag_name = name.replace(' ', '')
        tag_string = "tag #'{}".format(tag_name)
        tag_command = indicatortools.LilyPondCommand(
            tag_string,
            'before',
            )
        attach(tag_command, staff_group)

        return staff_group, tag_name

    ### SPECIAL METHODS ###

    def __call__(self):
        r'''Calls string orchestra template.

        Returns score.
        '''

        ### TAGS ###

        tag_names = []

        ### SCORE ###

        score = scoretools.Score(
            name='Score',
            )

        ### VIOLINS ###

        if self.violin_count:
            instrument = instrumenttools.Violin()
            instrument_count = self.violin_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    count=instrument_count,
                    instrument=instrument,
                    )
            score.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### VIOLAS ###

        if self.viola_count:
            instrument = instrumenttools.Viola()
            instrument_count = self.viola_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    count=instrument_count,
                    instrument=instrument,
                    )
            score.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### CELLOS ###

        if self.cello_count:
            instrument = instrumenttools.Cello()
            instrument_count = self.cello_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    count=instrument_count,
                    instrument=instrument,
                    )
            score.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### BASSES ###

        if self.contrabass_count:
            instrument = instrumenttools.Contrabass()
            instrument_count = self.contrabass_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    count=instrument_count,
                    instrument=instrument,
                    )
            score.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### TIME SIGNATURE CONTEXT ###

        time_signature_context = scoretools.Context(
            name='TimeSignatureContext',
            context_name='TimeSignatureContext',
            )
        instrument_tags = ' '.join(tag_names)
        tag_string = "tag #'({})".format(instrument_tags)
        tag_command = indicatortools.LilyPondCommand(tag_string, 'before')
        attach(tag_command, time_signature_context)

        score.insert(0, time_signature_context)

        return score

    ### PUBLIC PROPERTIES ###

    @property
    def cello_count(self):
        r'''Number of cellos in string orchestra.

        Returns nonnegative integer.
        '''
        return self._cello_count

    @property
    def contrabass_count(self):
        r'''Number of contrabasses in string orchestra.

        Returns nonnegative integer.
        '''
        return self._contrabass_count

    @property
    def viola_count(self):
        r'''Number of violas in string orcestra.

        Returns nonnegative integer.
        '''
        return self._viola_count

    @property
    def violin_count(self):
        r'''Number of violins in string orchestra.

        Returns nonnegative integer.
        '''
        return self._violin_count
