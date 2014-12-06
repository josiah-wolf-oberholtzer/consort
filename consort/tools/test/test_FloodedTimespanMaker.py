# -*- encoding: utf-8 -*-
from abjad.tools import systemtools
from abjad.tools import timespantools
from consort import tools
import collections


music_specifiers = collections.OrderedDict([
    ('One', None),
    ('Two', None),
    ])
target_timespan = timespantools.Timespan(0, 1)


def test_FloodedTimespanMaker_01():
    timespan_maker = tools.FloodedTimespanMaker()
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
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='One',
                    ),
                consort.tools.PerformedTimespan(
                    can_split=True,
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Two',
                    ),
                ]
            )
        '''), format(timespan_inventory)