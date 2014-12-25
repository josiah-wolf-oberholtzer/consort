# -*- encoding: utf-8 -*-
from abjad import attach
from abjad import abctools


class IndicatorExpression(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_indicator',
        '_is_annotation',
        '_scope',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        indicator=None,
        is_annotation=None,
        scope=None,
        ):
        self._indicator = indicator
        self._is_annotation = is_annotation
        self._scope = scope

    ### SPECIAL METHODS ###

    def __call__(self, component, name=None):
        attach(
            self.indicator,
            component,
            scope=self.scope,
            is_annotation=self.is_annotation,
            name=name,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def indicator(self):
        return self._indicator

    @property
    def is_annotation(self):
        return self._is_annotation

    @property
    def scope(self):
        return self._scope