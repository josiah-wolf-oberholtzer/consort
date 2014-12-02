# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import lilypondnametools
from abjad.tools import spannertools
from abjad.tools import markuptools


class ComplexTextSpanner(spannertools.Spanner):
    r'''A complex text spanner.

    ::

        >>> import consort
        >>> staff = Staff("c'4 d'4 r4 e'4")
        >>> spanner_one = consort.attachmenttools.ComplexTextSpanner(
        ...     direction=Up,
        ...     markup='foo',
        ...     )
        >>> spanner_two = consort.attachmenttools.ComplexTextSpanner(
        ...     direction=Down,
        ...     markup='bar',
        ...     )
        >>> attach(spanner_one, staff[:2])
        >>> attach(spanner_two, staff[3:])

    ::

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
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.text = \markup { bar }
            \once \override TextSpanner.bound-details.right-broken.text = ##f
            \once \override TextSpanner.bound-details.right.text = \markup {
                \draw-line
                    #'(0 . -1)
                }
            \once \override TextSpanner.dash-fraction = 1
            \once \override TextSpanner.direction = #down
            e'4 \startTextSpan
            <> \stopTextSpan
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

        if self._is_my_only_leaf(leaf):
            previous_is_similar = self._previous_spanner_is_similar(leaf)
            next_is_similar = self._next_spanner_is_similar(leaf)

            if previous_is_similar and next_is_similar:
                pass

            elif previous_is_similar:
                self._make_spanner_stop(lilypond_format_bundle)

            elif next_is_similar:
                self._make_spanner_start(lilypond_format_bundle)

            elif leaf.written_duration < durationtools.Duration(1, 8):
                self._make_markup(lilypond_format_bundle)

            else:
                self._make_spanner_start(lilypond_format_bundle)
                self._make_spanner_stop(lilypond_format_bundle)

        elif self._is_my_first_leaf(leaf):
            if not self._previous_spanner_is_similar(leaf):
                self._make_spanner_start(lilypond_format_bundle)

        elif self._is_my_last_leaf(leaf):
            if not self._next_spanner_is_similar(leaf):
                self._make_spanner_stop(lilypond_format_bundle)

        return lilypond_format_bundle

    def _previous_spanner_is_similar(self, leaf):
        previous_leaf = leaf._get_leaf(-1)
        previous_spanner = None
        previous_spanner_is_similar = False
        if previous_leaf is not None:
            spanners = previous_leaf._get_spanners(type(self))
            if spanners:
                assert len(spanners) == 1
                previous_spanner = tuple(spanners)[0]
                if previous_spanner.direction == self.direction:
                    if previous_spanner.markup == self.markup:
                        previous_spanner_is_similar = True
        return previous_spanner_is_similar

    def _next_spanner_is_similar(self, leaf):
        next_leaf = leaf._get_leaf(1)
        next_spanner = None
        next_spanner_is_similar = False
        if next_leaf is not None:
            spanners = next_leaf._get_spanners(type(self))
            if spanners:
                assert len(spanners) == 1
                next_spanner = tuple(spanners)[0]
                if next_spanner.direction == self.direction:
                    if next_spanner.markup == self.markup:
                        next_spanner_is_similar = True
        return next_spanner_is_similar

    def _make_spanner_start(self, lilypond_format_bundle):
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

    def _make_spanner_stop(self, lilypond_format_bundle):
        string = r'<> \stopTextSpan'
        lilypond_format_bundle.after.indicators.append(string)

    def _make_markup(self, lilypond_format_bundle):
        direction = self.direction or Up
        markup = markuptools.Markup(
            self.markup.contents,
            direction,
            )
        lilypond_format_bundle.right.markup.append(markup)

    ### PUBLIC PROPERTIES ###

    @property
    def direction(self):
        return self._direction

    @property
    def markup(self):
        return self._markup