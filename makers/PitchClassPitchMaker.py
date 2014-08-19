# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import detach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import mutate
from consort.makers.PitchMaker import PitchMaker


class PitchClassPitchMaker(PitchMaker):
    r'''PitchClass pitch maker.

    ::

        >>> from consort import makers
        >>> pitch_maker = makers.PitchClassPitchMaker(
        ...     groupings=(2, 1, 1, 1),
        ...     pitch_classes="c' d' e' f'",
        ...     )
        >>> print(format(pitch_maker))
        consort.makers.PitchClassPitchMaker(
            allow_repetition=False,
            groupings=(2, 1, 1, 1),
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
        '_groupings',
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
        groupings=None,
        octavations=None,
        pitch_classes=None,
        register_specifier=None,
        ):
        from consort import makers
        PitchMaker.__init__(
            self,
            allow_repetition=allow_repetition,
            )
        groupings = groupings or (1,)
        groupings = tuple(int(x) for x in groupings)
        assert all(0 < x for x in groupings)
        self._groupings = groupings
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

    def _calculate_pitches(self, octave_transposition_mapping, seed=0):
        grouping = self._groupings[seed]
        pitch_classes = self.pitch_classes[seed:seed + grouping]
        octavations = self.octavations or self._default_octavations
        octavations = octavations[seed:seed + grouping]
        pitches = []
        for pitch_class, octave in zip(pitch_classes, octavations):
            pitch_class = pitchtools.NamedPitchClass(pitch_class)
            pitch = pitchtools.Pitch(pitch_class, octave)
            pitches.append(pitch)
        pitches = octave_transposition_mapping([pitches])
        pitches = pitchtools.PitchSet(pitches)
        return pitches

    def _process_logical_tie(
        self,
        logical_tie,
        seed=0,
        ):
        if not self.pitch_classes:
            return
        octave_transposition_mapping = \
            self.__calculate_octave_transposition_mapping(
                logical_tie,
                seed=seed,
                )
        pitches = self._calculate_pitches(
            octave_transposition_mapping,
            seed=seed,
            )
        for i, leaf in enumerate(logical_tie):
            if 1 < len(pitches):
                chord = scoretools.Chord(leaf)
                chord.written_pitches = pitches
                grace_containers = inspect_(leaf).get_grace_containers('after')
                if grace_containers:
                    old_grace_container = grace_containers[0]
                    grace_notes = old_grace_container.select_leaves()
                    detach(scoretools.GraceContainer, leaf)
                mutate(leaf).replace(chord)
                if grace_containers:
                    new_grace_container = scoretools.GraceContainer(
                        grace_notes,
                        kind='after',
                        )
                    attach(new_grace_container, chord)
            else:
                leaf.written_pitch = pitches[0]

    ### PUBLIC PROPERTIES ###

    @property
    def groupings(self):
        return self._groupings

    @property
    def octavations(self):
        return self._octavations

    @property
    def pitch_classes(self):
        return self._pitch_classes

    @property
    def register_specifier(self):
        return self._register_specifier