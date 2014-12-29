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
        >>> attach(indicatortools.StringContactPoint('sul tasto'),
        ...     staff[2], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('sul tasto'),
        ...     staff[3], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('ordinario'),
        ...     staff[4], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('pizzicato'),
        ...     staff[5], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('ordinario'),
        ...     staff[6], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('sul ponticello'),
        ...     staff[7], scope=Staff)
        >>> attach(consort.StringContactSpanner(), staff[:])
        >>> print(format(staff))
        \new Staff {
            c'8 ^ \markup {
                \caps
                    S.T.
                }
            d'8
            e'8 ^ \markup {
                \parenthesize
                    \caps
                        S.T.
                }
            f'8 ^ \markup {
                \parenthesize
                    \caps
                        S.T.
                }
            g'8 ^ \markup {
                \caps
                    Ord.
                }
            a'8 ^ \markup {
                \caps
                    Pizz.
                }
            b'8 ^ \markup {
                \caps
                    Ord.
                }
            c''8 ^ \markup {
                \caps
                    S.P.
                }
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
        leaves = self._get_leaves()
        index = leaves.index(leaf)
        prototype = indicatortools.StringContactPoint
        agent = inspect_(leaf)
        pizzicato = indicatortools.StringContactPoint('pizzicato')

        previous_effective = agent.get_effective(prototype, n=-1)
        previous_attached = None
        for i in reversed(range(index)):
            previous_leaf = leaves[i]
            indicators = previous_leaf._get_indicators(
                indicatortools.StringContactPoint,
                )
            if indicators:
                previous_attached = indicators[0]
                break

        next_attached = None
        for i in range(index + 1, len(leaves)):
            next_leaf = leaves[i]
            indicators = next_leaf._get_indicators(
                indicatortools.StringContactPoint,
                )
            if indicators:
                next_attached = indicators[0]
                break

        current_attached = None
        indicators = inspect_(leaf).get_indicators(prototype)
        if indicators:
            current_attached = indicators[0]
        if self._is_my_first_leaf(leaf) and current_attached is None:
            current_attached = next_attached

        next_different = None
        for i in range(index + 1, len(leaves)):
            next_leaf = leaves[i]
            indicators = next_leaf._get_indicators(
                indicatortools.StringContactPoint,
                )
            if indicators:
                indicator = indicators[0]
                if indicator is not None and indicator != current_attached:
                    next_different = indicator
                    break

        starts_segment = False
        if current_attached is not None and \
            next_attached is not None and \
            current_attached != pizzicato and \
            next_different != pizzicato and \
            current_attached != next_attached:
            starts_segment = True

        stops_segment = False
        if current_attached is not None and \
            current_attached != pizzicato and \
            (next_different == pizzicato or next_different is None):
            stops_segment = True

        is_cautionary = False
        if current_attached and current_attached == previous_effective:
            is_cautionary = True
        if not self._is_my_first_leaf(leaf) and previous_attached is None:
            is_cautionary = True

        current_markup = None
        if current_attached is None and self._is_my_first_leaf(leaf):
            if next_attached is not None:
                current_markup = next_attached.markup
        elif current_attached is not None:
            current_markup = current_attached.markup
        elif current_attached == previous_attached == next_attached:
            current_markup = None
        elif current_attached == previous_effective and next_attached is None:
            current_markup = None

        if current_markup is not None:
            current_markup = markuptools.Markup(current_markup, 'up')
            if is_cautionary:
                current_markup = current_markup.parenthesize()

        return (
            current_attached,
            current_markup,
            is_cautionary,
            next_attached,
            next_different,
            previous_attached,
            previous_effective,
            starts_segment,
            stops_segment,
            )

    def _get_lilypond_format_bundle(self, leaf):
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)
        if not isinstance(leaf, scoretools.Leaf):
            return lilypond_format_bundle
        (
            current_attached,
            current_markup,
            is_cautionary,
            next_attached,
            next_different,
            previous_attached,
            previous_effective,
            starts_segment,
            stops_segment,
            ) = self._get_annotations(leaf)

        if current_markup is None:
            return lilypond_format_bundle

        if starts_segment and stops_segment:
            lilypond_format_bundle.right.markup.append(current_markup)
        elif stops_segment:
            lilypond_format_bundle.right.markup.append(current_markup)
        else:
            lilypond_format_bundle.right.markup.append(current_markup)

        return lilypond_format_bundle

    def _get_markup(
        self,
        leaf,
        current_attached,
        next_attached,
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

    def _add_segment_start_contributions(
        lilypond_format_bundle,
        start_markup=None,
        stop_markup=None,
        ):
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
        if start_markup:
            override_ = lilypondnametools.LilyPondGrobOverride(
                grob_name='TextSpanner',
                is_once=True,
                property_path=(
                    'bound-details',
                    'left',
                    'text',
                    ),
                value=start_markup,
                )
            override_string = '\n'.join(override_._override_format_pieces)
            lilypond_format_bundle.grob_overrides.append(override_string)
        if stop_markup:
            override_ = lilypondnametools.LilyPondGrobOverride(
                grob_name='TextSpanner',
                is_once=True,
                property_path=(
                    'bound-details',
                    'right',
                    'text',
                    ),
                value=stop_markup,
                )
            override_string = '\n'.join(override_._override_format_pieces)
            lilypond_format_bundle.grob_overrides.append(override_string)

    def _add_segment_stop_contributions(
        lilypond_format_bundle,
        ):
        string = r'\stopTextSpan'
        lilypond_format_bundle.right.spanner_stops.append(string)