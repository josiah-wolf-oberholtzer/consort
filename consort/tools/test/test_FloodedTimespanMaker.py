# -*- encoding: utf-8 -*-
from abjad.tools import systemtools
from abjad.tools import timespantools
import consort
import collections


music_specifiers = collections.OrderedDict([
    ('One', None),
    ('Two', None),
    ])
target_timespan = timespantools.Timespan(0, 10)


def test_FloodedTimespanMaker_01():
    timespan_maker = consort.FloodedTimespanMaker()
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(10, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(10, 1),
                    voice_name='Two',
                    ),
                ]
            )
        '''), format(timespan_inventory)


def test_FloodedTimespanMaker_02():
    timespan_maker = consort.FloodedTimespanMaker(padding=1)
    timespan_inventory = timespan_maker(
        target_timespan=target_timespan,
        music_specifiers=music_specifiers,
        )
    assert format(timespan_inventory) == systemtools.TestManager.clean_string(
        r'''
        timespantools.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=durationtools.Offset(-1, 1),
                    stop_offset=durationtools.Offset(0, 1),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=durationtools.Offset(-1, 1),
                    stop_offset=durationtools.Offset(0, 1),
                    voice_name='Two',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(10, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(10, 1),
                    voice_name='Two',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=durationtools.Offset(10, 1),
                    stop_offset=durationtools.Offset(11, 1),
                    voice_name='One',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=durationtools.Offset(10, 1),
                    stop_offset=durationtools.Offset(11, 1),
                    voice_name='Two',
                    ),
                ]
            )
        '''), format(timespan_inventory)