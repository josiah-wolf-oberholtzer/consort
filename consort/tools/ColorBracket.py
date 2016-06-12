# -*- coding: utf-8 -*-
from abjad import inspect_
from abjad.tools.spannertools.Spanner import Spanner


class ColorBracket(Spanner):
    r'''A color bracket.

    ..  note::

        Requires a Scheme definition for the ``\colorSpan`` command.

    ::

        >>> staff = Staff("c'4 d'4 e'4 f'4")
        >>> print(format(staff))
        \new Staff {
            c'4
            d'4
            e'4
            f'4
        }

    ::

        >>> import consort
        >>> red_bracket = consort.ColorBracket('red')
        >>> blue_bracket = consort.ColorBracket('blue')
        >>> attach(red_bracket, staff[:2])
        >>> attach(blue_bracket, staff[2:])
        >>> print(format(staff))
        \new Staff {
            \colorSpan #-4 #4 #(x11-color 'red)
            c'4 \(
            d'4
            \colorSpan #-4 #4 #(x11-color 'blue)
            e'4 \) \(
            f'4
            <> \)
        }

    ::

        >>> staff = Staff("c'4 d'4 e'4 f'4")
        >>> red = consort.Color(1, 0, 0)
        >>> blue = consort.Color(0, 0, 1)
        >>> red_bracket = consort.ColorBracket(red)
        >>> blue_bracket = consort.ColorBracket(blue)
        >>> attach(red_bracket, staff[:2])
        >>> attach(blue_bracket, staff[2:])
        >>> print(format(staff))
        \new Staff {
            \colorSpan #-4 #4 #(rgb-color 1.0 0.0 0.0)
            c'4 \(
            d'4
            \colorSpan #-4 #4 #(rgb-color 0.0 0.0 1.0)
            e'4 \) \(
            f'4
            <> \)
        }

    '''

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
        Spanner.__init__(
            self,
            overrides=overrides,
            )
        self._color = color

    ### PRIVATE METHODS ###

    def _format_after_leaf(self, leaf):
        result = Spanner._format_after_leaf(self, leaf)
        if self._is_my_last_leaf(leaf):
            next_leaf = leaf._get_leaf(1)
            if (
                next_leaf is None or
                not inspect_(next_leaf).has_spanner(type(self))
                ):
                result.append(r'<> \)')
        return result

    def _format_before_leaf(self, leaf):
        import consort
        result = []
        if self._is_my_first_leaf(leaf):
            result.extend(Spanner._format_before_leaf(self, leaf))
            if isinstance(self._color, consort.Color):
                string = r'\colorSpan #-4 #4 {}'.format(
                    self._color._lilypond_format,
                    )
            else:
                string = r"\colorSpan #-4 #4 #(x11-color '{})"
            string = string.format(self._color)
            result.append(string)
        return result

    def _format_right_of_leaf(self, leaf):
        result = []
        if self._is_my_first_leaf(leaf):
            previous_leaf = leaf._get_leaf(-1)
            if (
                previous_leaf is not None and
                inspect_(previous_leaf).has_spanner(type(self))
                ):
                result.append(r'\)')
            result.append(r'\(')
        return result

    ### PUBLIC PROPERTIES ###

    @property
    def color(self):
        return self._color
