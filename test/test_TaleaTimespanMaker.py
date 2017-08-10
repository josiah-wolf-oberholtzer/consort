import abjad
import collections
import consort
from abjad.tools import durationtools
from abjad.tools import rhythmmakertools
from abjad.tools import systemtools
from abjad.tools import timespantools


music_specifiers = collections.OrderedDict([
    ('One', None),
    ('Two', None),
    ])
target_timespan = abjad.Timespan(0, 1)


def test_TaleaTimespanMaker_01():
    timespan_maker = consort.TaleaTimespanMaker()
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        )


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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 4),
                    stop_offset=abjad.Offset(1, 2),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(5, 8),
                    stop_offset=abjad.Offset(7, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        )


def test_TaleaTimespanMaker_03():
    timespan_maker = consort.TaleaTimespanMaker(
        synchronize_step=True,
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        )


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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 8),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 8),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='One',
                    ),
                ]
            )
        '''
        )


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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        '''
        )


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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 8),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(5, 8),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 8),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='One',
                    ),
                ]
            )
        '''
        )


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
        target_timespan=abjad.Timespan(2, 3),
        music_specifiers=music_specifiers,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(2, 1),
                    stop_offset=abjad.Offset(17, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(17, 8),
                    stop_offset=abjad.Offset(19, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(19, 8),
                    stop_offset=abjad.Offset(21, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(21, 8),
                    stop_offset=abjad.Offset(11, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(23, 8),
                    stop_offset=abjad.Offset(3, 1),
                    voice_name='One',
                    ),
                ]
            )
        '''
        )


def test_TaleaTimespanMaker_08():
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='Two',
                    ),
                ]
            )
        ''')


def test_TaleaTimespanMaker_09():
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(0, 1),
            denominator=8,
            ),
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(5, 8),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='Two',
                    ),
                ]
            )
        ''')


def test_TaleaTimespanMaker_10():
    timespan_maker = consort.TaleaTimespanMaker(
        padding=abjad.Duration(1, 8),
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 8),
                    stop_offset=abjad.Offset(0, 1),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 8),
                    stop_offset=abjad.Offset(0, 1),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 4),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(5, 8),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(5, 8),
                    stop_offset=abjad.Offset(7, 8),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(7, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(7, 8),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='Two',
                    ),
                ]
            )
        ''')


def test_TaleaTimespanMaker_11():
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(0, 1),
            denominator=8,
            ),
        padding=abjad.Duration(1, 8),
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 8),
                    stop_offset=abjad.Offset(0, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 8),
                    stop_offset=abjad.Offset(1, 2),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(5, 8),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(7, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(7, 8),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='One',
                    ),
                ]
            )
        ''')


def test_TaleaTimespanMaker_12():
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(0, 1),
            denominator=8,
            ),
        padding=abjad.Duration(1, 8),
        playing_groupings=(2,),
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 8),
                    stop_offset=abjad.Offset(0, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 4),
                    stop_offset=abjad.Offset(1, 2),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 8),
                    stop_offset=abjad.Offset(1, 2),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(7, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 8),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(9, 8),
                    voice_name='One',
                    ),
                ]
            )
        ''')


def test_TaleaTimespanMaker_13():
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(0, 1),
            denominator=8,
            ),
        padding=abjad.Duration(1, 8),
        playing_groupings=(2,),
        playing_talea=rhythmmakertools.Talea(
            counts=(1, 2),
            denominator=8,
            ),
        synchronize_groupings=True,
        synchronize_step=True,
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 8),
                    stop_offset=abjad.Offset(0, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 4),
                    stop_offset=abjad.Offset(1, 2),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 8),
                    stop_offset=abjad.Offset(1, 2),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(5, 8),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(7, 8),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 8),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(9, 8),
                    voice_name='One',
                    ),
                ]
            )
        ''')


def test_TaleaTimespanMaker_14():
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(0, 1),
            denominator=8,
            ),
        padding=abjad.Duration(1, 8),
        playing_groupings=(2, 1),
        playing_talea=rhythmmakertools.Talea(
            counts=(1, 2),
            denominator=8,
            ),
        synchronize_groupings=False,
        synchronize_step=True,
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 8),
                    stop_offset=abjad.Offset(0, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 8),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 8),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(1, 4),
                    stop_offset=abjad.Offset(3, 8),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 8),
                    stop_offset=abjad.Offset(1, 2),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(5, 8),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(9, 8),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(9, 8),
                    stop_offset=abjad.Offset(5, 4),
                    voice_name='One',
                    ),
                ]
            )
        ''')

def test_TaleaTimespanMaker_15():
    target_timespan = abjad.Timespan(
        start_offset=abjad.Offset(7, 2),
        stop_offset=abjad.Offset(35, 8),
        )
    timespan_maker = consort.TaleaTimespanMaker(
        padding=abjad.Duration(1, 4),
        playing_talea=rhythmmakertools.Talea(
            counts=(8,),
            denominator=16,
            ),
        repeat=False,
        silence_talea=rhythmmakertools.Talea(
            counts=(8, 6, 10, 7, 12),
            denominator=8,
            ),
        synchronize_groupings=True,
        synchronize_step=True,
        )
    music_specifiers = collections.OrderedDict([
        ('One', None),
        ('Two', None),
        ('Three', None),
        ])
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(13, 4),
                    stop_offset=abjad.Offset(7, 2),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(13, 4),
                    stop_offset=abjad.Offset(7, 2),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(13, 4),
                    stop_offset=abjad.Offset(7, 2),
                    voice_name='Three',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 2),
                    stop_offset=abjad.Offset(4, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 2),
                    stop_offset=abjad.Offset(4, 1),
                    voice_name='Three',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 2),
                    stop_offset=abjad.Offset(4, 1),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(4, 1),
                    stop_offset=abjad.Offset(17, 4),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(4, 1),
                    stop_offset=abjad.Offset(17, 4),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(4, 1),
                    stop_offset=abjad.Offset(17, 4),
                    voice_name='Three',
                    ),
                ]
            )
        ''')
