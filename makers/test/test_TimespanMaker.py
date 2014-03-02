# -*- encoding: utf-8 -*-
from abjad import *
from consort import makers


voice_specifier = ('One', 'Two')
target_duration = Duration(1)


def test_TimespanMaker_01():
    timespan_maker = makers.TimespanMaker()
    timespan_inventory, final_offset = timespan_maker(
        target_duration=target_duration,
        voice_specifier=voice_specifier,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
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
        voice_specifier=voice_specifier,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(1, 8),
                    stop_offset=durationtools.Offset(3, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 2),
                    ),
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(5, 8),
                    stop_offset=durationtools.Offset(7, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
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
        voice_specifier=voice_specifier,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
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
        voice_specifier=voice_specifier,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(3, 8),
                    stop_offset=durationtools.Offset(5, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(5, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(7, 8),
                    stop_offset=durationtools.Offset(1, 1),
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
        voice_specifier=voice_specifier,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(5, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
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
        voice_specifier=voice_specifier,
        )
    assert final_offset == 1
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(1, 8),
                    stop_offset=durationtools.Offset(3, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(3, 8),
                    stop_offset=durationtools.Offset(5, 8),
                    ),
                makers.PerformedTimespan(
                    context_name='Two',
                    start_offset=durationtools.Offset(5, 8),
                    stop_offset=durationtools.Offset(3, 4),
                    ),
                makers.PerformedTimespan(
                    context_name='One',
                    start_offset=durationtools.Offset(7, 8),
                    stop_offset=durationtools.Offset(1, 1),
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)
