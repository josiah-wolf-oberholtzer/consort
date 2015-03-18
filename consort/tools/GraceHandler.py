# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad import attach
from abjad import new
from abjad import override
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import mathtools
from abjad.tools import schemetools
from abjad.tools import scoretools
from abjad.tools import selectiontools


class GraceHandler(abctools.AbjadValueObject):
    r'''A grace maker.

    ::

        >>> import consort
        >>> grace_handler = consort.GraceHandler(
        ...     counts=(0, 1, 0, 0, 2),
        ...     )
        >>> print(format(grace_handler))
        consort.tools.GraceHandler(
            counts=datastructuretools.CyclicTuple(
                [0, 1, 0, 0, 2]
                ),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_counts',
        '_only_if_preceded_by_nonsilence',
        '_only_if_preceded_by_silence',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        counts=(1,),
        only_if_preceded_by_nonsilence=None,
        only_if_preceded_by_silence=None,
        ):
        if not counts:
            counts = (0,),
        if not isinstance(counts, collections.Sequence):
            counts = (counts,)
        assert len(counts)
        assert mathtools.all_are_nonnegative_integer_equivalent_numbers(
            counts)
        self._counts = datastructuretools.CyclicTuple(counts)
        if only_if_preceded_by_nonsilence is not None:
            only_if_preceded_by_nonsilence = bool(
                only_if_preceded_by_nonsilence)
        if only_if_preceded_by_silence is not None:
            only_if_preceded_by_silence = bool(
                only_if_preceded_by_silence)
        assert not (
            only_if_preceded_by_silence and only_if_preceded_by_nonsilence
            )
        self._only_if_preceded_by_silence = only_if_preceded_by_silence
        self._only_if_preceded_by_nonsilence = only_if_preceded_by_nonsilence

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        seed=0,
        ):
        assert isinstance(logical_tie, selectiontools.LogicalTie)
        if self.counts is None:
            return
        previous_leaf = logical_tie.head._get_leaf(-1)
        if previous_leaf is None:
            return
        silence_prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            scoretools.Skip,
            )
        if self.only_if_preceded_by_silence:
            if not isinstance(previous_leaf, silence_prototype):
                return
        if self.only_if_preceded_by_nonsilence:
            if isinstance(previous_leaf, silence_prototype):
                return
        grace_count = self.counts[seed]
        if not grace_count:
            return
        kind = 'after'
        leaf_to_attach_to = previous_leaf
        leaves = []
        notes = scoretools.make_notes([0], [(1, 16)] * grace_count)
        leaves.extend(notes)
        assert len(leaves)
        grace_container = scoretools.GraceContainer(
            leaves,
            kind=kind,
            )
        override(grace_container).flag.stroke_style = \
            schemetools.Scheme('grace', force_quotes=True)
        override(grace_container).script.font_size = 0.5
        attach(grace_container, leaf_to_attach_to)

    ### PRIVATE METHODS ###

    @staticmethod
    def _process_session(segment_maker):
        import consort
        counter = collections.Counter()
        attack_point_map = segment_maker.attack_point_map
        for logical_tie in attack_point_map:
            music_specifier = \
                consort.SegmentMaker.logical_tie_to_music_specifier(
                    logical_tie)
            if not music_specifier:
                continue
            grace_handler = music_specifier.grace_handler
            if not grace_handler:
                continue
            previous_leaf = logical_tie.head._get_leaf(-1)
            if previous_leaf is None:
                continue
            if music_specifier not in counter:
                seed = music_specifier.seed or 0
                counter[music_specifier] = seed
            seed = counter[music_specifier]
            grace_handler(
                logical_tie,
                seed=seed,
                )
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
    def only_if_preceded_by_nonsilence(self):
        return self._only_if_preceded_by_nonsilence

    @property
    def only_if_preceded_by_silence(self):
        return self._only_if_preceded_by_silence