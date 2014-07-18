# -*- encoding: utf -*-
from abjad import *
from consort import makers


def test_SegmentMaker___call___01():

    score_template = makers.StringOrchestraScoreTemplate(
        violin_count=2,
        viola_count=1,
        cello_count=1,
        contrabass_count=0,
        )

    segment_maker = makers.SegmentMaker(
        duration_in_seconds=2,
        score_template=score_template,
        settings=(
            makers.SegmentSetting(
                music_specifier=makers.MusicSpecifier(),
                timespan_maker=makers.TimespanMaker(),
                voice_identifier=('Violin \\d+ Bowing Voice',),
                ),
            ),
        tempo=Tempo((1, 4), 60),
        time_signatures=(
            (5, 8),
            (7, 16),
            ),
        )

    result = segment_maker()

    assert result is not None