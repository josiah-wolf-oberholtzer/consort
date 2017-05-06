# -*- encoding: utf-8 -*-
from abjad.tools import systemtools
from abjad.tools import timespantools
import consort
import collections


def _make_timespan_inventory():
    timespan_inventory = timespantools.TimespanList([
        consort.PerformedTimespan(
            start_offset=0,
            stop_offset=20,
            voice_name='A',
            ),
        consort.PerformedTimespan(
            music_specifier=consort.MusicSpecifier(
                labels=('labeled',),
                ),
            start_offset=20,
            stop_offset=40,
            voice_name='A',
            ),
        consort.PerformedTimespan(
            music_specifier=consort.MusicSpecifier(
                labels=('labeled',),
                ),
            start_offset=25,
            stop_offset=50,
            voice_name='B',
            ),
        consort.PerformedTimespan(
            music_specifier=consort.MusicSpecifier(
                labels=('labeled',),
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


def test_BoundarTimespanMaker_01():
    timespan_inventory = _make_timespan_inventory()
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
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


def test_BoundaryTimespanMaker_02():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.BoundaryTimespanMaker(
        start_talea=5,
        stop_talea=5,
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
        timespantools.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(5, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(50, 1),
                    stop_offset=durationtools.Offset(55, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(65, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(100, 1),
                    stop_offset=durationtools.Offset(105, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_BoundaryTimespanMaker_03():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.BoundaryTimespanMaker(
        labels=['labeled'],
        start_talea=5,
        stop_talea=5,
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
        timespantools.TimespanList(
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
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(50, 1),
                    stop_offset=durationtools.Offset(55, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(65, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
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
                ]
            )
        ''')


def test_BoundaryTimespanMaker_04():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.BoundaryTimespanMaker(
        start_talea=5,
        stop_talea=15,
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
        timespantools.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(5, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(50, 1),
                    stop_offset=durationtools.Offset(65, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(100, 1),
                    stop_offset=durationtools.Offset(115, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_BoundaryTimespanMaker_05():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = timespantools.Timespan(0, 100)
    timespan_maker = consort.BoundaryTimespanMaker(
        start_talea=5,
        stop_talea=5,
        labels=['labeled'],
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=_make_timespan_inventory(),
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanList(
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
                    start_offset=durationtools.Offset(20, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(50, 1),
                    stop_offset=durationtools.Offset(55, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(65, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(60, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
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
                ]
            )
        ''')