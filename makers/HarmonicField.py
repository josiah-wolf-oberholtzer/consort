from abjad.tools import datastructuretools


class HarmonicField(datastructuretools.TypedFrozenset):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        items=None,
        ):
        import consort
        mapping = {}
        items = items or []
        entries = [consort.makers.HarmonicFieldEntry(x)
            for x in items]
        for entry in entries:
            mapping[float(entry.structural_pitch)] = entry
        datastructuretools.TypedFrozenset.__init__(
            self,
            items=entries,
            item_class=consort.makers.HarmonicFieldEntry,
            )

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest()
