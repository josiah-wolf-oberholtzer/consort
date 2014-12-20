# -*- encoding: utf-8 -*-
from abjad import abctools
from abjad import pitchtools


class PitchOperation(abctools.AbjadValueObject):
    r'''A transform stack.

    ::

        >>> import consort
        >>> pitch_operation = consort.PitchOperation(
        ...     operators=(
        ...         pitchtools.Rotation(1),
        ...         pitchtools.Transposition(2),
        ...         ),
        ...     )
        >>> print(format(pitch_operation))
        consort.tools.PitchOperation(
            operators=(
                pitchtools.Rotation(
                    index=1,
                    transpose=True,
                    ),
                pitchtools.Transposition(
                    index=2,
                    ),
                ),
            )

    ::

        >>> pitch_classes = pitchtools.PitchClassSegment([0, 1, 4, 7])
        >>> pitch_operation(pitch_classes)
        PitchClassSegment([2, 7, 8, 11])

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_operators',
        )

    ### INITIALIZER ###

    def __init__(self, operators=None):
        prototype = (
            pitchtools.Inversion,
            pitchtools.Multiplication,
            pitchtools.Transposition,
            pitchtools.Rotation,
            )
        if operators is not None:
            assert len(operators)
            assert all(isinstance(_, prototype) for _ in operators)
            operators = tuple(operators)
        self._operators = operators

    ### SPECIAL METHODS ###

    def __call__(self, pitch_expr):
        if self.operators is None:
            return pitch_expr
        for transform in self.operators:
            pitch_expr = transform(pitch_expr)
        return pitch_expr

    ### PUBLIC PROPERTIES ###

    @property
    def operators(self):
        return self._operators