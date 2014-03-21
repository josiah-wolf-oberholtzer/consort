# -*- encoding: utf-8 -*-
import collections
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class RegisterAgent(ConsortObject):
    r'''An register agent.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_division_inflections',
        '_global_inflections',
        '_octavations',
        '_phrase_inflections',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        division_inflections=None,
        global_inflections=None,
        octavations=None,
        phrase_inflections=None,
        ):
        from plague_water import makers
        pass

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        assert isinstance(music, scoretools.Container)

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
                seed = counter[register_agent]
                register_agent(
                    container,
                    seed=seed,
                    )
                counter[register_agent] += 1

    ### PUBLIC PROPERTIES ###

    @property
    def division_inflections(self):
        return self._division_inflections

    @property
    def global_inflections(self):
        return self._global_inflections

    @property
    def phrase_inflections(self):
        return self._phrase_inflections

    @property
    def octavations(self):
        return self._octavations
