from consort import makers
from consort import templates


def test_ConsortSegmentMaker_find_voice_names_01():
    template = templates.ConsortScoreTemplate(
        violin_count=2,
        viola_count=1,
        cello_count=1,
        contrabass_count=1,
        )
    voice_identifiers = (
        'Violin \\d+ LH Voice',
        'Viola LH Voice',
        )
    found_voice_names = makers.ConsortSegmentMaker.find_voice_names(
        template=template,
        voice_identifiers=voice_identifiers,
        )
    assert found_voice_names == (
        'Violin 1 LH Voice',
        'Violin 2 LH Voice',
        'Viola LH Voice',
        )
