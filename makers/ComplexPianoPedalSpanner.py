# -*- encoding: utf-8 -*-
from abjad.tools.spannertools.Spanner import Spanner


class ComplexPianoPedalSpanner(Spanner):
    r'''Complex piano pedal spanner.

    ::

        >>> from consort import makers
        >>> spanner = makers.ComplexPianoPedalSpanner()
        >>> print(format(spanner))
        consort.makers.ComplexPianoPedalSpanner(
            include_inner_leaves=False,
            let_vibrate=False,
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_include_inner_leaves',
        '_let_vibrate',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        include_inner_leaves=False,
        let_vibrate=False,
        overrides=None,
        ):
        Spanner.__init__(
            self,
            overrides=overrides,
            )
        self._include_inner_leaves = bool(include_inner_leaves)
        self._let_vibrate = bool(let_vibrate)

    ### PRIVATE PROPERTIES ###

    def _copy_keyword_args(self, new):
        new._include_inner_leaves = self.include_inner_leaves
        new._let_vibrate = self.let_vibrate

    def _format_right_of_leaf(self, leaf):
        result = []
        if self._is_my_first_leaf(leaf):
            result.append(r'\sustainOn')
        elif self.include_inner_leaves and not self._is_my_last_leaf(leaf):
            result.append(r'\sustainOff \sustainOn')
        return result

    def _format_before_leaf(self, leaf):
        from abjad.tools import lilypondnametools
        from abjad.tools import schemetools
        result = []
        if self.let_vibrate:
            next_leaf = leaf._get_leaf(1)
            if self._is_my_last_leaf(next_leaf) or \
                self._is_my_first_leaf(leaf) and \
                not self.include_inner_leaves:
                override = lilypondnametools.LilyPondGrobOverride(
                    grob_name='PianoPedalBracket',
                    is_once=True,
                    property_path='edge-height',
                    value=schemetools.SchemePair(1, 0, quoting="'"),
                    )
                result.append('\n'.join(override.override_format_pieces))
        return result

    def _format_after_leaf(self, leaf):
        result = []
        if self._is_my_last_leaf(leaf):
            next_leaf = leaf._get_leaf(1)
            if next_leaf is not None:
                result.append(r'<> \sustainOff')
            if self.let_vibrate:
                result.append(r'\LV')
        return result

    ### PUBLIC PROPERTIES ###

    @property
    def include_inner_leaves(self):
        return self._include_inner_leaves

    @property
    def let_vibrate(self):
        return self._let_vibrate