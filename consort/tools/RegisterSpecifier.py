# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import pitchtools


class RegisterSpecifier(abctools.AbjadValueObject):
    r'''A register specifier.

    ::

        >>> import consort
        >>> register_specifier = consort.RegisterSpecifier(
        ...     center_pitch=12,
        ...     division_inflections=(
        ...         consort.RegisterInflection(
        ...             inflections=(-6, 3, 6),
        ...             ratio=(1, 1),
        ...             ),
        ...         ),
        ...     phrase_inflections=(
        ...         consort.RegisterInflection(
        ...             inflections=(3, -3),
        ...             ratio=(1,),
        ...             ),
        ...         ),
        ...     segment_inflections=(
        ...         consort.RegisterInflection(
        ...             inflections=(-12, -9, 0, 12),
        ...             ratio=(3, 2, 1),
        ...             ),
        ...         ),
        ...     )
        >>> print(format(register_specifier))
        consort.tools.RegisterSpecifier(
            center_pitch=pitchtools.NumberedPitch(12),
            division_inflections=consort.tools.RegisterInflectionInventory(
                [
                    consort.tools.RegisterInflection(
                        inflections=pitchtools.IntervalSegment(
                            (
                                pitchtools.NumberedInterval(-6),
                                pitchtools.NumberedInterval(3),
                                pitchtools.NumberedInterval(6),
                                ),
                            item_class=pitchtools.NumberedInterval,
                            ),
                        ratio=mathtools.Ratio((1, 1)),
                        ),
                    ]
                ),
            phrase_inflections=consort.tools.RegisterInflectionInventory(
                [
                    consort.tools.RegisterInflection(
                        inflections=pitchtools.IntervalSegment(
                            (
                                pitchtools.NumberedInterval(3),
                                pitchtools.NumberedInterval(-3),
                                ),
                            item_class=pitchtools.NumberedInterval,
                            ),
                        ratio=mathtools.Ratio((1,)),
                        ),
                    ]
                ),
            segment_inflections=consort.tools.RegisterInflectionInventory(
                [
                    consort.tools.RegisterInflection(
                        inflections=pitchtools.IntervalSegment(
                            (
                                pitchtools.NumberedInterval(-12),
                                pitchtools.NumberedInterval(-9),
                                pitchtools.NumberedInterval(0),
                                pitchtools.NumberedInterval(12),
                                ),
                            item_class=pitchtools.NumberedInterval,
                            ),
                        ratio=mathtools.Ratio((3, 2, 1)),
                        ),
                    ]
                ),
            )

    ::

        >>> attack_point_signature = consort.AttackPointSignature(
        ...     division_position=0,
        ...     phrase_position=(1, 2),
        ...     segment_position=(4, 5),
        ...     )
        >>> register_specifier.find_register(attack_point_signature)
        NumberedPitch(6)

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_center_pitch',
        '_division_inflections',
        '_phrase_inflections',
        '_segment_inflections',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        center_pitch=None,
        division_inflections=None,
        phrase_inflections=None,
        segment_inflections=None,
        ):
        from consort.tools import RegisterInflectionInventory
        if isinstance(center_pitch, type(self)):
            expr = center_pitch
            self._center_pitch = expr.center_pitch
            self._division_inflections = expr.division_inflections
            self._phrase_inflections = expr.phrase_inflections
            self._segment_inflections = expr.segment_inflections
            return
        if center_pitch is not None:
            center_pitch = pitchtools.NumberedPitch(center_pitch)
        self._center_pitch = center_pitch
        if division_inflections is not None:
            if not isinstance(division_inflections, collections.Sequence):
                division_inflections = [division_inflections]
            division_inflections = RegisterInflectionInventory(
                division_inflections)
        self._division_inflections = division_inflections
        if phrase_inflections is not None:
            if not isinstance(phrase_inflections, collections.Sequence):
                phrase_inflections = [phrase_inflections]
            phrase_inflections = RegisterInflectionInventory(
                phrase_inflections)
        self._phrase_inflections = phrase_inflections
        if segment_inflections is not None:
            if not isinstance(segment_inflections, collections.Sequence):
                segment_inflections = [segment_inflections]
            segment_inflections = RegisterInflectionInventory(
                segment_inflections)
        self._segment_inflections = segment_inflections

    ### PUBLIC METHODS ###

    def find_register(
        self,
        attack_point_signature,
        seed=0,
        ):
        division_position = attack_point_signature.division_position
        phrase_position = attack_point_signature.phrase_position
        segment_position = attack_point_signature.segment_position
        seed = int(seed)
        register = self.center_pitch
        if register is None:
            register = pitchtools.NumberedPitch(0)
        if self.division_inflections:
            index = seed % len(self.division_inflections)
            inflection = self.division_inflections[index]
            deviation = inflection(division_position)
            register = register.transpose(deviation)
        if self.phrase_inflections:
            index = seed % len(self.phrase_inflections)
            inflection = self.phrase_inflections[index]
            deviation = inflection(phrase_position)
            register = register.transpose(deviation)
        if self.segment_inflections:
            index = seed % len(self.segment_inflections)
            inflection = self.segment_inflections[index]
            deviation = inflection(segment_position)
            register = register.transpose(deviation)
        return register

    ### PUBLIC PROPERTIES ###

    @property
    def center_pitch(self):
        return self._center_pitch

    @property
    def division_inflections(self):
        return self._division_inflections

    @property
    def phrase_inflections(self):
        return self._phrase_inflections

    @property
    def segment_inflections(self):
        return self._segment_inflections