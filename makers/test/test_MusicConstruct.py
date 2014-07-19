# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import systemtools
from abjad.tools import timespantools
from consort import makers

layer = 1
music_specifier = makers.MusicSpecifier()
score_template = makers.StringOrchestraScoreTemplate(
    violin_count=2,
    viola_count=1,
    cello_count=1,
    contrabass_count=0,
    )
target_timespan = timespantools.Timespan(0, 4)
timespan_maker = makers.TimespanMaker(
    playing_durations=durationtools.Duration(1, 1),
    silence_durations=durationtools.Duration(0),
    )


def test_MusicConstruct_01():

    music_construct = makers.MusicConstruct(
        music_specifier=music_specifier,
        timespan_maker=timespan_maker,
        voice_identifier=('Viola Bowing Voice',),
        )

    result = music_construct(layer, score_template, target_timespan)

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(2, 1),
                    stop_offset=durationtools.Offset(3, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 1),
                    stop_offset=durationtools.Offset(4, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicConstruct_02():

    music_construct = makers.MusicConstruct(
        music_specifier=music_specifier,
        timespan_maker=timespan_maker,
        timespan_identifier=timespantools.Timespan(1, 2),
        voice_identifier=('Viola Bowing Voice',),
        )

    result = music_construct(layer, score_template, target_timespan)

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicConstruct_03():

    music_construct = makers.MusicConstruct(
        music_specifier=music_specifier,
        timespan_maker=timespan_maker,
        timespan_identifier=timespantools.TimespanInventory([
            timespantools.Timespan(0, 1),
            timespantools.Timespan(2, 4),
            ]),
        voice_identifier=('Viola Bowing Voice',),
        )

    result = music_construct(layer, score_template, target_timespan)

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(2, 1),
                    stop_offset=durationtools.Offset(3, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 1),
                    stop_offset=durationtools.Offset(4, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicConstruct_04():

    music_construct = makers.MusicConstruct(
        music_specifier=music_specifier,
        timespan_maker=timespan_maker,
        timespan_identifier=makers.RatioPartsExpression(
            ratio=(1, 2, 1),
            parts=1,
            ),
        voice_identifier=('Viola Bowing Voice',),
        )

    result = music_construct(layer, score_template, target_timespan)

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(2, 1),
                    stop_offset=durationtools.Offset(3, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicConstruct_05():

    music_construct = makers.MusicConstruct(
        music_specifier=music_specifier,
        timespan_maker=timespan_maker,
        timespan_identifier=makers.RatioPartsExpression(
            ratio=(1, 2, 1),
            parts=(0, 2),
            ),
        voice_identifier=('Viola Bowing Voice',),
        )

    result = music_construct(layer, score_template, target_timespan)

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 1),
                    stop_offset=durationtools.Offset(4, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicConstruct_06():

    music_construct = makers.MusicConstruct(
        music_specifier=music_specifier,
        timespan_maker=timespan_maker,
        timespan_identifier=makers.RatioPartsExpression(
            ratio=(1, 1, 1),
            parts=1,
            ),
        voice_identifier=('Viola Bowing Voice',),
        )

    result = music_construct(layer, score_template, target_timespan)

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(4, 3),
                    stop_offset=durationtools.Offset(7, 3),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicConstruct_07():

    music_construct = makers.MusicConstruct(
        music_specifier=music_specifier,
        timespan_maker=timespan_maker,
        timespan_identifier=makers.RatioPartsExpression(
            ratio=(1, 1, 1, 2),
            parts=(1, 3),
            ),
        voice_identifier=('Viola Bowing Voice',),
        )

    result = music_construct(layer, score_template, target_timespan)

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(12, 5),
                    stop_offset=durationtools.Offset(17, 5),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)