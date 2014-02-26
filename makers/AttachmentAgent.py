# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class AttachmentAgent(abctools.AbjadObject):
    r'''An attachment agent.

    ::

        >>> from consort import makers
        >>> attachment_agent = makers.AttachmentAgent()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachment_specifiers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachment_specifiers=None,
        ):
        from consort import makers
        prototype = makers.AttachmentSpecifier
        if attachment_specifiers is not None:
            assert all(isinstance(x, prototype) for x in attachment_specifiers)
        self._attachment_specifiers = attachment_specifiers

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
                attachment_agent = music_specifier.attachment_agent
                if attachment_agent is None:
                    continue
                seed = counter[attachment_agent]
                attachment_agent(
                    container,
                    seed=seed,
                    )
                counter[attachment_agent] += 1

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_specifiers(self):
        return self._attachment_specifiers
