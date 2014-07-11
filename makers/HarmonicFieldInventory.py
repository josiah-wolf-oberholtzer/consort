# -*- encoding: utf-8 -*
from abjad.tools import datastructuretools


class HarmonicFieldInventory(datastructuretools.TypedList):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        items=None,
        ):
        import consort
        datastructuretools.TypedList.__init__(
            self,
            items=items,
            item_class=consort.makers.HarmonicField,
            )

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest()