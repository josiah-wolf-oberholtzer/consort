# -*- encoding: utf-8 -*-
from abjad import abctools


class HashCachingObject(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_hash',
        )

    ### INITIALIZER ###

    def __init__(self):
        self._hash = None

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            if format(self) == format(expr):
                return True
        return False

    def __hash__(self):
        if self._hash is None:
            hash_values = (type(self), format(self))
            self._hash = hash(hash_values)
        return self._hash
