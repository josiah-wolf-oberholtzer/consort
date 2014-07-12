# -*- encoding: utf-8 -*
from abjad.tools import abctools


class HarmonicFieldEntry(abctools.AbjadObject):
    r'''A harmonic field entry.

    ::

        >>> import consort
        >>> entry = consort.makers.HarmonicFieldEntry(
        ...     leading_grace_pitches=("f'", "e'", "df'"),
        ...     structural_pitch="c'",
        ...     tailing_grace_pitches=('bf', 'g', 'af'),
        ...     )
        >>> print(format(entry))
        makers.HarmonicFieldEntry(
            leading_grace_pitches=pitchtools.PitchSegment(
                (
                    pitchtools.NamedPitch("f'"),
                    pitchtools.NamedPitch("e'"),
                    pitchtools.NamedPitch("df'"),
                    ),
                item_class=pitchtools.NamedPitch,
                ),
            structural_pitch=pitchtools.NumberedPitch(0),
            tailing_grace_pitches=pitchtools.PitchSegment(
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
        '_leading_grace_pitches',
        '_structural_pitch',
        '_tailing_grace_pitches',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        leading_grace_pitches=None,
        structural_pitch=None,
        tailing_grace_pitches=None,
        ):
        from abjad.tools import pitchtools
        if isinstance(leading_grace_pitches, type(self)):
            expr = leading_grace_pitches
            leading_grace_pitches = expr.leading_grace_pitches
            structural_pitch = expr.structural_pitch
            tailing_grace_pitches = expr.tailing_grace_pitches
        leading_grace_pitches = leading_grace_pitches or ()
        leading_grace_pitches = pitchtools.PitchSegment(leading_grace_pitches)
        self._leading_grace_pitches = leading_grace_pitches
        structural_pitch = pitchtools.NumberedPitch(structural_pitch)
        self._structural_pitch = structural_pitch
        tailing_grace_pitches = tailing_grace_pitches or ()
        tailing_grace_pitches = pitchtools.PitchSegment(tailing_grace_pitches)
        self._tailing_grace_pitches = tailing_grace_pitches

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest()

    ### PUBLIC METHODS ###

    def invert(
        self,
        expr,
        axis=None,
        structural_pitch_class_subset=None,
        ):
        pass

    def invert_grace_pitches(
        self,
        structural_pitch_class_subset=None,
        ):
        pass

    def retrograde(
        self,
        structural_pitch_class_subset=None,
        ):
        pass

    def rotate(
        self,
        expr,
        structural_pitch_class_subset=None,
        ):
        pass

    def transpose(
        self,
        expr,
        include_grace_pitches=True,
        include_structural_pitches=True,
        structural_pitch_class_subset=None,
        ):
        pass

    ### PUBLIC PROPERTIES ###

    @property
    def leading_grace_pitches(self):
        return self._leading_grace_pitches

    @property
    def structural_pitch(self):
        return self._structural_pitch

    @property
    def tailing_grace_pitches(self):
        return self._tailing_grace_pitches