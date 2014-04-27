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
        >>> print(format(score))
        \context Score = "Score" <<
            \tag #'(Violin1 Violin2 Violin3 Violin4 Violin5 Violin6 Viola1 Viola2 Viola3 Viola4 Cello1 Cello2 Cello3 Contrabass1 Contrabass2)
            \context TimeSignatureContext = "TimeSignatureContext" {
            }
            \context StaffGroup = "Outer Staff Group" <<
                \context ViolinStaffGroup = "Violin Staff Group" <<
                    \tag #'Violin1
                    \context StringPerformerStaffGroup = "Violin 1 Staff Group" <<
                        \context StringBowingStaff = "Violin 1 StringBowing Staff" <<
                            \context StringBowingVoice = "Violin 1 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Violin 1 StringFingering Staff" <<
                            \clef "treble"
                            \context StringFingeringVoice = "Violin 1 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Violin2
                    \context StringPerformerStaffGroup = "Violin 2 Staff Group" <<
                        \context StringBowingStaff = "Violin 2 StringBowing Staff" <<
                            \context StringBowingVoice = "Violin 2 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Violin 2 StringFingering Staff" <<
                            \clef "treble"
                            \context StringFingeringVoice = "Violin 2 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Violin3
                    \context StringPerformerStaffGroup = "Violin 3 Staff Group" <<
                        \context StringBowingStaff = "Violin 3 StringBowing Staff" <<
                            \context StringBowingVoice = "Violin 3 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Violin 3 StringFingering Staff" <<
                            \clef "treble"
                            \context StringFingeringVoice = "Violin 3 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Violin4
                    \context StringPerformerStaffGroup = "Violin 4 Staff Group" <<
                        \context StringBowingStaff = "Violin 4 StringBowing Staff" <<
                            \context StringBowingVoice = "Violin 4 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Violin 4 StringFingering Staff" <<
                            \clef "treble"
                            \context StringFingeringVoice = "Violin 4 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Violin5
                    \context StringPerformerStaffGroup = "Violin 5 Staff Group" <<
                        \context StringBowingStaff = "Violin 5 StringBowing Staff" <<
                            \context StringBowingVoice = "Violin 5 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Violin 5 StringFingering Staff" <<
                            \clef "treble"
                            \context StringFingeringVoice = "Violin 5 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Violin6
                    \context StringPerformerStaffGroup = "Violin 6 Staff Group" <<
                        \context StringBowingStaff = "Violin 6 StringBowing Staff" <<
                            \context StringBowingVoice = "Violin 6 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Violin 6 StringFingering Staff" <<
                            \clef "treble"
                            \context StringFingeringVoice = "Violin 6 StringFingering Voice" {
                            }
                        >>
                    >>
                >>
                \context ViolaStaffGroup = "Viola Staff Group" <<
                    \tag #'Viola1
                    \context StringPerformerStaffGroup = "Viola 1 Staff Group" <<
                        \context StringBowingStaff = "Viola 1 StringBowing Staff" <<
                            \context StringBowingVoice = "Viola 1 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Viola 1 StringFingering Staff" <<
                            \clef "alto"
                            \context StringFingeringVoice = "Viola 1 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Viola2
                    \context StringPerformerStaffGroup = "Viola 2 Staff Group" <<
                        \context StringBowingStaff = "Viola 2 StringBowing Staff" <<
                            \context StringBowingVoice = "Viola 2 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Viola 2 StringFingering Staff" <<
                            \clef "alto"
                            \context StringFingeringVoice = "Viola 2 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Viola3
                    \context StringPerformerStaffGroup = "Viola 3 Staff Group" <<
                        \context StringBowingStaff = "Viola 3 StringBowing Staff" <<
                            \context StringBowingVoice = "Viola 3 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Viola 3 StringFingering Staff" <<
                            \clef "alto"
                            \context StringFingeringVoice = "Viola 3 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Viola4
                    \context StringPerformerStaffGroup = "Viola 4 Staff Group" <<
                        \context StringBowingStaff = "Viola 4 StringBowing Staff" <<
                            \context StringBowingVoice = "Viola 4 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Viola 4 StringFingering Staff" <<
                            \clef "alto"
                            \context StringFingeringVoice = "Viola 4 StringFingering Voice" {
                            }
                        >>
                    >>
                >>
                \context CelloStaffGroup = "Cello Staff Group" <<
                    \tag #'Cello1
                    \context StringPerformerStaffGroup = "Cello 1 Staff Group" <<
                        \context StringBowingStaff = "Cello 1 StringBowing Staff" <<
                            \context StringBowingVoice = "Cello 1 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Cello 1 StringFingering Staff" <<
                            \clef "bass"
                            \context StringFingeringVoice = "Cello 1 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Cello2
                    \context StringPerformerStaffGroup = "Cello 2 Staff Group" <<
                        \context StringBowingStaff = "Cello 2 StringBowing Staff" <<
                            \context StringBowingVoice = "Cello 2 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Cello 2 StringFingering Staff" <<
                            \clef "bass"
                            \context StringFingeringVoice = "Cello 2 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Cello3
                    \context StringPerformerStaffGroup = "Cello 3 Staff Group" <<
                        \context StringBowingStaff = "Cello 3 StringBowing Staff" <<
                            \context StringBowingVoice = "Cello 3 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Cello 3 StringFingering Staff" <<
                            \clef "bass"
                            \context StringFingeringVoice = "Cello 3 StringFingering Voice" {
                            }
                        >>
                    >>
                >>
                \context ContrabassStaffGroup = "Contrabass Staff Group" <<
                    \tag #'Contrabass1
                    \context StringPerformerStaffGroup = "Contrabass 1 Staff Group" <<
                        \context StringBowingStaff = "Contrabass 1 StringBowing Staff" <<
                            \context StringBowingVoice = "Contrabass 1 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Contrabass 1 StringFingering Staff" <<
                            \clef "bass_8"
                            \context StringFingeringVoice = "Contrabass 1 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Contrabass2
                    \context StringPerformerStaffGroup = "Contrabass 2 Staff Group" <<
                        \context StringBowingStaff = "Contrabass 2 StringBowing Staff" <<
                            \context StringBowingVoice = "Contrabass 2 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Contrabass 2 StringFingering Staff" <<
                            \clef "bass_8"
                            \context StringFingeringVoice = "Contrabass 2 StringFingering Voice" {
                            }
                        >>
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
        >>> print(format(score))
        \context Score = "Score" <<
            \tag #'(Violin1 Violin2 Viola Cello)
            \context TimeSignatureContext = "TimeSignatureContext" {
            }
            \context StaffGroup = "Outer Staff Group" <<
                \context ViolinStaffGroup = "Violin Staff Group" <<
                    \tag #'Violin1
                    \context StringPerformerStaffGroup = "Violin 1 Staff Group" <<
                        \context StringBowingStaff = "Violin 1 StringBowing Staff" <<
                            \context StringBowingVoice = "Violin 1 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Violin 1 StringFingering Staff" <<
                            \clef "treble"
                            \context StringFingeringVoice = "Violin 1 StringFingering Voice" {
                            }
                        >>
                    >>
                    \tag #'Violin2
                    \context StringPerformerStaffGroup = "Violin 2 Staff Group" <<
                        \context StringBowingStaff = "Violin 2 StringBowing Staff" <<
                            \context StringBowingVoice = "Violin 2 StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Violin 2 StringFingering Staff" <<
                            \clef "treble"
                            \context StringFingeringVoice = "Violin 2 StringFingering Voice" {
                            }
                        >>
                    >>
                >>
                \context ViolaStaffGroup = "Viola Staff Group" <<
                    \tag #'Viola
                    \context StringPerformerStaffGroup = "Viola Staff Group" <<
                        \context StringBowingStaff = "Viola StringBowing Staff" <<
                            \context StringBowingVoice = "Viola StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Viola StringFingering Staff" <<
                            \clef "alto"
                            \context StringFingeringVoice = "Viola StringFingering Voice" {
                            }
                        >>
                    >>
                >>
                \context CelloStaffGroup = "Cello Staff Group" <<
                    \tag #'Cello
                    \context StringPerformerStaffGroup = "Cello Staff Group" <<
                        \context StringBowingStaff = "Cello StringBowing Staff" <<
                            \context StringBowingVoice = "Cello StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Cello StringFingering Staff" <<
                            \clef "bass"
                            \context StringFingeringVoice = "Cello StringFingering Voice" {
                            }
                        >>
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
        >>> print(format(score))
        \context Score = "Score" <<
            \tag #'(Cello)
            \context TimeSignatureContext = "TimeSignatureContext" {
            }
            \context StaffGroup = "Outer Staff Group" <<
                \context CelloStaffGroup = "Cello Staff Group" <<
                    \tag #'Cello
                    \context StringPerformerStaffGroup = "Cello Staff Group" <<
                        \context StringBowingStaff = "Cello StringBowing Staff" <<
                            \context StringBowingVoice = "Cello StringBowing Voice" {
                            }
                        >>
                        \context StringFingeringStaff = "Cello StringFingering Staff" <<
                            \clef "bass"
                            \context StringFingeringVoice = "Cello StringFingering Voice" {
                            }
                        >>
                    >>
                >>
            >>
        >>

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_cello_count',
        '_contrabass_count',
        '_split_hands',
        '_use_percussion_clefs',
        '_viola_count',
        '_violin_count',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        violin_count=6,
        viola_count=4,
        cello_count=3,
        contrabass_count=2,
        split_hands=True,
        use_percussion_clefs=False,
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
        self._use_percussion_clefs = bool(use_percussion_clefs)

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
            context_name='StringPerformerStaffGroup',
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
                context_name='StringFingeringVoice',
                name='{} StringFingering Voice'.format(name),
                )
            lh_staff = scoretools.Staff(
                [
                    lh_voice
                    ],
                context_name='StringFingeringStaff',
                name='{} StringFingering Staff'.format(name),
                )
            lh_staff.is_simultaneous = True
            attach(pitch_range, lh_staff)
            attach(indicatortools.Clef(clef_name), lh_staff)
            rh_voice = scoretools.Voice(
                context_name='StringBowingVoice',
                name='{} StringBowing Voice'.format(name),
                )
            rh_staff = scoretools.Staff(
                [
                    rh_voice
                    ],
                context_name='StringBowingStaff',
                name='{} StringBowing Staff'.format(name),
                )
            rh_staff.is_simultaneous = True
            staff_group.extend([rh_staff, lh_staff])
        else:
            lh_voice = scoretools.Voice(
                context_name='StringFingeringVoice',
                name='{} Voice'.format(name),
                )
            lh_staff = scoretools.Staff(
                [
                    lh_voice
                    ],
                context_name='StringFingeringStaff',
                name='{} Staff'.format(name),
                )
            lh_staff.is_simultaneous = True
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
            name='Outer Staff Group',
            )

        score = scoretools.Score(
            [staff_group],
            name='Score',
            )

        ### VIOLINS ###

        if self.violin_count:
            clef_name = 'treble'
            if self.use_percussion_clefs:
                clef_name = 'percussion'
            instrument = instrumenttools.Violin()
            instrument_count = self.violin_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    clef_name=clef_name,
                    count=instrument_count,
                    instrument=instrument,
                    )
            staff_group.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### VIOLAS ###

        if self.viola_count:
            clef_name = 'alto'
            if self.use_percussion_clefs:
                clef_name = 'percussion'
            instrument = instrumenttools.Viola()
            instrument_count = self.viola_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    clef_name=clef_name,
                    count=instrument_count,
                    instrument=instrument,
                    )
            staff_group.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### CELLOS ###

        if self.cello_count:
            clef_name = 'bass'
            if self.use_percussion_clefs:
                clef_name = 'percussion'
            instrument = instrumenttools.Cello()
            instrument_count = self.cello_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    clef_name=clef_name,
                    count=instrument_count,
                    instrument=instrument,
                    )
            staff_group.append(instrument_staff_group)
            tag_names.extend(instrument_tag_names)

        ### BASSES ###

        if self.contrabass_count:
            clef_name = 'bass_8'
            if self.use_percussion_clefs:
                clef_name = 'percussion'
            instrument = instrumenttools.Contrabass()
            instrument_count = self.contrabass_count
            instrument_staff_group, instrument_tag_names = \
                self._make_instrument_staff_group(
                    clef_name=clef_name,
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
    def use_percussion_clefs(self):
        r'''Is true if each staff should use a percussion clef rather than the
        normal clef for that instrument.
        '''
        return self._use_percussion_clefs

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
