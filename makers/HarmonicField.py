# -*- encoding: utf-8 -*-
from abjad.tools import pitchtools
from abjad.tools import datastructuretools


class HarmonicField(datastructuretools.TypedTuple):
    r'''A harmonic field.

    ::

        >>> import consort
        >>> harmonic_field = consort.makers.HarmonicField([
        ...     consort.makers.HarmonicFieldEntry(
        ...         leading_pitches="ef' d'",
        ...         structural_pitch="c'",
        ...         tailing_pitches="d'",
        ...         ),
        ...     consort.makers.HarmonicFieldEntry(
        ...         leading_pitches="g'",
        ...         structural_pitch="ef'",
        ...         tailing_pitches="f' a'",
        ...         ),
        ...     consort.makers.HarmonicFieldEntry(
        ...         leading_pitches="f'' ef'' b'",
        ...         structural_pitch="c''",
        ...         ),
        ...     ])
        >>> print(format(harmonic_field))
        makers.HarmonicField(
            (
                makers.HarmonicFieldEntry(
                    leading_pitches=("ef'", "d'"),
                    structural_pitch=pitchtools.NamedPitch("c'"),
                    tailing_pitches=("d'",),
                    ),
                makers.HarmonicFieldEntry(
                    leading_pitches=("g'",),
                    structural_pitch=pitchtools.NamedPitch("ef'"),
                    tailing_pitches=("f'", "a'"),
                    ),
                makers.HarmonicFieldEntry(
                    leading_pitches=("f''", "ef''", "b'"),
                    structural_pitch=pitchtools.NamedPitch("c''"),
                    ),
                )
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_structural_pitches',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        items=None,
        ):
        import consort
        mapping = {}
        items = items or []
        entries = [self._item_callable(x) for x in items]
        for entry in entries:
            mapping[float(entry.structural_pitch)] = entry
        items = sorted(
            mapping.values(),
            key=lambda x: x.structural_pitch,
            )
        datastructuretools.TypedTuple.__init__(
            self,
            items=items,
            item_class=consort.makers.HarmonicFieldEntry,
            )
        self._structural_pitches = pitchtools.PitchSegment(
            [x.structural_pitch for x in self],
            )

    ### PRIVATE METHODS ###

    def _find_nearest_entries(
        self,
        structural_pitch,
        entry_count=1,
        pitch_range=None,
        ):
        entry_count = int(entry_count)
        structural_pitch = pitchtools.NamedPitch(structural_pitch)
        entries = sorted(self,
            key=lambda x: abs(
                (x.structural_pitch - structural_pitch).semitones
                ),
            )
        if pitch_range is not None:
            entries = [x for x in entries if x in pitch_range]
        return entries[:entry_count]

    def _find_matching_entries(
        self,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        matching_entries, nonmatching_entries = self[:], []
        if structural_pitch_class_subset:
            pitch_clas_set = pitchtools.PitchClassSet(
                items=structural_pitch_class_subset,
                item_class=pitchtools.NumberedPitchClass,
                )
            for entry in tuple(matching_entries):
                structural_pitch = entry.structural_pitch
                structural_pitch_class = structural_pitch.numbered_pitch_class
                if structural_pitch_class not in pitch_clas_set:
                    matching_entries.remove(entry)
                    nonmatching_entries.append(entry)
        if structural_pitch_range:
            pitch_range = pitchtools.PitchRange(structural_pitch_range)
            for entry in tuple(matching_entries):
                structural_pitch = entry.structural_pitch
                if structural_pitch not in pitch_range:
                    matching_entries.remove(entry)
                    nonmatching_entries.append(entry)
        return matching_entries, nonmatching_entries

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest()

    @property
    def _item_callable(self):
        import consort
        return consort.makers.HarmonicFieldEntry

    ### PUBLIC METHODS ###

    def invert(
        self,
        axis=None,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        r'''Inverts harmonic field around `axis`.

        ::

            >>> inverted_field = harmonic_field.invert("d'")
            >>> print(format(inverted_field))
            makers.HarmonicField(
                (
                    makers.HarmonicFieldEntry(
                        leading_pitches=('b,', 'cs', 'f'),
                        structural_pitch=pitchtools.NamedPitch('e'),
                        ),
                    makers.HarmonicFieldEntry(
                        leading_pitches=('a',),
                        structural_pitch=pitchtools.NamedPitch("cs'"),
                        tailing_pitches=('b', 'g'),
                        ),
                    makers.HarmonicFieldEntry(
                        leading_pitches=("cs'", "d'"),
                        structural_pitch=pitchtools.NamedPitch("e'"),
                        tailing_pitches=("d'",),
                        ),
                    )
                )

        Returns new harmonic field.
        '''
        from abjad.tools import pitchtools
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        axis = axis or pitchtools.NamedPitch("c'")
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.invert(axis=axis)
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + altered_entries
        return type(self)(all_entries)

    def invert_ornamental_pitches(
        self,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        r'''Inverts ornamental pitches in harmonic field around their
        structural pitch.

        ::

            >>> inverted_field = harmonic_field.invert_ornamental_pitches()
            >>> print(format(inverted_field))
            makers.HarmonicField(
                (
                    makers.HarmonicFieldEntry(
                        leading_pitches=('a', 'bf'),
                        structural_pitch=pitchtools.NamedPitch("c'"),
                        tailing_pitches=('bf',),
                        ),
                    makers.HarmonicFieldEntry(
                        leading_pitches=("cf'",),
                        structural_pitch=pitchtools.NamedPitch("ef'"),
                        tailing_pitches=("df'", 'bff'),
                        ),
                    makers.HarmonicFieldEntry(
                        leading_pitches=("g'", "a'", "df''"),
                        structural_pitch=pitchtools.NamedPitch("c''"),
                        ),
                    )
                )

        Returns new harmonic field.
        '''
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.invert_ornamental_pitches()
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + altered_entries
        return type(self)(all_entries)

    def retrograde(
        self,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        r'''Retrogrades ornamental pitches in this harmonic field around their
        structural pitch.

        ::

            >>> retrograded_field = harmonic_field.retrograde()
            >>> print(format(retrograded_field))
            makers.HarmonicField(
                (
                    makers.HarmonicFieldEntry(
                        leading_pitches=("d'",),
                        structural_pitch=pitchtools.NamedPitch("c'"),
                        tailing_pitches=("d'", "ef'"),
                        ),
                    makers.HarmonicFieldEntry(
                        leading_pitches=("a'", "f'"),
                        structural_pitch=pitchtools.NamedPitch("ef'"),
                        tailing_pitches=("g'",),
                        ),
                    makers.HarmonicFieldEntry(
                        structural_pitch=pitchtools.NamedPitch("c''"),
                        tailing_pitches=("b'", "ef''", "f''"),
                        ),
                    )
                )

        Returns new harmonic field.
        '''
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.retrograde()
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + altered_entries
        return type(self)(all_entries)

    def rotate(
        self,
        expr,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        r'''Rotates ornamental pitches, maintaining their structural pitch.

        ::

            >>> rotated_field = harmonic_field.rotate(1)
            >>> print(format(rotated_field))
            makers.HarmonicField(
                (
                    makers.HarmonicFieldEntry(
                        leading_pitches=('bf',),
                        structural_pitch=pitchtools.NamedPitch("c'"),
                        tailing_pitches=("ef'", "d'"),
                        ),
                    makers.HarmonicFieldEntry(
                        leading_pitches=('bff', "cf'"),
                        structural_pitch=pitchtools.NamedPitch("ef'"),
                        tailing_pitches=("g'",),
                        ),
                    makers.HarmonicFieldEntry(
                        structural_pitch=pitchtools.NamedPitch("c''"),
                        tailing_pitches=("f''", "ef''", "b'"),
                        ),
                    )
                )

        Returns new harmonic field.
        '''
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.rotate(expr)
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + altered_entries
        return type(self)(all_entries)

    def transpose(
        self,
        expr,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        r'''Transposes harmonic field.

        ::

            >>> transposed_field = harmonic_field.transpose('M2')
            >>> print(format(transposed_field))
            makers.HarmonicField(
                (
                    makers.HarmonicFieldEntry(
                        leading_pitches=("f'", "e'"),
                        structural_pitch=pitchtools.NamedPitch("d'"),
                        tailing_pitches=("e'",),
                        ),
                    makers.HarmonicFieldEntry(
                        leading_pitches=("a'",),
                        structural_pitch=pitchtools.NamedPitch("f'"),
                        tailing_pitches=("g'", "b'"),
                        ),
                    makers.HarmonicFieldEntry(
                        leading_pitches=("g''", "f''", "cs''"),
                        structural_pitch=pitchtools.NamedPitch("d''"),
                        ),
                    )
                )

        Returns new harmonic field.
        '''
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.transpose(expr)
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + altered_entries
        return type(self)(all_entries)

    ### PUBLIC PROPERTIES ###

    @property
    def pitches(self):
        r'''Gets all pitches in harmonic field.

        ::

            >>> pitches = harmonic_field.pitches
            >>> for pitch in pitches:
            ...     pitch
            ...
            NamedPitch("ef'")
            NamedPitch("d'")
            NamedPitch("c'")
            NamedPitch("d'")
            NamedPitch("g'")
            NamedPitch("ef'")
            NamedPitch("f'")
            NamedPitch("a'")
            NamedPitch("f''")
            NamedPitch("ef''")
            NamedPitch("b'")
            NamedPitch("c''")

        Returns pitch segment.
        '''
        pitches = []
        for entry in self:
            pitches.extend(entry.pitches)
        return pitchtools.PitchSegment(pitches)

    @property
    def pitch_range(self):
        r'''Gets pitch range of harmonic field.

        ::

            >>> pitch_range = harmonic_field.pitch_range
            >>> pitch_range
            PitchRange(range_string='[C4, F5]')

        Returns pitch range.
        '''
        from abjad.tools import pitchtools
        pitches = self.pitches
        minimum = min(pitches)
        maximum = max(pitches)
        pitch_range = pitchtools.PitchRange.from_pitches(minimum, maximum)
        return pitch_range

    @property
    def structural_pitches(self):
        r'''Gets all structural pitches in harmonic field.

        ::

            >>> for pitch in harmonic_field.structural_pitches:
            ...     pitch
            ...
            NamedPitch("c'")
            NamedPitch("ef'")
            NamedPitch("c''")

        Returns pitch segment.
        '''
        return self._structural_pitches
