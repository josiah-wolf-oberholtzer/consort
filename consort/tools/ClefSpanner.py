import abjad
from abjad.tools import spannertools


class ClefSpanner(spannertools.Spanner):
    r'''Clef spanner.

    ::

        >>> staff = abjad.Staff("c' d' e' f' g' a' b' c''")
        >>> clef = abjad.Clef('treble')
        >>> abjad.attach(clef, staff[0])
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

        >>> clef_spanner = consort.ClefSpanner('percussion')
        >>> abjad.attach(clef_spanner, staff[2:-2])
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

    ::

        >>> staff = abjad.Staff("r4 c'4 d'4 r4 e'4 f'4 r4")
        >>> clef = abjad.Clef('treble')
        >>> abjad.attach(clef, staff[0])
        >>> clef_spanner = consort.ClefSpanner('percussion')
        >>> abjad.attach(clef_spanner, staff[1:3])
        >>> clef_spanner = consort.ClefSpanner('percussion')
        >>> abjad.attach(clef_spanner, staff[4:6])
        >>> print(format(staff))
        \new Staff {
            \clef "treble"
            r4
            \clef "percussion"
            c'4
            d'4
            r4
            e'4
            f'4
            \clef "treble"
            r4
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
        clef = abjad.Clef(clef)
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
        import consort
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)

        prototype = (abjad.Note, abjad.Chord, type(None))

        first_leaf = self._get_leaves()[0]
        current_clef = abjad.inspect(first_leaf).get_effective(abjad.Clef)

        set_clef = False
        reset_clef = False

        if self._is_my_only_leaf(leaf):
            consort.debug('ONLY', leaf)
            if self.clef != current_clef:
                set_clef = True
                reset_clef = True

            previous_leaf = abjad.inspect(leaf).get_leaf(-1)
            consort.debug('\tP', previous_leaf)
            while not isinstance(previous_leaf, prototype):
                previous_leaf = abjad.inspect(previous_leaf).get_leaf(-1)
                consort.debug('\tP', previous_leaf)
            if previous_leaf is not None:
                spanners = abjad.inspect(previous_leaf).get_spanners(
                    type(self))
                spanners = tuple(spanners)
                if spanners:
                    consort.debug('\tPREV?', spanners)
                    if spanners[0].clef == self.clef:
                        set_clef = False

            next_leaf = abjad.inspect(leaf).get_leaf(1)
            consort.debug('\tN', next_leaf)
            while not isinstance(next_leaf, prototype):
                next_leaf = abjad.inspect(next_leaf).get_leaf(1)
                consort.debug('\tN', next_leaf)
            if next_leaf is not None:
                spanners = abjad.inspect(next_leaf).get_spanners(type(self))
                spanners = tuple(spanners)
                if spanners:
                    consort.debug('\tNEXT?', spanners)
                    if spanners[0].clef == self.clef:
                        reset_clef = False

        elif self._is_my_first_leaf(leaf):
            consort.debug('FIRST', leaf)
            if self.clef != current_clef:
                set_clef = True

            previous_leaf = abjad.inspect(leaf).get_leaf(-1)
            consort.debug('\tP', previous_leaf)
            while not isinstance(previous_leaf, prototype):
                previous_leaf = abjad.inspect(previous_leaf).get_leaf(-1)
                consort.debug('\tP', previous_leaf)
            if previous_leaf is not None:
                spanners = abjad.inspect(previous_leaf).get_spanners(type(self))
                spanners = tuple(spanners)
                if spanners:
                    consort.debug('\tPREV?', spanners)
                    if spanners[0].clef == self.clef:
                        set_clef = False

        elif self._is_my_last_leaf(leaf):
            consort.debug('LAST', leaf)
            if self.clef != current_clef and current_clef is not None:
                reset_clef = True

            next_leaf = abjad.inspect(leaf).get_leaf(1)
            consort.debug('\tN', next_leaf)
            while not isinstance(next_leaf, prototype):
                next_leaf = abjad.inspect(next_leaf).get_leaf(1)
                consort.debug('\tN', next_leaf)
            if next_leaf is not None:
                spanners = abjad.inspect(next_leaf).get_spanners(type(self))
                spanners = tuple(spanners)
                if spanners:
                    consort.debug('\tNEXT?', spanners)
                    if spanners[0].clef == self.clef:
                        reset_clef = False

        if set_clef:
            string = format(self.clef, 'lilypond')
            lilypond_format_bundle.before.indicators.append(string)

        if reset_clef and current_clef is not None:
            string = format(current_clef, 'lilypond')
            lilypond_format_bundle.after.indicators.append(string)

        return lilypond_format_bundle

    ### PUBLIC PROPERTIES ###

    @property
    def clef(self):
        return self._clef
