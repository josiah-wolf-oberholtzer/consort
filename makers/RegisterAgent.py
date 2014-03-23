# -*- encoding: utf-8 -*-
import collections
from abjad.tools import datastructuretools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from consort.makers.ConsortObject import ConsortObject


class RegisterAgent(ConsortObject):
    r'''An register agent.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_register',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        register=None,
        ):
        if register is not None:
            register = pitchtools.NamedPitch(register)
        self._register = register

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        assert isinstance(music, scoretools.Container)
        octave_transposition_mapping = self.octave_transposition_mapping
        iterator = iterate(music).by_logical_tie(pitched=True)
        for i, logical_tie in enumerate(iterator):
            i += seed
            octave = pitchtools.Octave(self.octavations[i])
            named_pitch = logical_tie.head.written_pitch
            named_pitch_class = named_pitch.named_pitch_class
            octavated_pitch = pitchtools.NamedPitch(named_pitch_class, octave)
            new_pitch = octave_transposition_mapping([octavated_pitch])
            for note in logical_tie:
                note.written_pitch = new_pitch

    ### PUBLIC METHODS ###

    @staticmethod
    def iterate_score(
        score,
        ):
        from consort import makers
        counter = collections.Counter()
        for voice in iterate(score).by_class(scoretools.Voice):
            for container in voice:
                prototype = makers.MusicSpecifier
                music_specifier = inspect_(container).get_effective(prototype)
                register_agent = music_specifier.register_agent
                if register_agent is None:
                    continue
                seed = counter[music_specifier]
                register_agent(
                    container,
                    seed=seed,
                    )
                counter[music_specifier] += 1

    ### PUBLIC PROPERTIES ###

    @property
    def octavations(self):
        return datastructuretools.CyclicTuple((
            2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, 9, 0, 4, 5, 2, 3, 5, 3, 6, 0,
            2, 8, 7, 4, 7, 1, 3, 5, 2, 6, 6, 2, 4, 9, 7, 7, 5, 7, 2, 4, 7, 0,
            ))

    @property
    def register(self):
        return self._register

    @property
    def octave_transposition_mapping(self):
        return pitchtools.OctaveTranspositionMapping([
            ('[C0, C5)', self.register),
            ('[C5, C10)', self.register + 6),
            ])
