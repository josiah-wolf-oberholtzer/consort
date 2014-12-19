# -*- encoding: utf-8 -*-
from abjad import new
from abjad import abctools
from abjad import mathtools
from abjad import timespantools
from supriya import timetools


class TransformSpecifier(abctools.AbjadValueObject):
    r'''A transform specifier.

    ::

        >>> import consort
        >>> transform_specifier = consort.TransformSpecifier(
        ...     transform_stacks=(
        ...         consort.TransformStack((
        ...             pitchtools.Rotation(1),
        ...             pitchtools.Transposition(1),
        ...             )),
        ...         None,
        ...         consort.TransformStack((
        ...             pitchtools.Rotation(-1),
        ...             pitchtools.Transposition(-1),
        ...             ))
        ...         ),
        ...     ratio=(1, 2, 1),
        ...     )
        >>> print(format(transform_specifier))
        consort.tools.TransformSpecifier(
            transform_stacks=(
                consort.tools.TransformStack(
                    transforms=(
                        pitchtools.Rotation(
                            index=1,
                            transpose=True,
                            ),
                        pitchtools.Transposition(
                            index=1,
                            ),
                        ),
                    ),
                None,
                consort.tools.TransformStack(
                    transforms=(
                        pitchtools.Rotation(
                            index=-1,
                            transpose=True,
                            ),
                        pitchtools.Transposition(
                            index=-1,
                            ),
                        ),
                    ),
                ),
            ratio=mathtools.Ratio(1, 2, 1),
            )

    '''

    def __init__(
        self,
        transform_stacks=(None,),
        ratio=(1, 1),
        ):
        import consort
        prototype = (
            consort.TransformStack,
            type(None),
            )
        assert all(isinstance(x, prototype) for x in transform_stacks)
        assert len(transform_stacks)
        self._transform_stacks = tuple(transform_stacks)
        ratio = mathtools.Ratio([abs(x) for x in ratio])
        assert len(ratio) == len(transform_stacks)
        self._ratio = ratio

    ### PRIVATE METHODS ###

    def _get_transform_timespans(self, stop_offset):
        transform_timespans = timetools.TimespanCollection()
        target_timespan = timespantools.Timespan(
            start_offset=0,
            stop_offset=stop_offset,
            )
        divided_timespans = target_timespan.divide_by_ratio(self.ratio)
        for i, timespan in enumerate(divided_timespans):
            transform_stack = self._transform_stacks[i]
            annotated_timespan = timespantools.AnnotatedTimespan(
                annotation=transform_stack,
                start_offset=timespan.start_offset,
                stop_offset=timespan.stop_offset,
                )
            transform_timespans.insert(annotated_timespan)
        return transform_timespans

    ### PUBLIC METHODS ###

    def get_pitch_expr_timespans(self, pitch_expr, stop_offset):
        r'''Gets pitch expr timespans.

        ::

            >>> pitch_expr = pitchtools.PitchClassSegment([0, 1, 4, 7])
            >>> timespans = transform_specifier.get_pitch_expr_timespans(
            ...     pitch_expr, 10)
            >>> print(format(timespans))
            supriya.tools.timetools.TimespanCollection(
                [
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(5, 2),
                        annotation=pitchtools.PitchClassSegment(
                            (
                                pitchtools.NumberedPitchClass(1),
                                pitchtools.NumberedPitchClass(6),
                                pitchtools.NumberedPitchClass(7),
                                pitchtools.NumberedPitchClass(10),
                                ),
                            item_class=pitchtools.NumberedPitchClass,
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(5, 2),
                        stop_offset=durationtools.Offset(15, 2),
                        annotation=pitchtools.PitchClassSegment(
                            (
                                pitchtools.NumberedPitchClass(0),
                                pitchtools.NumberedPitchClass(1),
                                pitchtools.NumberedPitchClass(4),
                                pitchtools.NumberedPitchClass(7),
                                ),
                            item_class=pitchtools.NumberedPitchClass,
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(15, 2),
                        stop_offset=durationtools.Offset(10, 1),
                        annotation=pitchtools.PitchClassSegment(
                            (
                                pitchtools.NumberedPitchClass(11),
                                pitchtools.NumberedPitchClass(2),
                                pitchtools.NumberedPitchClass(5),
                                pitchtools.NumberedPitchClass(10),
                                ),
                            item_class=pitchtools.NumberedPitchClass,
                            ),
                        ),
                    ]
                )

        Returns timespan colleciton.
        '''
        pitch_expr_timespans = timetools.TimespanCollection()
        transform_timespans = self._get_transform_timespans(stop_offset)
        for transform_timespan in transform_timespans:
            transform_stack = transform_timespan.annotation
            if transform_stack is not None:
                transformed_pitch_expr = transform_stack(pitch_expr)
            else:
                transformed_pitch_expr = pitch_expr
            pitch_expr_timespan = new(
                transform_timespan,
                annotation=transformed_pitch_expr,
                )
            pitch_expr_timespans.insert(pitch_expr_timespan)
        return pitch_expr_timespans

    ### PUBLIC PROPERTIES ###

    @property
    def ratio(self):
        return self._ratio

    @property
    def transform_stacks(self):
        return self._transform_stacks