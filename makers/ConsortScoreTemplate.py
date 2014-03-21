# -*- encoding: utf-8 -*-
from abjad import attach
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import indicatortools
from abjad.tools import instrumenttools
from abjad.tools import scoretools


class ConsortScoreTemplate(ConsortObject):
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
            \context OuterStaffGroup = "Outer Staff Group" <<
                \context ViolinStaffGroup = "Violin Staff Group" <<
                    \tag #'Violin1
                    \context PerformerStaffGroup = "Violin 1 Staff Group" <<
                        \context RHStaff = "Violin 1 RH Staff" {
                            \context RHVoice = "Violin 1 RH Voice" {
                            }
                        }
                        \context LHStaff = "Violin 1 LH Staff" {
                            \clef "treble"
                            \context LHVoice = "Violin 1 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Violin2
                    \context PerformerStaffGroup = "Violin 2 Staff Group" <<
                        \context RHStaff = "Violin 2 RH Staff" {
                            \context RHVoice = "Violin 2 RH Voice" {
                            }
                        }
                        \context LHStaff = "Violin 2 LH Staff" {
                            \clef "treble"
                            \context LHVoice = "Violin 2 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Violin3
                    \context PerformerStaffGroup = "Violin 3 Staff Group" <<
                        \context RHStaff = "Violin 3 RH Staff" {
                            \context RHVoice = "Violin 3 RH Voice" {
                            }
                        }
                        \context LHStaff = "Violin 3 LH Staff" {
                            \clef "treble"
                            \context LHVoice = "Violin 3 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Violin4
                    \context PerformerStaffGroup = "Violin 4 Staff Group" <<
                        \context RHStaff = "Violin 4 RH Staff" {
                            \context RHVoice = "Violin 4 RH Voice" {
                            }
                        }
                        \context LHStaff = "Violin 4 LH Staff" {
                            \clef "treble"
                            \context LHVoice = "Violin 4 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Violin5
                    \context PerformerStaffGroup = "Violin 5 Staff Group" <<
                        \context RHStaff = "Violin 5 RH Staff" {
                            \context RHVoice = "Violin 5 RH Voice" {
                            }
                        }
                        \context LHStaff = "Violin 5 LH Staff" {
                            \clef "treble"
                            \context LHVoice = "Violin 5 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Violin6
                    \context PerformerStaffGroup = "Violin 6 Staff Group" <<
                        \context RHStaff = "Violin 6 RH Staff" {
                            \context RHVoice = "Violin 6 RH Voice" {
                            }
                        }
                        \context LHStaff = "Violin 6 LH Staff" {
                            \clef "treble"
                            \context LHVoice = "Violin 6 LH Voice" {
                            }
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
                            \clef "alto"
                            \context LHVoice = "Viola 1 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Viola2
                    \context PerformerStaffGroup = "Viola 2 Staff Group" <<
                        \context RHStaff = "Viola 2 RH Staff" {
                            \context RHVoice = "Viola 2 RH Voice" {
                            }
                        }
                        \context LHStaff = "Viola 2 LH Staff" {
                            \clef "alto"
                            \context LHVoice = "Viola 2 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Viola3
                    \context PerformerStaffGroup = "Viola 3 Staff Group" <<
                        \context RHStaff = "Viola 3 RH Staff" {
                            \context RHVoice = "Viola 3 RH Voice" {
                            }
                        }
                        \context LHStaff = "Viola 3 LH Staff" {
                            \clef "alto"
                            \context LHVoice = "Viola 3 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Viola4
                    \context PerformerStaffGroup = "Viola 4 Staff Group" <<
                        \context RHStaff = "Viola 4 RH Staff" {
                            \context RHVoice = "Viola 4 RH Voice" {
                            }
                        }
                        \context LHStaff = "Viola 4 LH Staff" {
                            \clef "alto"
                            \context LHVoice = "Viola 4 LH Voice" {
                            }
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
                            \clef "bass"
                            \context LHVoice = "Cello 1 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Cello2
                    \context PerformerStaffGroup = "Cello 2 Staff Group" <<
                        \context RHStaff = "Cello 2 RH Staff" {
                            \context RHVoice = "Cello 2 RH Voice" {
                            }
                        }
                        \context LHStaff = "Cello 2 LH Staff" {
                            \clef "bass"
                            \context LHVoice = "Cello 2 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Cello3
                    \context PerformerStaffGroup = "Cello 3 Staff Group" <<
                        \context RHStaff = "Cello 3 RH Staff" {
                            \context RHVoice = "Cello 3 RH Voice" {
                            }
                        }
                        \context LHStaff = "Cello 3 LH Staff" {
                            \clef "bass"
                            \context LHVoice = "Cello 3 LH Voice" {
                            }
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
                            \clef "bass_8"
                            \context LHVoice = "Contrabass 1 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Contrabass2
                    \context PerformerStaffGroup = "Contrabass 2 Staff Group" <<
                        \context RHStaff = "Contrabass 2 RH Staff" {
                            \context RHVoice = "Contrabass 2 RH Voice" {
                            }
                        }
                        \context LHStaff = "Contrabass 2 LH Staff" {
                            \clef "bass_8"
                            \context LHVoice = "Contrabass 2 LH Voice" {
                            }
                        }
                    >>
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
            \context OuterStaffGroup = "Outer Staff Group" <<
                \context ViolinStaffGroup = "Violin Staff Group" <<
                    \tag #'Violin1
                    \context PerformerStaffGroup = "Violin 1 Staff Group" <<
                        \context RHStaff = "Violin 1 RH Staff" {
                            \context RHVoice = "Violin 1 RH Voice" {
                            }
                        }
                        \context LHStaff = "Violin 1 LH Staff" {
                            \clef "treble"
                            \context LHVoice = "Violin 1 LH Voice" {
                            }
                        }
                    >>
                    \tag #'Violin2
                    \context PerformerStaffGroup = "Violin 2 Staff Group" <<
                        \context RHStaff = "Violin 2 RH Staff" {
                            \context RHVoice = "Violin 2 RH Voice" {
                            }
                        }
                        \context LHStaff = "Violin 2 LH Staff" {
                            \clef "treble"
                            \context LHVoice = "Violin 2 LH Voice" {
                            }
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
                            \clef "alto"
                            \context LHVoice = "Viola LH Voice" {
                            }
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
                            \clef "bass"
                            \context LHVoice = "Cello LH Voice" {
                            }
                        }
                    >>
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
            \context OuterStaffGroup = "Outer Staff Group" <<
                \context CelloStaffGroup = "Cello Staff Group" <<
                    \tag #'Cello
                    \context PerformerStaffGroup = "Cello Staff Group" <<
                        \context RHStaff = "Cello RH Staff" {
                            \context RHVoice = "Cello RH Voice" {
                            }
                        }
                        \context LHStaff = "Cello LH Staff" {
                            \clef "bass"
                            \context LHVoice = "Cello LH Voice" {
                            }
                        }
                    >>
                >>
            >>
        >>

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_violin_count',
        '_viola_count',
        '_cello_count',
        '_contrabass_count',
        '_split_hands',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        violin_count=6,
        viola_count=4,
        cello_count=3,
        contrabass_count=2,
        split_hands=True,
        ):
        assert 0 <= violin_count
        assert 0 <= viola_count
        assert 0 <= cello_count
        assert 0 <= contrabass_count
        self._violin_count = int(violin_count)
        self._viola_count = int(viola_count)
        self._cello_count = int(cello_count)
        self._contrabass_count = int(contrabass_count)
        self._split_hands = bool(split_hands)

    ### PRIVATE METHODS ###

    def _make_instrument_staff_group(
        self,
        clef_name=None,
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
                self._make_performer_staff_group(
                    clef_name=clef_name,
                    instrument=instrument,
                    number=None,
                    )
            instrument_staff_group.append(performer_staff_group)
            tag_names.append(tag_name)
        else:
            for i in range(1, count + 1):
                performer_staff_group, tag_name = \
                    self._make_performer_staff_group(
                        clef_name=clef_name,
                        instrument=instrument,
                        number=i,
                        )
                instrument_staff_group.append(performer_staff_group)
                tag_names.append(tag_name)
        return instrument_staff_group, tag_names

    def _make_performer_staff_group(
        self,
        clef_name=None,
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
        staff_group = scoretools.StaffGroup(
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
        if self.split_hands:
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
            attach(indicatortools.Clef(clef_name), lh_staff)
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
            staff_group.extend([rh_staff, lh_staff])
        else:
            lh_voice = scoretools.Voice(
                context_name='LHVoice',
                name='{} Voice'.format(name),
                )
            lh_staff = scoretools.Staff(
                [
                    lh_voice
                    ],
                context_name='LHStaff',
                name='{} Staff'.format(name),
                )
            attach(pitch_range, lh_staff)
            attach(indicatortools.Clef(clef_name), lh_staff)
            staff_group.append(lh_staff)
        return staff_group, tag_name

    ### SPECIAL METHODS ###

    def __call__(self):
        r'''Calls string orchestra template.

        Returns score.
        '''

        ### TAGS ###

        tag_names = []

        ### SCORE ###

        staff_group = scoretools.StaffGroup(
            context_name='OuterStaffGroup',
            name='Outer Staff Group',
            )

        score = scoretools.Score(
            [staff_group],
            name='Score',
            )

        ### VIOLINS ###

        if self.violin_count:
            instrument = instrumenttools.Violin()
            instrument_count = self.violin_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    clef_name='treble',
                    count=instrument_count,
                    instrument=instrument,
                    )
            staff_group.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### VIOLAS ###

        if self.viola_count:
            instrument = instrumenttools.Viola()
            instrument_count = self.viola_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    clef_name='alto',
                    count=instrument_count,
                    instrument=instrument,
                    )
            staff_group.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### CELLOS ###

        if self.cello_count:
            instrument = instrumenttools.Cello()
            instrument_count = self.cello_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    clef_name='bass',
                    count=instrument_count,
                    instrument=instrument,
                    )
            staff_group.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### BASSES ###

        if self.contrabass_count:
            instrument = instrumenttools.Contrabass()
            instrument_count = self.contrabass_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    clef_name='bass_8',
                    count=instrument_count,
                    instrument=instrument,
                    )
            staff_group.append(instrument_staff_group)
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
    def split_hands(self):
        r'''Is true if each hands receives a separate staff.
        '''
        return self._split_hands

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
