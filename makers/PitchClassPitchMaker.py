# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from consort.makers.PitchMaker import PitchMaker


class PitchClassPitchMaker(PitchMaker):
    r'''PitchClass pitch maker.

    ::

        >>> from consort import makers
        >>> pitch_maker = makers.PitchClassPitchMaker(
        ...     pitch_classes="c' d' e' f'",
        ...     )
        >>> print(format(pitch_maker))
        consort.makers.PitchClassPitchMaker(
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
        '_register_specifier',
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
        pitch_classes=None,
        register_specifier=None,
        ):
        from consort import makers
        PitchMaker.__init__(
            self,
            allow_repetition=allow_repetition,
            chord_expressions=chord_expressions,
            )
        pitch_classes = pitchtools.PitchSegment(pitch_classes)
        pitch_classes = datastructuretools.CyclicTuple(pitch_classes)
        if octavations is not None:
            assert octavations
            assert all(isinstance(x, int) for x in octavations)
            octavations = datastructuretools.CyclicTuple(octavations)
        self._octavations = octavations
        self._pitch_classes = pitch_classes
        if register_specifier is not None:
            assert isinstance(register_specifier, makers.RegisterSpecifier)
        self._register_specifier = register_specifier

    ### PRIVATE METHODS ###

    def _calculate_octave_transposition_mapping(self, logical_tie, seed=0):
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
        octave_transposition_mapping = \
            pitchtools.OctaveTranspositionMapping([
                ('[C0, C4)', register),
                ('[C4, C8)', register + 6),
                ])
        return octave_transposition_mapping

    def _calculate_pitch(self, octave_transposition_mapping, seed=0):
        pitch_classes = self.pitch_classes or \
            datastructuretools.CyclicTuple([0])
        pitch_class = pitch_classes[seed]
        octavations = self.octavations or self._default_octavations
        octave = octavations[seed]
        pitch_class = pitchtools.NamedPitchClass(pitch_class)
        pitch = pitchtools.Pitch(pitch_class, octave)
        pitch = octave_transposition_mapping([pitch])
        return pitch

    def _process_logical_tie(
        self,
        logical_tie,
        seed=0,
        ):
        octave_transposition_mapping = \
            self.__calculate_octave_transposition_mapping(
                logical_tie,
                seed=seed,
                )
        pitch = self._calculate_pitch(
            octave_transposition_mapping,
            seed=seed,
            )
        for i, leaf in enumerate(logical_tie):
            leaf.written_pitch = pitch
        self._apply_chord_expression(logical_tie, seed)

    ### PUBLIC PROPERTIES ###

    @property
    def octavations(self):
        return self._octavations

    @property
    def pitch_classes(self):
        return self._pitch_classes

    @property
    def register_specifier(self):
        return self._register_specifier