# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import pitchtools
from abjad.tools import sequencetools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class HarmonicFieldPitchMaker(abctools.AbjadValueObject):
    r'''A harmonic field pitch maker.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_allow_repetition',
        '_chord_specifiers',
        '_harmonic_fields',
        '_register_specifier',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        allow_repetition=False,
        chord_specifiers=None,
        harmonic_fields=None,
        register_specifier=None,
        ):
        from consort import makers
        self._allow_repetition = bool(allow_repetition)
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
        music,
        seed=0,
        ):
        pitch_range = inspect_(music).get_effective(pitchtools.PitchRange)
        previous_pitch = None
        iterator = iterate(music).by_logical_tie(pitched=True)
        for i, logical_tie in enumerate(iterator):
            previous_pitch = self._process_logical_tie(
                logical_tie,
                previous_pitch=previous_pitch,
                pitch_range=pitch_range,
                seed=seed + i,
                )

    ### PRIVATE METHODS ###

    def _process_grace_notes(
        self,
        logical_tie,
        harmonic_field_entry,
        pitch_range,
        ):
        previous_leaf = logical_tie.head._get_leaf(-1)
        if not previous_leaf:
            return
        grace_containers = inspect_(previous_leaf).get_grace_containers('after')
        if not grace_containers:
            return
        after_grace = grace_containers[0]
        leaves = reversed(after_grace.select_leaves())
        pitches = harmonic_field_entry.leading_pitches + \
            (harmonic_field_entry.structural_pitch,)
        pitches = pitches.retrograde()
        for i, leaf in enumerate(leaves, 1):
            pitch = pitches[i]
            if pitch < pitch_range.start_pitch:
                pitch = pitch.transpose(12)
            elif pitch_range.stop_pitch < pitch:
                pitch = pitch.transpose(-12)
            leaf.written_pitch = pitch

    def _process_logical_tie(
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
        harmonic_field_entry = harmonic_field_entries[0]
        structural_pitch = harmonic_field_entry.structural_pitch
        if not self.allow_repetition:
            if structural_pitch == previous_pitch:
                structural_pitch = harmonic_field_entries[1]
        for note in logical_tie:
            note.written_pitch = structural_pitch
        if self.chord_specifiers:
            chord_specifier = self.chord_specifiers[seed]
            chord_specifier(
                logical_tie,
                pitch_range=pitch_range,
                )
        self._process_grace_notes(logical_tie, harmonic_field_entry)
        return structural_pitch

    ### PUBLIC PROPERTIES ###

    @property
    def allow_repetition(self):
        return self._allow_repetition

    @property
    def chord_specifiers(self):
        return self._chord_specifiers

    @property
    def harmonic_fields(self):
        return self._harmonic_fields

    @property
    def register_specifer(self):
        return self._register_specifier