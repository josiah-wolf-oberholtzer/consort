# -*- encoding: utf-8 -*-
import abc
from abjad import attach
from abjad import detach
from abjad import inspect_
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
            grace_notes = old_grace_container.select_leaves()
            detach(scoretools.GraceContainer, old_leaf)
        mutate(old_leaf).replace(new_leaf)
        if grace_containers:
            new_grace_container = scoretools.GraceContainer(
                grace_notes,
                kind='after',
                )
            attach(new_grace_container, new_leaf)