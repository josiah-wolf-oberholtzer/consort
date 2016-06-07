# -*- coding: utf-8 -*-
from abjad.tools.spannertools.HorizontalBracket import HorizontalBracket


class ColorBracket(HorizontalBracket):
    r'''A color bracket.'''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_color',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        color='white',
        overrides=None,
        ):
        HorizontalBracket.__init__(
            self,
            overrides=overrides,
            )
        self._color = color

    ### PRIVATE METHODS ###

    def _format_after_leaf(self, leaf):
        result = HorizontalBracket._format_after_leaf(self, leaf)
        if self._is_my_last_leaf(leaf):
            result.append(r'<> \stopGroup')
        return result

    def _format_before_leaf(self, leaf):
        result = HorizontalBracket._format_before_leaf(self, leaf)
        if self._is_my_first_leaf(leaf):
            string = r"\colorSpan #-4 #4 #(x11-color '{})"
            string = string.format(self._color)
            result.append(string)
        return result

    def _format_right_of_leaf(self, leaf):
        result = []
        if self._is_my_first_leaf(leaf):
            result.append(r'\startGroup')
        return result
