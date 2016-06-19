# -*- encoding: utf-8 -*-
from abjad import iterate
from abjad.tools import indicatortools
from abjad.tools import scoretools
from abjad.tools import stringtools
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
            e'2 \parenthesizeDynamic \p
            f'2
            g'2
            a'2
            b'2 \p
            c''2 \f
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    _scheme = stringtools.normalize('''
    parenthesizeDynamic = #(define-event-function (parser location dyn) (ly:event?)
        (make-dynamic-script
            #{ \markup \concat {
                \normal-text \italic \fontsize #2 (
                \pad-x #0.2 #(ly:music-property dyn 'text)
                \normal-text \italic \fontsize #2 )
            }
            #}))
    ''')

    ### PRIVATE METHODS ###

    def _attachment_test_all(self, component_expression):
        return True

    def _get_lilypond_format_bundle(self, component):
        indicators = component._get_indicators(
            indicatortools.Dynamic)
        assert len(indicators) == 1
        bundle = systemtools.LilyPondFormatBundle()
        if self.name == 'niente':
            return bundle
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
        previous_name = previous_indicator.name
        previous_name = \
            self._composite_dynamic_name_to_steady_state_dynamic_name.get(
                previous_name, previous_name)
        if previous_name != self.name:
            bundle.right.indicators.append(string)
            return bundle
        if not isinstance(previous_component, scoretools.Leaf):
            previous_component = next(iterate(previous_component).by_leaf())
        if component._logical_measure_number is None:
            component._update_logical_measure_numbers()
        measure_number = component._logical_measure_number
        previous_measure_number = previous_component._logical_measure_number
        assert measure_number is not None
        assert previous_measure_number is not None
        if measure_number == previous_measure_number:
            return bundle
        elif abs(measure_number - previous_measure_number) == 1:
            string = r'\parenthesizeDynamic {}'.format(string)
            bundle.right.indicators.append(string)
            return bundle
        bundle.right.indicators.append(string)
        return bundle
