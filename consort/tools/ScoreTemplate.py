# -*- encoding: utf-8 -*-
import abc
from abjad import attach
from abjad.tools import abctools
from abjad.tools import indicatortools
from abjad.tools import instrumenttools
from abjad.tools import scoretools
from abjad.tools import stringtools


class ScoreTemplate(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_composite_context_pairs',
        '_context_name_abbreviations',
        )

    _is_populated = False

    ### INITIALIZER ###

    def __init__(self):
        self._context_name_abbreviations = {}
        self._composite_context_pairs = {}

        if not type(self)._is_populated:
            self()
            type(self)._is_populated = True

    ### SPECIAL METHODS ###

    @abc.abstractmethod
    def __call__(self):
        raise NotImplementedError

    ### PRIVATE METHODS ###

    def _attach_tag(self, label, context):
        label = stringtools.to_dash_case(label)
        tag = indicatortools.LilyPondCommand(
            name="tag #'{}".format(label),
            format_slot='before',
            )
        attach(tag, context)

    def _make_voice(self, name, abbreviation=None, context_name=None):
        name = name.title()
        abbreviation = abbreviation or name
        abbreviation = stringtools.to_snake_case(abbreviation)
        voice_name = '{} Voice'.format(name)
        voice = scoretools.Voice(
            name=voice_name,
            context_name=context_name,
            )
        self._context_name_abbreviations[abbreviation] = voice.name
        return voice

    def _make_staff(
        self,
        name,
        clef,
        abbreviation=None,
        context_name=None,
        instrument=None,
        tag=None,
        ):
        name = name.title()
        staff_name = '{} Staff'.format(name)
        context_name = context_name or staff_name
        context_name = context_name.replace(' ', '')
        abbreviation = abbreviation or name
        abbreviation = stringtools.to_snake_case(abbreviation)
        voice = self._make_voice(name, abbreviation=abbreviation)
        staff = scoretools.Staff(
            [voice],
            context_name=context_name,
            name=staff_name
            )
        if not isinstance(clef, indicatortools.Clef):
            clef = indicatortools.Clef(clef)
        attach(clef, staff)
        if tag:
            self._attach_tag(tag, staff)
        if instrument:
            assert isinstance(instrument, instrumenttools.Instrument)
            attach(instrument, staff)
        return staff

    def _populate(self):
        if not type(self)._is_populated:
            self()
            type(self)._is_populated = True

    ### PUBLIC PROPERTIES ###

    @property
    def all_voice_names(self):
        self._populate()
        result = []
        for name in self.context_name_abbreviations:
            if name in self.composite_context_pairs:
                continue
            result.append(name)
        return tuple(result)

    @property
    def composite_context_pairs(self):
        self._populate()
        return self._composite_context_pairs

    @property
    def context_name_abbreviations(self):
        self._populate()
        return self._context_name_abbreviations