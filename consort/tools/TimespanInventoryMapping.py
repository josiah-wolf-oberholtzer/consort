# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools
from abjad.tools import timespantools


class TimespanInventoryMapping(datastructuretools.TypedOrderedDict):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    def __illustration__(self, range_=None, scale=None):
        timespan_inventory = timespantools.TimespanInventory()
        for key, value in self.items():
            timespan_inventory.extend(value)
        return timespan_inventory.__illustrate__(range_=range_, scale=scale)

    ### PRIVATE PROPERTIES ###

    @property
    def _item_coercer(self):
        return timespantools.TimespanInventory
