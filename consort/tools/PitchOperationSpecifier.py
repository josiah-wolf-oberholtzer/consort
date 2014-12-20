# -*- encoding: utf-8 -*-
from abjad import new
from abjad import abctools
from abjad import mathtools
from abjad import timespantools
from supriya import timetools


class PitchOperationSpecifier(abctools.AbjadValueObject):
    r'''A operation specifier.

    ::

        >>> import consort
        >>> pitch_operation_specifier = consort.PitchOperationSpecifier(
        ...     pitch_operations=(
        ...         consort.PitchOperation((
        ...             pitchtools.Rotation(1),
        ...             pitchtools.Transposition(1),
        ...             )),
        ...         None,
        ...         consort.PitchOperation((
        ...             pitchtools.Rotation(-1),
        ...             pitchtools.Transposition(-1),
        ...             ))
        ...         ),
        ...     ratio=(1, 2, 1),
        ...     )
        >>> print(format(pitch_operation_specifier))
        consort.tools.PitchOperationSpecifier(
            pitch_operations=(
                consort.tools.PitchOperation(
                    operators=(
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
                consort.tools.PitchOperation(
                    operators=(
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

    ### CLASS VARIABLES ###

    __slots__ = (
        '_pitch_operations',
        '_ratio',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pitch_operations=(None,),
        ratio=(1,),
        ):
        import consort
        prototype = (
            consort.PitchOperation,
            type(None),
            )
        assert all(isinstance(x, prototype) for x in pitch_operations)
        assert len(pitch_operations)
        self._pitch_operations = tuple(pitch_operations)
        ratio = mathtools.Ratio([abs(x) for x in ratio])
        assert len(ratio) == len(pitch_operations)
        self._ratio = ratio

    ### PRIVATE METHODS ###

    def _get_timespans(self, stop_offset):
        timespans = timetools.TimespanCollection()
        target_timespan = timespantools.Timespan(
            start_offset=0,
            stop_offset=stop_offset,
            )
        divided_timespans = target_timespan.divide_by_ratio(self.ratio)
        for i, timespan in enumerate(divided_timespans):
            pitch_operation = self._pitch_operations[i]
            annotated_timespan = timespantools.AnnotatedTimespan(
                annotation=pitch_operation,
                start_offset=timespan.start_offset,
                stop_offset=timespan.stop_offset,
                )
            timespans.insert(annotated_timespan)
        return timespans

    ### PUBLIC METHODS ###

    def get_timespans(self, pitch_expr, stop_offset):
        r'''Gets pitch expr timespans.

        ::

            >>> pitch_expr = pitchtools.PitchClassSegment([0, 1, 4, 7])
            >>> timespans = pitch_operation_specifier.get_timespans(
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
        operation_timespans = self._get_timespans(stop_offset)
        for operation_timespan in operation_timespans:
            pitch_operation = operation_timespan.annotation
            if pitch_operation is not None:
                operationed_pitch_expr = pitch_operation(pitch_expr)
            else:
                operationed_pitch_expr = pitch_expr
            pitch_expr_timespan = new(
                operation_timespan,
                annotation=operationed_pitch_expr,
                )
            pitch_expr_timespans.insert(pitch_expr_timespan)
        return pitch_expr_timespans

    ### PUBLIC PROPERTIES ###

    @property
    def ratio(self):
        return self._ratio

    @property
    def pitch_operations(self):
        return self._pitch_operations