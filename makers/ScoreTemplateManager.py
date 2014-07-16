# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import indicatortools
from abjad.tools import scoretools
from abjad.tools.topleveltools import attach


class ScoreTemplateManager(abctools.AbjadObject):

    ### PUBLIC METHODS ###

    @staticmethod
    def make_performer_group(instrument, context_name=None, label=None):
        context_name = context_name or 'SinglePerformerGroup'
        label = label or instrument.instrument_name.replace(' ', '-').lower()
        name = '{} Performer Group'.format(instrument.instrument_name.title())
        performer_group = scoretools.StaffGroup(
            context_name='SinglePerformerGroup',
            name=name,
            )
        performer_group.is_simultaneous = True
        tag = indicatortools.LilyPondCommand(
            name='keepWithTag #"score.{}"'.format(label),
            format_slot='before',
            )
        attach(tag, performer_group)
        attach(instrument, performer_group, scope=scoretools.StaffGroup)
        return performer_group, label

    @staticmethod
    def make_single_basic_performer(
        instrument,
        context_name=None,
        label=None,
        ):
        performer_group, label = ScoreTemplateManager.make_performer_group(
            instrument,
            context_name=context_name,
            label=label,
            )
        name = instrument.instrument_name.title()
        staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Voice'.format(name),
                    ),
                ],
            name='{} Staff'.format(name),
            )
        performer_group.append(staff)
        return performer_group, label

    @staticmethod
    def make_single_piano_performer(instrument):
        performer_group, label = ScoreTemplateManager.make_performer_group(
            instrument)
        name = instrument.instrument_name.title()
        upper_staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Upper Voice'.format(name),
                    ),
                ],
            name='{} Upper Staff'.format(name),
            )
        dynamics = scoretools.Context(
            context_name='Dynamics',
            name='{} Dynamics'.format(name),
            )
        lower_staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Lower Voice'.format(name),
                    ),
                ],
            name='{} Lower Staff'.format(name),
            )
        pedals = scoretools.Context(
            context_name='Dynamics',
            name='{} Pedals'.format(name),
            )
        performer_group.extend((
            upper_staff,
            dynamics,
            lower_staff,
            pedals,
            ))
        return performer_group, label

    @staticmethod
    def make_single_string_performer(instrument):
        performer_group, label = ScoreTemplateManager.make_performer_group(
            instrument)
        name = instrument.instrument_name.title()
        bowing_staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Bowing Voice'.format(name),
                    ),
                ],
            context_name='BowingStaff',
            name='{} Bowing Staff'.format(name),
            )
        fingering_staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Fingering Voice'.format(name),
                    ),
                ],
            context_name='FingeringStaff',
            name='{} Fingering Staff'.format(name),
            )
        performer_group.append(bowing_staff)
        performer_group.append(fingering_staff)
        return performer_group, label

    @staticmethod
    def make_single_wind_performer(instrument):
        performer_group, label = ScoreTemplateManager.make_performer_group(
            instrument)
        name = instrument.instrument_name.title()
        wind_staff = scoretools.Staff(
            [
                scoretools.Voice(
                    name='{} Voice'.format(name),
                    ),
                ],
            name='{}  Staff'.format(name),
            )
        performer_group.append(wind_staff)
        return performer_group, label

    @staticmethod
    def make_time_signature_context(labels):
        time_signature_context = scoretools.Context(
            context_name='TimeSignatureContext',
            name='TimeSignatureContext',
            )
        labels = '.'.join(labels)
        tag = indicatortools.LilyPondCommand(
            name='keepWithTag #"score.{}"'.format(labels),
            format_slot='before',
            )
        attach(tag, time_signature_context)
        return time_signature_context

    @staticmethod
    def attach_tag(label, context):
        tag = indicatortools.LilyPondCommand(
            name='keepWithTag #"{}"'.format(label),
            format_slot='before',
            )
        attach(tag, context) 