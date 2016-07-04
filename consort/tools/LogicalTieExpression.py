# -*- encoding: utf-8 -*-
import abc
from abjad import attach
from abjad import detach
from abjad import inspect_
from abjad import iterate
from abjad import mutate
from abjad.tools import abctools
from abjad.tools import scoretools


class LogicalTieExpression(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    @abc.abstractmethod
    def __call__(self, logical_tie, pitch_range=None):
        raise NotImplementedError

    ### PRIVATE METHODS ###

    def _replace(self, old_leaf, new_leaf):
        grace_containers = inspect_(old_leaf).get_grace_containers('after')
        if grace_containers:
            old_grace_container = grace_containers[0]
            grace_notes = list(iterate(old_grace_container).by_leaf())
            detach(scoretools.GraceContainer, old_leaf)

        indicator_expressions = inspect_(old_leaf).get_indicators(unwrap=False)
        #for indicator_expression in indicator_expressions:
        #    detach(indicator, old_leaf)

        timespan = old_leaf._timespan
        start_offset = old_leaf._start_offset
        stop_offset = old_leaf._stop_offset
        logical_measure_number = old_leaf._logical_measure_number
        mutate(old_leaf).replace(new_leaf)
        new_leaf._timespan = timespan
        new_leaf._start_offset = start_offset
        new_leaf._stop_offset = stop_offset
        new_leaf._logical_measure_number = logical_measure_number

        if grace_containers:
            new_grace_container = scoretools.GraceContainer(
                grace_notes,
                kind='after',
                )
            attach(new_grace_container, new_leaf)

        for indicator_expression in indicator_expressions:
            attach(indicator_expression, new_leaf)
