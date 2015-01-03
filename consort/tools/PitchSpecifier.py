# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import mathtools
from abjad.tools import pitchtools
from abjad.tools import timespantools


class PitchSpecifier(abctools.AbjadValueObject):
    r'''A pitch specifier.

    ::

        >>> import consort
        >>> pitch_specifier = consort.PitchSpecifier(
        ...     pitch_segments=(
        ...         "c' e' g'",
        ...         "fs' gs'",
        ...         "b",
        ...         ),
        ...     ratio=(1, 2, 3),
        ...     )
        >>> print(format(pitch_specifier))
        consort.tools.PitchSpecifier(
            pitch_segments=(
                pitchtools.PitchSegment(
                    (
                        pitchtools.NamedPitch("c'"),
                        pitchtools.NamedPitch("e'"),
                        pitchtools.NamedPitch("g'"),
                        ),
                    item_class=pitchtools.NamedPitch,
                    ),
                pitchtools.PitchSegment(
                    (
                        pitchtools.NamedPitch("fs'"),
                        pitchtools.NamedPitch("gs'"),
                        ),
                    item_class=pitchtools.NamedPitch,
                    ),
                pitchtools.PitchSegment(
                    (
                        pitchtools.NamedPitch('b'),
                        ),
                    item_class=pitchtools.NamedPitch,
                    ),
                ),
            ratio=mathtools.Ratio(1, 2, 3),
            )

    ::

        >>> pitch_specifier = consort.PitchSpecifier("c' e' g' a'")
        >>> print(format(pitch_specifier))
        consort.tools.PitchSpecifier(
            pitch_segments=(
                pitchtools.PitchSegment(
                    (
                        pitchtools.NamedPitch("c'"),
                        pitchtools.NamedPitch("e'"),
                        pitchtools.NamedPitch("g'"),
                        pitchtools.NamedPitch("a'"),
                        ),
                    item_class=pitchtools.NamedPitch,
                    ),
                ),
            ratio=mathtools.Ratio(1),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_pitch_segments',
        '_ratio',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pitch_segments=("c'",),
        ratio=(1,),
        ):
        if not isinstance(pitch_segments, (list, tuple)):
            pitch_segments = (pitch_segments,)
        coerced_pitch_segments = []
        for pitch_segment in pitch_segments:
            pitch_segment = pitchtools.PitchSegment(
                pitch_segment,
                item_class=pitchtools.NamedPitch,
                )
            assert len(pitch_segment)
            coerced_pitch_segments.append(pitch_segment)
        pitch_segments = tuple(coerced_pitch_segments)
        assert len(pitch_segments)
        ratio = mathtools.Ratio([abs(x) for x in ratio])
        assert len(ratio) == len(pitch_segments)
        self._pitch_segments = pitch_segments
        self._ratio = ratio

    ### PUBLIC METHODS ###

    def get_timespans(self, stop_offset):
        r'''Gets pitch segment timespans.

        ::

            >>> pitch_specifier = consort.PitchSpecifier(
            ...     pitch_segments=(
            ...         "c' e' g'",
            ...         "fs' g'",
            ...         "b",
            ...         ),
            ...     ratio=(1, 2, 3),
            ...     )
            >>> timespans = pitch_specifier.get_timespans(stop_offset=10)
            >>> print(format(timespans))
            consort.tools.TimespanCollection(
                [
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(5, 3),
                        annotation=pitchtools.PitchSegment(
                            (
                                pitchtools.NamedPitch("c'"),
                                pitchtools.NamedPitch("e'"),
                                pitchtools.NamedPitch("g'"),
                                ),
                            item_class=pitchtools.NamedPitch,
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(5, 3),
                        stop_offset=durationtools.Offset(5, 1),
                        annotation=pitchtools.PitchSegment(
                            (
                                pitchtools.NamedPitch("fs'"),
                                pitchtools.NamedPitch("g'"),
                                ),
                            item_class=pitchtools.NamedPitch,
                            ),
                        ),
                    timespantools.AnnotatedTimespan(
                        start_offset=durationtools.Offset(5, 1),
                        stop_offset=durationtools.Offset(10, 1),
                        annotation=pitchtools.PitchSegment(
                            (
                                pitchtools.NamedPitch('b'),
                                ),
                            item_class=pitchtools.NamedPitch,
                            ),
                        ),
                    ]
                )

        '''
        import consort
        timespans = consort.TimespanCollection()
        target_timespan = timespantools.Timespan(
            start_offset=0,
            stop_offset=stop_offset,
            )
        divided_timespans = target_timespan.divide_by_ratio(self.ratio)
        for i, timespan in enumerate(divided_timespans):
            pitch_segment = self._pitch_segments[i]
            annotated_timespan = timespantools.AnnotatedTimespan(
                annotation=pitch_segment,
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
    def pitch_segments(self):
        return self._pitch_segments