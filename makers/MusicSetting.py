# -*- encoding: utf-8 -*-
import abc
from abjad.tools import abctools
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
                timespantools.TimespanInventory,
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

    @abc.abstractmethod
    def __call__(
        self,
        layer,
        score_template,
        target_timespan,
        timespan_inventory=None,
        ):
        from consort import makers
        assert score_template is not None
        voice_names = makers.SegmentMaker._find_voice_names(
            score_template=score_template,
            voice_identifier=self.voice_identifier,
            )
        assert voice_names, voice_names
        assert isinstance(target_timespan, timespantools.Timespan)
        target_timespans = timespantools.TimespanInventory([target_timespan])
        if isinstance(self.timespan_identifier, timespantools.Timespan):
            target_timespans = target_timespans & self.timespan_identifier
        elif isinstance(self.timespan_identifier,
            timespantools.TimespanInventory):
            for timespan in self.timespan_identifier:
                target_timespans = target_timespans - timespan
        elif isinstance(self.timespan_identifier, makers.RatioPartsExpression):
            parts = self.timespan_identifier(target_timespans[0])
            for part in parts:
                target_timespans = target_timespans & part
        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
        return target_timespans, voice_names, timespan_inventory

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