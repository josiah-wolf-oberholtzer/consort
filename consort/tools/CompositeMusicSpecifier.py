# -*- encoding: utf-8 -*-
import collections
from consort.tools.HashCachingObject import HashCachingObject


class CompositeMusicSpecifier(HashCachingObject):
    r'''A composite music specifier.

    ::

        >>> import consort
        >>> music_specifier = consort.CompositeMusicSpecifier(
        ...     primary_music_specifier='one',
        ...     primary_voice_name='Viola 1 RH',
        ...     rotation_indices=(0, 1, -1),
        ...     secondary_voice_name='Viola 1 LH',
        ...     secondary_music_specifier=consort.MusicSpecifierSequence(
        ...         application_rate='phrase',
        ...         music_specifiers=['two', 'three', 'four'],
        ...         ),
        ...     )
        >>> print(format(music_specifier))
        consort.tools.CompositeMusicSpecifier(
            primary_music_specifier=consort.tools.MusicSpecifierSequence(
                music_specifiers=datastructuretools.CyclicTuple(
                    ['one']
                    ),
                ),
            primary_voice_name='Viola 1 RH',
            rotation_indices=(0, 1, -1),
            secondary_music_specifier=consort.tools.MusicSpecifierSequence(
                application_rate='phrase',
                music_specifiers=datastructuretools.CyclicTuple(
                    ['two', 'three', 'four']
                    ),
                ),
            secondary_voice_name='Viola 1 LH',
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_include_inner_starts',
        '_include_inner_stops',
        '_primary_music_specifier',
        '_primary_voice_name',
        '_rotation_indices',
        '_secondary_music_specifier',
        '_secondary_voice_name',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        include_inner_starts=None,
        include_inner_stops=None,
        primary_music_specifier=None,
        primary_voice_name=None,
        rotation_indices=None,
        secondary_music_specifier=None,
        secondary_voice_name=None,
        ):
        import consort
        HashCachingObject.__init__(self)
        prototype = consort.MusicSpecifierSequence
        if include_inner_starts is not None:
            include_inner_starts = bool(include_inner_starts)
        self._include_inner_starts = include_inner_starts
        if include_inner_stops is not None:
            include_inner_stops = bool(include_inner_stops)
        self._include_inner_stops = include_inner_stops
        if not isinstance(primary_music_specifier, prototype):
            primary_music_specifier = consort.MusicSpecifierSequence(
                music_specifiers=primary_music_specifier,
                )
        self._primary_music_specifier = primary_music_specifier
        if primary_voice_name is not None:
            primary_voice_name = str(primary_voice_name)
        self._primary_voice_name = primary_voice_name
        if rotation_indices is not None:
            if not isinstance(rotation_indices, collections.Sequence):
                rotation_indices = int(rotation_indices)
                rotation_indices = (rotation_indices,)
            rotation_indices = tuple(rotation_indices)
        self._rotation_indices = rotation_indices
        if not isinstance(secondary_music_specifier, prototype):
            secondary_music_specifier = consort.MusicSpecifierSequence(
                music_specifiers=secondary_music_specifier,
                )
        self._secondary_music_specifier = secondary_music_specifier
        if secondary_voice_name is not None:
            secondary_voice_name = str(secondary_voice_name)
        self._secondary_voice_name = secondary_voice_name

    ### PUBLIC PROPERTIES ###

    @property
    def include_inner_starts(self):
        return self._include_inner_starts

    @property
    def include_inner_stops(self):
        return self._include_inner_stops

    @property
    def primary_music_specifier(self):
        return self._primary_music_specifier

    @property
    def primary_voice_name(self):
        return self._primary_voice_name

    @property
    def rotation_indices(self):
        return self._rotation_indices

    @property
    def secondary_music_specifier(self):
        return self._secondary_music_specifier

    @property
    def secondary_voice_name(self):
        return self._secondary_voice_name