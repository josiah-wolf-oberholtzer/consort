# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import mathtools


class SegmentSession(ConsortObject):
    r'''A segment-maker session.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        'meters',
        'score',
        'scores',
        'segment_duration',
        'segment_maker',
        'timespan_inventory_mapping',
        'unrewritten_score',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        segment_maker=None,
        ):
        self.meters = None
        self.score = None
        self.scores = []
        self.segment_duration = None
        self.segment_maker = segment_maker
        self.timespan_inventory_mapping = None
        self.unrewritten_score = None

    ### PRIVATE PROPERTIES ###

    @property
    def _storage_format_specifier(self):
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