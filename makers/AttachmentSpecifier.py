# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad.tools import datastructuretools
from abjad.tools import sequencetools
from abjad.tools import spannertools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import new
from experimental.tools import selectortools
from abjad.tools import abctools


class AttachmentSpecifier(abctools.AbjadValueObject):
    r'''An attachment specifier.

    ::

        >>> from consort import makers
        >>> attachment_specifier = makers.AttachmentSpecifier(
        ...     attachments=(indicatortools.Articulation('>'),),
        ...     selector=selectortools.Selector().by_leaves().by_run(Note)[0],
        ...     )
        >>> print(format(attachment_specifier))
        makers.AttachmentSpecifier(
            attachments=(
                indicatortools.Articulation('>'),
                ),
            selector=selectortools.Selector(
                callbacks=(
                    selectortools.PrototypeSelectorCallback(
                        scoretools.Leaf
                        ),
                    selectortools.RunSelectorCallback(
                        scoretools.Note
                        ),
                    selectortools.SliceSelectorCallback(0),
                    ),
                ),
            )

    ::

        >>> attachment_specifier = makers.AttachmentSpecifier(
        ...     attachments=(
        ...         makers.DynamicExpression(
        ...             hairpin_start_token='sfz',
        ...             hairpin_stop_token='o',
        ...             ),
        ...         ),
        ...     selector=selectortools.Selector().by_leaves().by_run(Note),
        ...     )

    ::

        >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
        >>> attachment_specifier(staff)
        >>> print(format(staff))
        \new Staff {
            c'8 \sfz
            r8
            d'8 \sfz
            e'8
            r8
            \override Hairpin #'circled-tip = ##t
            f'8 \> \sfz
            g'8
            a'8 \!
            \revert Hairpin #'circled-tip
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachments',
        '_selector',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachments=None,
        selector=None,
        ):
        if attachments is not None:
            if not isinstance(attachments, collections.Sequence):
                attachments = (attachments,)
            attachments = tuple(attachments)
        self._attachments = attachments
        if selector is not None:
            assert isinstance(selector, selectortools.Selector)
        self._selector = selector

    ### PUBLIC METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        if not self.attachments or not self.selector:
            return
        all_attachments = datastructuretools.CyclicTuple(self.attachments)
        all_attachments = sequencetools.rotate_sequence(all_attachments, seed)
        selections = self.selector(music)
        for i, selection in enumerate(selections):
            attachments = all_attachments[i]
            if attachments is None:
                continue
            if not isinstance(attachments, tuple):
                attachments = (attachments,)
            for attachment in attachments:
                if isinstance(attachment, spannertools.Spanner):
                    attach(attachment, selection)
                elif hasattr(attachment, '__call__'):
                    attachment(selection)
                else:
                    for component in selection:
                        attach(attachment, component)

    ### PUBLIC METHODS ###

    def reverse(self):
        attachments = sequencetools.Sequence(*self.attachments)
        return new(self,
            attachments=attachments.reverse(),
            )

    def rotate(self, n=0):
        attachments = sequencetools.Sequence(*self.attachments)
        return new(self,
            attachments=attachments.rotate(n),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachments(self):
        return self._attachments

    @property
    def selector(self):
        return self._selector