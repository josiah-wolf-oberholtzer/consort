# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import pitchtools
from abjad.tools import datastructuretools


class RegisterSpecifier(abctools.AbjadValueObject):
    r'''A register specifier.

    ::

        >>> from consort import makers
        >>> register_specifier = makers.RegisterSpecifier(
        ...     center_pitch=12,
        ...     division_inflections=(
        ...         makers.RegisterInflection(
        ...             inflections=(-6, 3, 6),
        ...             ratio=(1, 1),
        ...             ),
        ...         ),
        ...     phrase_inflections=(
        ...         makers.RegisterInflection(
        ...             inflections=(3, -3),
        ...             ratio=(1,),
        ...             ),
        ...         ),
        ...     segment_inflections=(
        ...         makers.RegisterInflection(
        ...             inflections=(-12, -9, 0, 12),
        ...             ratio=(3, 2, 1),
        ...             ),
        ...         ),
        ...     )
        >>> print(format(register_specifier))
        consort.makers.RegisterSpecifier(
            center_pitch=pitchtools.NumberedPitch(12),
            division_inflections=datastructuretools.CyclicTuple(
                [
                    consort.makers.RegisterInflection(
                        inflections=pitchtools.IntervalSegment(
                            (
                                pitchtools.NumberedInterval(-6),
                                pitchtools.NumberedInterval(3),
                                pitchtools.NumberedInterval(6),
                                ),
                            item_class=pitchtools.NumberedInterval,
                            ),
                        ratio=mathtools.Ratio(1, 1),
                        ),
                    ]
                ),
            phrase_inflections=datastructuretools.CyclicTuple(
                [
                    consort.makers.RegisterInflection(
                        inflections=pitchtools.IntervalSegment(
                            (
                                pitchtools.NumberedInterval(3),
                                pitchtools.NumberedInterval(-3),
                                ),
                            item_class=pitchtools.NumberedInterval,
                            ),
                        ratio=mathtools.Ratio(1),
                        ),
                    ]
                ),
            segment_inflections=datastructuretools.CyclicTuple(
                [
                    consort.makers.RegisterInflection(
                        inflections=pitchtools.IntervalSegment(
                            (
                                pitchtools.NumberedInterval(-12),
                                pitchtools.NumberedInterval(-9),
                                pitchtools.NumberedInterval(0),
                                pitchtools.NumberedInterval(12),
                                ),
                            item_class=pitchtools.NumberedInterval,
                            ),
                        ratio=mathtools.Ratio(3, 2, 1),
                        ),
                    ]
                ),
            )

    ::

        >>> attack_point_signature = makers.AttackPointSignature(
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
        from consort import makers
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
        prototype = makers.RegisterInflection
        if division_inflections is not None:
            if isinstance(division_inflections, prototype):
                division_inflections = [division_inflections]
            assert all(isinstance(x, prototype) for x in division_inflections)
            division_inflections = datastructuretools.CyclicTuple(
                division_inflections)
        self._division_inflections = division_inflections
        if phrase_inflections is not None:
            if isinstance(phrase_inflections, prototype):
                phrase_inflections = [phrase_inflections]
            assert all(isinstance(x, prototype) for x in phrase_inflections)
            phrase_inflections = datastructuretools.CyclicTuple(
                phrase_inflections)
        self._phrase_inflections = phrase_inflections
        if segment_inflections is not None:
            if isinstance(segment_inflections, prototype):
                segment_inflections = [segment_inflections]
            assert all(isinstance(x, prototype) for x in segment_inflections)
            segment_inflections = datastructuretools.CyclicTuple(
                segment_inflections)
        self._segment_inflections = segment_inflections

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        r'''Attribute manifest.

        ::

            >>> from consort import makers
            >>> register_specifier = makers.RegisterSpecifier()
            >>> attribute_manifest = register_specifier._attribute_manifest

        '''
        from abjad.tools import systemtools
        from consort import makers
        from scoremanager import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='center_pitch',
                display_string='center pitch',
                command='c',
                editor=idetools.getters.get_named_pitch,
                ),
            systemtools.AttributeDetail(
                name='division_inflections',
                display_string='division inflections',
                command='di',
                editor=makers.RegisterInflection,
                ),
            systemtools.AttributeDetail(
                name='phrase_inflections',
                display_string='phrase inflections',
                command='pi',
                editor=makers.RegisterInflection,
                ),
            systemtools.AttributeDetail(
                name='segment_inflections',
                display_string='segment inflections',
                command='si',
                editor=makers.RegisterInflection,
                ),
            )

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
            inflection = self.division_inflections[seed]
            deviation = inflection(division_position)
            register = register.transpose(deviation)
        if self.phrase_inflections:
            inflection = self.phrase_inflections[seed]
            deviation = inflection(phrase_position)
            register = register.transpose(deviation)
        if self.segment_inflections:
            inflection = self.segment_inflections[seed]
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