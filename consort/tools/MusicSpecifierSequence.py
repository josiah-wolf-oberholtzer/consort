# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import mathtools
from abjad.tools import sequencetools


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
            application_rate = application_rate or 'phrase'
            assert application_rate in ('division', 'phrase')
        if music_specifiers is not None:
            if not isinstance(music_specifiers, collections.Sequence) or \
                isinstance(music_specifiers, str):
                music_specifiers = [music_specifiers]
            music_specifiers = datastructuretools.CyclicTuple(music_specifiers)
            assert len(music_specifiers)
        self._application_rate = application_rate
        self._music_specifiers = music_specifiers

    ### SPECIAL METHODS ###

    def __call__(
        self,
        durations=None,
        layer=None,
        padding=None,
        seed=None,
        start_offset=None,
        timespan_specifier=None,
        voice_name=None,
        ):
        import consort
        timespans = []
        timespan_specifier = timespan_specifier or \
            consort.TimespanSpecifier()
        seed = seed or 0
        durations = [_ for _ in durations if _]
        offsets = mathtools.cumulative_sums(durations, start_offset)
        if not offsets:
            return timespans
        if padding:
            timespan = consort.SilentTimespan(
                layer=layer,
                start_offset=start_offset - padding,
                stop_offset=start_offset,
                voice_name=voice_name,
                )
            timespans.append(timespan)
        for start_offset, stop_offset in \
            sequencetools.iterate_sequence_nwise(offsets):
            music_specifier = self[seed]
            timespan = consort.PerformedTimespan(
                forbid_fusing=timespan_specifier.forbid_fusing,
                forbid_splitting=timespan_specifier.forbid_splitting,
                layer=layer,
                minimum_duration=timespan_specifier.minimum_duration,
                music_specifier=music_specifier,
                start_offset=start_offset,
                stop_offset=stop_offset,
                voice_name=voice_name,
                )
            timespans.append(timespan)
            if self.application_rate == 'division':
                seed += 1
        if padding:
            timespan = consort.SilentTimespan(
                layer=layer,
                start_offset=offsets[-1],
                stop_offset=offsets[-1] + padding,
                voice_name=voice_name,
                )
            timespans.append(timespan)
        return timespans

    def __getitem__(self, item):
        return self._music_specifiers[item]

    def __len__(self):
        return len(self._music_specifiers)

    ### PUBLIC PROPERTIES ###

    @property
    def application_rate(self):
        return self._application_rate

    @property
    def music_specifiers(self):
        return self._music_specifiers