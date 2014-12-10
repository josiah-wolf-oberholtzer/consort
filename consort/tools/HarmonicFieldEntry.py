# -*- encoding: utf-8 -*
from abjad.tools import abctools
from abjad.tools import systemtools
from abjad.tools.topleveltools import new
from ide import idetools


class HarmonicFieldEntry(abctools.AbjadObject):
    r'''A harmonic field entry.

    ::

        >>> import consort
        >>> entry = consort.HarmonicFieldEntry(
        ...     leading_pitches=("f'", "e'", "df'"),
        ...     structural_pitch="c'",
        ...     tailing_pitches=('bf', 'g', 'af'),
        ...     )
        >>> print(format(entry))
        consort.tools.HarmonicFieldEntry(
            leading_pitches=("f'", "e'", "df'"),
            structural_pitch=pitchtools.NamedPitch("c'"),
            tailing_pitches=('bf', 'g', 'af'),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_leading_pitches',
        '_structural_pitch',
        '_tailing_pitches',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        leading_pitches=None,
        structural_pitch=0,
        tailing_pitches=None,
        ):
        from abjad.tools import pitchtools
        if isinstance(leading_pitches, type(self)):
            expr = leading_pitches
            leading_pitches = expr.leading_pitches
            structural_pitch = expr.structural_pitch
            tailing_pitches = expr.tailing_pitches
        leading_pitches = leading_pitches or None
        if leading_pitches is not None:
            leading_pitches = pitchtools.PitchSegment(leading_pitches)
        self._leading_pitches = leading_pitches
        structural_pitch = pitchtools.NamedPitch(structural_pitch)
        self._structural_pitch = structural_pitch
        tailing_pitches = tailing_pitches or None
        if tailing_pitches is not None:
            tailing_pitches = pitchtools.PitchSegment(tailing_pitches)
        self._tailing_pitches = tailing_pitches

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='leading_pitches',
                display_string='leading grace pitches',
                command='lp',
                editor=idetools.getters.get_string,
                ),
            systemtools.AttributeDetail(
                name='structural_pitch',
                display_string='structural pitch',
                command='sp',
                editor=idetools.getters.get_string,
                ),
            systemtools.AttributeDetail(
                name='tailing_pitches',
                display_string='tailing grace pitches',
                command='tp',
                editor=idetools.getters.get_string,
                ),
            )

    @property
    def _storage_format_specification(self):
        def procedure(pitches):
            if pitches is None:
                return pitches
            return tuple(str(pitch) for pitch in pitches)
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_callables={
                'leading_pitches': procedure,
                'tailing_pitches': procedure,
                },
            )

    ### PUBLIC METHODS ###

    def invert(
        self,
        axis=None,
        ):
        r'''Inverts harmonic field entry.

        ::

            >>> inverted_entry = entry.invert()
            >>> print(format(inverted_entry))
            consort.tools.HarmonicFieldEntry(
                leading_pitches=('g', 'af', 'b'),
                structural_pitch=pitchtools.NamedPitch("c'"),
                tailing_pitches=("d'", "f'", "e'"),
                )

        Inverts harmonic field entry around `axis`.

        ::

            >>> inverted_entry = entry.invert(axis="d'")
            >>> print(format(inverted_entry))
            consort.tools.HarmonicFieldEntry(
                leading_pitches=('b', "c'", "ds'"),
                structural_pitch=pitchtools.NamedPitch("e'"),
                tailing_pitches=("fs'", "a'", "gs'"),
                )

        Returns new harmonic field entry.
        '''
        from abjad.tools import pitchtools
        axis = axis or pitchtools.NamedPitch("c'")
        leading_pitches = self.leading_pitches
        if leading_pitches is not None:
            leading_pitches = leading_pitches.invert(axis)
        structural_pitch = self.structural_pitch.invert(axis)
        tailing_pitches = self.tailing_pitches
        if tailing_pitches is not None:
            tailing_pitches = tailing_pitches.invert(axis)
        return new(self,
            leading_pitches=leading_pitches,
            structural_pitch=structural_pitch,
            tailing_pitches=tailing_pitches,
            )

    def invert_ornamental_pitches(
        self,
        ):
        r'''Inverts ornamental pitches around structural pitch.

        ::

            >>> inverted_entry = entry.invert_ornamental_pitches()
            >>> print(format(inverted_entry))
            consort.tools.HarmonicFieldEntry(
                leading_pitches=('g', 'af', 'b'),
                structural_pitch=pitchtools.NamedPitch("c'"),
                tailing_pitches=("d'", "f'", "e'"),
                )

        Returns new harmonic field entry.
        '''
        axis = self.structural_pitch
        leading_pitches = self.leading_pitches
        if leading_pitches is not None:
            leading_pitches = leading_pitches.invert(axis)
        tailing_pitches = self.tailing_pitches
        if tailing_pitches is not None:
            tailing_pitches = tailing_pitches.invert(axis)
        return new(self,
            leading_pitches=leading_pitches,
            tailing_pitches=tailing_pitches,
            )

    def retrograde(
        self,
        ):
        r'''Retrogrades harmonic field entry ornamental pitches around the
        structural pitch.

        ::

            >>> retrograded_entry = entry.retrograde()
            >>> print(format(retrograded_entry))
            consort.tools.HarmonicFieldEntry(
                leading_pitches=('af', 'g', 'bf'),
                structural_pitch=pitchtools.NamedPitch("c'"),
                tailing_pitches=("df'", "e'", "f'"),
                )

        Returns new harmonic field entry
        '''
        leading_pitches = self.tailing_pitches
        tailing_pitches = self.leading_pitches
        if leading_pitches is not None:
            leading_pitches = leading_pitches.retrograde()
        if tailing_pitches is not None:
            tailing_pitches = tailing_pitches.retrograde()
        return new(self,
            leading_pitches=leading_pitches,
            tailing_pitches=tailing_pitches,
            )

    def rotate(
        self,
        expr,
        ):
        r'''Rotates harmonic field entry pitches, maintaining the structural
        pitch.

        ::

            >>> rotated_entry = entry.rotate(1)
            >>> print(format(rotated_entry))
            consort.tools.HarmonicFieldEntry(
                leading_pitches=("e'", "d'", 'b'),
                structural_pitch=pitchtools.NamedPitch("c'"),
                tailing_pitches=("f'", "e'", "df'"),
                )

        Returns new harmonic field entry.
        '''
        leading_pitches = self.tailing_pitches
        tailing_pitches = self.leading_pitches
        if leading_pitches is not None:
            leading_segment = leading_pitches + (self.structural_pitch,)
            leading_segment = leading_segment.retrograde()
            leading_segment = leading_segment.rotate(-expr, transpose=True)
            leading_segment = leading_segment.retrograde()
            leading_pitches = leading_segment[:-1]
        if tailing_pitches is not None:
            tailing_segment = (self.structural_pitch,) + tailing_pitches
            tailing_segment.rotate(expr, transpose=True)
            tailing_pitches = tailing_segment[1:]
        return new(self,
            leading_pitches=leading_pitches,
            tailing_pitches=tailing_pitches,
            )

    def transpose(
        self,
        expr,
        ):
        r'''Transposes all pitches in harmonic field entry.

        ::

            >>> transposed_entry = entry.transpose('M2')
            >>> print(format(transposed_entry))
            consort.tools.HarmonicFieldEntry(
                leading_pitches=("g'", "fs'", "ef'"),
                structural_pitch=pitchtools.NamedPitch("d'"),
                tailing_pitches=("c'", 'a', 'bf'),
                )

        Returns new harmonic field entry.
        '''
        leading_pitches = self.leading_pitches
        if leading_pitches is not None:
            leading_pitches = leading_pitches.transpose(expr)
        structural_pitch = self.structural_pitch.transpose(expr)
        tailing_pitches = self.tailing_pitches
        if tailing_pitches is not None:
            tailing_pitches = tailing_pitches.transpose(expr)
        return new(self,
            leading_pitches=leading_pitches,
            structural_pitch=structural_pitch,
            tailing_pitches=tailing_pitches,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def leading_pitches(self):
        return self._leading_pitches

    @property
    def pitch_range(self):
        from abjad.tools import pitchtools
        pitches = self.pitches
        minimum = min(pitches)
        maximum = max(pitches)
        pitch_range = pitchtools.PitchRange.from_pitches(minimum, maximum)
        return pitch_range

    @property
    def pitches(self):
        pitches = []
        if self.leading_pitches is not None:
            pitches.extend(self.leading_pitches)
        pitches.append(self.structural_pitch)
        if self.tailing_pitches is not None:
            pitches.extend(self.tailing_pitches)
        return tuple(pitches)

    @property
    def structural_pitch(self):
        return self._structural_pitch

    @property
    def tailing_pitches(self):
        return self._tailing_pitches