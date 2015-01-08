# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import datastructuretools


class MusicSpecifierSequence(abctools.AbjadValueObject):
    r'''A music specifier sequence.

    ::

        >>> import consort
        >>> sequence_a = consort.MusicSpecifierSequence(
        ...     music_specifiers='music',
        ...     )
        >>> print(format(sequence_a))
        consort.tools.MusicSpecifierSequence(
            music_specifiers=datastructuretools.CyclicTuple(
                ['music']
                ),
            )

    ::

        >>> sequence_b = consort.MusicSpecifierSequence(
        ...     application_rate='phrase',
        ...     music_specifiers=['one', 'two', 'three'],
        ...     )
        >>> print(format(sequence_b))
        consort.tools.MusicSpecifierSequence(
            application_rate='phrase',
            music_specifiers=datastructuretools.CyclicTuple(
                ['one', 'two', 'three']
                ),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_application_rate',
        '_music_specifiers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        application_rate=None,
        music_specifiers=None,
        ):
        if application_rate is not None:
            application_rate = application_rate or 'division'
            assert application_rate in ('division', 'phrase')
        if music_specifiers is not None:
            if not isinstance(music_specifiers, collections.Sequence) or \
                isinstance(music_specifiers, str):
                music_specifiers = [music_specifiers]
            music_specifiers = datastructuretools.CyclicTuple(music_specifiers)
            assert len(music_specifiers)
        self._application_rate = application_rate
        self._music_specifiers = music_specifiers

    ### PUBLIC PROPERTIES ###

    @property
    def application_rate(self):
        return self._application_rate

    @property
    def music_specifiers(self):
        return self._music_specifiers