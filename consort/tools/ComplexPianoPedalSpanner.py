from abjad.tools import spannertools


class ComplexPianoPedalSpanner(spannertools.Spanner):
    r'''Complex piano pedal spanner.

    ::

        >>> spanner = consort.ComplexPianoPedalSpanner()
        >>> print(format(spanner))
        consort.tools.ComplexPianoPedalSpanner(
            include_inner_leaves=False,
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_include_inner_leaves',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        include_inner_leaves=False,
        overrides=None,
        ):
        spannertools.Spanner.__init__(
            self,
            overrides=overrides,
            )
        self._include_inner_leaves = bool(include_inner_leaves)

    ### PRIVATE PROPERTIES ###

    def _copy_keyword_args(self, new):
        new._include_inner_leaves = self.include_inner_leaves

    def _get_lilypond_format_bundle(self, leaf):
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)
        if self._is_my_first_leaf(leaf):
            string = r'\sustainOn'
            lilypond_format_bundle.right.spanner_starts.append(string)
        elif self.include_inner_leaves and not self._is_my_last_leaf(leaf):
            string = r'\sustainOff \sustainOn'
            lilypond_format_bundle.right.spanner_starts.append(string)
        if self._is_my_last_leaf(leaf):
            string = r'<> \sustainOff'
            lilypond_format_bundle.after.indicators.append(string)
        return lilypond_format_bundle

    ### PUBLIC PROPERTIES ###

    @property
    def include_inner_leaves(self):
        return self._include_inner_leaves
