# -*- encoding: utf-8 -*-
from abjad.tools import abctools


class AttachmentAgent(abctools.AbjadObject):
    r'''An attachment agent.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachment_specifiers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachment_specifiers=None,
        ):
        from consort import makers
        prototype = makers.AttachmentSpecifier
        if attachment_specifiers is not None:
            assert all(isinstance(x, prototype) for x in attachment_specifiers)
        self._attachment_specifiers = attachment_specifiers

    ### SPECIAL METHODS ###

    def __call__(self, music):
        pass

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_specifiers(self):
        return self._attachment_specifiers
