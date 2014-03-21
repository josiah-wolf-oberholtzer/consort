# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import rhythmmakertools


class MusicSpecifier(abctools.AbjadObject):
    r'''A music specifier.

    ::

        >>> from consort import makers
        >>> music_specifier = makers.MusicSpecifier()
        >>> print format(music_specifier)
        makers.MusicSpecifier()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_alteration_agent',
        '_attachment_agent',
        '_chord_agent',
        '_grace_agent',
        '_is_sentinel',
        '_pitch_agent',
        '_register_agent',
        '_rhythm_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        alteration_agent=None,
        attachment_agent=None,
        chord_agent=None,
        grace_agent=None,
        is_sentinel=None,
        pitch_agent=None,
        register_agent=None,
        rhythm_maker=None,
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
        if is_sentinel is not None:
            is_sentinel = bool(is_sentinel)
        self._is_sentinel = is_sentinel
        if pitch_agent is not None:
            assert isinstance(pitch_agent, makers.PitchAgent)
        self._pitch_agent = pitch_agent
        if register_agent is not None:
            assert isinstance(register_agent, makers.RegisterAgent)
        self._register_agent = register_agent
        if rhythm_maker is not None:
            assert isinstance(rhythm_maker, rhythmmakertools.RhythmMaker)
        self._rhythm_maker = rhythm_maker

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
    def is_sentinel(self):
        return self._is_sentinel

    @property
    def pitch_agent(self):
        return self._pitch_agent

    @property
    def register_agent(self):
        return self._register_agent

    @property
    def rhythm_maker(self):
        return self._rhythm_maker
