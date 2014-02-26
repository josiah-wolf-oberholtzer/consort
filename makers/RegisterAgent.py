# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class RegisterAgent(abctools.AbjadObject):
    r'''An register agent.

    ::

        >>> from consort import makers
        >>> register_agent = makers.RegisterAgent()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(
        self,
        ):
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
        for voice in iterate(score).by_context(voice):
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
