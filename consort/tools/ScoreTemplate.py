# -*- encoding: utf-8 -*-
import abc
import collections
from abjad import abctools


class ScoreTemplate(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_composite_context_pairs',
        '_context_name_abbreviations',
        )

    ### INITIALIZER ###

    def __init__(self):
        self._context_name_abbreviations = collections.OrderedDict()
        self._composite_context_pairs = collections.OrderedDict()

    ### SPECIAL METHODS ###

    @abc.abstractmethod
    def __call__(self):
        raise NotImplementedError

    ### PUBLIC PROPERTIES ###

    @property
    def composite_context_pairs(self):
        return self._composite_context_pairs

    @property
    def context_name_abbreviations(self):
        return self._context_name_abbreviations