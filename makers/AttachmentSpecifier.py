# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from experimental.tools import selectortools


class AttachmentSpecifier(abctools.AbjadObject):
    r'''An attachment specifier.

    ::

        >>> from consort import makers
        >>> attachment_specifier = makers.AttachmentSpecifier(
        ...     attachments=(indicatortools.Articulation('>'),),
        ...     selector=selectortools.Selector().by_leaves()[0],
        ...     )
        >>> print format(attachment_specifier)
        makers.AttachmentSpecifier(
            attachments=(
                indicatortools.Articulation(),
                ),
            selector=selectortools.Selector(
                callbacks=(
                    selectortools.PrototypeSelectorCallback(
                        scoretools.Leaf
                        ),
                    selectortools.SliceSelectorCallback(0),
                    ),
                ),
            )

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

    ### PUBLIC PROPERTIES ###

    @property
    def attachments(self):
        return self._attachments

    @property
    def selector(self):
        return self._selector
