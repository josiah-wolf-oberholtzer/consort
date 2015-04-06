# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad import attach
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondnametools
from abjad.tools import schemetools
from abjad.tools import sequencetools
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
        original_seed = seed
        current_dynamic = None
        current_hairpin = None
        selections, components = self._get_selections(music)
        length = len(components)
        for index, component in enumerate(components[:-1]):
            selection = selections[index]
            dynamic, hairpin, hairpin_override = self._get_attachments(
                index, length, seed, original_seed)
            #print(index, dynamic, hairpin)
            if dynamic != current_dynamic:
                attach(dynamic, component)
                current_dynamic = dynamic
            if hairpin is not None:
                attach(hairpin, selection)
                current_hairpin = hairpin
            if current_hairpin is not None and hairpin_override is not None:
                attach(hairpin_override, component)
            seed += 1
        dynamic, _, _ = self._get_attachments(
            length - 1, length, seed, original_seed)
        attach(dynamic, components[-1])

    ### PRIVATE METHODS ###

    def _get_attachments(self, index, length, seed, original_seed):
        dynamic_seed = seed
        if self.start_dynamic_tokens:
            dynamic_seed -= 1

        this_token = self.dynamic_tokens[dynamic_seed]
        next_token = self.dynamic_tokens[dynamic_seed + 1]
        this_dynamic = indicatortools.Dynamic(this_token)
        next_dynamic = indicatortools.Dynamic(next_token)

        hairpin = None
        hairpin_override = None
        if this_dynamic.ordinal < next_dynamic.ordinal:
            hairpin = spannertools.Crescendo(include_rests=True)
        elif next_dynamic.ordinal < this_dynamic.ordinal:
            hairpin = spannertools.Decrescendo(include_rests=True)
        transition = self.transitions[seed]
        if transition == 'constante':
            hairpin = spannertools.Crescendo(include_rests=True)
        if transition in ('flared', 'constante'):
            hairpin_override = lilypondnametools.LilyPondGrobOverride(
                grob_name='Hairpin',
                is_once=True,
                property_path='stencil',
                value=schemetools.Scheme('{}-hairpin'.format(transition)),
                )
        return this_dynamic, hairpin, hairpin_override

    @staticmethod
    def _get_selections(music):
        r"""Gets selections and attach components from `music`.

        ..  container:: example

            ::

                >>> music = Staff(r'''
                ...     { c'4 d'4 e'4 f'4 }
                ...     { g'4 a'4 b'4 }
                ...     { c''4 }
                ... ''')
                >>> result = consort.DynamicExpression._get_selections(music)
                >>> selections, attach_components = result
                >>> for _ in selections:
                ...     _
                ...
                ContiguousSelection(Note("c'4"), Note("d'4"), Note("e'4"), Note("f'4"), Note("g'4"))
                ContiguousSelection(Note("g'4"), Note("a'4"), Note("b'4"), Note("c''4"))

            ::

                >>> for _ in attach_components:
                ...     _
                ...
                Note("c'4")
                Note("g'4")
                Note("c''4")

        ..  container:: example

            ::

                >>> music = Staff(r'''
                ...     { c'4 d'4 e'4 }
                ...     { f'4 g'4 a'4 }
                ...     { b'4 c''4 }
                ... ''')
                >>> result = consort.DynamicExpression._get_selections(music)
                >>> selections, attach_components = result
                >>> for _ in selections:
                ...     _
                ...
                ContiguousSelection(Note("c'4"), Note("d'4"), Note("e'4"), Note("f'4"))
                ContiguousSelection(Note("f'4"), Note("g'4"), Note("a'4"), Note("b'4"))
                ContiguousSelection(Note("b'4"), Note("c''4"))

            ::

                >>> for _ in attach_components:
                ...     _
                ...
                Note("c'4")
                Note("f'4")
                Note("b'4")
                Note("c''4")

        ..  container:: example

            ::

                >>> music = Staff(r'''
                ...     { c'8 d'8 e'8 }
                ...     { f'8 g'8 a'8 }
                ...     { b'32 c''16. }
                ... ''')
                >>> result = consort.DynamicExpression._get_selections(music)
                >>> selections, attach_components = result
                >>> for _ in selections:
                ...     _
                ...
                ContiguousSelection(Note("c'8"), Note("d'8"), Note("e'8"), Note("f'8"))
                ContiguousSelection(Note("f'8"), Note("g'8"), Note("a'8"), Note("b'32"), Note("c''16."))

            ::

                >>> for _ in attach_components:
                ...     _
                ...
                Note("c'8")
                Note("f'8")
                Note("c''16.")

        """
        attach_components = []
        selections = []
        for i, division in enumerate(music):
            selection = division.select_leaves()
            if i < len(music) - 1:
                selection = selection + music[i + 1].select_leaves()[:1]
                selections.append(selection)
                attach_components.append(selection[0])
            elif (
                selection.get_duration() <= durationtools.Duration(1, 8) or
                len(selection) == 1
                ):
                attach_components.append(selection[-1])
                if selections:
                    selections[-1] = selections[-1] + selection[1:]
            elif (
                    durationtools.Duration(1, 8) < (
                    selection[-1]._get_timespan().start_offset -
                    selection[0]._get_timespan().start_offset
                        )
                    ):
                selections.append(selection)
                attach_components.append(selection[0])
                attach_components.append(selection[-1])
            else:
                attach_components.append(selection[0])
        return selections, attach_components

    ### PUBLIC PROPERTIES ###

    @property
    def dynamic_tokens(self):
        return self._dynamic_tokens

    @property
    def transitions(self):
        return self._transitions