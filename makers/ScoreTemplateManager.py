# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import indicatortools
from abjad.tools import scoretools
from abjad.tools import stringtools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import set_


class ScoreTemplateManager(abctools.AbjadObject):

    ### PUBLIC METHODS ###

    @staticmethod
    def make_staff_name(name):
        name = ''.join(x for x in name if x.isalpha())
        name = '{}Staff'.format(name)
        return name

    @staticmethod
    def make_ensemble_group(
        name,
        performer_groups,
        ):
        staff_group = scoretools.StaffGroup(
            performer_groups,
            name=name,
            context_name='EnsembleGroup',
            )
        return staff_group

    @staticmethod
    def make_performer_group(
        context_name=None,
        instrument=None,
        label=None,
        ):
        context_name = context_name or 'PerformerGroup'
        name = '{} Performer Group'.format(instrument.instrument_name.title())
        performer_group = scoretools.StaffGroup(
            context_name=context_name,
            name=name,
            )
        performer_group.is_simultaneous = True
        label = label or instrument.instrument_name.replace(' ', '-').lower()
        ScoreTemplateManager.attach_tag(label, performer_group)
        attach(
            instrument,
            performer_group,
            scope=context_name,
            is_annotation=True,
            )
        manager = set_(performer_group)
        manager.instrument_name = instrument.instrument_name_markup
        manager.short_instrument_name = instrument.short_instrument_name_markup
        return performer_group

    @staticmethod
    def make_single_basic_performer(
        context_name=None,
        instrument=None,
        label=None,
        ):
        performer_group = ScoreTemplateManager.make_performer_group(
            context_name=context_name,
            instrument=instrument,
            label=label,
            )
        name = instrument.instrument_name.title()
        context_name = ScoreTemplateManager.make_staff_name(name)
        staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Voice'.format(name),
                    ),
                ],
            context_name=context_name,
            name='{} Staff'.format(name),
            )
        performer_group.append(staff)
        return performer_group

    @staticmethod
    def make_single_piano_performer(instrument):
        performer_group = ScoreTemplateManager.make_performer_group(
            context_name='PianoStaff',
            instrument=instrument,
            )
        name = instrument.instrument_name.title()
        upper_staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Upper Voice'.format(name),
                    ),
                ],
            context_name='PianoUpperStaff',
            name='{} Upper Staff'.format(name),
            )
        dynamics = scoretools.Voice(
            context_name='Dynamics',
            name='{} Dynamics'.format(name),
            )
        lower_staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Lower Voice'.format(name),
                    ),
                ],
            context_name='PianoLowerStaff',
            name='{} Lower Staff'.format(name),
            )
        pedals = scoretools.Voice(
            context_name='Dynamics',
            name='{} Pedals'.format(name),
            )
        performer_group.extend((
            upper_staff,
            dynamics,
            lower_staff,
            pedals,
            ))
        return performer_group

    @staticmethod
    def make_single_string_performer(
        clef=None,
        instrument=None,
        score_template=None,
        split=True,
        ):
        performer_group = ScoreTemplateManager.make_performer_group(
            context_name='StringPerformerGroup',
            instrument=instrument,
            )
        name = instrument.instrument_name.title()
        abbreviation = stringtools.to_accent_free_snake_case(name)
        if split:
            right_hand_voice = scoretools.Voice(
                name='{} Bowing Voice'.format(name),
                )
            right_hand_staff = scoretools.Staff(
                [right_hand_voice],
                context_name='BowingStaff',
                name='{} Bowing Staff'.format(name),
                )
            left_hand_voice = scoretools.Voice(
                name='{} Fingering Voice'.format(name),
                )
            left_hand_staff = scoretools.Staff(
                [left_hand_voice],
                context_name='FingeringStaff',
                name='{} Fingering Staff'.format(name),
                )
            performer_group.append(right_hand_staff)
            performer_group.append(left_hand_staff)
            attach(clef, left_hand_voice)
            right_hand_abbreviation = '{}_rh'.format(abbreviation)
            left_hand_abbreviation = '{}_lh'.format(abbreviation)
            score_template._voice_name_abbreviations[
                right_hand_abbreviation] = right_hand_voice.name
            score_template._voice_name_abbreviations[
                left_hand_abbreviation] = left_hand_voice.name
        else:
            voice = scoretools.Voice(
                name='{} Voice'.format(name),
                )
            staff = scoretools.Staff(
                [voice],
                context_name='StringStaff',
                name='{} Staff'.format(name),
                )
            performer_group.append(staff)
            attach(clef, voice)
            score_template._voice_name_abbreviations[abbreviation] = voice.name
        return performer_group

    @staticmethod
    def make_single_wind_performer(
        clef=None,
        instrument=None,
        score_template=None,
        ):
        performer_group = ScoreTemplateManager.make_performer_group(
            instrument=instrument,
            )
        name = instrument.instrument_name.title()
        context_name = ScoreTemplateManager.make_staff_name(name)
        voice = scoretools.Voice(
            name='{} Voice'.format(name),
            )
        staff = scoretools.Staff(
            [voice],
            context_name=context_name,
            name='{} Staff'.format(name),
            )
        performer_group.append(staff)
        attach(clef, voice)
        abbreviation = stringtools.to_accent_free_snake_case(name)
        score_template._voice_name_abbreviations[abbreviation] = voice.name
        return performer_group

    @staticmethod
    def make_time_signature_context():
        time_signature_context = scoretools.Context(
            context_name='TimeSignatureContext',
            name='TimeSignatureContext',
            )
        label = 'time'
        ScoreTemplateManager.attach_tag(label, time_signature_context)
        return time_signature_context

    @staticmethod
    def attach_tag(label, context):
        tag = indicatortools.LilyPondCommand(
            name="tag {}".format(label),
            format_slot='before',
            )
        attach(tag, context)