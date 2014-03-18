# -*- encoding: utf-8 -*-
from abjad import *
from consort import makers


voice_names = ('One', 'Two')
target_duration = Duration(1)


def test_TimespanMaker_01():
    timespan_maker = makers.TimespanMaker()
    timespan_inventory, final_offset = timespan_maker(
        target_duration=target_duration,
        voice_names=voice_names,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Two',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TimespanMaker_02():
    timespan_maker = makers.TimespanMaker(
        initial_silence_durations=(
            Duration(1, 8),
            Duration(1, 4),
            ),
        )
    timespan_inventory, final_offset = timespan_maker(
        target_duration=target_duration,
        voice_names=voice_names,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 8),
                    stop_offset=durationtools.Offset(3, 8),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Two',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(5, 8),
                    stop_offset=durationtools.Offset(7, 8),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TimespanMaker_03():
    timespan_maker = makers.TimespanMaker(
        synchronize_step=True,
        )
    timespan_inventory, final_offset = timespan_maker(
        target_duration=target_duration,
        voice_names=voice_names,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Two',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TimespanMaker_04():
    timespan_maker = makers.TimespanMaker(
        playing_durations=(
            Duration(1, 8),
            Duration(1, 4),
            ),
        )
    timespan_inventory, final_offset = timespan_maker(
        target_duration=target_duration,
        voice_names=voice_names,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Two',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(3, 8),
                    stop_offset=durationtools.Offset(5, 8),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(5, 8),
                    voice_name='Two',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(7, 8),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='One',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TimespanMaker_05():
    timespan_maker = makers.TimespanMaker(
        playing_durations=(
            Duration(1, 8),
            Duration(1, 4),
            ),
        synchronize_step=True,
        )
    timespan_inventory, final_offset = timespan_maker(
        target_duration=target_duration,
        voice_names=voice_names,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Two',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(5, 8),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TimespanMaker_06():
    timespan_maker = makers.TimespanMaker(
        initial_silence_durations=(
            Duration(0),
            Duration(1, 8),
            ),
        playing_durations=(
            Duration(1, 8),
            Duration(1, 4),
            ),
        )
    timespan_inventory, final_offset = timespan_maker(
        target_duration=target_duration,
        voice_names=voice_names,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(1, 8),
                    stop_offset=durationtools.Offset(3, 8),
                    voice_name='Two',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(3, 8),
                    stop_offset=durationtools.Offset(5, 8),
                    voice_name='One',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(5, 8),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Two',
                    ),
                makers.PerformedTimespan(
                    minimum_duration=durationtools.Duration(1, 8),
                    start_offset=durationtools.Offset(7, 8),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='One',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)
