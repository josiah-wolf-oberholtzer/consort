import abjad
from abjad.tools import durationtools


class Proportions(abjad.TypedList):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(self, items=None):
        abjad.TypedList.__init__(
            self,
            items=items,
            )

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest()

    ### PUBLIC METHODS ###

    def get_segment_desired_duration_in_seconds(self, segment_index, total_seconds):
        segment_proportions = self[segment_index]
        segment_total = sum(abjad.flatten_sequence(
            segment_proportions))
        ratio = abjad.Multiplier(segment_total, self.total)
        desired_duration_in_seconds = ratio * total_seconds
        return desired_duration_in_seconds

    ### PUBLIC PROPERTIES ###

    @property
    def total(self):
        return sum(abjad.flatten_sequence(self))
