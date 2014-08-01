# -*- encoding: utf-8 -*-
import collections
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import scoretools
from abjad.tools import schemetools
from abjad.tools import selectiontools
from abjad.tools import sequencetools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import override
from abjad.tools.topleveltools import new


class GraceMaker(ConsortObject):
    r'''A grace agent.

    ::

        >>> from consort import makers
        >>> grace_maker = makers.GraceMaker(
        ...     counts=(0, 1, 0, 0, 2),
        ...     )
        >>> print(format(grace_maker))
        makers.GraceMaker(
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
        seed=0,
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

    ### PUBLIC METHODS ###

    @staticmethod
    def iterate_score(
        score,
        ):
        from consort import makers
        counter = collections.Counter()
        for leaf in iterate(score).by_timeline(scoretools.Note):
            logical_tie = inspect_(leaf).get_logical_tie()
            if leaf is not logical_tie.head:
                continue
            prototype = makers.MusicSpecifier
            music_specifier = inspect_(leaf).get_effective(prototype)
            grace_maker = music_specifier.grace_maker
            if grace_maker is None:
                continue
            seed = counter[music_specifier]
            grace_maker(logical_tie, seed=seed)
            counter[music_specifier] += 1

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