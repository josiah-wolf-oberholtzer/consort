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
        return hash((type(self), format(self)))
