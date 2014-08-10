# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools.topleveltools import iterate


class NonsemanticPitchMaker(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        ):
        pass

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        iterator = iterate(music).by_logical_tie(pitched=True)
        for i, logical_tie in enumerate(iterator):
            self._process_logical_tie(
                logical_tie,
                seed=seed + i,
                )

    ### PRIVATE METHODS ###

    def _process_logical_tie(
        self,
        logical_tie,
        seed=0,
        ):
        pass