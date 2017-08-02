import abjad
from abjad.tools import pitchtools
from consort.tools.PitchHandler import PitchHandler


class PitchClassPitchHandler(PitchHandler):
    r'''PitchClass pitch maker.

    ::

        >>> pitch_handler = consort.PitchClassPitchHandler(
        ...     pitch_specifier="c' d' e' f'",
        ...     )
        >>> print(format(pitch_handler))
        consort.tools.PitchClassPitchHandler(
            pitch_specifier=consort.tools.PitchSpecifier(
                pitch_segments=(
                    abjad.PitchSegment(
                        (
                            abjad.NamedPitch("c'"),
                            abjad.NamedPitch("d'"),
                            abjad.NamedPitch("e'"),
                            abjad.NamedPitch("f'"),
                            ),
                        item_class=abjad.NamedPitch,
                        ),
                    ),
                ratio=abjad.Ratio((1,)),
                ),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_leap_constraint',
        '_octavations',
        '_pitch_range',
        '_register_specifier',
        '_register_spread',
        )

    _default_octavations = abjad.CyclicTuple([
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
        deviations=None,
        forbid_repetitions=None,
        grace_expressions=None,
        leap_constraint=None,
        logical_tie_expressions=None,
        octavations=None,
        pitch_application_rate=None,
        pitch_range=None,
        register_specifier=None,
        register_spread=None,
        pitch_operation_specifier=None,
        pitch_specifier=None,
        pitches_are_nonsemantic=None,
        use_self_as_seed_key=None,
        ):
        PitchHandler.__init__(
            self,
            deviations=deviations,
            forbid_repetitions=forbid_repetitions,
            grace_expressions=grace_expressions,
            logical_tie_expressions=logical_tie_expressions,
            pitch_application_rate=pitch_application_rate,
            pitch_operation_specifier=pitch_operation_specifier,
            pitch_specifier=pitch_specifier,
            pitches_are_nonsemantic=pitches_are_nonsemantic,
            use_self_as_seed_key=use_self_as_seed_key,
            )
        self._initialize_leap_constraint(leap_constraint)
        self._initialize_octavations(octavations)
        self._initialize_pitch_range(pitch_range)
        self._initialize_register_specifier(register_specifier)
        self._initialize_register_spread(register_spread)

    ### SPECIAL METHODS ###

    def __call__(
        self,
        attack_point_signature,
        logical_tie,
        music_specifier,
        pitch_choices,
        previous_pitch,
        seed_session,
        ):
        previous_pitch_class = None
        if previous_pitch is not None:
            previous_pitch_class = abjad.NamedPitchClass(previous_pitch)
        instrument = self._get_instrument(logical_tie, music_specifier)
        pitch_range = self._get_pitch_range(
            instrument,
            logical_tie,
            )
        registration = self._get_registration(
            attack_point_signature,
            logical_tie,
            seed_session.current_timewise_phrase_seed,
            )
        pitch_class = self._get_pitch_class(
            attack_point_signature,
            pitch_choices,
            previous_pitch_class,
            seed_session.current_phrased_voicewise_logical_tie_seed,
            )
        pitch = self._get_pitch(
            pitch_class,
            registration,
            seed_session.current_phrased_voicewise_logical_tie_seed,
            )
        pitch = self._constrain_interval(
            pitch,
            previous_pitch,
            )
        pitch = self._apply_deviation(
            pitch,
            seed_session.current_unphrased_voicewise_logical_tie_seed,
            )
        pitch_range = self.pitch_range or pitch_range
        if pitch_range is not None:
            pitch = self._fit_pitch_to_pitch_range(
                pitch,
                pitch_range,
                )
        return pitch

    ### PRIVATE METHODS ###

    def _constrain_interval(self, current_pitch, previous_pitch):
        if previous_pitch is None or not self.leap_constraint:
            return current_pitch
        maximum_leap = self.leap_constraint.semitones
        #semitones = float(current_pitch) - float(previous_pitch)
        semitones = float(previous_pitch) - float(current_pitch)
        if maximum_leap < semitones:  # descent
            current_pitch = current_pitch.transpose(12)
        elif semitones < -maximum_leap:  # ascent
            current_pitch = current_pitch.transpose(-12)
        return current_pitch

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

    def _get_pitch(
        self,
        pitch_class,
        registration,
        seed,
        ):
        octavations = self.octavations or self._default_octavations
        octave = octavations[seed]
        pitch = abjad.NamedPitch((pitch_class, octave))
        pitch_range = pitchtools.PitchRange('[C0, C8)')
        pitch = self._fit_pitch_to_pitch_range(pitch, pitch_range)
        pitch = registration([pitch])[0]
        pitch = abjad.NamedPitch(pitch)
        return pitch

    def _get_pitch_class(
        self,
        attack_point_signature,
        pitch_choices,
        previous_pitch_class,
        seed,
        ):
        pitch_class = pitch_choices[seed]
        pitch_class = pitchtools.NamedPitchClass(pitch_class)
        if previous_pitch_class is not None:
            previous_pitch_class = float(previous_pitch_class)
        if pitch_choices and \
            1 < len(set(pitch_choices)) and \
            self.forbid_repetitions:
            if self.pitch_application_rate == 'phrase':
                if attack_point_signature.is_first_of_phrase:
                    while float(pitch_class) == previous_pitch_class:
                        seed += 1
                        pitch_class = pitch_choices[seed]
                        pitch_class = pitchtools.NamedPitchClass(pitch_class)
            elif self.pitch_application_rate == 'division':
                if attack_point_signature.is_first_of_division:
                    while float(pitch_class) == previous_pitch_class:
                        seed += 1
                        pitch_class = pitch_choices[seed]
                        pitch_class = pitchtools.NamedPitchClass(pitch_class)
            else:
                while float(pitch_class) == previous_pitch_class:
                    seed += 1
                    pitch_class = pitch_choices[seed]
                    pitch_class = pitchtools.NamedPitchClass(pitch_class)
        return pitch_class

    def _get_registration(
        self,
        attack_point_signature,
        logical_tie,
        phrase_seed,
        ):
        import consort
        register_specifier = self.register_specifier
        if register_specifier is None:
            register_specifier = consort.RegisterSpecifier()
        register = register_specifier.find_register(
            attack_point_signature,
            seed=phrase_seed,
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

    def _initialize_leap_constraint(self, leap_constraint):
        if leap_constraint is not None:
            leap_constraint = abjad.NumberedInterval(leap_constraint)
            leap_constraint = abs(leap_constraint)
        self._leap_constraint = leap_constraint

    def _initialize_octavations(self, octavations):
        if octavations is not None:
            assert octavations
            assert all(isinstance(x, int) for x in octavations)
            octavations = abjad.CyclicTuple(octavations)
        self._octavations = octavations

    def _initialize_pitch_classes(self, pitch_classes):
        pitch_classes = pitchtools.PitchClassSegment(
            items=pitch_classes,
            item_class=pitchtools.NumberedPitchClass,
            )
        pitch_classes = abjad.CyclicTuple(pitch_classes)
        self._pitch_classes = pitch_classes

    def _initialize_pitch_range(self, pitch_range):
        if pitch_range is not None:
            assert isinstance(pitch_range, pitchtools.PitchRange)
        self._pitch_range = pitch_range

    def _initialize_register_specifier(self, register_specifier):
        import consort
        if register_specifier is not None:
            assert isinstance(register_specifier, consort.RegisterSpecifier)
        self._register_specifier = register_specifier

    def _initialize_register_spread(self, register_spread):
        if register_spread is not None:
            register_spread = int(register_spread)
            assert 0 <= register_spread < 12
        self._register_spread = register_spread

    ### PUBLIC METHODS ###

    def transpose(self, expr):
        pitch_specifier = self.pitch_specifier
        if pitch_specifier is not None:
            pitch_specifier = pitch_specifier.transpose(expr)
        register_specifier = self.register_specifier
        if register_specifier is not None:
            register_specifier = register_specifier.transpose(expr)
        return abjad.new(
            self,
            pitch_specifier=pitch_specifier,
            register_specifier=register_specifier,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def leap_constraint(self):
        return self._leap_constraint

    @property
    def octavations(self):
        return self._octavations

    @property
    def pitch_range(self):
        return self._pitch_range

    @property
    def register_specifier(self):
        return self._register_specifier

    @property
    def register_spread(self):
        return self._register_spread
