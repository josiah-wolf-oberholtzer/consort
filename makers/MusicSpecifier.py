# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import rhythmmakertools


class MusicSpecifier(ConsortObject):
    r'''A music specifier.

    ::

        >>> from consort import makers
        >>> music_specifier = makers.MusicSpecifier()
        >>> print(format(music_specifier))
        makers.MusicSpecifier()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachment_agent',
        '_grace_maker',
        '_is_sentinel',
        '_pitch_maker',
        '_rhythm_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachment_agent=None,
        grace_maker=None,
        is_sentinel=None,
        pitch_maker=None,
        rhythm_maker=None,
        ):
        from consort import makers
        if attachment_agent is not None:
            assert isinstance(attachment_agent, makers.AttachmentAgent)
        self._attachment_agent = attachment_agent
        if grace_maker is not None:
            assert isinstance(grace_maker, makers.GraceMaker)
        self._grace_maker = grace_maker
        if is_sentinel is not None:
            is_sentinel = bool(is_sentinel)
        self._is_sentinel = is_sentinel
        if pitch_maker is not None:
            assert isinstance(pitch_maker, makers.PitchMaker)
        self._pitch_maker = pitch_maker
        if rhythm_maker is not None:
            assert isinstance(rhythm_maker, rhythmmakertools.RhythmMaker)
        self._rhythm_maker = rhythm_maker

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_agent(self):
        return self._attachment_agent

    @property
    def grace_maker(self):
        return self._grace_maker

    @property
    def is_sentinel(self):
        return self._is_sentinel

    @property
    def pitch_maker(self):
        return self._pitch_maker

    @property
    def rhythm_maker(self):
        return self._rhythm_maker