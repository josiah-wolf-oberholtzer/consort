# -*- encoding: utf-8 -*-
import bisect
import collections
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools import sequencetools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import new
from consort.makers.ConsortObject import ConsortObject


class PitchAgent(ConsortObject):
    r'''A pitch agent.

    ::

        >>> from consort import makers
        >>> pitch_agent = makers.PitchAgent()
        >>> print(format(pitch_agent))
        makers.PitchAgent()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_pitch_segments',
        '_pitch_segment_ratio',
        '_transforms',
        '_transform_ratio',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pitch_segments=None,
        pitch_segment_ratio=None,
        transforms=None,
        transform_ratio=None
        ):
        from consort import makers
        if pitch_segments is not None:
            assert isinstance(pitch_segments, collections.Sequence)
            assert len(pitch_segments)
            pitch_segments = tuple([pitchtools.PitchSegment(x)
                for x in pitch_segments])
        self._pitch_segments = pitch_segments
        if pitch_segment_ratio is not None:
            pitch_segment_ratio = mathtools.Ratio(pitch_segment_ratio)
            assert len(pitch_segment_ratio) == len(pitch_segments)
        self._pitch_segment_ratio = pitch_segment_ratio
        if transforms is not None:
            prototype = (type(None), makers.PitchClassSegmentTransform)
            assert isinstance(transforms, collections.Sequence)
            assert len(transforms)
            assert all(isinstance(x, prototype) for x in transforms)
            transforms = tuple(transforms)
        self._transforms = transforms
        if transform_ratio is not None:
            transform_ratio = mathtools.Ratio(transform_ratio)
            assert len(transform_ratio) == len(transforms)
        self._transform_ratio = transform_ratio

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        seed=0,
        ):
        assert isinstance(logical_tie, selectiontools.LogicalTie)
        if self.pitch_segments is None:
            return
        segment = inspect_(logical_tie.head).get_parentage().root
        segment_duration = inspect_(segment).get_duration()
        start_offset = logical_tie.get_timespan().start_offset
        pitch_segment_ratio = self.pitch_segment_ratio
        if pitch_segment_ratio is None:
            pitch_segment_ratio = (1,) * len(self.pitch_segments)
        pitch_segment_offsets = self._duration_and_ratio_to_offsets(
            duration=segment_duration,
            ratio=pitch_segment_ratio,
            )
        pitch_segment_index = self._offset_and_offsets_to_index(
            offset=start_offset,
            offsets=pitch_segment_offsets,
            )
        pitch_segment = self.pitch_segments[pitch_segment_index]
        pitch_segment = pitch_segment.rotate(seed)
        current_pitch = pitch_segment[0]
        previous_leaf = inspect_(logical_tie.head).get_leaf(-1)
        previous_pitch = None
        if isinstance(previous_leaf, scoretools.Note):
            previous_pitch = previous_leaf.written_pitch
            if 1 < len(set(pitch_segment)):
                while previous_pitch == current_pitch:
                    pitch_segment = pitch_segment.rotate(1)
                    current_pitch = pitch_segment[0]
        for note in logical_tie:
            note.written_pitch = current_pitch

    ### PRIVATE METHODS ###

    def _duration_and_ratio_to_offsets(
        self,
        duration=None,
        ratio=None,
        ):
        ratio_sum = sum(ratio)
        duration_parts = []
        for ratio_part in ratio:
            multiplier = durationtools.Multiplier(ratio_part, ratio_sum)
            duration_part = duration * multiplier
            duration_parts.append(duration_part)
        offsets = mathtools.cumulative_sums(duration_parts)
        offsets = offsets[:-1]
        return offsets

    def _offset_and_offsets_to_index(
        self,
        offset=None,
        offsets=None,
        ):
        if offset in offsets:
            return offsets.index(offset)
        return bisect.bisect(offsets, offset) - 1

    ### PUBLIC METHODS ###

    @staticmethod
    def iterate_score(
        score,
        ):
        from consort import makers
        counter = collections.Counter()
        for leaf in iterate(score).by_timeline(scoretools.Note):
            logical_tie = inspect_(leaf).get_logical_tie()
            if not isinstance(leaf, scoretools.Note) or \
                leaf is not logical_tie.head:
                continue
            prototype = makers.MusicSpecifier
            music_specifier = inspect_(leaf).get_effective(prototype)
            pitch_agent = music_specifier.pitch_agent
            if pitch_agent is None:
                continue
            seed = counter[music_specifier]
            pitch_agent(logical_tie, seed=seed)
            counter[music_specifier] += 1

    def reverse(self):
        pitch_segments = self.pitch_segments
        if pitch_segments is not None:
            pitch_segments = [x.reverse() for x in reversed(pitch_segments)]
        pitch_segment_ratio = self.pitch_segment_ratio
        if pitch_segment_ratio is not None:
            pitch_segment_ratio = sequencetools.reverse_sequence(
                pitch_segment_ratio)
        transforms = self.transforms
        if transforms is not None:
            transforms = reversed(transforms)
        transform_ratio = self.transform_ratio
        if transform_ratio is not None:
            transform_ratio = sequencetools.reverse_sequence(transform_ratio)
        return new(self,
            pitch_segments=pitch_segments,
            pitch_segment_ratio=pitch_segment_ratio,
            transforms=transforms,
            transform_ratio=transform_ratio,
            )

    def rotate(self, n=0):
        pitch_segments = self.pitch_segments
        if pitch_segments is not None:
            pitch_segments = [x.rotate()
                for x in sequencetools.rotate_sequence(pitch_segments, n)]
        pitch_segment_ratio = self.pitch_segment_ratio
        if pitch_segment_ratio is not None:
            pitch_segment_ratio = sequencetools.rotate_sequence(
                pitch_segment_ratio, n)
        transforms = self.transforms
        if transforms is not None:
            transforms = sequencetools.rotate_sequence(transforms, n)
        transform_ratio = self.transform_ratio
        if transform_ratio is not None:
            transform_ratio = sequencetools.rotate_sequence(transform_ratio, n)
        return new(self,
            pitch_segments=pitch_segments,
            pitch_segment_ratio=pitch_segment_ratio,
            transforms=transforms,
            transform_ratio=transform_ratio,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def pitch_segments(self):
        return self._pitch_segments

    @property
    def pitch_segment_ratio(self):
        return self._pitch_segment_ratio

    @property
    def transforms(self):
        return self._transforms

    @property
    def transform_ratio(self):
        return self._transform_ratio
