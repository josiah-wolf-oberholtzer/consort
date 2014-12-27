# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad import attach
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondnametools
from abjad.tools import schemetools
from abjad.tools import spannertools


class DynamicExpression(abctools.AbjadValueObject):
    r"""A dynamic phrasing expression.

    ::

        >>> import consort
        >>> dynamic_expression = consort.DynamicExpression(
        ...     dynamic_tokens='f p pp pp',
        ...     transitions=('flared', None),
        ...     )
        >>> print(format(dynamic_expression))
        consort.tools.DynamicExpression(
            dynamic_tokens=datastructuretools.CyclicTuple(
                ['f', 'p', 'pp', 'pp']
                ),
            transitions=datastructuretools.CyclicTuple(
                ['flared', None]
                ),
            )

    ..  container:: example

        ::

            >>> music = Staff(r'''
            ...     { c'4 d'4 e'4 f'4 }
            ...     { g'4 a'4 b'4 }
            ...     { c''4 }
            ... ''')
            >>> print(format(music))
            \new Staff {
                {
                    c'4
                    d'4
                    e'4
                    f'4
                }
                {
                    g'4
                    a'4
                    b'4
                }
                {
                    c''4
                }
            }

        ::

            >>> dynamic_expression(music)
            >>> print(format(music))
            \new Staff {
                {
                    \once \override Hairpin.stencil = #flared-hairpin
                    c'4 \f \>
                    d'4
                    e'4
                    f'4
                }
                {
                    g'4 \p \>
                    a'4
                    b'4
                }
                {
                    c''4 \pp
                }
            }

    ..  container:: example

        ::

            >>> music = Staff(r'''
            ...     { c'4 d'4 e'4 f'4 }
            ...     { g'4 a'4 b'4 }
            ...     { c''4 c'4 }
            ... ''')

        ::

            >>> dynamic_expression(music, seed=2)
            >>> print(format(music))
            \new Staff {
                {
                    c'4 \pp
                    d'4
                    e'4
                    f'4
                }
                {
                    g'4 \<
                    a'4
                    b'4
                }
                {
                    \once \override Hairpin.stencil = #flared-hairpin
                    c''4 \f \>
                    c'4 \p
                }
            }

    ..  container:: example

        ::

            >>> music = Staff("{ c'4 }")
            >>> dynamic_expression(music, seed=1)
            >>> print(format(music))
            \new Staff {
                {
                    c'4 \p
                }
            }

    ..  container:: example

        ::

            >>> music = Staff("{ c'4 d'4 }")
            >>> dynamic_expression(music, seed=1)
            >>> print(format(music))
            \new Staff {
                {
                    c'4 \p \>
                    d'4 \pp
                }
            }

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_dynamic_tokens',
        '_transitions',
        )

    _transition_types = (
        'constante',
        'flared',
        'simple',
        None,
        )

    ### INITIALIZER ###

    def __init__(
        self,
        dynamic_tokens=('f', 'p'),
        transitions=None,
        ):
        if isinstance(dynamic_tokens, str):
            dynamic_tokens = dynamic_tokens.split()
        assert all(_ in indicatortools.Dynamic._dynamic_name_to_dynamic_ordinal
            for _ in dynamic_tokens)
        assert len(dynamic_tokens)
        dynamic_tokens = datastructuretools.CyclicTuple(dynamic_tokens)
        self._dynamic_tokens = dynamic_tokens
        if isinstance(transitions, (str, type(None))):
            transitions = [transitions]
        assert all(_ in self._transition_types for _ in transitions)
        transitions = datastructuretools.CyclicTuple(transitions)
        self._transitions = transitions

    ### SPECIAL METHODS ###

    def __call__(self, music, name=None, seed=0):
        current_dynamic = None
        current_hairpin = None
        selections = self._get_selections(music)
        if 1 < len(selections):
            for selection in selections[:-1]:
                dynamic, hairpin, transition = self._get_attachments(seed)
                #print('A', seed, selection, dynamic, hairpin, transition)
                #print('?', self.dynamic_tokens[seed], self.dynamic_tokens)
                if dynamic != current_dynamic:
                    if current_hairpin is not None:
                        current_hairpin._extend([selection[0]])
                    current_dynamic = dynamic
                    attach(dynamic, selection[0], name=name)
                if hairpin is not None:
                    current_hairpin = hairpin
                    attach(hairpin, selection, name=name)
                    hairpin_override = self._get_hairpin_override(
                        transition)
                    if hairpin_override is not None:
                        attach(hairpin_override, selection[0], name=name)
                elif current_hairpin is not None:
                    #print('SELECTION', selection)
                    #print('LEAVES', current_hairpin._get_leaves())
                    if current_hairpin._is_my_last_leaf(selection[0]):
                        current_hairpin._extend(selection[1:])
                    else:
                        current_hairpin._extend(selection)
                seed += 1
        dynamic, hairpin, transition = self._get_attachments(seed)
        selection = selections[-1]
        #print('B', seed, selection, dynamic, hairpin, transition)
        #print('?', self.dynamic_tokens[seed], self.dynamic_tokens)
        if selection.get_duration() <= durationtools.Duration(1, 8):
            if current_hairpin is not None:
                current_hairpin._extend(selection)
                if dynamic != current_dynamic:
                    attach(dynamic, selection[-1], name=name)
            else:
                attach(dynamic, selection[0], name=name)
                if 1 < len(selection) and transition == 'constante':
                    attach(hairpin, selection, name=name)
                    hairpin_override = self._get_hairpin_override(transition)
                    if hairpin_override is not None:
                        attach(hairpin_override, selection[0], name=name)
        else:
            if dynamic != current_dynamic:
                if current_hairpin:
                    current_hairpin._extend([selection[0]])
                current_dynamic = dynamic
                attach(dynamic, selection[0], name=name)
                if hairpin is not None:
                    current_hairpin = hairpin
                    if 1 < len(selection):
                        attach(hairpin, selection, name=name)
                        hairpin_override = self._get_hairpin_override(transition)
                        if hairpin_override is not None:
                            attach(hairpin_override, selection[0], name=name)
            elif current_hairpin is not None:
                current_hairpin._extend(selection)
            seed += 1
            dynamic, _, _ = self._get_attachments(seed)
            #print('C', seed, selection, dynamic, hairpin, transition)
            #print('?', self.dynamic_tokens[seed], self.dynamic_tokens)
            if dynamic != current_dynamic and 1 < len(selection):
                attach(dynamic, selection[-1], name=name)
        #print()

    ### PRIVATE METHODS ###

    def _get_attachments(self, i):
        this_dynamic = indicatortools.Dynamic(self.dynamic_tokens[i])
        next_dynamic = indicatortools.Dynamic(self.dynamic_tokens[i + 1])
        if this_dynamic.ordinal < next_dynamic.ordinal:
            hairpin = spannertools.Crescendo(include_rests=True)
        elif next_dynamic.ordinal < this_dynamic.ordinal:
            hairpin = spannertools.Decrescendo(include_rests=True)
        else:
            hairpin = None
        transition = self.transitions[i]
        if transition == 'constante':
            hairpin = spannertools.Crescendo(include_rests=True)
        return this_dynamic, hairpin, transition

    def _get_hairpin_override(self, transition):
        grob_override = None
        if transition in ('flared', 'constante'):
            grob_override = lilypondnametools.LilyPondGrobOverride(
                grob_name='Hairpin',
                is_once=True,
                property_path='stencil',
                value=schemetools.Scheme('{}-hairpin'.format(transition)),
                )
        return grob_override

    def _get_selections(self, music):
        selections = []
        for division in music:
            selection = division.select_leaves()
            selections.append(selection)
        return selections

    ### PUBLIC PROPERTIES ###

    @property
    def dynamic_tokens(self):
        return self._dynamic_tokens

    @property
    def transitions(self):
        return self._transitions