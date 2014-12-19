# -*- encoding: utf-8 -*-
from abjad import abctools
from abjad import pitchtools


class TransformStack(abctools.AbjadValueObject):
    r'''A transform stack.

    ::

        >>> import consort
        >>> transform_stack = consort.TransformStack(
        ...     transforms=(
        ...         pitchtools.Rotation(1),
        ...         pitchtools.Transposition(2),
        ...         ),
        ...     )
        >>> print(format(transform_stack))
        consort.tools.TransformStack(
            transforms=(
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
        >>> transform_stack(pitch_classes)
        PitchClassSegment([2, 7, 8, 11])

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_transforms',
        )

    ### INITIALIZER ###

    def __init__(self, transforms=None):
        prototype = (
            pitchtools.Inversion,
            pitchtools.Multiplication,
            pitchtools.Transposition,
            pitchtools.Rotation,
            )
        if transforms is not None:
            assert len(transforms)
            assert all(isinstance(_, prototype) for _ in transforms)
            transforms = tuple(transforms)
        self._transforms = transforms

    ### SPECIAL METHODS ###

    def __call__(self, pitch_expr):
        if self.transforms is None:
            return pitch_expr
        for transform in self.transforms:
            pitch_expr = transform(pitch_expr)
        return pitch_expr

    ### PUBLIC PROPERTIES ###

    @property
    def transforms(self):
        return self._transforms