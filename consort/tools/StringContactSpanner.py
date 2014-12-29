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

    ..  doctest::

        >>> print(format(staff))
        \new Staff {
            c'8 ^ \markup {
                \vcenter
                    \italic
                        \caps
                            S.T.
                }
            d'8
            e'8
            \once \override TextSpanner.arrow-width = 0.25
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.left.text = \markup {
                \halign
                    #0
                    \halign
                        #0
                        \concat
                            {
                                \hspace
                                    #1
                                \parenthesize
                                    \caps
                                        S.T.
                                \hspace
                                    #1
                            }
                }
            \once \override TextSpanner.bound-details.right-broken.padding = 0
            \once \override TextSpanner.bound-details.right.arrow = ##t
            \once \override TextSpanner.bound-details.right.padding = 0
            \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.right.text = \markup {
                \halign
                    #0
                    \halign
                        #0
                        \concat
                            {
                                \hspace
                                    #1
                                \caps
                                    Ord.
                                \hspace
                                    #1
                            }
                }
            \once \override TextSpanner.dash-fraction = 0.25
            \once \override TextSpanner.dash-period = 1
            f'8 \startTextSpan
            g'8 \stopTextSpan ^ \markup {
                \vcenter
                    \italic
                        \caps
                            Ord.
                }
            a'8 ^ \markup {
                \vcenter
                    \italic
                        \caps
                            Pizz.
                }
            \once \override TextSpanner.arrow-width = 0.25
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.left.text = \markup {
                \halign
                    #0
                    \halign
                        #0
                        \concat
                            {
                                \hspace
                                    #1
                                \caps
                                    Ord.
                                \hspace
                                    #1
                            }
                }
            \once \override TextSpanner.bound-details.right-broken.padding = 0
            \once \override TextSpanner.bound-details.right.arrow = ##t
            \once \override TextSpanner.bound-details.right.padding = 0
            \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.right.text = \markup {
                \halign
                    #0
                    \halign
                        #0
                        \concat
                            {
                                \hspace
                                    #1
                                \caps
                                    S.P.
                                \hspace
                                    #1
                            }
                }
            \once \override TextSpanner.dash-fraction = 0.25
            \once \override TextSpanner.dash-period = 1
            b'8 \stopTextSpan \startTextSpan
            c''8 \stopTextSpan
        }

    ::

        >>> staff = Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
        >>> attach(indicatortools.StringContactPoint('ordinario'),
        ...     staff[0], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('sul tasto'),
        ...     staff[2], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('ordinario'),
        ...     staff[4], scope=Staff)
        >>> attach(indicatortools.StringContactPoint('sul tasto'),
        ...     staff[6], scope=Staff)
        >>> attach(consort.StringContactSpanner(), staff[:])

    ..  doctest::

        >>> print(format(staff))
        \new Staff {
            \once \override TextSpanner.arrow-width = 0.25
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.left.text = \markup {
                \halign
                    #0
                    \halign
                        #0
                        \concat
                            {
                                \hspace
                                    #1
                                \caps
                                    Ord.
                                \hspace
                                    #1
                            }
                }
            \once \override TextSpanner.bound-details.right-broken.padding = 0
            \once \override TextSpanner.bound-details.right.arrow = ##t
            \once \override TextSpanner.bound-details.right.padding = 3.5
            \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center
            \once \override TextSpanner.dash-fraction = 0.25
            \once \override TextSpanner.dash-period = 1
            c'8 \startTextSpan
            d'8
            \once \override TextSpanner.arrow-width = 0.25
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.left.text = \markup {
                \halign
                    #0
                    \halign
                        #0
                        \concat
                            {
                                \hspace
                                    #1
                                \caps
                                    S.T.
                                \hspace
                                    #1
                            }
                }
            \once \override TextSpanner.bound-details.right-broken.padding = 0
            \once \override TextSpanner.bound-details.right.arrow = ##t
            \once \override TextSpanner.bound-details.right.padding = 3.5
            \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center
            \once \override TextSpanner.dash-fraction = 0.25
            \once \override TextSpanner.dash-period = 1
            e'8 \stopTextSpan \startTextSpan
            f'8
            \once \override TextSpanner.arrow-width = 0.25
            \once \override TextSpanner.bound-details.left-broken.text = ##f
            \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.left.text = \markup {
                \halign
                    #0
                    \halign
                        #0
                        \concat
                            {
                                \hspace
                                    #1
                                \caps
                                    Ord.
                                \hspace
                                    #1
                            }
                }
            \once \override TextSpanner.bound-details.right-broken.padding = 0
            \once \override TextSpanner.bound-details.right.arrow = ##t
            \once \override TextSpanner.bound-details.right.padding = 0
            \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center
            \once \override TextSpanner.bound-details.right.text = \markup {
                \halign
                    #0
                    \halign
                        #0
                        \concat
                            {
                                \hspace
                                    #1
                                \caps
                                    S.T.
                                \hspace
                                    #1
                            }
                }
            \once \override TextSpanner.dash-fraction = 0.25
            \once \override TextSpanner.dash-period = 1
            g'8 \stopTextSpan \startTextSpan
            a'8
            b'8 \stopTextSpan
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
        leaves = self._get_leaves()
        index = leaves.index(leaf)
        prototype = indicatortools.StringContactPoint
        agent = inspect_(leaf)
        pizzicato = indicatortools.StringContactPoint('pizzicato')

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
        next_next_different = None
        for i in range(index + 1, len(leaves)):
            next_leaf = leaves[i]
            indicators = next_leaf._get_indicators(
                indicatortools.StringContactPoint,
                )
            if indicators:
                indicator = indicators[0]
                if indicator != current_attached and next_different is None:
                    next_different = indicator
                if next_different is not None and indicator != next_different:
                    next_next_different = indicator
                    break

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
        if current_attached is not None and \
            not self._is_my_first_leaf(leaf) and \
            previous_attached is None:
            previous_attached = current_attached

        previous_different = None
        for i in reversed(range(index)):
            previous_leaf = leaves[i]
            indicators = previous_leaf._get_indicators(
                indicatortools.StringContactPoint,
                )
            if indicators:
                indicator = indicators[0]
                if indicator != current_attached:
                    previous_different = indicator

        has_start_markup = False
        if current_attached is not None and \
            next_attached is not None and \
            current_attached != pizzicato and \
            next_different != pizzicato and \
            current_attached != next_attached:
            has_start_markup = True

        has_stop_markup = False
        if current_attached is not None and \
            current_attached != pizzicato and \
            (next_next_different == pizzicato or next_next_different is None):
            has_stop_markup = True

        stops_text_spanner = False
        if current_attached is not None and \
            previous_different is not None and \
            current_attached != pizzicato and \
            previous_different != pizzicato:
            stops_text_spanner = True

        is_cautionary = False
        if current_attached and current_attached == previous_attached:
            is_cautionary = True

        current_markup = None
        if current_attached is not None:
            current_markup = current_attached.markup
        if current_attached == previous_attached == next_attached and \
            current_attached != pizzicato:
            current_markup = None
        elif current_attached == previous_effective and \
            next_attached is None and \
            current_attached != pizzicato:
            current_markup = None
#        elif current_attached == previous_effective and \
#            current_attached == pizzicato:
#            current_markup = None

        if current_markup is not None:
            if is_cautionary:
                current_markup = current_markup.parenthesize()

        results = (
            current_attached,
            current_markup,
            has_start_markup,
            has_stop_markup,
            is_cautionary,
            next_attached,
            next_different,
            previous_attached,
            previous_effective,
            stops_text_spanner,
            )

        #print(leaf)
        #for _ in results:
        #    print('\t', _)

        return results

    def _get_lilypond_format_bundle(self, leaf):
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)
        if not isinstance(leaf, scoretools.Leaf):
            return lilypond_format_bundle
        (
            current_attached,
            current_markup,
            has_start_markup,
            has_stop_markup,
            is_cautionary,
            next_attached,
            next_different,
            previous_attached,
            previous_effective,
            stops_text_spanner,
            ) = self._get_annotations(leaf)

        if current_markup is None:
            #print('\tRETURNING+++++++++++++++')
            return lilypond_format_bundle

        if has_start_markup and has_stop_markup:
            self._add_segment_start_contributions(
                lilypond_format_bundle,
                start_markup=current_markup,
                stop_markup=next_different.markup,
                )
        elif has_start_markup:
            self._add_segment_start_contributions(
                lilypond_format_bundle,
                start_markup=current_markup,
                )

        if stops_text_spanner:
            self._add_segment_stop_contributions(lilypond_format_bundle)

        should_attach_markup = False
        if current_markup and \
            not has_start_markup and \
            next_different is not None:
            should_attach_markup = True
        if current_markup and \
            current_attached == indicatortools.StringContactPoint('pizzicato'):
            should_attach_markup = True

        if should_attach_markup:
            current_markup = markuptools.Markup(current_markup, Up)
            current_markup = current_markup.italic()
            current_markup = current_markup.vcenter()
            lilypond_format_bundle.right.markup.append(current_markup)

#        pizzicato = indicatortools.StringContactPoint('pizzicato')
#        if current_attached == pizzicato and not previous_attached:
#            current_markup = pizzicato.markup
#            current_markup = markuptools.Markup(current_markup, Up)
#            current_markup = current_markup.italic()
#            current_markup = current_markup.vcenter()
#            lilypond_format_bundle.right.markup.append(current_markup)

        return lilypond_format_bundle

    def _add_segment_start_contributions(
        self,
        lilypond_format_bundle,
        start_markup=None,
        stop_markup=None,
        ):
        right_padding = 0
        if stop_markup is None:
            right_padding = 3.5
        line_segment = indicatortools.Arrow(
            dash_fraction=0.25,
            dash_period=1,
            right_padding=right_padding,
            )

        if start_markup is not None:
            start_markup = markuptools.Markup.concat([
                markuptools.Markup.hspace(1),
                start_markup,
                markuptools.Markup.hspace(1),
                ])
            start_markup = start_markup.halign(0)

        if stop_markup is not None:
            stop_markup = markuptools.Markup.concat([
                markuptools.Markup.hspace(1),
                stop_markup,
                markuptools.Markup.hspace(1),
                ])
            stop_markup = stop_markup.halign(0)

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
                value=start_markup.halign(0),
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
                value=stop_markup.halign(0),
                )
            override_string = '\n'.join(override_._override_format_pieces)
            lilypond_format_bundle.grob_overrides.append(override_string)

    def _add_segment_stop_contributions(
        self,
        lilypond_format_bundle,
        ):
        string = r'\stopTextSpan'
        lilypond_format_bundle.right.spanner_stops.append(string)