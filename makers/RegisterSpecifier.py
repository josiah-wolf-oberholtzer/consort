# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import pitchtools
from abjad.tools import sequencetools


class RegisterSpecifier(abctools.AbjadValueObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_center_pitch',
        '_division_deviations',
        '_phrase_deviations',
        '_segment_deviations',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        center_pitch=0,
        division_deviations=None,
        phrase_deviations=None,
        segment_deviations=None,
        ):
        from consort import makers
        self._center_pitch = pitchtools.NumberedPitch(center_pitch)
        prototype = makers.BreakPointFunction
        if division_deviations is not None:
            if isinstance(division_deviations, prototype):
                division_deviations = [division_deviations]
            assert all(isinstance(x, prototype) for x in division_deviations)
            division_deviations = sequencetools.CyclicTuple(
                division_deviations)
        self._division_deviations = division_deviations
        if phrase_deviations is not None:
            if isinstance(phrase_deviations, prototype):
                phrase_deviations = [phrase_deviations]
            assert all(isinstance(x, prototype) for x in phrase_deviations)
            phrase_deviations = sequencetools.CyclicTuple(phrase_deviations)
        self._phrase_deviations = phrase_deviations
        if segment_deviations is not None:
            if isinstance(segment_deviations, prototype):
                segment_deviations = [segment_deviations]
            assert all(isinstance(x, prototype) for x in segment_deviations)
            segment_deviations = sequencetools.CyclicTuple(segment_deviations)
        self._segment_deviations = segment_deviations

    ### PUBLIC METHODS ###

    def find_register(
        self,
        division_position,
        phrase_position,
        segment_position,
        seed=0,
        ):
        seed = int(seed)
        register = self.center_pitch
        if self.division_deviations:
            break_point = self.division_deviations[seed]
            deviation = break_point[division_position]
            register = register.transpose(deviation)
        if self.phrase_deviations:
            break_point = self.phrase_deviations[seed]
            deviation = break_point[phrase_position]
            register = register.transpose(deviation)
        if self.segment_deviations:
            break_point = self.segment_deviations[seed]
            deviation = break_point[segment_position]
            register = register.transpose(deviation)
        return register

    ### PUBLIC PROPERTIES ###

    @property
    def center_pitch(self):
        return self._center_pitch

    @property
    def division_deviations(self):
        return self._division_deviations

    @property
    def phrase_deviations(self):
        return self._phrase_deviations

    @property
    def segment_deviations(self):
        return self._segment_deviations