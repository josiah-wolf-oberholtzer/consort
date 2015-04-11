# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad import attach
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import lilypondnametools
from abjad.tools import mathtools
from abjad.tools import schemetools
from abjad.tools import scoretools
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

    ..  container:: example

        ::

            >>> music = Staff("{ r4 c'4 r4 } { r4 d'4 r4 } { r4 e' r4 } ")
            >>> dynamic_expression(music)
            >>> print(format(music))
            \new Staff {
                {
                    r4
                    \once \override Hairpin.stencil = #flared-hairpin
                    c'4 \f \>
                    r4
                }
                {
                    r4
                    d'4 \p \>
                    r4
                }
                {
                    r4
                    e'4 \pp
                    r4
                }
            }

    ..  container:: example

        ::

            >>> music = Staff("{ c'16 c'16 }")
            >>> dynamic_expression(music)
            >>> print(format(music))
            \new Staff {
                {
                    c'16 \f
                    c'16
                }
            }

    ..  container:: example

        ::

            >>> music = Staff("{ c'1 }")
            >>> dynamic_expression = consort.DynamicExpression(
            ...     dynamic_tokens='fp',
            ...     )
            >>> dynamic_expression(music)
            >>> print(format(music))
            \new Staff {
                {
                    c'1 \fp
                }
            }

    ..  container:: example

        ::

            >>> music = Staff("{ c'1 }")
            >>> dynamic_expression = consort.DynamicExpression(
            ...     dynamic_tokens='fp',
            ...     unsustained=True,
            ...     )
            >>> dynamic_expression(music)
            >>> print(format(music))
            \new Staff {
                {
                    c'1 \p
                }
            }

    ..  container:: example

        ::

            >>> music = Staff(r'''
            ...     { c'4 d'4 e'4 }
            ...     { c'4 d'4 e'4 }
            ...     { c'4 d'4 e'4 }
            ...     { c'4 d'4 e'4 }
            ...     { c'4 d'4 e'4 }
            ... ''')
            >>> dynamic_expression = consort.DynamicExpression(
            ...     division_period=2,
            ...     dynamic_tokens='p ppp',
            ...     start_dynamic_tokens='o',
            ...     stop_dynamic_tokens='o',
            ...     )
            >>> dynamic_expression(music)
            >>> print(format(music))
            \new Staff {
                {
                    \once \override Hairpin.circled-tip = ##t
                    c'4 \<
                    d'4
                    e'4
                }
                {
                    c'4
                    d'4
                    e'4
                }
                {
                    \once \override Hairpin.circled-tip = ##t
                    c'4 \p \>
                    d'4
                    e'4
                }
                {
                    c'4
                    d'4
                    e'4
                }
                {
                    c'4
                    d'4
                    e'4 \!
                }
            }

    ..  container:: exmaple

        ::

            >>> music = Staff("{ c'8. } { e'8. } { g'8. }")
            >>> dynamic_expression = consort.DynamicExpression(
            ...     division_period=2,
            ...     dynamic_tokens='p ppp',
            ...     start_dynamic_tokens='o',
            ...     stop_dynamic_tokens='o',
            ...     )
            >>> dynamic_expression(music)
            >>> print(format(music))
            \new Staff {
                {
                    \once \override Hairpin.circled-tip = ##t
                    c'8. \<
                }
                {
                    e'8.
                }
                {
                    g'8. \p
                }
            }

    ..  container:: example

        ::

            >>> music = Staff(r'''
            ... { c'8 ~ c'4 }
            ... \times 3/4 { d'16 d' d' d' r d' d' r }
            ... ''')
            >>> dynamic_expression = consort.DynamicExpression(
            ...     dynamic_tokens='mf mp fff',
            ...     start_dynamic_tokens='f',
            ...     stop_dynamic_tokens='mf',
            ...     )
            >>> dynamic_expression(music)
            >>> print(format(music))
            \new Staff {
                {
                    c'8 \f ~ \>
                    c'4
                }
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/4 {
                    d'16 \mf
                    d'16
                    d'16
                    d'16
                    r16
                    d'16
                    d'16
                    r16
                }
            }

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_division_period',
        '_dynamic_tokens',
        '_only_first',
        '_start_dynamic_tokens',
        '_stop_dynamic_tokens',
        '_transitions',
        '_unsustained',
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
        dynamic_tokens=('ppp',),
        division_period=None,
        only_first=None,
        start_dynamic_tokens=None,
        stop_dynamic_tokens=None,
        transitions=None,
        unsustained=None,
        ):
        dynamic_tokens = self._tokens_to_cyclic_tuple(dynamic_tokens)
        assert dynamic_tokens
        self._dynamic_tokens = dynamic_tokens
        if division_period is not None:
            division_period = int(division_period)
            assert 0 < division_period
        self._division_period = division_period
        self._start_dynamic_tokens = self._tokens_to_cyclic_tuple(
            start_dynamic_tokens)
        self._stop_dynamic_tokens = self._tokens_to_cyclic_tuple(
            stop_dynamic_tokens)
        if isinstance(transitions, (str, type(None))):
            transitions = [transitions]
        assert all(_ in self._transition_types for _ in transitions)
        transitions = datastructuretools.CyclicTuple(transitions)
        self._transitions = transitions
        if only_first is not None:
            only_first = bool(only_first)
        self._only_first = only_first
        if unsustained is not None:
            unsustained = bool(unsustained)
        self._unsustained = unsustained

    ### SPECIAL METHODS ###

    def __call__(self, music, name=None, seed=0):
        original_seed = seed
        current_dynamic = None
        current_hairpin = None
        selections, components = self._get_selections(music)
        #print(selections)
        #print(components)
        length = len(components)
        if self.only_first:
            length = 1
            components = components[:1]
        for index, component in enumerate(components[:-1]):
            selection = selections[index]
            dynamic, hairpin, hairpin_override = self._get_attachments(
                index, length, seed, original_seed)
            if dynamic != current_dynamic:
                if dynamic.name != 'o':
                    attach(dynamic, component, name=name)
                current_dynamic = dynamic
            if self.unsustained:
                inner_leaves = selection[1:-1]
                prototype = scoretools.Rest
                if (
                    len(inner_leaves) and
                    all(isinstance(_, prototype) for _ in inner_leaves)
                    ):
                    hairpin = None
            if hairpin is not None:
                attach(hairpin, selection, name=name)
                current_hairpin = hairpin
            if current_hairpin is not None and hairpin_override is not None:
                attach(hairpin_override, component, name=name)
            seed += 1
        dynamic, _, _ = self._get_attachments(
            length - 1, length, seed, original_seed)
        if self.unsustained:
            if dynamic is not None:
                if length == 1:
                    if not selections or len(selections[0]) < 4:
                        if dynamic.name in dynamic._composite_dynamic_name_to_steady_state_dynamic_name:
                            dynamic_name = dynamic._composite_dynamic_name_to_steady_state_dynamic_name[dynamic.name]
                            dynamic = indicatortools.Dynamic(dynamic_name)
        if dynamic != current_dynamic and dynamic.name != 'o':
            attach(dynamic, components[-1], name=name)

    ### PRIVATE METHODS ###

    def _get_attachments(self, index, length, seed, original_seed):
        dynamic_seed = seed
        if self.start_dynamic_tokens:
            dynamic_seed -= 1

        this_token = None
        next_token = None
        this_dynamic = None
        next_dynamic = None
        hairpin = None
        hairpin_override = None

        if length == 1:
            if self.start_dynamic_tokens:
                this_token = self.start_dynamic_tokens[original_seed]
            elif self.stop_dynamic_tokens:
                this_token = self.stop_dynamic_tokens[original_seed]
            else:
                this_token = self.dynamic_tokens[dynamic_seed]
            if this_token == 'o':
                this_token = self.dynamic_tokens[dynamic_seed]
        elif length == 2:
            if index == 0:
                if self.start_dynamic_tokens:
                    this_token = self.start_dynamic_tokens[original_seed]
                else:
                    this_token = self.dynamic_tokens[dynamic_seed]
                if self.stop_dynamic_tokens:
                    next_token = self.stop_dynamic_tokens[original_seed]
                else:
                    next_token = self.dynamic_tokens[dynamic_seed + 1]
            elif index == 1:
                if self.stop_dynamic_tokens:
                    this_token = self.stop_dynamic_tokens[original_seed]
                    if (
                        this_token == 'o' and
                        self.start_dynamic_tokens and
                        self.start_dynamic_tokens[original_seed] == 'o'
                        ):
                        this_token = self.dynamic_tokens[dynamic_seed]
                else:
                    this_token = self.dynamic_tokens[dynamic_seed]
            if this_token == next_token == 'o':
                next_token = self.dynamic_tokens[dynamic_seed]
        else:
            #print('!!!', index)
            if index == 0:
                if self.start_dynamic_tokens:
                    this_token = self.start_dynamic_tokens[original_seed]
                    next_token = self.dynamic_tokens[dynamic_seed + 1]
                    #print('A1', this_token, next_token)
                else:
                    this_token = self.dynamic_tokens[dynamic_seed]
                    next_token = self.dynamic_tokens[dynamic_seed + 1]
                    #print('A2', this_token, next_token)
            elif index == length - 1:  # Last component.
                if self.stop_dynamic_tokens:
                    this_token = self.stop_dynamic_tokens[original_seed]
                    #print('B1', this_token, next_token)
                else:
                    this_token = self.dynamic_tokens[dynamic_seed]
                    #print('B2', this_token, next_token)
            elif index == length - 2:  # Next to last component.
                this_token = self.dynamic_tokens[dynamic_seed]
                if self.stop_dynamic_tokens:
                    next_token = self.stop_dynamic_tokens[original_seed]
                    #print('C1', this_token, next_token)
                else:
                    next_token = self.dynamic_tokens[dynamic_seed + 1]
                    #print('C2', this_token, next_token)
            else:
                this_token = self.dynamic_tokens[dynamic_seed]
                next_token = self.dynamic_tokens[dynamic_seed + 1]
                #print('D1', this_token, next_token)

        this_dynamic = indicatortools.Dynamic(this_token)
        this_dynamic_ordinal = mathtools.NegativeInfinity()
        if this_dynamic.name != 'o':
            this_dynamic_ordinal = this_dynamic.ordinal
        if next_token is not None:
            next_dynamic = indicatortools.Dynamic(next_token)
            next_dynamic_ordinal = mathtools.NegativeInfinity()
            if next_dynamic.name != 'o':
                next_dynamic_ordinal = next_dynamic.ordinal

        if next_dynamic is not None:
            if this_dynamic_ordinal < next_dynamic_ordinal:
                hairpin = spannertools.Crescendo(include_rests=True)
            elif next_dynamic_ordinal < this_dynamic_ordinal:
                hairpin = spannertools.Decrescendo(include_rests=True)

        if hairpin is not None:
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
            if this_dynamic.name == 'o' or next_dynamic.name == 'o':
                hairpin_override = lilypondnametools.LilyPondGrobOverride(
                    grob_name='Hairpin',
                    is_once=True,
                    property_path='circled-tip',
                    value=True,
                    )

        #print(index, this_dynamic, next_dynamic, hairpin)

        return this_dynamic, hairpin, hairpin_override

    def _partition_selections(self, music):
        period = self.division_period or 1
        selections = [_.select_leaves() for _ in music]
        parts = sequencetools.partition_sequence_by_counts(
            selections, [period], cyclic=True, overhang=True)
        if len(parts[-1]) < period and 1 < len(parts):
            part = parts.pop()
            parts[-1].extend(part)
        selections = []
        for part in parts:
            selection = part[0]
            for next_selection in part[1:]:
                selection = selection + next_selection
            selections.append(selection)
        return selections

    def _reorganize_selections(self, selections):
        prototype = (scoretools.Note, scoretools.Chord)
        for i, leaf in enumerate(selections[0]):
            if isinstance(leaf, prototype):
                break
        selections[0] = selections[0][i:]
        for i, leaf in enumerate(reversed(selections[-1])):
            if isinstance(leaf, prototype):
                break
        if i == 0:
            i = None
        else:
            i = -i
        selections[-1] = selections[-1][:i]
        if len(selections) == 1:
            return selections
        for i in range(len(selections) - 1):
            selection_one, selection_two = selections[i], selections[i + 1]
            for j, leaf in enumerate(selection_two):
                if isinstance(leaf, prototype):
                    break
            if 0 < j:
                left, right = selection_two[:j], selection_two[j:]
                selection_one = selection_one + left
                selection_two = right
                selections[i] = selection_one
                selections[i + 1] = selection_two
        return selections

    def _get_selections(self, music):
        r"""Gets selections and attach components from `music`.

        ..  container:: example

            ::

                >>> music = Staff(r'''
                ...     { c'4 d'4 e'4 f'4 }
                ...     { g'4 a'4 b'4 }
                ...     { c''4 }
                ... ''')
                >>> dynamic_expression = consort.DynamicExpression("f")
                >>> result = dynamic_expression._get_selections(music)
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
                >>> dynamic_expression = consort.DynamicExpression("f")
                >>> result = dynamic_expression._get_selections(music)
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
                >>> result = dynamic_expression._get_selections(music)
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

        ..  container:: example

            ::

                >>> music = Staff("{ r4 c'4 r4 } { r4 d'4 r4 } { r4 e' r4 } ")
                >>> result = dynamic_expression._get_selections(music)
                >>> selections, attach_components = result
                >>> for _ in selections:
                ...     _
                ...
                ContiguousSelection(Note("c'4"), Rest('r4'), Rest('r4'), Note("d'4"))
                ContiguousSelection(Note("d'4"), Rest('r4'), Rest('r4'), Note("e'4"))

            ::

                >>> for _ in attach_components:
                ...     _
                ...
                Note("c'4")
                Note("d'4")
                Note("e'4")

        ..  container:: example

            ::

                >>> music = Staff("{ c'8. } { e'8. } { g'8. }")
                >>> dynamic_expression = consort.DynamicExpression(
                ...     division_period=2,
                ...     dynamic_tokens='p ppp',
                ...     start_dynamic_tokens='o',
                ...     stop_dynamic_tokens='o',
                ...     )
                >>> result = dynamic_expression._get_selections(music)
                >>> selections, attach_components = result
                >>> for _ in selections:
                ...     _
                ...
                ContiguousSelection(Note("c'8."), Note("e'8."), Note("g'8."))

            ::

                >>> for _ in attach_components:
                ...     _
                ...
                Note("c'8.")
                Note("g'8.")

        """
        #print('---', music)
        initial_selections = self._partition_selections(music)
        initial_selections = self._reorganize_selections(initial_selections)
        #print('   ', initial_selections)
        attach_components = []
        selections = []
        assert len(initial_selections)
        for i, selection in enumerate(initial_selections):
            if i < len(initial_selections) - 1:
                selection = selection + (initial_selections[i + 1][0],)
                selections.append(selection)
                attach_components.append(selection[0])
            elif ((selection.get_duration() <= durationtools.Duration(1, 8) and
                1 < len(selections)) or len(selection) == 1
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
        #print('   ', attach_components)
        return selections, attach_components

    def _tokens_to_cyclic_tuple(self, tokens):
        if tokens is None:
            return tokens
        if isinstance(tokens, str):
            tokens = tokens.split()
        for token in tokens:
            if token == 'o':
                continue
            assert token in indicatortools.Dynamic._dynamic_names
        assert len(tokens)
        tokens = datastructuretools.CyclicTuple(tokens)
        return tokens

    ### PUBLIC PROPERTIES ###

    @property
    def division_period(self):
        return self._division_period

    @property
    def dynamic_tokens(self):
        return self._dynamic_tokens

    @property
    def only_first(self):
        return self._only_first

    @property
    def period(self):
        return self._period

    @property
    def start_dynamic_tokens(self):
        return self._start_dynamic_tokens

    @property
    def stop_dynamic_tokens(self):
        return self._stop_dynamic_tokens

    @property
    def transitions(self):
        return self._transitions

    @property
    def unsustained(self):
        return self._unsustained