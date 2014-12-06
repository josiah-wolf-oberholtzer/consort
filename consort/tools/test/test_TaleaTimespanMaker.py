# -*- encoding: utf-8 -*-
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import timespantools
import consort
import collections


music_specifiers = collections.OrderedDict([
    ('One', None),
    ('Two', None),
    ])
target_timespan = timespantools.Timespan(0, 1)


def test_TaleaTimespanMaker_01():
    timespan_maker = consort.TaleaTimespanMaker()
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TaleaTimespanMaker_02():
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(1, 2),
            denominator=8,
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 8),
                    stop_offset=durationtools.Offset(3, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(5, 8),
                    stop_offset=durationtools.Offset(7, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TaleaTimespanMaker_03():
    timespan_maker = consort.TaleaTimespanMaker(
        synchronize_step=True,
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TaleaTimespanMaker_04():
    timespan_maker = consort.TaleaTimespanMaker(
        playing_talea=rhythmmakertools.Talea(
            counts=(1, 2),
            denominator=8,
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(3, 8),
                    stop_offset=durationtools.Offset(5, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(5, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(7, 8),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='One',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TaleaTimespanMaker_05():
    timespan_maker = consort.TaleaTimespanMaker(
        playing_talea=rhythmmakertools.Talea(
            counts=(1, 2),
            denominator=8,
            ),
        synchronize_step=True,
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(5, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TaleaTimespanMaker_06():
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(0, 1),
            denominator=8,
            ),
        playing_talea=rhythmmakertools.Talea(
            counts=(1, 2),
            denominator=8,
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(1, 8),
                    stop_offset=durationtools.Offset(3, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(3, 8),
                    stop_offset=durationtools.Offset(5, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(5, 8),
                    stop_offset=durationtools.Offset(3, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(7, 8),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='One',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)


def test_TaleaTimespanMaker_07():
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(0, 1),
            denominator=8,
            ),
        playing_talea=rhythmmakertools.Talea(
            counts=(1, 2),
            denominator=8,
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=timespantools.Timespan(2, 3),
        music_specifiers=music_specifiers,
        )
    assert systemtools.TestManager.compare(
        format(timespan_inventory),
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(2, 1),
                    stop_offset=durationtools.Offset(17, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(17, 8),
                    stop_offset=durationtools.Offset(19, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(19, 8),
                    stop_offset=durationtools.Offset(21, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(21, 8),
                    stop_offset=durationtools.Offset(11, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(23, 8),
                    stop_offset=durationtools.Offset(3, 1),
                    voice_name='One',
                    ),
                ]
            )
        '''
        ), format(timespan_inventory)