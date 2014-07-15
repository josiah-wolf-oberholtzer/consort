from consort import makers


def test_ConsortSegmentMaker__find_voice_names_01():
    template = makers.ConsortScoreTemplate(
        violin_count=2,
        viola_count=1,
        cello_count=1,
        contrabass_count=1,
        )
    voice_identifiers = (
        'Violin \\d+ LH Voice',
        'Viola LH Voice',
        )
    found_voice_names = makers.ConsortSegmentMaker._find_voice_names(
        template=template,
        voice_identifiers=voice_identifiers,
        )
    assert found_voice_names == (
        'Violin 1 LH Voice',
        'Violin 2 LH Voice',
        'Viola LH Voice',
        )