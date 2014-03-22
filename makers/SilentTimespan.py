# -*- encoding: utf-8 -*-
from abjad.tools import timespantools


class SilentTimespan(timespantools.Timespan):
    r'''A silent timespan.
    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### PUBLIC PROPERTIES ###

    @property
    def color(self):
        return None

    @property
    def is_left_broken(self):
        return False

    @property
    def is_right_broken(self):
        return False
