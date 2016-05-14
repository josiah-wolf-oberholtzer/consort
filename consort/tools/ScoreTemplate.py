# -*- encoding: utf-8 -*-
import abc
import importlib
from abjad import Multiplier
from abjad import attach
from abjad import iterate
from abjad.tools import abctools
from abjad.tools import indicatortools
from abjad.tools import instrumenttools
from abjad.tools import lilypondfiletools
from abjad.tools import scoretools
from abjad.tools import stringtools
try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib


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

    def __illustrate__(self):
        score = self()
        time_signatures = [
            (3, 4), (7, 8), (2, 4), (5, 16),
            (4, 4), (6, 8), (5, 4), (3, 8),
            (3, 4), (7, 8), (2, 4), (5, 16),
            ]
        for voice in iterate(score).by_class(scoretools.Voice):
            for pair in time_signatures:
                rest = scoretools.MultimeasureRest(1)
                attach(Multiplier(pair), rest)
                voice.append(rest)
        for pair in time_signatures:
            skip = scoretools.Skip(1)
            attach(Multiplier(pair), skip)
            score['Time Signature Context'].append(skip)
            attach(
                indicatortools.TimeSignature(pair),
                skip,
                scope=scoretools.Score,
                )
        module = importlib.import_module(type(self).__module__)
        score_path = pathlib.Path(module.__file__).parent.parent
        stylesheet_path = score_path.joinpath('stylesheets', 'stylesheet.ily')
        stylesheet_path = stylesheet_path.resolve()
        lilypond_file = lilypondfiletools.make_basic_lilypond_file(
            score,
            includes=[str(stylesheet_path)],
            use_relative_includes=True,
            )
        return lilypond_file

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
        voices=None,
        ):
        name = name.title()
        staff_name = '{} Staff'.format(name)
        context_name = context_name or staff_name
        context_name = context_name.replace(' ', '')
        abbreviation = abbreviation or name
        abbreviation = stringtools.to_snake_case(abbreviation)
        voices = voices or [self._make_voice(name, abbreviation=abbreviation)]
        staff = scoretools.Staff(
            voices,
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
