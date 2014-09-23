# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from consort.makers.PitchHandler import PitchHandler


class PitchClassPitchHandler(PitchHandler):
    r'''PitchClass pitch maker.

    ::

        >>> from consort import makers
        >>> pitch_handler = makers.PitchClassPitchHandler(
        ...     pitch_classes="c' d' e' f'",
        ...     )
        >>> print(format(pitch_handler))
        consort.makers.PitchClassPitchHandler(
            allow_repetition=False,
            pitch_classes=datastructuretools.CyclicTuple(
                [
                    pitchtools.NamedPitch("c'"),
                    pitchtools.NamedPitch("d'"),
                    pitchtools.NamedPitch("e'"),
                    pitchtools.NamedPitch("f'"),
                    ]
                ),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_octavations',
        '_pitch_classes',
        '_pitch_range',
        '_register_specifier',
        '_register_spread',
        )

    _default_octavations = datastructuretools.CyclicTuple([
        4, 2, 1, 0, 5, 6, 7, 3,
        0, 5, 3, 1, 7, 4, 2, 6,
        2, 1, 5, 3, 4, 0, 7, 6,
        1, 2, 4, 0, 5, 7, 6, 3,
        7, 0, 3, 1, 5, 4, 6, 2,
        6, 1, 2, 0, 7, 5, 3, 4,
        3, 0, 4, 7, 2, 5, 6, 1,
        2, 3, 4, 7, 5, 1, 0, 6,
        ])

    ### INITIALIZER ###

    def __init__(
        self,
        allow_repetition=None,
        chord_expressions=None,
        octavations=None,
        pitch_application_rate=None,
        pitch_classes=None,
        pitch_range=None,
        register_specifier=None,
        register_spread=None,
        transform_stack=None,
        ):
        from consort import makers
        PitchHandler.__init__(
            self,
            allow_repetition=allow_repetition,
            chord_expressions=chord_expressions,
            pitch_application_rate=pitch_application_rate,
            transform_stack=transform_stack,
            )
        pitch_classes = pitchtools.PitchSegment(pitch_classes)
        pitch_classes = datastructuretools.CyclicTuple(pitch_classes)
        if octavations is not None:
            assert octavations
            assert all(isinstance(x, int) for x in octavations)
            octavations = datastructuretools.CyclicTuple(octavations)
        self._octavations = octavations
        if pitch_range is not None:
            assert isinstance(pitch_range, pitchtools.PitchRange)
        self._pitch_range = pitch_range
        self._pitch_classes = pitch_classes
        if register_specifier is not None:
            assert isinstance(register_specifier, makers.RegisterSpecifier)
        self._register_specifier = register_specifier
        if register_spread is not None:
            register_spread = int(register_spread)
            assert 0 <= register_spread < 12
        self._register_spread = register_spread

    ### PRIVATE METHODS ###

    def _calculate_registration(self, logical_tie, seed=0):
        from consort import makers
        attack_point_signature = makers.AttackPointSignature.from_logical_tie(
            logical_tie,
            )
        register_specifier = self.register_specifier
        if register_specifier is None:
            register_specifier = makers.RegisterSpecifier()
        register = register_specifier.find_register(
            attack_point_signature,
            seed=seed
            )
        register_spread = self.register_spread
        if register_spread is None:
            register_spread = 6
        registration = \
            pitchtools.Registration([
                ('[C0, C4)', register),
                ('[C4, C8)', register + register_spread),
                ])
        return registration

    def _calculate_pitch(self, registration, seed=0):
        pitch_classes = self.pitch_classes or \
            datastructuretools.CyclicTuple([0])
        pitch_class = pitch_classes[seed]
        octavations = self.octavations or self._default_octavations
        octave = octavations[seed]
        pitch_class = pitchtools.NamedPitchClass(pitch_class)
        if self.transform_stack:
            for transform in self.transform_stack:
                pitch_class = transform(pitch_class)
        pitch = pitchtools.NamedPitch(pitch_class, octave)
        pitch_range = pitchtools.PitchRange('[C0, C8)')
        pitch = self._fit_pitch_to_pitch_range(pitch, pitch_range)
        pitch = registration([pitch])[0]
        pitch = pitchtools.NamedPitch(pitch)
        return pitch

    def _fit_pitch_to_pitch_range(self, pitch, pitch_range):
        while pitch <= pitch_range.start_pitch and \
            pitch not in pitch_range:
            pitch = pitch.transpose(12)
        while pitch_range.stop_pitch <= pitch and \
            pitch not in pitch_range:
            pitch = pitch.transpose(-12)
        assert pitch in pitch_range, \
            (pitch, pitch.octave_number, pitch_range)
        return pitch

    def _process_logical_tie(
        self,
        logical_tie,
        pitch_range=None,
        previous_pitch=None,
        music_index=0,
        logical_tie_index=0,
        ):
        registration = \
            self._calculate_registration(
                logical_tie,
                seed=music_index,
                )
        pitch = self._calculate_pitch(
            registration,
            seed=music_index + logical_tie_index,
            )
        pitch_range = self.pitch_range or pitch_range
        if pitch_range is not None:
            pitch = self._fit_pitch_to_pitch_range(pitch, pitch_range)
        for i, leaf in enumerate(logical_tie):
            leaf.written_pitch = pitch
        self._apply_chord_expression(
            logical_tie,
            seed=music_index + logical_tie_index,
            pitch_range=pitch_range,
            )
        return pitch

    ### PUBLIC PROPERTIES ###

    @property
    def octavations(self):
        return self._octavations

    @property
    def pitch_classes(self):
        return self._pitch_classes

    @property
    def pitch_range(self):
        return self._pitch_range

    @property
    def register_specifier(self):
        return self._register_specifier

    @property
    def register_spread(self):
        return self._register_spread