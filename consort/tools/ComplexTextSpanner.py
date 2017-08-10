import abjad
from abjad.tools import lilypondnametools
from abjad.tools import spannertools
from abjad.tools import markuptools


class ComplexTextSpanner(spannertools.Spanner):
    r'''A complex text spanner.

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 r4 e'4")
            >>> spanner_one = consort.ComplexTextSpanner(
            ...     direction=Up,
            ...     markup='foo',
            ...     )
            >>> spanner_two = consort.ComplexTextSpanner(
            ...     direction=Down,
            ...     markup='bar',
            ...     )
            >>> abjad.attach(spanner_one, staff[:2])
            >>> abjad.attach(spanner_two, staff[3:])

        ::

            >>> print(format(staff))
            \new Staff {
                \once \override TextSpanner.bound-details.left-broken.text = \markup { foo }
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
                \once \override TextScript.parent-alignment-X = #left
                \once \override TextScript.self-alignment-X = #left
                e'4 _ \markup { bar }
            }

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 f'4")
            >>> spanner_one = consort.ComplexTextSpanner(
            ...     direction=Up,
            ...     markup='foo',
            ...     )
            >>> spanner_two = consort.ComplexTextSpanner(
            ...     direction=Down,
            ...     markup='bar',
            ...     )
            >>> abjad.attach(spanner_one, staff[:2])
            >>> abjad.attach(spanner_two, staff[3:])

        ::

            >>> print(format(staff))
            \new Staff {
                \once \override TextSpanner.bound-details.left-broken.text = \markup { foo }
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
                e'4
                \once \override TextScript.parent-alignment-X = #left
                \once \override TextScript.self-alignment-X = #left
                f'4 _ \markup { bar }
            }

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'8 d' e' r r a' b' c''")
            >>> spanner_one = consort.ComplexTextSpanner(
            ...     direction=Up,
            ...     markup='foo',
            ...     )
            >>> spanner_two = consort.ComplexTextSpanner(
            ...     direction=Up,
            ...     markup='foo',
            ...     )
            >>> abjad.attach(spanner_one, staff[:3])
            >>> abjad.attach(spanner_two, staff[5:])

        ::

            >>> print(format(staff))
            \new Staff {
                \once \override TextSpanner.bound-details.left-broken.text = \markup { foo }
                \once \override TextSpanner.bound-details.left.text = \markup { foo }
                \once \override TextSpanner.bound-details.right-broken.text = ##f
                \once \override TextSpanner.bound-details.right.text = \markup {
                    \draw-line
                        #'(0 . -1)
                    }
                \once \override TextSpanner.dash-fraction = 1
                \once \override TextSpanner.direction = #up
                c'8 \startTextSpan
                d'8
                e'8
                r8
                r8
                a'8
                b'8
                c''8
                <> \stopTextSpan
            }

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'8 d' e' f' g' a' b' c''")
            >>> spanner_one = consort.ComplexTextSpanner(
            ...     direction=Up,
            ...     markup='foo',
            ...     )
            >>> spanner_two = consort.ComplexTextSpanner(
            ...     direction=Down,
            ...     markup='bar',
            ...     )
            >>> spanner_three = consort.ComplexTextSpanner(
            ...     direction=Up,
            ...     markup='foo',
            ...     )
            >>> abjad.attach(spanner_one, staff[:3])
            >>> abjad.attach(spanner_two, staff[3:5])
            >>> abjad.attach(spanner_three, staff[5:])

        ::

            >>> print(format(staff))
            \new Staff {
                \once \override TextSpanner.bound-details.left-broken.text = \markup { foo }
                \once \override TextSpanner.bound-details.left.text = \markup { foo }
                \once \override TextSpanner.bound-details.right-broken.text = ##f
                \once \override TextSpanner.bound-details.right.text = \markup {
                    \draw-line
                        #'(0 . -1)
                    }
                \once \override TextSpanner.dash-fraction = 1
                \once \override TextSpanner.direction = #up
                c'8 \startTextSpan
                d'8
                e'8
                <> \stopTextSpan
                \once \override TextSpanner.bound-details.left-broken.text = \markup { bar }
                \once \override TextSpanner.bound-details.left.text = \markup { bar }
                \once \override TextSpanner.bound-details.right-broken.text = ##f
                \once \override TextSpanner.bound-details.right.text = \markup {
                    \draw-line
                        #'(0 . -1)
                    }
                \once \override TextSpanner.dash-fraction = 1
                \once \override TextSpanner.direction = #down
                f'8 \startTextSpan
                g'8
                <> \stopTextSpan
                \once \override TextSpanner.bound-details.left-broken.text = \markup { foo }
                \once \override TextSpanner.bound-details.left.text = \markup { foo }
                \once \override TextSpanner.bound-details.right-broken.text = ##f
                \once \override TextSpanner.bound-details.right.text = \markup {
                    \draw-line
                        #'(0 . -1)
                    }
                \once \override TextSpanner.dash-fraction = 1
                \once \override TextSpanner.direction = #up
                a'8 \startTextSpan
                b'8
                c''8
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
                return lilypond_format_bundle

            elif previous_is_similar:
                self._make_spanner_stop(lilypond_format_bundle)

            elif next_is_similar:
                self._make_spanner_start(lilypond_format_bundle)

            else:
                self._make_markup(lilypond_format_bundle)

        elif self._is_my_first_leaf(leaf):
            if not self._previous_spanner_is_similar(leaf):
                self._make_spanner_start(lilypond_format_bundle)

        elif self._is_my_last_leaf(leaf):
            if not self._next_spanner_is_similar(leaf):
                self._make_spanner_stop(lilypond_format_bundle)

        return lilypond_format_bundle

    def _make_markup(self, lilypond_format_bundle):
        direction = self.direction or Up
        markup = markuptools.Markup(
            self.markup.contents,
            direction,
            )
        lilypond_format_bundle.right.markup.append(markup)
        override = lilypondnametools.LilyPondGrobOverride(
            grob_name='TextScript',
            is_once=True,
            property_path=('parent-alignment-X',),
            value=Left,
            )
        lilypond_format_bundle.update(override)
        override = lilypondnametools.LilyPondGrobOverride(
            grob_name='TextScript',
            is_once=True,
            property_path=('self-alignment-X',),
            value=Left,
            )
        lilypond_format_bundle.update(override)

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
            value=self.markup,
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

#    def _next_spanner_is_similar(self, leaf):
#        next_leaf = leaf._get_leaf(1)
#        next_spanner = None
#        next_spanner_is_similar = False
#        if next_leaf is not None:
#            spanners = next_leaf._get_spanners(type(self))
#            if spanners:
#                assert len(spanners) == 1
#                next_spanner = tuple(spanners)[0]
#                if next_spanner.direction == self.direction:
#                    if next_spanner.markup == self.markup:
#                        next_spanner_is_similar = True
#        return next_spanner_is_similar

    def _next_spanner_is_similar(self, leaf):
        leaf_prototype = (abjad.Note, abjad.Chord)
        next_spanner = None
        next_spanner_is_similar = False
        for index in range(1, 5):
            next_leaf = leaf._get_leaf(index)
            if next_leaf is None:
                break
            elif isinstance(next_leaf, abjad.MultimeasureRest):
                break
            has_spanner = next_leaf._has_spanner(type(self),
                in_parentage=True)
            if not has_spanner:
                if isinstance(next_leaf, leaf_prototype):
                    break
                continue
            next_spanner = next_leaf._get_spanner(type(self))
            if next_spanner.direction != self.direction:
                break
            if next_spanner.markup != self.markup:
                break
            next_spanner_is_similar = True
        return next_spanner_is_similar

    def _previous_spanner_is_similar(self, leaf):
        leaf_prototype = (abjad.Note, abjad.Chord)
        previous_spanner = None
        previous_spanner_is_similar = False
        for index in range(1, 5):
            previous_leaf = leaf._get_leaf(-index)
            if previous_leaf is None:
                break
            elif isinstance(previous_leaf, abjad.MultimeasureRest):
                break
            has_spanner = previous_leaf._has_spanner(type(self),
                in_parentage=True)
            if not has_spanner:
                if isinstance(previous_leaf, leaf_prototype):
                    break
                continue
            previous_spanner = previous_leaf._get_spanner(type(self))
            if previous_spanner.direction != self.direction:
                break
            if previous_spanner.markup != self.markup:
                break
            previous_spanner_is_similar = True
        return previous_spanner_is_similar

    ### PUBLIC PROPERTIES ###

    @property
    def direction(self):
        return self._direction

    @property
    def markup(self):
        return self._markup
