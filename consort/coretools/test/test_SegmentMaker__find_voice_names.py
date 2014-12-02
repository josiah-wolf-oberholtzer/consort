# -*- encoding: utf-8 -*-
from abjad.tools import templatetools
import consort


def test_SegmentMaker__find_voice_names_01():
    score_template = templatetools.StringOrchestraScoreTemplate(
        violin_count=2,
        viola_count=1,
        cello_count=1,
        contrabass_count=1,
        )
    voice_identifier = (
        'Violin \\d+ Bowing Voice',
        'Viola Bowing Voice',
        )
    found_voice_names = consort.coretools.SegmentMaker._find_voice_names(
        score_template=score_template,
        voice_identifier=voice_identifier,
        )
    assert found_voice_names == (
        'Violin 1 Bowing Voice',
        'Violin 2 Bowing Voice',
        'Viola Bowing Voice',
        )