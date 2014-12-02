# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import spannertools
from abjad.tools.topleveltools import inspect_


class ClefSpanner(spannertools.Spanner):
    r'''Clef spanner.

    ::

        >>> from consort import makers
        >>> staff = Staff("c' d' e' f' g' a' b' c''")
        >>> clef = Clef('treble')
        >>> attach(clef, staff[0])
        >>> print(format(staff))
        \new Staff {
            \clef "treble"
            c'4
            d'4
            e'4
            f'4
            g'4
            a'4
            b'4
            c''4
        }

    ::

        >>> clef_spanner = makers.ClefSpanner('percussion')
        >>> attach(clef_spanner, staff[2:-2])
        >>> print(format(staff))
        \new Staff {
            \clef "treble"
            c'4
            d'4
            \clef "percussion"
            e'4
            f'4
            g'4
            a'4
            \clef "treble"
            b'4
            c''4
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_clef',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        clef='percussion',
        overrides=None,
        ):
        spannertools.Spanner.__init__(
            self,
            overrides=overrides,
            )
        clef = indicatortools.Clef(clef)
        self._clef = clef

    ### SPECIAL METHODS ###

    def __getnewargs__(self):
        r'''Gets new arguments of spanner.

        Returns empty tuple.
        '''
        return (
            self.clef,
            )

    ### PRIVATE METHODS ###

    def _copy_keyword_args(self, new):
        new._clef = self.clef

    def _get_lilypond_format_bundle(self, leaf):
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)
        first_leaf = self._leaves[0]
        current_clef = inspect_(first_leaf).get_effective(indicatortools.Clef)
        if self._is_my_only_leaf(leaf):
            if self.clef != current_clef:
                string = format(self.clef, 'lilypond')
                lilypond_format_bundle.before.indicators.append(string)
                string = format(current_clef, 'lilypond')
                lilypond_format_bundle.after.indicators.append(string)
        elif self._is_my_first_leaf(leaf):
            if self.clef != current_clef:
                string = format(self.clef, 'lilypond')
                lilypond_format_bundle.before.indicators.append(string)
        elif self._is_my_last_leaf(leaf):
            if self.clef != current_clef and current_clef is not None:
                string = format(current_clef, 'lilypond')
                lilypond_format_bundle.after.indicators.append(string)
        return lilypond_format_bundle

    ### PUBLIC PROPERTIES ###

    @property
    def clef(self):
        return self._clef