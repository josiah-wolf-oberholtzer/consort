# -*- encoding: utf-8 -*-
from abjad.tools import systemtools
from abjad.tools import timespantools
import consort
import collections


def _make_timespan_inventory():
    timespan_inventory = timespantools.TimespanInventory([
        consort.PerformedTimespan(
            start_offset=0,
            stop_offset=20,
            voice_name='A',
            ),
        consort.PerformedTimespan(
            music_specifier=consort.MusicSpecifier(
                labels=('pedaled',),
                ),
            start_offset=20,
            stop_offset=40,
            voice_name='A',
            ),
        consort.PerformedTimespan(
            music_specifier=consort.MusicSpecifier(
                labels=('pedaled',),
                ),
            start_offset=25,
            stop_offset=50,
            voice_name='B',
            ),
        consort.PerformedTimespan(
            music_specifier=consort.MusicSpecifier(
                labels=('pedaled',),
                ),
            start_offset=60,
            stop_offset=80,
            voice_name='A',
            ),
        consort.PerformedTimespan(
            start_offset=65,
            stop_offset=100,
            voice_name='B',
            ),
        ])
    timespan_inventory.sort()
    return timespan_inventory


def test_DependentTimespanMaker_01():
    timespan_inventory = _make_timespan_inventory()
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_02():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_03():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ('D', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='D',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='D',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_04():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(10, 90)
    timespan_maker = consort.DependentTimespanMaker(
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(10, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(90, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_05():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(10, 90)
    timespan_maker = consort.DependentTimespanMaker(
        voice_names=(
            'A',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(10, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_06():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(25, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(65, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_07():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_stops=True,
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(40, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(80, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_08():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(25, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(40, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(65, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(80, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_09():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        rotation_indices=(1,),
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(10, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(10, 1),
                    stop_offset=durationtools.Offset(30, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(30, 1),
                    stop_offset=durationtools.Offset(35, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(35, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(80, 1),
                    stop_offset=durationtools.Offset(85, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(85, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_10():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        rotation_indices=(0, 1),
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(25, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(40, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(80, 1),
                    stop_offset=durationtools.Offset(85, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(85, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_11():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        labels=('pedaled',),
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(25, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(40, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_12():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        rotation_indices=(-1,),
        labels=('pedaled',),
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(35, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(35, 1),
                    stop_offset=durationtools.Offset(45, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(45, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_13():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(25, 75)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        rotation_indices=(-1,),
        labels=('pedaled',),
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(35, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(35, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(75, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_14():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(25, 75)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        rotation_indices=(-1,),
        labels=('no-such-label',),
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanInventory(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('pedaled',),
                        ),
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')