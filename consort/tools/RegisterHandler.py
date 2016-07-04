# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad import inspect_
from abjad.tools import datastructuretools
from abjad.tools import instrumenttools
from abjad.tools import pitchtools
from consort.tools.HashCachingObject import HashCachingObject


class RegisterHandler(HashCachingObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_application_rate',
        '_logical_tie_expressions',
        '_logical_tie_expressions_are_phrased',
        '_octavations',
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
        application_rate=None,
        logical_tie_expressions=None,
        logical_tie_expressions_are_phrased=None,
        octavations=None,
        pitch_range=None,
        register_specifier=None,
        register_spread=None,
        ):
        HashCachingObject.__init__(self)
        self._initialize_application_rate(application_rate)
        self._initialize_logical_tie_expressions(logical_tie_expressions)
        self._initialize_octavations(octavations)
        self._initialize_pitch_range(pitch_range)
        self._initialize_register_specifier(register_specifier)
        self._initialize_register_spread(register_spread)
        if logical_tie_expressions_are_phrased is not None:
            logical_tie_expressions_are_phrased = bool(logical_tie_expressions_are_phrased)
        self._logical_tie_expressions_are_phrased = logical_tie_expressions_are_phrased

    ### SPECIAL METHODS ###

    def __call__(
        self,
        attack_point_signature,
        logical_tie,
        music_specifier,
        seed_session,
        ):
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
        pitch_class = logical_tie[0].written_pitch.named_pitch_class
        pitch = self._get_pitch(
            pitch_class,
            registration,
            seed_session.current_phrased_voicewise_logical_tie_seed,
            )
        pitch_range = self.pitch_range or pitch_range
        if pitch_range is not None:
            pitch = self._fit_pitch_to_pitch_range(
                pitch,
                pitch_range,
                )
        for leaf in logical_tie:
            leaf.written_pitch = pitch
        if self.logical_tie_expressions_are_phrased:
            logical_tie_seed = seed_session.current_phrased_voicewise_logical_tie_seed
        else:
            logical_tie_seed = seed_session.current_unphrased_voicewise_logical_tie_seed
        self._apply_logical_tie_expression(
            logical_tie=logical_tie,
            pitch_range=pitch_range,
            seed=logical_tie_seed,
            )

    ### PRIVATE METHODS ###

    def _apply_logical_tie_expression(
        self,
        logical_tie,
        pitch_range,
        seed,
        ):
        if not self.logical_tie_expressions:
            return
        logical_tie_expression = self.logical_tie_expressions[seed]
        if logical_tie_expression is None:
            return
        logical_tie_expression(
            logical_tie,
            pitch_range=pitch_range,
            )

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

    @staticmethod
    def _get_instrument(logical_tie, music_specifier):
        if music_specifier.instrument is not None:
            return music_specifier.instrument
        component = logical_tie.head
        prototype = instrumenttools.Instrument
        instrument = inspect_(component).get_effective(prototype)
        return instrument

    def _get_pitch(
        self,
        pitch_class,
        registration,
        seed,
        ):
        octavations = self.octavations or self._default_octavations
        octave = octavations[seed]
        pitch = pitchtools.NamedPitch(pitch_class, octave)
        pitch_range = pitchtools.PitchRange('[C0, C8)')
        pitch = self._fit_pitch_to_pitch_range(pitch, pitch_range)
        pitch = registration([pitch])[0]
        pitch = pitchtools.NamedPitch(pitch)
        return pitch

    @staticmethod
    def _get_pitch_range(
        instrument,
        logical_tie,
        ):
        prototype = pitchtools.PitchRange
        component = logical_tie.head
        pitch_range = inspect_(component).get_effective(prototype)
        if pitch_range is None and instrument is not None:
            pitch_range = instrument.pitch_range
        return pitch_range

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

    def _initialize_application_rate(self, application_rate):
        assert application_rate in (
            None, 'logical_tie', 'division', 'phrase',
            )
        self._application_rate = application_rate

    def _initialize_logical_tie_expressions(self, logical_tie_expressions):
        import consort
        if logical_tie_expressions:
            prototype = (consort.LogicalTieExpression, type(None))
            assert logical_tie_expressions, logical_tie_expressions
            assert all(isinstance(_, prototype)
                for _ in logical_tie_expressions), \
                logical_tie_expressions
            logical_tie_expressions = datastructuretools.CyclicTuple(
                logical_tie_expressions,
                )
        self._logical_tie_expressions = logical_tie_expressions

    def _initialize_octavations(self, octavations):
        if octavations is not None:
            assert octavations
            assert all(isinstance(x, int) for x in octavations)
            octavations = datastructuretools.CyclicTuple(octavations)
        self._octavations = octavations

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

    @staticmethod
    def _process_session(segment_maker):
        import consort
        maker = consort.SegmentMaker
        attack_point_map = segment_maker.attack_point_map
        seed_session = consort.SeedSession()
        for logical_tie in attack_point_map:
            music_specifier = maker.logical_tie_to_music_specifier(logical_tie)
            if not music_specifier or not music_specifier.register_handler:
                continue
            register_handler = music_specifier.register_handler
            attack_point_signature = attack_point_map[logical_tie]
            application_rate = register_handler.application_rate
            voice = consort.SegmentMaker.logical_tie_to_voice(logical_tie)
            seed_session(
                application_rate,
                attack_point_signature,
                music_specifier,
                voice,
                )
            register_handler(
                attack_point_signature,
                logical_tie,
                music_specifier,
                seed_session,
                )

    ### PUBLIC PROPERTIES ###

    @property
    def application_rate(self):
        return self._application_rate

    @property
    def logical_tie_expressions(self):
        return self._logical_tie_expressions

    @property
    def logical_tie_expressions_are_phrased(self):
        return self._logical_tie_expressions_are_phrased

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
