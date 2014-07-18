# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import timespantools


class MusicSetting(abctools.AbjadObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_color',
        '_timespan_identifier',
        '_voice_identifier',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        color=None,
        timespan_identifier=None,
        voice_identifier=None,
        ):
        from consort import makers
        if color is not None:
            color = str(color)
        self._color = color
        if timespan_identifier is not None:
            prototype = (
                timespantools.Timespan,
                makers.RatioPartsExpression,
                )
            assert isinstance(timespan_identifier, prototype)
        self._timespan_identifier = timespan_identifier
        if voice_identifier is not None:
            if isinstance(voice_identifier, str):
                voice_identifier = (voice_identifier,)
            voice_identifier = tuple(voice_identifier)
            assert all(isinstance(x, str) for x in voice_identifier)
        self._voice_identifier = voice_identifier

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer,
        target_duration,
        timespan_inventory=None,
        ):
        raise NotImplementedError

    ### PUBLIC PROPERTIES ###

    @property
    def color(self):
        return self._color

    @property
    def timespan_identifier(self):
        return self._timespan_identifier

    @property
    def voice_identifier(self):
        return self._voice_identifier
