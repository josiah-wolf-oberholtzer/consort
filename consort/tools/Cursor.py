# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import datastructuretools


class Cursor(abctools.AbjadValueObject):
    r'''A cursor.

    ::

        >>> import consort
        >>> cursor = consort.Cursor([1, 2, 3])
        >>> cursor.next()
        1

    ::

        >>> cursor.next()
        2

    ::

        >>> cursor.next()
        3

    ::

        >>> cursor.next()
        1

    ::

        >>> cursor.next()
        2

    ::

        >>> cursor.backtrack()
        2

    ::

        >>> cursor.backtrack()
        1

    ::

        >>> cursor.backtrack()
        3

    ::

        >>> cursor.next()
        3

    ::

        >>> cursor.next()
        1

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_sequence',
        '_index',
        )

    ### INITIALIZER ###

    def __init__(self, sequence=(1, 2, 3), index=None):
        self._sequence = datastructuretools.CyclicTuple(sequence)
        if index is not None:
            index = int(index)
        self._index = index

    ### PUBLIC METHODS ###

    def backtrack(self):
        if not self._sequence:
            return
        if self._index is None:
            self._index = 0
        self._index -= 1
        index = self._index
        return self._sequence[index]

    def next(self):
        if not self._sequence:
            return
        if self._index is None:
            self._index = 1
            return self._sequence[0]
        index = self._index
        self._index += 1
        return self._sequence[index]

    ### PUBLIC PROPERTIES ###

    @property
    def index(self):
        return self._index

    @property
    def sequence(self):
        return self._sequence