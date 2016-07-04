# -*- encoding: utf-8 -*-
from abjad import attach
from abjad import inspect_
from abjad import iterate
from abjad import override
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import instrumenttools
from abjad.tools import selectiontools
from abjad.tools import spannertools


class SimpleDynamicExpression(abctools.AbjadValueObject):
    r'''A dynamic expression.

    ..  container:: example

        ::

            >>> import consort
            >>> dynamic_expression = consort.SimpleDynamicExpression(
            ...     hairpin_start_token='sfp',
            ...     hairpin_stop_token='niente',
            ...     )

        ::

            >>> staff = Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
            >>> dynamic_expression(staff[2:-2])
            >>> print(format(staff))
            \new Staff {
                c'8
                d'8
                \override Hairpin.circled-tip = ##t
                e'8 \> \sfp
                f'8
                g'8
                a'8 \!
                \revert Hairpin.circled-tip
                b'8
                c''8
            }

    ..  container:: example

        ::

            >>> dynamic_expression = consort.SimpleDynamicExpression(
            ...     'f', 'p',
            ...     )
            >>> staff = Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
            >>> dynamic_expression(staff[2:-2])
            >>> print(format(staff))
            \new Staff {
                c'8
                d'8
                e'8 \> \f
                f'8
                g'8
                a'8 \p
                b'8
                c''8
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_hairpin_start_token',
        '_hairpin_stop_token',
        '_minimum_duration',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        hairpin_start_token='p',
        hairpin_stop_token=None,
        minimum_duration=durationtools.Duration(1, 4),
        ):
        known_dynamics = indicatortools.Dynamic._dynamic_names
        assert hairpin_start_token in known_dynamics, \
            (known_dynamics, hairpin_start_token)
        if hairpin_stop_token is not None:
            assert hairpin_stop_token in known_dynamics
        assert hairpin_start_token != 'niente' or hairpin_stop_token != 'niente'
        if hairpin_start_token == 'niente':
            assert hairpin_stop_token is not None
        self._hairpin_start_token = hairpin_start_token
        self._hairpin_stop_token = hairpin_stop_token
        if minimum_duration is not None:
            minimum_duration = durationtools.Duration(minimum_duration)
        self._minimum_duration = minimum_duration

    ### SPECIAL METHODS ###

    def __call__(self, music, name=None):
        if not isinstance(music, selectiontools.Selection):
            music = selectiontools.Selection(music)
        is_short_group = False
        if len(music) < 2:
            is_short_group = True
        elif self.minimum_duration is not None:
            if music.get_duration() < self.minimum_duration:
                is_short_group = True
        instrument = inspect_(music[0]).get_effective(
            instrumenttools.Instrument,
            )
        logical_ties = tuple(iterate(music).by_logical_tie(pitched=True))
        if len(logical_ties) < 3:
            if instrument == instrumenttools.Piano() or \
                instrument == instrumenttools.Percussion():
                is_short_group = True
        grace_notes = None
        previous_leaf = inspect_(music[0]).get_leaf(-1)
        if previous_leaf is not None:
            graces = inspect_(previous_leaf).get_grace_containers('after')
            if graces:
                assert len(graces) == 1
                grace_notes = list(iterate(graces[0]).by_leaf())
                music = selectiontools.ContiguousSelect(
                    tuple(grace_notes) + tuple(music),
                    )
        start_token = self.hairpin_start_token
        stop_token = self.hairpin_stop_token
        if is_short_group or stop_token is None:
            if start_token == 'niente':
                start_token = stop_token
            if start_token.startswith('fp'):
                start_token = start_token[1:]
            command = indicatortools.LilyPondCommand(start_token, 'right')
            attach(command, music[0], name=name)
            return
        start_ordinal = NegativeInfinity
        if start_token != 'niente':
            start_ordinal = indicatortools.Dynamic.dynamic_name_to_dynamic_ordinal(
                start_token)
        stop_ordinal = NegativeInfinity
        if stop_token != 'niente':
            stop_ordinal = indicatortools.Dynamic.dynamic_name_to_dynamic_ordinal(stop_token)
        items = []
        is_circled = False
        if start_ordinal < stop_ordinal:
            if start_token != 'niente':
                items.append(start_token)
            else:
                is_circled = True
            items.append('<')
            items.append(stop_token)
        elif stop_ordinal < start_ordinal:
            items.append(start_token)
            items.append('>')
            if stop_token != 'niente':
                items.append(stop_token)
            else:
                #items.append('!')
                is_circled = True
        hairpin_descriptor = ' '.join(items)
        hairpin = spannertools.Hairpin(
            descriptor=hairpin_descriptor,
            include_rests=False,
            )
        if is_circled:
            override(hairpin).hairpin.circled_tip = True
        attach(hairpin, music, name=name)

    ### PUBLIC PROPERTIES ###

    @property
    def hairpin_start_token(self):
        return self._hairpin_start_token

    @property
    def hairpin_stop_token(self):
        return self._hairpin_stop_token

    @property
    def minimum_duration(self):
        return self._minimum_duration
