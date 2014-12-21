# -*- encoding: utf-8 -*-
import collections
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
        if not isinstance(pitch_operations, collections.Sequence):
                pitch_operations = (pitch_operations,)
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

    ### PUBLIC METHODS ###

    def get_timespans(self, stop_offset):
        r'''Gets pitch expr timespans.

        ::

            >>> timespans = pitch_operation_specifier.get_timespans(10)
            >>> print(format(timespans))
            supriya.tools.timetools.TimespanCollection(
                [
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(5, 2),
                        annotation=consort.tools.PitchOperation(
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
                        annotation=consort.tools.PitchOperation(
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

        Returns timespan colleciton.
        '''
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

    ### PUBLIC PROPERTIES ###

    @property
    def ratio(self):
        return self._ratio

    @property
    def pitch_operations(self):
        return self._pitch_operations