import abjad
from abjad.tools import abctools


class Cursor(abctools.AbjadValueObject):
    r'''A cursor.

    ..  container:: example

        ::

            >>> cursor = consort.Cursor([1, 2, 3])
            >>> next(cursor)
            1

        ::

            >>> next(cursor)
            2

        ::

            >>> next(cursor)
            3

        ::

            >>> next(cursor)
            1

        ::

            >>> next(cursor)
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

            >>> next(cursor)
            3

        ::

            >>> next(cursor)
            1

    ..  container:: example

        ::

            >>> talea = abjad.rhythmmakertools.Talea(
            ...    counts=(2, 1, 3, 2, 4, 1, 1),
            ...    denominator=16,
            ...    )
            >>> cursor = consort.Cursor(talea)
            >>> for _ in range(10):
            ...     next(cursor)
            ...
            Duration(1, 8)
            Duration(1, 16)
            Duration(3, 16)
            Duration(1, 8)
            Duration(1, 4)
            Duration(1, 16)
            Duration(1, 16)
            Duration(1, 8)
            Duration(1, 16)
            Duration(3, 16)

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_sequence',
        '_index',
        )

    ### INITIALIZER ###

    def __init__(self, sequence=(1, 2, 3), index=None):
        self._sequence = abjad.CyclicTuple(sequence)
        if index is not None:
            index = int(index)
        self._index = index

    ### SPECIAL METHODS ###

    def __iter__(self):
        while True:
            yield self.next()

    def __next__(self):
        return self.next()

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
