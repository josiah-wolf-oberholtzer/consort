# -*- encoding: utf-8 -*-
import collections
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import new


class AttachmentAgent(ConsortObject):
    r'''An attachment agent.

    ::

        >>> from consort import makers
        >>> attachment_agent = makers.AttachmentAgent()
        >>> print(format(attachment_agent))
        makers.AttachmentAgent()

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
            if len(attachment_specifiers):
                attachment_specifiers = tuple(attachment_specifiers)
            else:
                attachment_specifiers = None
        self._attachment_specifiers = attachment_specifiers

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        assert isinstance(music, scoretools.Container)
        if self.attachment_specifiers is None:
            return
        for attachment_specifier in self.attachment_specifiers:
            attachment_specifier(music, seed=seed)

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
                attachment_agent = music_specifier.attachment_agent
                if attachment_agent is None:
                    continue
                seed = counter[attachment_agent]
                attachment_agent(
                    container,
                    seed=seed,
                    )
                counter[attachment_agent] += 1

    def reverse(self):
        attachment_specifiers = self.attachment_specifiers
        if attachment_specifiers is None:
            return new(self)
        attachment_specifiers = [
            attachment_specifier.reverse()
            for attachment_specifier in attachment_specifiers
            ]
        return new(self,
            attachment_specifiers=attachment_specifiers,
            )

    def rotate(self, n=0):
        attachment_specifiers = self.attachment_specifiers
        attachment_specifiers = [
            attachment_specifier.rotate(n)
            for attachment_specifier in attachment_specifiers
            ]
        return new(self,
            attachment_specifiers=attachment_specifiers,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_specifiers(self):
        return self._attachment_specifiers
