# -*- encoding: utf-8 -*-
from abjad.tools import abctools


class MusicSpecifier(abctools.AbjadObject):
    r'''A music specifier.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_alteration_agent',
        '_attachment_agent',
        '_chord_agent',
        '_grace_agent',
        '_pitch_agent',
        '_register_agent',
        '_rhythm_maker',
        '_timespan_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        alteration_agent=None,
        attachment_agent=None,
        chord_agent=None,
        grace_agent=None,
        pitch_agent=None,
        register_agent=None,
        rhythm_maker=None,
        timespan_maker=None,
        ):
        from consort import makers
        if alteration_agent is not None:
            assert isinstance(alteration_agent, makers.AlterationAgent)
        self._alteration_agent = alteration_agent
        if attachment_agent is not None:
            assert isinstance(attachment_agent, makers.AttachmentAgent)
        self._attachment_agent = attachment_agent
        if chord_agent is not None:
            assert isinstance(chord_agent, makers.ChordAgent)
        self._chord_agent = chord_agent
        if grace_agent is not None:
            assert isinstance(grace_agent, makers.GraceAgent)
        self._grace_agent = grace_agent
        if pitch_agent is not None:
            assert isinstance(pitch_agent, makers.PitchAgent)
        self._pitch_agent = pitch_agent
        if register_agent is not None:
            assert isinstance(register_agent, makers.RegisterAgent)
        self._register_agent = register_agent
        if rhythm_maker is not None:
            assert isinstance(rhythm_maker, makers.RhythmMaker)
        self._rhythm_maker = rhythm_maker
        if timespan_maker is not None:
            assert isinstance(alteration_agent, makers.TimespanMaker)
        self._timespan_maker = timespan_maker

    ### PUBLIC PROPERTIES ###

    @property
    def alteration_agent(self):
        return self._alteration_agent

    @property
    def attachment_agent(self):
        return self._attachment_agent

    @property
    def chord_agent(self):
        return self._chord_agent

    @property
    def grace_agent(self):
        return self._grace_agent

    @property
    def pitch_agent(self):
        return self._pitch_agent

    @property
    def register_agent(self):
        return self._register_agent

    @property
    def rhythm_maker(self):
        return self._rhythm_maker

    @property
    def timespan_maker(self):
        return self._timespan_maker
