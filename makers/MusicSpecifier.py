# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import rhythmmakertools


class MusicSpecifier(abctools.AbjadValueObject):
    r'''A music specifier.

    ::

        >>> from consort import makers
        >>> music_specifier = makers.MusicSpecifier()
        >>> print(format(music_specifier))
        consort.makers.MusicSpecifier()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachment_maker',
        '_grace_maker',
        '_is_sentinel',
        '_pitch_maker',
        '_rhythm_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachment_maker=None,
        grace_maker=None,
        is_sentinel=None,
        pitch_maker=None,
        rhythm_maker=None,
        ):
        from consort import makers
        if attachment_maker is not None:
            assert isinstance(attachment_maker, makers.AttachmentMaker)
        self._attachment_maker = attachment_maker
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

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            if format(self) == format(expr):
                return True
        return False

    def __hash__(self):
        hash_values = (type(self), format(self))
        return hash(hash_values)

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        r'''Attribute manifest.

        ::
            
            >>> from consort import makers
            >>> music_specifier = makers.MusicSpecifier()
            >>> print(format(music_specifier._attribute_manifest))
            systemtools.AttributeManifest()

        '''
        from abjad.tools import systemtools
        from consort import makers
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='attachment_maker',
                display_string='attachment maker',
                command='am',
                editor=makers.AttachmentMaker,
                ),
            systemtools.AttributeDetail(
                name='grace_maker',
                display_string='grace maker',
                command='am',
                editor=makers.GraceMaker,
                ),
            systemtools.AttributeDetail(
                name='pitch_maker',
                display_string='pitch maker',
                command='am',
                editor=makers.PitchMaker,
                ),
            systemtools.AttributeDetail(
                name='rhythm_maker',
                display_string='rhythm maker',
                command='am',
                editor=rhythmmakertools.RhythmMaker,
                ),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_maker(self):
        return self._attachment_maker

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