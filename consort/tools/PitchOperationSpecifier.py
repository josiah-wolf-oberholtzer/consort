# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import mathtools
from abjad.tools import pitchtools
from abjad.tools import timespantools


class PitchOperationSpecifier(abctools.AbjadValueObject):
    r'''A operation specifier.

    ..  container:: example

        ::

            >>> import consort
            >>> pitch_operation_specifier = consort.PitchOperationSpecifier(
            ...     pitch_operations=(
            ...         pitchtools.PitchOperation((
            ...             pitchtools.Rotation(1),
            ...             pitchtools.Transposition(1),
            ...             )),
            ...         None,
            ...         pitchtools.PitchOperation((
            ...             pitchtools.Rotation(-1),
            ...             pitchtools.Transposition(-1),
            ...             ))
            ...         ),
            ...     ratio=(1, 2, 1),
            ...     )
            >>> print(format(pitch_operation_specifier))
            consort.tools.PitchOperationSpecifier(
                pitch_operations=(
                    pitchtools.PitchOperation(
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
                    pitchtools.PitchOperation(
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
        '_is_cumulative',
        '_pitch_operations',
        '_ratio',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pitch_operations=None,
        ratio=None,
        is_cumulative=None,
        ):
        if pitch_operations is not None:
            if not isinstance(pitch_operations, collections.Sequence):
                pitch_operations = (pitch_operations,)
            prototype = (
                pitchtools.PitchOperation,
                type(None),
                )
            coerced_pitch_operations = []
            for x in pitch_operations:
                if not isinstance(x, prototype):
                    x = pitchtools.PitchOperation(x)
                coerced_pitch_operations.append(x)
            pitch_operations = tuple(coerced_pitch_operations)
            assert len(pitch_operations)

        if pitch_operations and not ratio:
            ratio = [1] * len(pitch_operations)

        if ratio is not None:
            ratio = mathtools.Ratio([abs(_) for _ in ratio])
            assert len(ratio) == len(pitch_operations)

        if is_cumulative is not None:
            is_cumulative = bool(is_cumulative)

        self._is_cumulative = is_cumulative
        self._pitch_operations = pitch_operations
        self._ratio = ratio

    ### PUBLIC METHODS ###

    def get_timespans(self, stop_offset):
        r'''Gets pitch expr timespans.

        ..  container:: example

            ::

                >>> timespans = pitch_operation_specifier.get_timespans(10)
                >>> print(format(timespans))
                consort.tools.TimespanCollection(
                    [
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(0, 1),
                            stop_offset=durationtools.Offset(5, 2),
                            annotation=pitchtools.PitchOperation(
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
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(5, 2),
                            stop_offset=durationtools.Offset(15, 2),
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(15, 2),
                            stop_offset=durationtools.Offset(10, 1),
                            annotation=pitchtools.PitchOperation(
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
                        ]
                    )

        ..  container:: example

            ::

                >>> pitch_operation_specifier = consort.PitchOperationSpecifier(
                ...     is_cumulative=True,
                ...     pitch_operations=(
                ...         pitchtools.Rotation(1),
                ...         pitchtools.Transposition(1),
                ...         pitchtools.Inversion(),
                ...         None,
                ...         ),
                ...     ratio=(1, 2, 3, 1),
                ...     )
                >>> timespans = pitch_operation_specifier.get_timespans(10)
                >>> print(format(timespans))
                consort.tools.TimespanCollection(
                    [
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(0, 1),
                            stop_offset=durationtools.Offset(10, 7),
                            annotation=pitchtools.PitchOperation(
                                operators=(
                                    pitchtools.Rotation(
                                        index=1,
                                        transpose=True,
                                        ),
                                    ),
                                ),
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(10, 7),
                            stop_offset=durationtools.Offset(30, 7),
                            annotation=pitchtools.PitchOperation(
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
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(30, 7),
                            stop_offset=durationtools.Offset(60, 7),
                            annotation=pitchtools.PitchOperation(
                                operators=(
                                    pitchtools.Rotation(
                                        index=1,
                                        transpose=True,
                                        ),
                                    pitchtools.Transposition(
                                        index=1,
                                        ),
                                    pitchtools.Inversion(),
                                    ),
                                ),
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(60, 7),
                            stop_offset=durationtools.Offset(10, 1),
                            annotation=pitchtools.PitchOperation(
                                operators=(
                                    pitchtools.Rotation(
                                        index=1,
                                        transpose=True,
                                        ),
                                    pitchtools.Transposition(
                                        index=1,
                                        ),
                                    pitchtools.Inversion(),
                                    ),
                                ),
                            ),
                        ]
                    )

        Returns timespan collection.
        '''
        import consort
        timespans = consort.TimespanCollection()
        if not self.ratio or not self.pitch_operations:
            annotated_timespan = timespantools.AnnotatedTimespan(
                start_offset=0,
                stop_offset=stop_offset,
                ),
            timespans.insert(annotated_timespan)
        else:
            target_timespan = timespantools.Timespan(
                start_offset=0,
                stop_offset=stop_offset,
                )
            divided_timespans = target_timespan.divide_by_ratio(self.ratio)
            pitch_operation = pitchtools.PitchOperation()
            for i, timespan in enumerate(divided_timespans):
                current_pitch_operation = self._pitch_operations[i]
                if self.is_cumulative:
                    if current_pitch_operation:
                        pitch_operation = pitchtools.PitchOperation(
                            (pitch_operation.operators or ()) +
                            current_pitch_operation.operators
                            )
                else:
                    pitch_operation = current_pitch_operation
                annotated_timespan = timespantools.AnnotatedTimespan(
                    annotation=pitch_operation,
                    start_offset=timespan.start_offset,
                    stop_offset=timespan.stop_offset,
                    )
                timespans.insert(annotated_timespan)
        return timespans

    ### PUBLIC PROPERTIES ###

    @property
    def is_cumulative(self):
        return self._is_cumulative

    @property
    def ratio(self):
        return self._ratio

    @property
    def pitch_operations(self):
        return self._pitch_operations