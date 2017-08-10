from abjad.tools import abctools
from abjad.tools import systemtools


class HashCachingObject(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_format',
        '_hash',
        )

    ### INITIALIZER ###

    def __init__(self):
        self._format = None
        self._hash = None

    ### SPECIAL METHODS ###

    #@profile
    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            if format(self) == format(expr):
                return True
        return False

    #@profile
    def __format__(self, format_specification=''):
        if self._format is None:
            agent = systemtools.StorageFormatAgent(self)
            self._format = agent.get_storage_format()
        return self._format

    #@profile
    def __hash__(self):
        if self._hash is None:
            self._hash = hash((type(self), format(self)))
        return self._hash
