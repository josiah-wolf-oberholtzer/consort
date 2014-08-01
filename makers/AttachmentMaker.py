# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import new


class AttachmentMaker(abctools.AbjadValueObject):
    r'''An attachment agent.

    ::

        >>> from consort import makers
        >>> attachment_maker = makers.AttachmentMaker()
        >>> print(format(attachment_maker))
        makers.AttachmentMaker()

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
                attachment_maker = music_specifier.attachment_maker
                if attachment_maker is None:
                    continue
                seed = counter[attachment_maker]
                attachment_maker(
                    container,
                    seed=seed,
                    )
                counter[attachment_maker] += 1

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
