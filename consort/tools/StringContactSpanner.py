# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad import inspect_
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import spannertools
from abjad.tools import scoretools
from abjad.tools import lilypondnametools


class StringContactSpanner(spannertools.Spanner):
    r'''String contact spanner.

    ::

        >>> import consort
        >>> staff = Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
        >>> attach(indicatortools.StringContactPoint('sul ponticello'),
        ...     staff[0], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('sul tasto'),
        ...     staff[2], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('sul tasto'),
        ...     staff[4], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('pizzicato'),
        ...     staff[5], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('ordinario'),
        ...     staff[6], scope=Staff)
        >>> attach(consort.StringContactSpanner(), staff[:])
        >>> print(format(staff))
        \new Staff {
            \once \override TextSpanner.arrow-width = 0.25
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.left.text = \markup {
                \concat
                    {
                        \caps
                            S.P.
                        \hspace
                            #0.25
                    }
                }
            \once \override TextSpanner.bound-details.right-broken.padding = 0
            \once \override TextSpanner.bound-details.right.arrow = ##t
            \once \override TextSpanner.bound-details.right.padding = 1.5
            \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center
            \once \override TextSpanner.dash-fraction = 1
            c'8 \startTextSpan
            d'8
            e'8 \stopTextSpan ^ \markup {
                \caps
                    S.T.
                }
            f'8
            \once \override TextSpanner.arrow-width = 0.25
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.left.text = \markup {
                \concat
                    {
                        \override
                            #'(padding . 0.75)
                            \parenthesize
                                \smaller
                                    \caps
                                        S.T.
                        \hspace
                            #0.25
                    }
                }
            \once \override TextSpanner.bound-details.right-broken.padding = 0
            \once \override TextSpanner.bound-details.right.arrow = ##t
            \once \override TextSpanner.bound-details.right.padding = 1.5
            \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center
            \once \override TextSpanner.dash-fraction = 1
            g'8 \stopTextSpan \startTextSpan
            \once \override TextSpanner.arrow-width = 0.25
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.left.text = \markup {
                \concat
                    {
                        \caps
                            Pizz.
                        \hspace
                            #0.25
                    }
                }
            \once \override TextSpanner.bound-details.right-broken.padding = 0
            \once \override TextSpanner.bound-details.right.arrow = ##t
            \once \override TextSpanner.bound-details.right.padding = 1.5
            \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center
            \once \override TextSpanner.dash-fraction = 1
            a'8 \stopTextSpan \startTextSpan
            b'8 \stopTextSpan ^ \markup {
                \caps
                    Ord.
                }
            c''8
        }
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(
        self,
        overrides=None,
        ):
        spannertools.Spanner.__init__(
            self,
            overrides=overrides,
            )

    ### PRIVATE METHODS ###

    def _get_annotations(self, leaf):
        prototype = indicatortools.StringContactPoint
        agent = inspect_(leaf)

        previous_attached = None
        previous_effective = agent.get_effective(prototype, n=-1)

        current_attached = None
        current_effective = agent.get_effective(prototype)
        indicators = inspect_(leaf).get_indicators(prototype)
        if indicators:
            current_attached = indicators[0]

        next_attached = None
        next_effective = agent.get_effective(prototype, n=1)

        leaves = self._get_leaves()
        index = leaves.index(leaf)
        for i in range(index + 1, len(leaves)):
            next_leaf = leaves[i]
            indicators = next_leaf._get_indicators(
                indicatortools.StringContactPoint,
                )
            if indicators:
                next_attached = indicators[0]
                break
        for i in reversed(range(index)):
            previous_leaf = leaves[i]
            indicators = previous_leaf._get_indicators(
                indicatortools.StringContactPoint,
                )
            if indicators:
                previous_attached = indicators[0]
                break

        return (
            current_attached,
            current_effective,
            next_attached,
            next_effective,
            previous_attached,
            previous_effective,
            )

    def _get_lilypond_format_bundle(self, leaf):
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)
        if not isinstance(leaf, scoretools.Leaf):
            return lilypond_format_bundle
        (
            current_attached,
            current_effective,
            next_attached,
            next_effective,
            previous_attached,
            previous_effective,
            ) = self._get_annotations(leaf)
#        print(leaf)
#        print('CURR ATT:', current_attached)
#        print('CURR EFF:', current_effective)
#        print('NEXT ATT:', next_attached)
#        print('NEXT EFF:', next_effective)
#        print('PREV ATT:', previous_attached)
#        print('PREV EFF:', previous_effective)
        markup = self._get_markup(
            leaf,
            current_attached,
            current_effective,
            next_attached,
            next_effective,
            previous_attached,
            previous_effective,
            )
        if markup is None:
            #print()
            return lilypond_format_bundle
        markup = markuptools.Markup(markup, Up)
        is_cautionary = False
        if current_attached and current_attached == previous_effective:
            is_cautionary = True
        if not self._is_my_first_leaf(leaf) and previous_attached is None:
            is_cautionary = True
        if is_cautionary:
            markup = markup.parenthesize()
            markup = markup.override(('padding', 0.1))
        should_attach_markup = False
        if current_attached is not None and \
            next_attached is not None and \
            next_attached != current_attached:
            should_attach_markup = True
            line_segment = indicatortools.Arrow(
                dash_fraction=0.25,
                dash_period=1,
                left_padding=4,
                right_padding=4,
                )
            string = r'\startTextSpan'
            lilypond_format_bundle.right.spanner_starts.append(string)
            overrides = line_segment._get_lilypond_grob_overrides()
            for override_ in overrides:
                override_string = '\n'.join(override_._override_format_pieces)
                lilypond_format_bundle.grob_overrides.append(override_string)
        if current_attached is not None and previous_attached is not None:
            string = r'\stopTextSpan'
            lilypond_format_bundle.right.spanner_stops.append(string)
        if current_attached is not None and (
            next_attached is None or next_attached == current_attached):
            should_attach_markup = True
        elif current_attached is None and self._is_my_first_leaf(leaf):
            should_attach_markup = True
        if should_attach_markup:
            markup = markup.italic()
            markup = markup.vcenter()
            lilypond_format_bundle.right.markup.append(markup)
        #print()

        return lilypond_format_bundle

    def _get_markup(
        self,
        leaf,
        current_attached,
        current_effective,
        next_attached,
        next_effective,
        previous_attached,
        previous_effective,
        ):
        if current_attached is None and self._is_my_first_leaf(leaf):
            if previous_attached is None:
                if next_attached is not None:
                    return next_attached.markup
        if current_attached == previous_attached == next_attached:
            return None
        if current_attached == previous_effective and next_attached is None:
            return None
        if current_attached:
            return current_attached.markup
        return None