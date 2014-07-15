# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import sequencetools


class Proportions(abctools.AbjadObject, collections.Sequence):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_proportions',
        )

    ### INITIALIZER ###

    def __init__(self, proportions=None):
        proportions = proportions or []
        proportions = tuple(proportions)
        self._proportions = proportions

    ### SPECIAL METHODS ###

    def __getitem__(self, item):
        return self._proportions[item]

    def __len__(self):
        return len(self._proportions)

    ### PUBLIC METHODS ###

    def get_segment_duration_in_seconds(self, segment_index, total_seconds):
        segment_proportions = self[segment_index]
        segment_total = sum(sequencetools.flatten_sequence(
            segment_proportions))
        ratio = durationtools.Multiplier(segment_total, self.total)
        duration_in_seconds = ratio * total_seconds
        return duration_in_seconds

    ### PUBLIC PROPERTIES ###

    @property
    def total(self):
        return sum(sequencetools.flatten_sequence(self))