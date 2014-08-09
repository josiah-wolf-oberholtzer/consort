# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import sequencetools


class HarmonicFieldPitchMaker(abctools.AbjadValueObject):
    r'''A harmonic field pitch maker.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_harmonic_fields',
        '_register_specifier',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        chord_specifiers=None,
        harmonic_fields=None,
        register_specifier=None,
        ):
        from consort import makers
        prototype = makers.ChordSpecifier
        if isinstance(chord_specifiers, prototype):
            chord_specifiers = (chord_specifiers,)
        assert all(isinstance(x, prototype) for x in chord_specifiers)
        chord_specifiers = sequencetools.CyclicTuple(chord_specifiers)
        self._chord_specifiers = chord_specifiers
        prototype = makers.HarmonicField
        if isinstance(harmonic_fields, prototype):
            harmonic_fields = (harmonic_fields,)
        assert all(isinstance(x, prototype) for x in harmonic_fields)
        harmonic_fields = sequencetools.CyclicTuple(harmonic_fields)
        self._harmonic_fields = harmonic_fields
        if register_specifier is not None:
            assert isinstance(register_specifier, makers.RegisterSpecifier)
        self._register_specifier = register_specifier

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        previous_pitch,
        pitch_range,
        seed=0,
        ):
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
        harmonic_field = self.harmonic_fields[seed]
        harmonic_field_entries = harmonic_field._find_nearest_entries(
            register,
            entry_count=2,
            pitch_range=pitch_range,
            )
        resulting_pitch = harmonic_field_entries[0]
        if resulting_pitch == previous_pitch:
            resulting_pitch = harmonic_field_entries[1]
        for note in logical_tie:
            note.written_pitch = resulting_pitch
        if self.chord_specifiers:
            chord_specifier = self.chord_specifiers[seed]
            chord_specifier(
                logical_tie,
                pitch_range=pitch_range,
                )

    ### PUBLIC PROPERTIES ###

    @property
    def chord_specifiers(self):
        return self._chord_specifiers

    @property
    def harmonic_fields(self):
        return self._harmonic_fields

    @property
    def register_specifer(self):
        return self._register_specifier