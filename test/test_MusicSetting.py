import abjad
import consort
from abjad.tools import durationtools
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import templatetools
from abjad.tools import timespantools

layer = 1
score_template = templatetools.StringOrchestraScoreTemplate(
    violin_count=2,
    viola_count=1,
    cello_count=1,
    contrabass_count=0,
    )
segment_timespan = abjad.Timespan(0, 4)
timespan_maker = consort.TaleaTimespanMaker(
    playing_talea=rhythmmakertools.Talea(
        counts=(1,),
        denominator=1,
        ),
    silence_talea=None,
    )
timespan_quantization = abjad.Duration(1, 16)


def test_MusicSetting_01():

    music_setting = consort.MusicSetting(
        timespan_maker=timespan_maker,
        viola_bowing_voice=consort.tools.MusicSpecifier(),
        )

    result = music_setting(
        layer=layer,
        score_template=score_template,
        segment_timespan=segment_timespan,
        )

    assert format(result) == abjad.String.normalize(
        '''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(2, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 1),
                    stop_offset=abjad.Offset(4, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicSetting_02():

    music_setting = consort.MusicSetting(
        timespan_maker=timespan_maker,
        timespan_identifier=abjad.Timespan(1, 2),
        viola_bowing_voice=consort.tools.MusicSpecifier(),
        )

    result = music_setting(
        layer=layer,
        score_template=score_template,
        segment_timespan=segment_timespan,
        )

    assert format(result) == abjad.String.normalize(
        '''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicSetting_03():

    music_setting = consort.MusicSetting(
        timespan_maker=timespan_maker,
        timespan_identifier=abjad.TimespanList([
            abjad.Timespan(0, 1),
            abjad.Timespan(2, 4),
            ]),
        viola_bowing_voice=consort.tools.MusicSpecifier(),
        )

    result = music_setting(
        layer=layer,
        score_template=score_template,
        segment_timespan=segment_timespan,
        )

    assert format(result) == abjad.String.normalize(
        '''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(2, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 1),
                    stop_offset=abjad.Offset(4, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicSetting_04():

    music_setting = consort.MusicSetting(
        timespan_maker=timespan_maker,
        timespan_identifier=consort.RatioPartsExpression(
            ratio=(1, 2, 1),
            parts=1,
            ),
        viola_bowing_voice=consort.tools.MusicSpecifier(),
        )

    result = music_setting(
        layer=layer,
        score_template=score_template,
        segment_timespan=segment_timespan,
        )

    assert format(result) == abjad.String.normalize(
        '''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(2, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(2, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicSetting_05():

    music_setting = consort.MusicSetting(
        timespan_maker=timespan_maker,
        timespan_identifier=consort.RatioPartsExpression(
            ratio=(1, 2, 1),
            parts=(0, 2),
            ),
        viola_bowing_voice=consort.tools.MusicSpecifier(),
        )

    result = music_setting(
        layer=layer,
        score_template=score_template,
        segment_timespan=segment_timespan,
        )

    assert format(result) == abjad.String.normalize(
        '''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 1),
                    stop_offset=abjad.Offset(4, 1),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicSetting_06():

    music_setting = consort.MusicSetting(
        timespan_maker=timespan_maker,
        timespan_identifier=consort.RatioPartsExpression(
            ratio=(1, 1, 1),
            parts=1,
            ),
        viola_bowing_voice=consort.tools.MusicSpecifier(),
        )

    result = music_setting(
        layer=layer,
        score_template=score_template,
        segment_timespan=segment_timespan,
        timespan_quantization=timespan_quantization,
        )

    assert format(result) == abjad.String.normalize(
        '''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(21, 16),
                    stop_offset=abjad.Offset(37, 16),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicSetting_07():

    music_setting = consort.MusicSetting(
        timespan_maker=timespan_maker,
        timespan_identifier=consort.RatioPartsExpression(
            ratio=(1, 1, 1, 2),
            parts=(1, 3),
            ),
        viola_bowing_voice=consort.tools.MusicSpecifier(),
        )

    result = music_setting(
        layer=layer,
        score_template=score_template,
        segment_timespan=segment_timespan,
        timespan_quantization=timespan_quantization,
        )

    assert format(result) == abjad.String.normalize(
        '''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(19, 8),
                    stop_offset=abjad.Offset(27, 8),
                    layer=1,
                    music_specifier=consort.tools.MusicSpecifier(),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)
