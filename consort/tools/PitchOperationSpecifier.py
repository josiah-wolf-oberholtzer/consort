# -*- encoding: utf-8 -*-
import collections
from abjad import new
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
            ...         pitchtools.CompoundOperator((
            ...             pitchtools.Rotation(1, stravinsky=True),
            ...             pitchtools.Transposition(1),
            ...             )),
            ...         None,
            ...         pitchtools.CompoundOperator((
            ...             pitchtools.Rotation(-1, stravinsky=True),
            ...             pitchtools.Transposition(-1),
            ...             ))
            ...         ),
            ...     ratio=(1, 2, 1),
            ...     )
            >>> print(format(pitch_operation_specifier))
            consort.tools.PitchOperationSpecifier(
                pitch_operations=(
                    pitchtools.CompoundOperator(
                        operators=[
                            pitchtools.Rotation(
                                n=1,
                                stravinsky=True,
                                ),
                            pitchtools.Transposition(
                                n=1,
                                ),
                            ],
                        ),
                    None,
                    pitchtools.CompoundOperator(
                        operators=[
                            pitchtools.Rotation(
                                n=-1,
                                stravinsky=True,
                                ),
                            pitchtools.Transposition(
                                n=-1,
                                ),
                            ],
                        ),
                    ),
                ratio=mathtools.Ratio((1, 2, 1)),
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
                pitchtools.CompoundOperator,
                type(None),
                )
            coerced_pitch_operations = []
            for x in pitch_operations:
                if not isinstance(x, prototype):
                    x = pitchtools.CompoundOperator(x)
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
                            annotation=pitchtools.CompoundOperator(
                                operators=[
                                    pitchtools.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    pitchtools.Transposition(
                                        n=1,
                                        ),
                                    ],
                                ),
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(5, 2),
                            stop_offset=durationtools.Offset(15, 2),
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(15, 2),
                            stop_offset=durationtools.Offset(10, 1),
                            annotation=pitchtools.CompoundOperator(
                                operators=[
                                    pitchtools.Rotation(
                                        n=-1,
                                        stravinsky=True,
                                        ),
                                    pitchtools.Transposition(
                                        n=-1,
                                        ),
                                    ],
                                ),
                            ),
                        ]
                    )

        ..  container:: example

            ::

                >>> pitch_operation_specifier = consort.PitchOperationSpecifier(
                ...     is_cumulative=True,
                ...     pitch_operations=(
                ...         pitchtools.Rotation(1, stravinsky=True),
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
                            annotation=pitchtools.CompoundOperator(
                                operators=[
                                    pitchtools.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    ],
                                ),
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(10, 7),
                            stop_offset=durationtools.Offset(30, 7),
                            annotation=pitchtools.CompoundOperator(
                                operators=[
                                    pitchtools.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    pitchtools.Transposition(
                                        n=1,
                                        ),
                                    ],
                                ),
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(30, 7),
                            stop_offset=durationtools.Offset(60, 7),
                            annotation=pitchtools.CompoundOperator(
                                operators=[
                                    pitchtools.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    pitchtools.Transposition(
                                        n=1,
                                        ),
                                    pitchtools.Inversion(),
                                    ],
                                ),
                            ),
                        timespantools.AnnotatedTimespan(
                            start_offset=durationtools.Offset(60, 7),
                            stop_offset=durationtools.Offset(10, 1),
                            annotation=pitchtools.CompoundOperator(
                                operators=[
                                    pitchtools.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    pitchtools.Transposition(
                                        n=1,
                                        ),
                                    pitchtools.Inversion(),
                                    ],
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
            pitch_operation = pitchtools.CompoundOperator()
            for i, timespan in enumerate(divided_timespans):
                current_pitch_operation = self._pitch_operations[i]
                if self.is_cumulative:
                    if current_pitch_operation:
                        pitch_operation = pitchtools.CompoundOperator(
                            (pitch_operation.operators or []) +
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

    def rotate(self, rotation):
        r'''Rotates pitch operation specifier.

        ::

            >>> pitch_operation_specifier = consort.PitchOperationSpecifier(
            ...     pitch_operations=(
            ...         pitchtools.CompoundOperator((
            ...             pitchtools.Rotation(1, stravinsky=True),
            ...             pitchtools.Transposition(1),
            ...             )),
            ...         None,
            ...         pitchtools.CompoundOperator((
            ...             pitchtools.Rotation(-1, stravinsky=True),
            ...             pitchtools.Transposition(-1),
            ...             ))
            ...         ),
            ...     ratio=(1, 2, 1),
            ...     )
            >>> rotated_specifier = pitch_operation_specifier.rotate(1)
            >>> print(format(rotated_specifier))
            consort.tools.PitchOperationSpecifier(
                pitch_operations=(
                    pitchtools.CompoundOperator(
                        operators=[
                            pitchtools.Rotation(
                                n=-1,
                                stravinsky=True,
                                ),
                            pitchtools.Transposition(
                                n=-1,
                                ),
                            ],
                        ),
                    pitchtools.CompoundOperator(
                        operators=[
                            pitchtools.Rotation(
                                n=1,
                                stravinsky=True,
                                ),
                            pitchtools.Transposition(
                                n=1,
                                ),
                            ],
                        ),
                    None,
                    ),
                ratio=mathtools.Ratio((1, 1, 2)),
                )

        Returns new pitch specifier.
        '''
        import consort
        rotation = int(rotation)
        pitch_operations = consort.rotate(self.pitch_operations, rotation)
        ratio = consort.rotate(self.ratio, rotation)
        return new(
            self,
            pitch_operations=pitch_operations,
            ratio=ratio,
            )

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
