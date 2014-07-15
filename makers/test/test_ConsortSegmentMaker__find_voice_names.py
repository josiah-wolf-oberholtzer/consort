from consort import makers


def test_ConsortSegmentMaker__find_voice_names_01():
    score_template = makers.ConsortScoreTemplate(
        violin_count=2,
        viola_count=1,
        cello_count=1,
        contrabass_count=1,
        )
    voice_identifiers = (
        'Violin \\d+ Bowing Voice',
        'Viola Bowing Voice',
        )
    found_voice_names = makers.ConsortSegmentMaker._find_voice_names(
        score_template=score_template,
        voice_identifiers=voice_identifiers,
        )
    assert found_voice_names == (
        'Violin 1 Bowing Voice',
        'Violin 2 Bowing Voice',
        'Viola Bowing Voice',
        )