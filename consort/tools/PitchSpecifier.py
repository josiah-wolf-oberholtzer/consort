import abjad
from abjad.tools import abctools
from abjad.tools import pitchtools


class PitchSpecifier(abctools.AbjadValueObject):
    r'''A pitch specifier.

    ::

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
                abjad.PitchSegment(
                    (
                        abjad.NamedPitch("c'"),
                        abjad.NamedPitch("e'"),
                        abjad.NamedPitch("g'"),
                        ),
                    item_class=abjad.NamedPitch,
                    ),
                abjad.PitchSegment(
                    (
                        abjad.NamedPitch("fs'"),
                        abjad.NamedPitch("gs'"),
                        ),
                    item_class=abjad.NamedPitch,
                    ),
                abjad.PitchSegment(
                    (
                        abjad.NamedPitch('b'),
                        ),
                    item_class=abjad.NamedPitch,
                    ),
                ),
            ratio=abjad.Ratio((1, 2, 3)),
            )

    Pitch specifiers can be instantiated from a string of pitch names:

    ::

        >>> pitch_specifier = consort.PitchSpecifier("c' e' g' a'")
        >>> print(format(pitch_specifier))
        consort.tools.PitchSpecifier(
            pitch_segments=(
                abjad.PitchSegment(
                    (
                        abjad.NamedPitch("c'"),
                        abjad.NamedPitch("e'"),
                        abjad.NamedPitch("g'"),
                        abjad.NamedPitch("a'"),
                        ),
                    item_class=abjad.NamedPitch,
                    ),
                ),
            ratio=abjad.Ratio((1,)),
            )

    Pitch specifiers can be instantiated from a single pitch:

    ::

        >>> pitch_specifier = consort.PitchSpecifier(abjad.NamedPitch("ds'"))
        >>> print(format(pitch_specifier))
        consort.tools.PitchSpecifier(
            pitch_segments=(
                abjad.PitchSegment(
                    (
                        abjad.NamedPitch("ds'"),
                        ),
                    item_class=abjad.NamedPitch,
                    ),
                ),
            ratio=abjad.Ratio((1,)),
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
        pitch_segments=None,
        ratio=None,
        ):
        if pitch_segments is not None:
            if isinstance(pitch_segments, pitchtools.Pitch):
                pitch_segments = abjad.PitchSegment([pitch_segments])
            elif isinstance(pitch_segments, str):
                pitch_segments = abjad.PitchSegment(pitch_segments)
            if isinstance(pitch_segments, abjad.PitchSegment):
                pitch_segments = [pitch_segments]
            coerced_pitch_segments = []
            for pitch_segment in pitch_segments:
                pitch_segment = abjad.PitchSegment(
                    pitch_segment,
                    item_class=abjad.NamedPitch,
                    )
                if not pitch_segment:
                    pitch_segment = abjad.PitchSegment("c'")
                coerced_pitch_segments.append(pitch_segment)
            pitch_segments = tuple(coerced_pitch_segments)
            assert len(pitch_segments)

        if pitch_segments and not ratio:
            ratio = [1] * len(pitch_segments)

        if ratio is not None:
            ratio = abjad.Ratio([abs(x) for x in ratio])
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
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset(0, 1),
                        stop_offset=abjad.Offset(5, 3),
                        annotation=abjad.PitchSegment(
                            (
                                abjad.NamedPitch("c'"),
                                abjad.NamedPitch("e'"),
                                abjad.NamedPitch("g'"),
                                ),
                            item_class=abjad.NamedPitch,
                            ),
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset(5, 3),
                        stop_offset=abjad.Offset(5, 1),
                        annotation=abjad.PitchSegment(
                            (
                                abjad.NamedPitch("fs'"),
                                abjad.NamedPitch("g'"),
                                ),
                            item_class=abjad.NamedPitch,
                            ),
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset(5, 1),
                        stop_offset=abjad.Offset(10, 1),
                        annotation=abjad.PitchSegment(
                            (
                                abjad.NamedPitch('b'),
                                ),
                            item_class=abjad.NamedPitch,
                            ),
                        ),
                    ]
                )

        '''
        import consort
        timespans = consort.TimespanCollection()
        if not self.ratio or not self.pitch_segments:
            pitch_segment = abjad.PitchSegment("c'")
            annotated_timespan = abjad.AnnotatedTimespan(
                annotation=pitch_segment,
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
            for i, timespan in enumerate(divided_timespans):
                pitch_segment = self._pitch_segments[i]
                annotated_timespan = abjad.AnnotatedTimespan(
                    annotation=pitch_segment,
                    start_offset=timespan.start_offset,
                    stop_offset=timespan.stop_offset,
                    )
                timespans.insert(annotated_timespan)
        return timespans

    def rotate(self, rotation):
        r'''Rotates pitch specifier.

        ::

            >>> pitch_specifier = consort.PitchSpecifier(
            ...     pitch_segments=(
            ...         "c' e' g'",
            ...         "fs' gs'",
            ...         "b",
            ...         ),
            ...     ratio=(1, 2, 3),
            ...     )
            >>> rotated_pitch_specifier = pitch_specifier.rotate(1)
            >>> print(format(rotated_pitch_specifier))
            consort.tools.PitchSpecifier(
                pitch_segments=(
                    abjad.PitchSegment(
                        (
                            abjad.NamedPitch('b'),
                            ),
                        item_class=abjad.NamedPitch,
                        ),
                    abjad.PitchSegment(
                        (
                            abjad.NamedPitch("c'"),
                            abjad.NamedPitch('f'),
                            abjad.NamedPitch('a'),
                            ),
                        item_class=abjad.NamedPitch,
                        ),
                    abjad.PitchSegment(
                        (
                            abjad.NamedPitch("fs'"),
                            abjad.NamedPitch("e'"),
                            ),
                        item_class=abjad.NamedPitch,
                        ),
                    ),
                ratio=abjad.Ratio((3, 1, 2)),
                )

        Returns new pitch specifier.
        '''
        import consort
        rotation = int(rotation)
        pitch_segments = tuple(
            _.rotate(rotation, stravinsky=True)
            for _ in self.pitch_segments
            )
        pitch_segments = consort.rotate(pitch_segments, rotation)
        ratio = consort.rotate(self.ratio, rotation)
        return abjad.new(
            self,
            pitch_segments=pitch_segments,
            ratio=ratio,
            )

    def transpose(self, expr=0):
        r'''Transposes pitch specifier.

        ::

            >>> pitch_specifier = consort.PitchSpecifier(
            ...     pitch_segments=(
            ...         "c' e' g'",
            ...         "fs' gs'",
            ...         "b",
            ...         ),
            ...     ratio=(1, 2, 3),
            ...     )
            >>> transposed_pitch_specifier = pitch_specifier.transpose('M2')
            >>> print(format(transposed_pitch_specifier))
            consort.tools.PitchSpecifier(
                pitch_segments=(
                    abjad.PitchSegment(
                        (
                            abjad.NamedPitch("d'"),
                            abjad.NamedPitch("fs'"),
                            abjad.NamedPitch("a'"),
                            ),
                        item_class=abjad.NamedPitch,
                        ),
                    abjad.PitchSegment(
                        (
                            abjad.NamedPitch("gs'"),
                            abjad.NamedPitch("as'"),
                            ),
                        item_class=abjad.NamedPitch,
                        ),
                    abjad.PitchSegment(
                        (
                            abjad.NamedPitch("cs'"),
                            ),
                        item_class=abjad.NamedPitch,
                        ),
                    ),
                ratio=abjad.Ratio((1, 2, 3)),
                )

        Returns new pitch specifier.
        '''
        pitch_segments = (_.transpose(expr) for _ in self.pitch_segments)
        return abjad.new(self, pitch_segments=pitch_segments)

    ### PUBLIC PROPERTIES ###

    @property
    def ratio(self):
        return self._ratio

    @property
    def pitch_segments(self):
        return self._pitch_segments
