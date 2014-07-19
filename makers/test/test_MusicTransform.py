# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import timespantools
from abjad.tools.topleveltools import new
from consort import makers

layer = 1
music_specifier = makers.MusicSpecifier(
    rhythm_maker=rhythmmakertools.TupletRhythmMaker(
        tuplet_ratios=[(1, 1, 1, 1)],
        ),
    )
score_template = makers.StringOrchestraScoreTemplate(
    violin_count=2,
    viola_count=1,
    cello_count=1,
    contrabass_count=0,
    )
target_timespan = timespantools.Timespan(0, 2)
timespan_maker = makers.TimespanMaker(
    playing_durations=durationtools.Duration(1, 1),
    silence_durations=durationtools.Duration(0),
    )
red_music_construct = makers.MusicConstruct(
    color='red',
    music_specifier=music_specifier,
    timespan_identifier=makers.RatioPartsExpression(
        ratio=(1, 1),
        parts=0,
        ),
    timespan_maker=timespan_maker,
    voice_identifier=('Viola Bowing Voice', 'Cello Bowing Voice'),
    )
blue_music_construct = makers.MusicConstruct(
    color='blue',
    music_specifier=music_specifier,
    timespan_identifier=makers.RatioPartsExpression(
        ratio=(1, 1),
        parts=1,
        ),
    timespan_maker=timespan_maker,
    voice_identifier=('Viola Bowing Voice', 'Cello Bowing Voice'),
    )
test_timespan_inventory = timespantools.TimespanInventory()
test_timespan_inventory = red_music_construct(
    layer=layer,
    score_template=score_template,
    target_timespan=target_timespan,
    timespan_inventory=test_timespan_inventory,
    )
test_timespan_inventory = blue_music_construct(
    layer=layer,
    score_template=score_template,
    target_timespan=target_timespan,
    timespan_inventory=test_timespan_inventory,
    )


def test_MusicTransform_01():

    assert systemtools.TestManager.compare(
        test_timespan_inventory,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(1, 1, 1, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(1, 1, 1, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(1, 1, 1, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(1, 1, 1, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(test_timespan_inventory)


def test_MusicTransform_02():

    layer = 2
    music_transform = makers.MusicTransform(
        rhythm_maker__tuplet_ratios=[(2, 1)],
        voice_identifier=('Viola Bowing Voice', 'Cello Bowing Voice'),
        )
    timespan_inventory = new(test_timespan_inventory)
    result = music_transform(
        layer, score_template, target_timespan,
        timespan_inventory=timespan_inventory,
        )

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    color='red',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicTransform_03():

    layer = 2
    music_transform = makers.MusicTransform(
        color='blue',
        rhythm_maker__tuplet_ratios=[(2, 1)],
        voice_identifier=('Viola Bowing Voice', 'Cello Bowing Voice'),
        )
    timespan_inventory = new(test_timespan_inventory)
    result = music_transform(
        layer, score_template, target_timespan,
        timespan_inventory=timespan_inventory,
        )

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(1, 1, 1, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(1, 1, 1, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicTransform_04():

    layer = 2
    music_transform = makers.MusicTransform(
        rhythm_maker__tuplet_ratios=[(2, 1)],
        voice_identifier=('Viola Bowing Voice',),
        )
    timespan_inventory = new(test_timespan_inventory)
    result = music_transform(
        layer, score_template, target_timespan,
        timespan_inventory=timespan_inventory,
        )

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    color='red',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(1, 1, 1, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(1, 1, 1, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicTransform_05():

    layer = 2
    music_transform = makers.MusicTransform(
        rhythm_maker__tuplet_ratios=[(2, 1)],
        timespan_identifier=makers.RatioPartsExpression(
            ratio=(1, 1, 1),
            parts=1,
            ),
        voice_identifier=('Viola Bowing Voice', 'Cello Bowing Voice'),
        )
    timespan_inventory = new(test_timespan_inventory)
    result = music_transform(
        layer, score_template, target_timespan,
        timespan_inventory=timespan_inventory,
        )

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    color='red',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)


def test_MusicTransform_06():

    layer = 2
    music_transform = makers.MusicTransform(
        rhythm_maker__tuplet_ratios=[(2, 1)],
        rhythm_maker__tie_specifier=rhythmmakertools.TieSpecifier(
            tie_across_divisions=True,
            ),
        voice_identifier=('Viola Bowing Voice', 'Cello Bowing Voice'),
        )
    timespan_inventory = new(test_timespan_inventory)
    result = music_transform(
        layer, score_template, target_timespan,
        timespan_inventory=timespan_inventory,
        )

    assert systemtools.TestManager.compare(
        result,
        '''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    color='red',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            tie_specifier=rhythmmakertools.TieSpecifier(
                                tie_across_divisions=True,
                                tie_split_notes=True,
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='red',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            tie_specifier=rhythmmakertools.TieSpecifier(
                                tie_across_divisions=True,
                                tie_split_notes=True,
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            tie_specifier=rhythmmakertools.TieSpecifier(
                                tie_across_divisions=True,
                                tie_split_notes=True,
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    color='blue',
                    layer=2,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(
                        rhythm_maker=rhythmmakertools.TupletRhythmMaker(
                            tuplet_ratios=(
                                mathtools.Ratio(2, 1),
                                ),
                            tie_specifier=rhythmmakertools.TieSpecifier(
                                tie_across_divisions=True,
                                tie_split_notes=True,
                                ),
                            ),
                        ),
                    start_offset=durationtools.Offset(1, 1),
                    stop_offset=durationtools.Offset(2, 1),
                    voice_name='Cello Bowing Voice',
                    ),
                ]
            )
        ''',
        ), format(result)