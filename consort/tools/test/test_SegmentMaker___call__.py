# -*- encoding: utf -*-
from abjad.tools import indicatortools
from abjad.tools import templatetools
import consort


def test_SegmentMaker___call___01():

    score_template = templatetools.StringOrchestraScoreTemplate(
        violin_count=2,
        viola_count=1,
        cello_count=1,
        contrabass_count=0,
        )

    segment_maker = consort.tools.SegmentMaker(
        duration_in_seconds=2,
        score_template=score_template,
        settings=(
            consort.tools.MusicSetting(
                timespan_maker=consort.timespantools.TaleaTimespanMaker(),
                violin_1_bowing_voice=None,
                violin_2_bowing_voice=None,
                ),
            ),
        tempo=indicatortools.Tempo((1, 4), 60),
        permitted_time_signatures=(
            (5, 8),
            (7, 16),
            ),
        )

    result = segment_maker()

    assert result is not None