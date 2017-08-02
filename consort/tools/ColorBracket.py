import abjad
from abjad.tools.spannertools.Spanner import Spanner


class ColorBracket(Spanner):
    r'''A color bracket.

    ..  note::

        Requires a Scheme definition for the ``\colorSpan`` command.

    ::

        >>> staff = abjad.Staff("c'4 d'4 e'4 f'4")
        >>> print(format(staff))
        \new Staff {
            c'4
            d'4
            e'4
            f'4
        }

    ::

        >>> red_bracket = consort.ColorBracket('red')
        >>> blue_bracket = consort.ColorBracket('blue')
        >>> abjad.attach(red_bracket, staff[:2])
        >>> abjad.attach(blue_bracket, staff[2:])
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

        >>> staff = abjad.Staff("c'4 d'4 e'4 f'4")
        >>> red = consort.Color(1, 0, 0)
        >>> blue = consort.Color(0, 0, 1)
        >>> red_bracket = consort.ColorBracket(red)
        >>> blue_bracket = consort.ColorBracket(blue)
        >>> abjad.attach(red_bracket, staff[:2])
        >>> abjad.attach(blue_bracket, staff[2:])
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

    ::

        >>> staff = abjad.Staff("r2 d'2 r2")
        >>> red_bracket = consort.ColorBracket(red)
        >>> abjad.attach(red_bracket, staff[1:2])
        >>> print(format(staff))
        \new Staff {
            r2
            \colorSpan #-4 #4 #(rgb-color 1.0 0.0 0.0)
            d'2 \(
            <> \)
            r2
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

    def _get_lilypond_format_bundle(self, leaf):
        import consort
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)
        if self._is_my_first_leaf(leaf):
            # Add color command
            if isinstance(self._color, consort.Color):
                string = r'\colorSpan #-4 #4 {}'.format(
                    self._color._lilypond_format,
                    )
            else:
                string = r"\colorSpan #-4 #4 #(x11-color '{})"
            string = string.format(self._color)
            lilypond_format_bundle.opening.commands.append(string)
            # Check for previous spanner and terminate if it exists
            previous_leaf = leaf._get_leaf(-1)
            if (
                previous_leaf is not None and
                abjad.inspect(previous_leaf).has_spanner(type(self))
                ):
                string = r'\)'
                lilypond_format_bundle.right.spanner_stops.append(string)
            # Start the spanner
            string = r'\('
            lilypond_format_bundle.right.spanner_starts.append(string)
        if self._is_my_last_leaf(leaf):
            # Check for next spanner, don't terminate if it exists
            next_leaf = leaf._get_leaf(1)
            if (
                next_leaf is None or
                not abjad.inspect(next_leaf).has_spanner(type(self))
                ):
                string = r'<> \)'
                lilypond_format_bundle.closing.commands.append(string)
        return lilypond_format_bundle

    ### PUBLIC PROPERTIES ###

    @property
    def color(self):
        return self._color
