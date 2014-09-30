# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad.tools import timespantools
from supriya.tools import timetools


def subtract_timespan_inventories(inventory_one, inventory_two):
    r'''Subtracts `inventory_two` from `inventory_one`.

    ::

        >>> inventory_one = timespantools.TimespanInventory([
        ...     timespantools.Timespan(0, 10),
        ...     timespantools.Timespan(10, 20),
        ...     timespantools.Timespan(40, 80),
        ...     ])

    ::

        >>> inventory_two = timespantools.TimespanInventory([
        ...     timespantools.Timespan(5, 15),
        ...     timespantools.Timespan(25, 35),
        ...     timespantools.Timespan(35, 45),
        ...     timespantools.Timespan(55, 65),
        ...     timespantools.Timespan(85, 95),
        ...     ])

    ::

        >>> from consort import makers
        >>> result = makers.subtract_timespan_inventories(
        ...      inventory_one, inventory_two)
        >>> print(format(result))
        timespantools.TimespanInventory(
            [
                timespantools.Timespan(
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(5, 1),
                    ),
                timespantools.Timespan(
                    start_offset=durationtools.Offset(15, 1),
                    stop_offset=durationtools.Offset(20, 1),
                    ),
                timespantools.Timespan(
                    start_offset=durationtools.Offset(45, 1),
                    stop_offset=durationtools.Offset(55, 1),
                    ),
                timespantools.Timespan(
                    start_offset=durationtools.Offset(65, 1),
                    stop_offset=durationtools.Offset(80, 1),
                    ),
                ]
            )

    ::

        >>> from consort import makers
        >>> result = makers.subtract_timespan_inventories(
        ...      inventory_two, inventory_one)
        >>> print(format(result))
        timespantools.TimespanInventory(
            [
                timespantools.Timespan(
                    start_offset=durationtools.Offset(25, 1),
                    stop_offset=durationtools.Offset(35, 1),
                    ),
                timespantools.Timespan(
                    start_offset=durationtools.Offset(35, 1),
                    stop_offset=durationtools.Offset(40, 1),
                    ),
                timespantools.Timespan(
                    start_offset=durationtools.Offset(85, 1),
                    stop_offset=durationtools.Offset(95, 1),
                    ),
                ]
            )

    '''
    from consort import makers
    resulting_timespans = timetools.TimespanCollection()
    if not inventory_one or not inventory_two:
        return resulting_timespans
    subtractee_index = 0
    subtractor_index = 0
    subtractee = None
    subtractor = None
    subtractee_is_modified = False
    while subtractee_index < len(inventory_one) and \
        subtractor_index < len(inventory_two):
        if subtractee is None:
            subtractee = inventory_one[subtractee_index]
            subtractee_is_modified = False
        if subtractor is None:
            subtractor = inventory_two[subtractor_index]
#        print('ROUND X:')
#        print('\tSUBTRACTEE', subtractee)
#        print('\tSUBTRACTOR', subtractor)
        if subtractee.intersects_timespan(subtractor):
#            print('\tBATTLING')
            subtraction = subtractee - subtractor
            if len(subtraction) == 1:
#                print('\t\tONE SURVIVOR:', subtraction)
                subtractee = subtraction[0]
                subtractee_is_modified = True
            elif len(subtraction) == 2:
#                print('\t\tTWO SURVIVORS:', subtraction)
                resulting_timespans.insert(subtraction[0])
                subtractee = subtraction[1]
                subtractee_is_modified = True
            else:
#                print('\t\tNO SURVIVORS')
                subtractee = None
                subtractee_index += 1
        else:
#            print('\tDRAWING')
            if subtractee.stops_before_or_at_offset(subtractor.start_offset):
#                print('\t\tNEW SUBTRACTEE')
                resulting_timespans.insert(subtractee)
                subtractee = None
                subtractee_index += 1
            else:
#                print('\t\tNEW SUBTRACTOR')
                subtractor = None
                subtractor_index += 1
    if subtractee_is_modified:
        if subtractee:
            resulting_timespans.insert(subtractee)
        resulting_timespans.insert(inventory_one[subtractee_index + 1:])
    else:
        resulting_timespans.insert(inventory_one[subtractee_index:])
    for timespan in inventory_two:
        if isinstance(timespan, makers.SilentTimespan):
            continue
        resulting_timespans.insert(timespan)
    return resulting_timespans