# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import systemtools


class ConsortObject(abctools.AbjadObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        return systemtools.StorageFormatManager.compare(self, expr)

    def __hash__(self):
        hash_values = systemtools.StorageFormatManager.get_hash_values(self)
        try:
            result = hash(hash_values)
        except TypeError as e:
            print hash_values
            raise e
        return result
