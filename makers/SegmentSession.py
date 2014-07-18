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
        'segment_maker',
        'voicewise_timespans',
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
        self.segment_maker = segment_maker
        self.voicewise_timespans = None
        self.unrewritten_score = None

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
    def segment_duration(self):
        return sum(x.duration for x in self.time_signatures)

    @property
    def time_signatures(self):
        return (
            meter.implied_time_signature
            for meter in self.meters
            )
