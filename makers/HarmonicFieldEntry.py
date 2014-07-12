# -*- encoding: utf-8 -*
from abjad.tools import abctools
from abjad.tools.topleveltools import new


class HarmonicFieldEntry(abctools.AbjadObject):
    r'''A harmonic field entry.

    ::

        >>> import consort
        >>> entry = consort.makers.HarmonicFieldEntry(
        ...     leading_pitches=("f'", "e'", "df'"),
        ...     structural_pitch="c'",
        ...     tailing_pitches=('bf', 'g', 'af'),
        ...     )
        >>> print(format(entry))
        makers.HarmonicFieldEntry(
            leading_pitches=pitchtools.PitchSegment(
                (
                    pitchtools.NamedPitch("f'"),
                    pitchtools.NamedPitch("e'"),
                    pitchtools.NamedPitch("df'"),
                    ),
                item_class=pitchtools.NamedPitch,
                ),
            structural_pitch=pitchtools.NumberedPitch(0),
            tailing_pitches=pitchtools.PitchSegment(
                (
                    pitchtools.NamedPitch('bf'),
                    pitchtools.NamedPitch('g'),
                    pitchtools.NamedPitch('af'),
                    ),
                item_class=pitchtools.NamedPitch,
                ),
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
        structural_pitch=None,
        tailing_pitches=None,
        ):
        from abjad.tools import pitchtools
        if isinstance(leading_pitches, type(self)):
            expr = leading_pitches
            leading_pitches = expr.leading_pitches
            structural_pitch = expr.structural_pitch
            tailing_pitches = expr.tailing_pitches
        leading_pitches = leading_pitches or ()
        leading_pitches = pitchtools.PitchSegment(leading_pitches)
        self._leading_pitches = leading_pitches
        structural_pitch = pitchtools.NumberedPitch(structural_pitch)
        self._structural_pitch = structural_pitch
        tailing_pitches = tailing_pitches or ()
        tailing_pitches = pitchtools.PitchSegment(tailing_pitches)
        self._tailing_pitches = tailing_pitches

    ### PRIVATE METHODS ###

    def _transpose_pitch_wrapped_to_range(self, pitch, interval, pitch_range):
        pass

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        from scoremanager import idetools
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

    ### PUBLIC METHODS ###

    def invert(
        self,
        axis=None,
        ):
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

    def rotate_octaves(
        self,
        expr,
        bounding_pitch_range,
        ):
        interval = 12 * expr
        leading_pitches = self.tailing_pitches
        tailing_pitches = self.leading_pitches
        if leading_pitches is not None:
            leading_pitches = [
                self._transpose_pitch_wrapped_to_range(
                    leading_pitch,
                    interval,
                    bounding_pitch_range,
                    )
                for leading_pitch in leading_pitches
                ]
        structural_pitch = self._transpose_pitch_wrapped_to_range(
            self.structural_pitch,
            interval,
            bounding_pitch_range,
            )
        if tailing_pitches is not None:
            tailing_pitches = [
                self._transpose_pitch_wrapped_to_range(
                    tailing_pitch,
                    interval,
                    bounding_pitch_range,
                    )
                for tailing_pitch in tailing_pitches
                ]
        return new(self,
            leading_pitches=leading_pitches,
            structural_pitch=structural_pitch,
            tailing_pitches=tailing_pitches,
            )

    def rotate_pitch_classes(
        self,
        expr,
        ):
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
