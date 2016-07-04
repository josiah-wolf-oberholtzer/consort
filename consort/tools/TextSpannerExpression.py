# -*- encoding: utf-8 -*-
from abjad import abctools
from abjad import attach
from abjad import iterate
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import markuptools
from abjad.tools import spannertools


class TextSpannerExpression(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_markup_tokens',
        '_transitions',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        markup_tokens=None,
        transitions=None,
        ):
        if markup_tokens is not None:
            coerced_markup_tokens = []
            for x in markup_tokens:
                if isinstance(x, (markuptools.Markup, type(None))):
                    markup = x
                elif hasattr(x, 'markup'):
                    markup = x.markup
                elif hasattr(x, '_get_markup'):
                    markup = x._get_markup()
                else:
                    markup = markuptools.Markup(x)
                coerced_markup_tokens.append(markup)
            markup_tokens = datastructuretools.CyclicTuple(
                coerced_markup_tokens)
        self._markup_tokens = markup_tokens
        if transitions:
            prototype = (indicatortools.LineSegment, type(None))
            assert len(transitions)
            assert all(isinstance(_, prototype) for _ in transitions)
            transitions = datastructuretools.CyclicTuple(transitions)
        self._transitions = transitions

    ### SPECIAL METHODS ###

    def __call__(self, music, name=None, seed=0):
        selections = self._get_selections(music)
        if 1 < len(selections):
            for selection in selections[:-1]:
                markup, transition = self._get_attachments(seed)
                # do stuff
                seed += 1
        markup, transition = self._get_attachments(seed)
        selection = selections[-1]
        if selection.get_duration() <= durationtools.Duration(1, 8):
            # do stuff
            pass
        else:
            # do stuff
            seed += 1
            markup, transition = self._get_attachments(seed)
            # do stuff
        text_spanner = spannertools.TextSpanner()
        attach(text_spanner, music, name=name)

    ### PRIVATE METHODS ###

    def _get_selections(self, music):
        selections = []
        for division in music:
            selection = list(iterate(division).by_leaf())
            selections.append(selection)
        return selections

    ### PUBLIC PROPERTIES ###

    @property
    def markup_tokens(self):
        return self._markup_tokens

    @property
    def transitions(self):
        return self._transitions
