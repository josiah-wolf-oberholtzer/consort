# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import scoretools
from abjad.tools import schemetools
from abjad.tools import selectiontools
from abjad.tools import sequencetools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import new
from abjad.tools.topleveltools import override


class GraceHandler(abctools.AbjadValueObject):
    r'''A grace maker.

    ::

        >>> import consort
        >>> grace_handler = consort.rhythmtools.GraceHandler(
        ...     counts=(0, 1, 0, 0, 2),
        ...     )
        >>> print(format(grace_handler))
        consort.rhythmtools.GraceHandler(
            counts=(0, 1, 0, 0, 2),
            minimum_preceding_duration=durationtools.Duration(1, 16),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_counts',
        '_minimum_preceding_duration',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        counts=None,
        minimum_preceding_duration=durationtools.Duration(1, 16),
        ):
        if counts is not None:
            assert len(counts)
            assert mathtools.all_are_nonnegative_integer_equivalent_numbers(
                counts)
            counts = tuple(counts)
        self._counts = counts
        minimum_preceding_duration = durationtools.Duration(
            minimum_preceding_duration)
        self._minimum_preceding_duration = minimum_preceding_duration

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        music_index=0,
        ):
        assert isinstance(logical_tie, selectiontools.LogicalTie)
        if self.counts is None:
            return
        counts = sequencetools.Sequence(*self.counts).rotate(seed)
        previous_leaf = logical_tie.head._get_leaf(-1)
        if previous_leaf is None:
            return
        grace_count = counts[0]
        if not grace_count:
            return
        kind = 'after'
        leaf_to_attach_to = previous_leaf
        grace_notes = scoretools.make_notes([0], [(1, 16)] * grace_count)
        assert len(grace_notes)
        grace_container = scoretools.GraceContainer(
            grace_notes,
            kind=kind,
            )
        override(grace_container).stem.length = 8
        override(grace_container).flag.stroke_style = \
            schemetools.Scheme('grace', force_quotes=True)
        override(grace_container).script.font_size = 0.5
        attach(grace_container, leaf_to_attach_to)

    @staticmethod
    def _process_session(segment_session):
        import consort
        score = segment_session.score
        counter = collections.Counter()
        for voice in iterate(score).by_class(scoretools.Voice):
            for container in voice:
                prototype = consort.consorttools.MusicSpecifier
                music_specifier = inspect_(container).get_effective(prototype)
                maker = music_specifier.grace_handler
                if maker is None:
                    continue
                if music_specifier not in counter:
                    seed = music_specifier.seed or 0
                    counter[music_specifier] = seed
                seed = counter[music_specifier]
                maker(container, music_index=seed)
                counter[music_specifier] += 1

    ### PUBLIC METHODS ###

    def reverse(self):
        counts = self.counts
        if counts is not None:
            counts = counts.reverse()
        return new(self,
            counts=counts,
            )

    def rotate(self, n=0):
        counts = self.counts
        if counts is not None:
            counts = counts.rotate(n)
        return new(self,
            counts=counts,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def counts(self):
        return self._counts

    @property
    def minimum_preceding_duration(self):
        return self._minimum_preceding_duration