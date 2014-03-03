# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import timespantools


class VoiceSpecifier(abctools.AbjadObject):
    r'''A context specifier.

    ::

        >>> from consort import makers
        >>> voice_specifier = makers.VoiceSpecifier(
        ...     music_specifier=makers.MusicSpecifier(),
        ...     timespan_maker=makers.TimespanMaker(),
        ...     voice_identifier=(),
        ...     )
        >>> print format(voice_specifier)
        makers.VoiceSpecifier()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_music_specifier',
        '_timespan_maker',
        '_voice_identifier',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        music_specifier=None,
        timespan_maker=None,
        voice_identifier=None,
        ):
        from consort import makers
        assert isinstance(music_specifier, makers.MusicSpecifier)
        self._music_specifier = music_specifier
        assert isinstance(timespan_maker, makers.TimespanMaker)
        self._timespan_maker = timespan_maker
        if isinstance(voice_identifier, str):
            voice_identifier = (voice_identifier,)
        assert isinstance(voice_identifier, tuple)
        assert len(voice_identifier)
        assert all(isinstance(voice_identifier, str)
            for x in voice_identifier)
        self._voice_identifier = voice_identifier

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer=None,
        template=None,
        ):
        return timespantools.TimespanInventory()

    ### PUBLIC PROPERTIES ###

    @property
    def music_specifier(self):
        return self._music_specifier

    @property
    def timespan_maker(self):
        return self._timespan_maker

    @property
    def voice_identifier(self):
        return self._voice_identifier
