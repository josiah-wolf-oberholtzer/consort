# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import mathtools
from abjad.tools import pitchtools
from abjad.tools import timespantools


class PitchOperationSpecifier(abctools.AbjadValueObject):
    r'''A operation specifier.

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
        '_pitch_operations',
        '_ratio',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pitch_operations=None,
        ratio=None,
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
            ratio = mathtools.Ratio([abs(x) for x in ratio])
            assert len(ratio) == len(pitch_operations)

        self._pitch_operations = pitch_operations
        self._ratio = ratio

    ### PUBLIC METHODS ###

    def get_timespans(self, stop_offset):
        r'''Gets pitch expr timespans.

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
            for i, timespan in enumerate(divided_timespans):
                pitch_operation = self._pitch_operations[i]
                annotated_timespan = timespantools.AnnotatedTimespan(
                    annotation=pitch_operation,
                    start_offset=timespan.start_offset,
                    stop_offset=timespan.stop_offset,
                    )
                timespans.insert(annotated_timespan)
        return timespans

    ### PUBLIC PROPERTIES ###

    @property
    def ratio(self):
        return self._ratio

    @property
    def pitch_operations(self):
        return self._pitch_operations