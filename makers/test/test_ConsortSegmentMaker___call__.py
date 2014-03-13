from consort import makers
from consort import templates


def test_ConsortSegmentMaker___call___01():

    template = templates.ConsortScoreTemplate(
        violin_count=2,
        viola_count=1,
        cello_count=1,
        contrabass_count=0,
        )

    segment_maker = makers.ConsortSegmentMaker(
        permitted_time_signatures=(
            (5, 8),
            (7, 16),
            ),
        target_duration=2,
        template=template,
        voice_specifiers=(
            makers.VoiceSpecifier(
                music_specifier=makers.MusicSpecifier(),
                timespan_maker=makers.TimespanMaker(),
                voice_identifiers=('Violin \\d+ LH Voice',),
                ),
            ),
        )

    result = segment_maker()

    assert result is not None
