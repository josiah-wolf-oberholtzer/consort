# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import timespantools


class VoiceSpecifier(abctools.AbjadObject):
    r'''A context specifier.

    ::

        >>> from consort import makers
        >>> voice_specifier = makers.VoiceSpecifier()
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
        self._music_specifier = music_specifier
        self._timespan_maker = timespan_maker
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
