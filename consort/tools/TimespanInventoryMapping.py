# -*- encoding: utf-8 -*-
from abjad.tools import timespantools


class TimespanInventoryMapping(dict):

    ### SPECIAL METHODS ###

    def __illustration__(self, range_=None, scale=None):
        timespan_inventory = timespantools.TimespanInventory()
        for key, value in self.items():
            timespan_inventory.extend(value)
        return timespan_inventory.__illustrate__(
            key='voice_name',
            range_=range_,
            scale=scale,
            )