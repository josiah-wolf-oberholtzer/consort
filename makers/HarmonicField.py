from abjad.tools import datastructuretools


class HarmonicField(datastructuretools.TypedList):

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
        entries = [self._item_callable(x) for x in items]
        for entry in entries:
            mapping[float(entry.structural_pitch)] = entry
        items = list(mapping.values())
        datastructuretools.TypedList.__init__(
            self,
            items=items,
            item_class=consort.makers.HarmonicFieldEntry,
            keep_sorted=True,
            )

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest()

    @property
    def _item_callable(self):
        import consort
        return consort.makers.HarmonicFieldEntry

    ### PUBLIC METHODS ###

    def invert(
        self,
        expr,
        axis=None,
        structural_pitch_class_subset=None,
        ):
        pass

    def invert_grace_pitches(
        self,
        structural_pitch_class_subset=None,
        ):
        pass

    def retrograde(
        self,
        structural_pitch_class_subset=None,
        ):
        pass

    def rotate_pitch_classes(
        self,
        expr,
        structural_pitch_class_subset=None,
        ):
        pass

    def rotate_octaves(
        self,
        expr,
        structural_pitch_class_subset=None,
        ):
        pass

    def transpose(
        self,
        expr,
        include_grace_pitches=True,
        include_structural_pitches=True,
        structural_pitch_class_subset=None,
        ):
        pass

    ### PUBLIC PROPERTIES ###

    @property
    def octave_range(self):
        pass