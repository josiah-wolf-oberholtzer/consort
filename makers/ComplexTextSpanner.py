# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import lilypondnametools
from abjad.tools import spannertools
from abjad.tools import markuptools


class ComplexTextSpanner(spannertools.Spanner):
    r'''A complex text spanner.

    ::

        >>> from consort import makers
        >>> staff = Staff("c'4 d'4 r4 e'4")
        >>> spanner_one = makers.ComplexTextSpanner(
        ...     direction=Up,
        ...     markup='foo',
        ...     )
        >>> spanner_two = makers.ComplexTextSpanner(
        ...     direction=Down,
        ...     markup='bar',
        ...     )
        >>> attach(spanner_one, staff[:2])
        >>> attach(spanner_two, staff[3:])
        >>> print(format(staff))
        \new Staff {
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.text = \markup { foo }
            \once \override TextSpanner.bound-details.right-broken.text = ##f
            \once \override TextSpanner.bound-details.right.text = \markup {
                \draw-line
                    #'(0 . -1)
                }
            \once \override TextSpanner.dash-fraction = 1
            \once \override TextSpanner.direction = #up
            c'4 \startTextSpan
            d'4
            <> \stopTextSpan
            r4
            e'4 _ \markup { bar }
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_direction',
        '_markup',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        direction=None,
        markup=None,
        overrides=None,
        ):
        spannertools.Spanner.__init__(
            self,
            overrides=overrides,
            )
        assert direction in (Up, Down, None)
        self._direction = direction
        self._markup = markuptools.Markup(markup)

    ### PRIVATE METHODS ###

    def _copy_keyword_args(self, new):
        new._markup = self.markup

    def _get_lilypond_format_bundle(self, leaf):
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)

        if self._is_my_only_leaf(leaf) and \
            leaf.written_duration < durationtools.Duration(1, 8):
            direction = self.direction or Up
            markup = markuptools.Markup(
                self.markup.contents,
                direction,
                )
            lilypond_format_bundle.right.markup.append(markup)
            return lilypond_format_bundle

        if self._is_my_first_leaf(leaf):

            override = lilypondnametools.LilyPondGrobOverride(
                grob_name='TextSpanner',
                is_once=True,
                property_path=('bound-details', 'left', 'text'),
                value=self.markup,
                )
            lilypond_format_bundle.update(override)

            override = lilypondnametools.LilyPondGrobOverride(
                grob_name='TextSpanner',
                is_once=True,
                property_path=('bound-details', 'left-broken', 'text'),
                value=False,
                )
            lilypond_format_bundle.update(override)

            override = lilypondnametools.LilyPondGrobOverride(
                grob_name='TextSpanner',
                is_once=True,
                property_path=('bound-details', 'right', 'text'),
                value=markuptools.Markup(r"\draw-line #'(0 . -1)")
                )
            lilypond_format_bundle.update(override)

            override = lilypondnametools.LilyPondGrobOverride(
                grob_name='TextSpanner',
                is_once=True,
                property_path=('bound-details', 'right-broken', 'text'),
                value=False,
                )
            lilypond_format_bundle.update(override)

            override = lilypondnametools.LilyPondGrobOverride(
                grob_name='TextSpanner',
                is_once=True,
                property_path=('dash-fraction',),
                value=1,
                )
            lilypond_format_bundle.update(override)

            if self.direction is not None:
                override = lilypondnametools.LilyPondGrobOverride(
                    grob_name='TextSpanner',
                    is_once=True,
                    property_path=('direction',),
                    value=self.direction,
                    )
                lilypond_format_bundle.update(override)

            string = r'\startTextSpan'
            lilypond_format_bundle.right.spanner_starts.append(string)

        if self._is_my_last_leaf(leaf):
            string = r'<> \stopTextSpan'
            lilypond_format_bundle.after.indicators.append(string)

        return lilypond_format_bundle

    ### PUBLIC PROPERTIES ###

    @property
    def direction(self):
        return self._direction

    @property
    def markup(self):
        return self._markup