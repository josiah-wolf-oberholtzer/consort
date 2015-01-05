# -*- encoding: utf-8 -*-
import collections
from consort.tools.HashCachingObject import HashCachingObject


class CompositeMusicSpecifier(HashCachingObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_include_inner_starts',
        '_include_inner_stops',
        '_primary',
        '_rotation_indices',
        '_secondary',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        primary=None,
        secondary=None,
        include_inner_starts=None,
        include_inner_stops=None,
        rotation_indices=None,
        ):
        import consort
        HashCachingObject.__init__(self)
        if include_inner_starts is not None:
            include_inner_starts = bool(include_inner_starts)
        self._include_inner_starts = include_inner_starts
        if include_inner_stops is not None:
            include_inner_stops = bool(include_inner_stops)
        self._include_inner_stops = include_inner_stops
        if primary is not None:
            assert isinstance(primary, consort.MusicSpecifier)
        self._primary = primary
        if rotation_indices is not None:
            if not isinstance(rotation_indices, collections.Sequence):
                rotation_indices = int(rotation_indices)
                rotation_indices = (rotation_indices,)
            rotation_indices = tuple(rotation_indices)
        self._rotation_indices = rotation_indices
        if secondary is not None:
            assert isinstance(secondary, consort.MusicSpecifier)
        self._secondary = secondary

    ### PUBLIC PROPERTIES ###

    @property
    def include_inner_starts(self):
        return self._include_inner_starts

    @property
    def include_inner_stops(self):
        return self._include_inner_stops

    @property
    def primary(self):
        return self._primary

    @property
    def rotation_indices(self):
        return self._rotation_indices

    @property
    def secondary(self):
        return self._secondary