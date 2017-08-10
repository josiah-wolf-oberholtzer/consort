import abjad
import consort
import collections
from abjad.tools import systemtools
from abjad.tools import timespantools


def _make_timespan_inventory():
    timespan_inventory = abjad.TimespanList([
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


def test_DependentTimespanMaker_01():
    timespan_inventory = _make_timespan_inventory()
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_02():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=abjad.TimespanList()
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            []
            )
        ''')


def test_DependentTimespanMaker_03():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        hysteresis=(1, 8),
        voice_names=(
            'A',
            'B',
            ),
        )
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=abjad.TimespanList()
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            []
            )
        ''')



def test_DependentTimespanMaker_04():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_05():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ('D', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='D',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='D',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_06():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(10, 90)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(10, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(90, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_07():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(10, 90)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(10, 1),
                    stop_offset=abjad.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_08():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(25, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(65, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_09():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_10():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(25, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(65, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_11():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(10, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(10, 1),
                    stop_offset=abjad.Offset(30, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(30, 1),
                    stop_offset=abjad.Offset(35, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(35, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(85, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(85, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_12():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(25, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(85, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(85, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='C',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_13():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        labels=('labeled',),
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(25, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_14():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        rotation_indices=(-1,),
        labels=('labeled',),
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(35, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(35, 1),
                    stop_offset=abjad.Offset(45, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(45, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_15():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(25, 75)
    timespan_maker = consort.DependentTimespanMaker(
        include_inner_starts=True,
        include_inner_stops=True,
        rotation_indices=(-1,),
        labels=('labeled',),
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(35, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(35, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(75, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_16():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(25, 75)
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
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_17():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        voice_names=(
            'A',
            ),
        )
    timespan_inventory = _make_timespan_inventory()
    timespan_inventory.extend([
        consort.SilentTimespan(40, 50, voice_name='A'),
        consort.SilentTimespan(55, 60, voice_name='A'),
        consort.SilentTimespan(80, 90, voice_name='A'),
        ])
    timespan_inventory.sort()
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='A',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(55, 1),
                    stop_offset=abjad.Offset(60, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(90, 1),
                    voice_name='A',
                    ),
                ]
            )
        ''')
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=timespan_inventory,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='A',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(55, 1),
                    stop_offset=abjad.Offset(60, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(90, 1),
                    voice_name='A',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_18():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        padding=1,
        voice_names=(
            'A',
            ),
        )
    timespan_inventory = _make_timespan_inventory()
    timespan_inventory.extend([
        consort.SilentTimespan(40, 50, voice_name='A'),
        consort.SilentTimespan(55, 60, voice_name='A'),
        consort.SilentTimespan(80, 90, voice_name='A'),
        ])
    timespan_inventory.sort()
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=timespan_inventory,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 1),
                    stop_offset=abjad.Offset(0, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(20, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(40, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(40, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(25, 1),
                    stop_offset=abjad.Offset(50, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='B',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(41, 1),
                    voice_name='C',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='A',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(55, 1),
                    stop_offset=abjad.Offset(60, 1),
                    voice_name='A',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(59, 1),
                    stop_offset=abjad.Offset(60, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    music_specifier=consort.tools.MusicSpecifier(
                        labels=('labeled',),
                        ),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(60, 1),
                    stop_offset=abjad.Offset(80, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='B',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(81, 1),
                    voice_name='C',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(90, 1),
                    voice_name='A',
                    ),
                ]
            )
        ''')


def test_DependentTimespanMaker_19():
    music_specifiers = collections.OrderedDict([
        ('C', None),
        ])
    target_timespan = abjad.Timespan(0, 100)
    timespan_maker = consort.DependentTimespanMaker(
        hysteresis=10,
        voice_names=['A'],
        )
    timespan_inventory = abjad.TimespanList([
        consort.PerformedTimespan(0, 10, voice_name='A'),
        consort.PerformedTimespan(5, 15, voice_name='A'),
        consort.PerformedTimespan(20, 30, voice_name='A'),
        consort.PerformedTimespan(40, 50, voice_name='A'),
        consort.PerformedTimespan(65, 75, voice_name='A'),
        consort.PerformedTimespan(80, 100, voice_name='A'),
        ])
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        timespan_inventory=timespan_inventory,
        )
    assert format(timespan_inventory) == abjad.String.normalize(
        r'''
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(10, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(30, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(5, 1),
                    stop_offset=abjad.Offset(15, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(20, 1),
                    stop_offset=abjad.Offset(30, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(40, 1),
                    stop_offset=abjad.Offset(50, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(75, 1),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(65, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(80, 1),
                    stop_offset=abjad.Offset(100, 1),
                    voice_name='A',
                    ),
                ]
            )
        ''')
