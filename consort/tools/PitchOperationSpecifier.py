import abjad
import collections
from abjad.tools import abctools


class PitchOperationSpecifier(abctools.AbjadValueObject):
    r'''A operation specifier.

    ..  container:: example

        ::

            >>> pitch_operation_specifier = consort.PitchOperationSpecifier(
            ...     pitch_operations=(
            ...         abjad.CompoundOperator((
            ...             abjad.Rotation(1, stravinsky=True),
            ...             abjad.Transposition(1),
            ...             )),
            ...         None,
            ...         abjad.CompoundOperator((
            ...             abjad.Rotation(-1, stravinsky=True),
            ...             abjad.Transposition(-1),
            ...             ))
            ...         ),
            ...     ratio=(1, 2, 1),
            ...     )
            >>> print(format(pitch_operation_specifier))
            consort.tools.PitchOperationSpecifier(
                pitch_operations=(
                    abjad.CompoundOperator(
                        operators=[
                            abjad.Rotation(
                                n=1,
                                stravinsky=True,
                                ),
                            abjad.Transposition(
                                n=1,
                                ),
                            ],
                        ),
                    None,
                    abjad.CompoundOperator(
                        operators=[
                            abjad.Rotation(
                                n=-1,
                                stravinsky=True,
                                ),
                            abjad.Transposition(
                                n=-1,
                                ),
                            ],
                        ),
                    ),
                ratio=abjad.Ratio((1, 2, 1)),
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
                abjad.CompoundOperator,
                type(None),
                )
            coerced_pitch_operations = []
            for x in pitch_operations:
                if not isinstance(x, prototype):
                    x = abjad.CompoundOperator(x)
                coerced_pitch_operations.append(x)
            pitch_operations = tuple(coerced_pitch_operations)
            assert len(pitch_operations)

        if pitch_operations and not ratio:
            ratio = [1] * len(pitch_operations)

        if ratio is not None:
            ratio = abjad.Ratio([abs(_) for _ in ratio])
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

                >>> pitch_operation_specifier = consort.PitchOperationSpecifier(
                ...     pitch_operations=(
                ...         abjad.CompoundOperator((
                ...             abjad.Rotation(1, stravinsky=True),
                ...             abjad.Transposition(1),
                ...             )),
                ...         None,
                ...         abjad.CompoundOperator((
                ...             abjad.Rotation(-1, stravinsky=True),
                ...             abjad.Transposition(-1),
                ...             ))
                ...         ),
                ...     ratio=(1, 2, 1),
                ...     )
                >>> timespans = pitch_operation_specifier.get_timespans(10)
                >>> print(format(timespans))
                consort.tools.TimespanCollection(
                    [
                        abjad.AnnotatedTimespan(
                            start_offset=abjad.Offset(0, 1),
                            stop_offset=abjad.Offset(5, 2),
                            annotation=abjad.CompoundOperator(
                                operators=[
                                    abjad.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    abjad.Transposition(
                                        n=1,
                                        ),
                                    ],
                                ),
                            ),
                        abjad.AnnotatedTimespan(
                            start_offset=abjad.Offset(5, 2),
                            stop_offset=abjad.Offset(15, 2),
                            ),
                        abjad.AnnotatedTimespan(
                            start_offset=abjad.Offset(15, 2),
                            stop_offset=abjad.Offset(10, 1),
                            annotation=abjad.CompoundOperator(
                                operators=[
                                    abjad.Rotation(
                                        n=-1,
                                        stravinsky=True,
                                        ),
                                    abjad.Transposition(
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
                ...         abjad.Rotation(1, stravinsky=True),
                ...         abjad.Transposition(1),
                ...         abjad.Inversion(),
                ...         None,
                ...         ),
                ...     ratio=(1, 2, 3, 1),
                ...     )
                >>> timespans = pitch_operation_specifier.get_timespans(10)
                >>> print(format(timespans))
                consort.tools.TimespanCollection(
                    [
                        abjad.AnnotatedTimespan(
                            start_offset=abjad.Offset(0, 1),
                            stop_offset=abjad.Offset(10, 7),
                            annotation=abjad.CompoundOperator(
                                operators=[
                                    abjad.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    ],
                                ),
                            ),
                        abjad.AnnotatedTimespan(
                            start_offset=abjad.Offset(10, 7),
                            stop_offset=abjad.Offset(30, 7),
                            annotation=abjad.CompoundOperator(
                                operators=[
                                    abjad.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    abjad.Transposition(
                                        n=1,
                                        ),
                                    ],
                                ),
                            ),
                        abjad.AnnotatedTimespan(
                            start_offset=abjad.Offset(30, 7),
                            stop_offset=abjad.Offset(60, 7),
                            annotation=abjad.CompoundOperator(
                                operators=[
                                    abjad.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    abjad.Transposition(
                                        n=1,
                                        ),
                                    abjad.Inversion(),
                                    ],
                                ),
                            ),
                        abjad.AnnotatedTimespan(
                            start_offset=abjad.Offset(60, 7),
                            stop_offset=abjad.Offset(10, 1),
                            annotation=abjad.CompoundOperator(
                                operators=[
                                    abjad.Rotation(
                                        n=1,
                                        stravinsky=True,
                                        ),
                                    abjad.Transposition(
                                        n=1,
                                        ),
                                    abjad.Inversion(),
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
            annotated_timespan = abjad.AnnotatedTimespan(
                start_offset=0,
                stop_offset=stop_offset,
                ),
            timespans.insert(annotated_timespan)
        else:
            target_timespan = abjad.Timespan(
                start_offset=0,
                stop_offset=stop_offset,
                )
            divided_timespans = target_timespan.divide_by_ratio(self.ratio)
            pitch_operation = abjad.CompoundOperator()
            for i, timespan in enumerate(divided_timespans):
                current_pitch_operation = self._pitch_operations[i]
                if self.is_cumulative:
                    if current_pitch_operation:
                        pitch_operation = abjad.CompoundOperator(
                            (pitch_operation.operators or []) +
                            current_pitch_operation.operators
                            )
                else:
                    pitch_operation = current_pitch_operation
                annotated_timespan = abjad.AnnotatedTimespan(
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
            ...         abjad.CompoundOperator((
            ...             abjad.Rotation(1, stravinsky=True),
            ...             abjad.Transposition(1),
            ...             )),
            ...         None,
            ...         abjad.CompoundOperator((
            ...             abjad.Rotation(-1, stravinsky=True),
            ...             abjad.Transposition(-1),
            ...             ))
            ...         ),
            ...     ratio=(1, 2, 1),
            ...     )
            >>> rotated_specifier = pitch_operation_specifier.rotate(1)
            >>> print(format(rotated_specifier))
            consort.tools.PitchOperationSpecifier(
                pitch_operations=(
                    abjad.CompoundOperator(
                        operators=[
                            abjad.Rotation(
                                n=-1,
                                stravinsky=True,
                                ),
                            abjad.Transposition(
                                n=-1,
                                ),
                            ],
                        ),
                    abjad.CompoundOperator(
                        operators=[
                            abjad.Rotation(
                                n=1,
                                stravinsky=True,
                                ),
                            abjad.Transposition(
                                n=1,
                                ),
                            ],
                        ),
                    None,
                    ),
                ratio=abjad.Ratio((1, 1, 2)),
                )

        Returns new pitch specifier.
        '''
        import consort
        rotation = int(rotation)
        pitch_operations = consort.rotate(self.pitch_operations, rotation)
        ratio = consort.rotate(self.ratio, rotation)
        return abjad.new(
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
