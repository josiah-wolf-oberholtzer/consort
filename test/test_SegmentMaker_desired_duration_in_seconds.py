import abjad
import consort
from abjad.tools import durationtools
from abjad.tools import templatetools


def test_SegmentMaker_desired_duration_in_seconds_01():
    segment_maker = consort.SegmentMaker(
        desired_duration_in_seconds=4,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(),
        tempo=abjad.MetronomeMark((1, 4), 60),
        )
    assert segment_maker.desired_duration_in_seconds == 4
    assert segment_maker.desired_duration == abjad.Duration(1)


def test_SegmentMaker_desired_duration_in_seconds_02():
    segment_maker = consort.SegmentMaker(
        desired_duration_in_seconds=1,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(),
        tempo=abjad.MetronomeMark((1, 4), 60),
        )
    assert segment_maker.desired_duration_in_seconds == 1
    assert segment_maker.desired_duration == abjad.Duration(1, 4)


def test_SegmentMaker_desired_duration_in_seconds_03():
    segment_maker = consort.SegmentMaker(
        desired_duration_in_seconds=4,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(),
        tempo=abjad.MetronomeMark((1, 4), 120),
        )
    assert segment_maker.desired_duration_in_seconds == 4
    assert segment_maker.desired_duration == abjad.Duration(2)


def test_SegmentMaker_desired_duration_in_seconds_04():
    segment_maker = consort.SegmentMaker(
        desired_duration_in_seconds=4,
        score_template=templatetools.GroupedRhythmicStavesScoreTemplate(),
        tempo=abjad.MetronomeMark((1, 4), 90),
        )
    assert segment_maker.desired_duration_in_seconds == 4
    assert segment_maker.desired_duration == abjad.Duration(3, 2)
