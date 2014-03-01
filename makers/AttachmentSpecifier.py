# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import sequencetools
from abjad.tools import spannertools
from abjad.tools.topleveltools import attach
from experimental.tools import selectortools


class AttachmentSpecifier(abctools.AbjadObject):
    r'''An attachment specifier.

    ::

        >>> from consort import makers
        >>> attachment_specifier = makers.AttachmentSpecifier(
        ...     attachments=(indicatortools.Articulation('>'),),
        ...     selector=selectortools.Selector().by_leaves().by_run(Note)[0],
        ...     )
        >>> print format(attachment_specifier)
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

        >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
        >>> attachment_specifier(staff)
        >>> print format(staff)
        \new Staff {
            c'8 -\accent
            r8
            d'8 -\accent
            e'8
            r8
            f'8 -\accent
            g'8
            a'8
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
        assert isinstance(attachments, tuple)
        self._attachments = attachments
        assert isinstance(selector, selectortools.Selector)
        self._selector = selector

    ### PUBLIC METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
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
                else:
                    for component in selection:
                        attach(attachment, component)

    ### PUBLIC PROPERTIES ###

    @property
    def attachments(self):
        return self._attachments

    @property
    def selector(self):
        return self._selector