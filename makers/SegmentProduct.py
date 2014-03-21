# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import mathtools


class SegmentProduct(ConsortObject):
    r'''A segment product.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        'lilypond_file',
        'meters',
        'score',
        'segment_duration',
        'segment_maker',
        'timespan_inventory_mapping',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        segment_maker=None,
        ):
        self.lilypond_file = None
        self.meters = None
        self.score = None
        self.segment_duration = None
        self.segment_maker = segment_maker
        self.timespan_inventory_mapping = None

    ### PRIVATE PROPERTIES ###

    @property
    def _storage_format_specification(self):
        from abjad.tools import systemtools
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=None,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def measure_offsets(self):
        measure_durations = [x.duration for x in self.time_signatures]
        measure_offsets = mathtools.cumulative_sums(measure_durations)
        return measure_offsets

    @property
    def time_signatures(self):
        return (
            meter.implied_time_signature
            for meter in self.meters
            )
