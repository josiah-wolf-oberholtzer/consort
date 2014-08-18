# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import pitchtools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class PitchMaker(abctools.AbjadValueObject):
    
    ### CLASS VARIABLES ###

    __slots__ = (
        '_allow_repetition',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        allow_repetition=False,
        ):
        self._allow_repetition = bool(allow_repetition)

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        pitch_range = inspect_(music).get_effective(pitchtools.PitchRange)
        previous_pitch = None
        iterator = iterate(music).by_logical_tie(pitched=True)
        for i, logical_tie in enumerate(iterator):
            previous_pitch = self._process_logical_tie(
                logical_tie,
                previous_pitch=previous_pitch,
                pitch_range=pitch_range,
                seed=seed + i,
                )

    ### PUBLIC PROPERTIES ###

    @property
    def allow_repetition(self):
        return self._allow_repetition
