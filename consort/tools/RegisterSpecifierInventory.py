# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools


class RegisterSpecifierInventory(datastructuretools.TypedList):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest()

    @property
    def _item_callable(self):
        import consort
        return consort.RegisterSpecifier
