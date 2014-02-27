# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import timespantools


class ContextSpecifier(abctools.AbjadObject):
    r'''A context specifier.

    ::

        >>> from consort import makers
        >>> context_specifier = makers.ContextSpecifier()
        >>> print format(context_specifier)
        makers.ContextSpecifier()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(
        self,
        ):
        pass

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer=None,
        template=None,
        ):
        return timespantools.TimespanInventory()
