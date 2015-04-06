# -*- encoding: utf-8 -*-
from abjad import attach
from abjad import set_
from abjad.tools import abctools
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import scoretools
from abjad.tools import stringtools


class ScoreTemplateManager(abctools.AbjadObject):

    ### PUBLIC METHODS ###

    @staticmethod
    def attach_tag(label, context):
        label = stringtools.to_dash_case(label)
        tag = indicatortools.LilyPondCommand(
            name="tag #'{}".format(label),
            format_slot='before',
            )
        attach(tag, context)

    @staticmethod
    def make_auxiliary_staff(
        primary_instrument=None,
        secondary_instrument=None,
        score_template=None,
        ):
        name = '{} {}'.format(
            primary_instrument.instrument_name.title(),
            secondary_instrument.instrument_name.title(),
            )
        voice = scoretools.Voice(
            name='{} Voice'.format(name),
            )
        context_name = ScoreTemplateManager.make_staff_name(
            secondary_instrument.instrument_name.title(),
            )
        staff = scoretools.Staff(
            [voice],
            name='{} Staff'.format(name),
            context_name=context_name,
            )
        abbreviation = stringtools.to_snake_case(name)
        score_template._context_name_abbreviations[abbreviation] = voice.name
        return staff

    @staticmethod
    def make_column_markup(string, space):
        string_parts = string.split()
        if len(string_parts) == 1:
            markup = markuptools.Markup(string_parts[0]).hcenter_in(space)
        else:
            markups = [markuptools.Markup(_) for _ in string_parts]
            markup = markuptools.Markup.center_column(markups, direction=None)
            markup = markup.hcenter_in(space)
        return markup

    @staticmethod
    def make_ensemble_group(
        label=None,
        name=None,
        performer_groups=None,
        ):
        ensemble_group = scoretools.StaffGroup(
            performer_groups,
            name=name,
            context_name='EnsembleGroup',
            )
        if label is not None:
            ScoreTemplateManager.attach_tag(label, ensemble_group)
        return ensemble_group

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
        if label is not None:
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
        clef=None,
        context_name=None,
        instrument=None,
        label=None,
        score_template=None,
        ):
        performer_group = ScoreTemplateManager.make_performer_group(
            context_name=context_name,
            instrument=instrument,
            label=label,
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
        abbreviation = stringtools.to_snake_case(name)
        score_template._context_name_abbreviations[abbreviation] = voice.name
        return performer_group

    @staticmethod
    def make_single_piano_performer(
        instrument=None,
        score_template=None,
        ):
        performer_group = ScoreTemplateManager.make_performer_group(
            context_name='PianoStaff',
            instrument=instrument,
            label=stringtools.to_dash_case(instrument.instrument_name),
            )
        name = instrument.instrument_name.title()
        upper_voice = scoretools.Voice(
            name='{} Upper Voice'.format(name),
            )
        upper_staff = scoretools.Staff(
            [upper_voice],
            context_name='PianoUpperStaff',
            name='{} Upper Staff'.format(name),
            )
        dynamics = scoretools.Voice(
            context_name='Dynamics',
            name='{} Dynamics'.format(name),
            )
        lower_voice = scoretools.Voice(
            name='{} Lower Voice'.format(name),
            )
        lower_staff = scoretools.Staff(
            [lower_voice],
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
        attach(indicatortools.Clef('treble'), upper_voice)
        attach(indicatortools.Clef('bass'), lower_voice)
        score_template._context_name_abbreviations.update(
            piano_dynamics=dynamics.name,
            piano_lh=lower_voice.name,
            piano_pedals=pedals.name,
            piano_rh=upper_voice.name,
            )
        return performer_group

    @staticmethod
    def make_single_string_performer(
        abbreviation=None,
        clef=None,
        instrument=None,
        score_template=None,
        split=True,
        ):
        performer_group = ScoreTemplateManager.make_performer_group(
            context_name='StringPerformerGroup',
            instrument=instrument,
            label=stringtools.to_dash_case(instrument.instrument_name),
            )
        name = instrument.instrument_name.title()
        abbreviation = abbreviation or \
            stringtools.to_snake_case(name)
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
            attach(clef, left_hand_staff)
            attach(indicatortools.Clef('percussion'), right_hand_staff)
            right_hand_abbreviation = '{}_rh'.format(abbreviation)
            left_hand_abbreviation = '{}_lh'.format(abbreviation)
            score_template._context_name_abbreviations.update({
                abbreviation: performer_group.name,
                right_hand_abbreviation: right_hand_voice.name,
                left_hand_abbreviation: left_hand_voice.name,
                })
            score_template._composite_context_pairs[abbreviation] = (
                right_hand_abbreviation,
                left_hand_abbreviation,
                )
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
            score_template._context_name_abbreviations[abbreviation] = \
                voice.name
        return performer_group

    @staticmethod
    def make_single_wind_performer(
        abbreviation=None,
        clef=None,
        instrument=None,
        score_template=None,
        ):
        performer_group = ScoreTemplateManager.make_performer_group(
            instrument=instrument,
            label=stringtools.to_dash_case(instrument.instrument_name),
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
        abbreviation = abbreviation or \
            stringtools.to_snake_case(name)
        score_template._context_name_abbreviations[abbreviation] = voice.name
        return performer_group

    @staticmethod
    def make_staff_name(name):
        name = ''.join(x for x in name if x.isalpha())
        name = '{}Staff'.format(name)
        return name

    @staticmethod
    def make_voice_name(name):
        name = ''.join(x for x in name if x.isalpha())
        name = '{}Voice'.format(name)
        return name

    @staticmethod
    def make_time_signature_context():
        time_signature_context = scoretools.Context(
            context_name='TimeSignatureContext',
            name='Time Signature Context',
            )
        label = 'time'
        ScoreTemplateManager.attach_tag(label, time_signature_context)
        return time_signature_context