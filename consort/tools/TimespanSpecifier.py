# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import durationtools


class TimespanSpecifier(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_forbid_fusing',
        '_forbid_splitting',
        '_minimum_duration',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        forbid_fusing=None,
        forbid_splitting=None,
        minimum_duration=None,
        ):
        if forbid_fusing is not None:
            forbid_fusing = bool(forbid_fusing)
        self._forbid_fusing = forbid_fusing
        if forbid_splitting is not None:
            forbid_splitting = bool(forbid_splitting)
        self._forbid_splitting = forbid_splitting
        if minimum_duration is not None:
            minimum_duration = durationtools.Duration(minimum_duration)
        self._minimum_duration = minimum_duration

    ### PUBLIC PROPERTIES ###

    @property
    def forbid_fusing(self):
        return self._forbid_fusing

    @property
    def forbid_splitting(self):
        return self._forbid_splitting

    @property
    def minimum_duration(self):
        return self._minimum_duration