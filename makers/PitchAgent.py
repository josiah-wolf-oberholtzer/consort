# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import mathtools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class PitchAgent(abctools.AbjadObject):
    r'''A pitch agent.

    ::

        >>> from consort import makers
        >>> pitch_agent = makers.PitchAgent()
        >>> print format(pitch_agent)
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

    ### PUBLIC METHODS ###

    @staticmethod
    def iterate_score(
        score,
        ):
        from consort import makers
        counter = collections.Counter()
        for leaf in iterate(score).by_timeline(scoretools.Note):
            logical_tie = inspect_(leaf).get_logical_tie()
            if leaf is not logical_tie.head:
                continue
            prototype = makers.MusicSpecifier
            music_specifier = inspect_(leaf).get_effective(prototype)
            pitch_agent = music_specifier.pitch_agent
            if pitch_agent is None:
                continue
            seed = counter[pitch_agent]
            pitch_agent(logical_tie, seed=seed)
            counter[pitch_agent] += 1

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
