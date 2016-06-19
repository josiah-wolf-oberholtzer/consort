# -*- encoding: utf-8 -*-
from abjad import iterate
from abjad.tools import indicatortools
from abjad.tools import scoretools
from abjad.tools import systemtools


class Dynamic(indicatortools.Dynamic):
    r'''A fancy dynamic.

    ::


        >>> staff = Staff("c'2 d'2 e'2 f'2 g'2 a'2 b'2 c''2")
        >>> piano = Dynamic('p')
        >>> forte = Dynamic('f')
        >>> attach(piano, staff[0])
        >>> attach(piano, staff[1])
        >>> attach(piano, staff[2])
        >>> attach(piano, staff[6])
        >>> attach(forte, staff[7])
        >>> print(format(staff))
        \new Staff {
            c'2 \p
            d'2 \p
            e'2 \p
            f'2
            g'2
            a'2
            b'2 \p
            c''2 \f
        }

    ::

        >>> import consort
        >>> staff = Staff("c'2 d'2 e'2 f'2 g'2 a'2 b'2 c''2")
        >>> piano = consort.Dynamic('p')
        >>> forte = consort.Dynamic('f')
        >>> attach(piano, staff[0])
        >>> attach(piano, staff[1])
        >>> attach(piano, staff[2])
        >>> attach(piano, staff[6])
        >>> attach(forte, staff[7])
        >>> print(format(staff))
        \new Staff {
            c'2 \p
            d'2
            e'2 \parenthesize \p
            f'2
            g'2
            a'2
            b'1 \p
            c''2 \f
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### PRIVATE METHODS ###

    def _get_lilypond_format_bundle(self, component):
        bundle = systemtools.LilyPondFormatBundle()
        string = r'\{}'.format(self.name)
        if not isinstance(component, scoretools.Leaf):
            component = next(iterate(component).by_leaf())
        indicator_expression = component._get_effective(
            indicatortools.Dynamic,
            unwrap=False,
            n=-1,
            )
        if indicator_expression is None:
            bundle.right.indicators.append(string)
            return bundle
        previous_indicator = indicator_expression.indicator
        previous_component = indicator_expression.component
        if previous_indicator.name != self.name:
            bundle.right.indicators.append(string)
            return bundle
        if not isinstance(previous_component, scoretools.Leaf):
            previous_component = next(iterate(previous_component).by_leaf())
        if component._logical_measure_number is None:
            component._update_logical_measure_numbers()
        logical_measure = component._logical_measure_number
        previous_logical_measure = previous_component._logical_measure_number
        if logical_measure == previous_logical_measure:
            return bundle
        elif abs(logical_measure - previous_logical_measure) == 1:
            string = r'\parenthesize {}'.format(string)
            bundle.right.indicators.append(string)
            return bundle
        bundle.right.indicators.append(string)
        return bundle
