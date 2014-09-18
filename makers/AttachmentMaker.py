# -*- encoding: utf-8 -*-
import collections
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class AttachmentMaker(abctools.AbjadValueObject):
    r'''An attachment maker.

    ::

        >>> from consort import makers
        >>> attachment_maker = makers.AttachmentMaker()
        >>> print(format(attachment_maker))
        consort.makers.AttachmentMaker()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachment_expressions',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachment_expressions=None,
        ):
        from consort import makers
        prototype = makers.AttachmentExpression
        if attachment_expressions is not None:
            for attachment_expression in attachment_expressions:
                assert isinstance(attachment_expression, prototype)
        self._attachment_expressions = attachment_expressions

    ### SPECIAL METHODS ###

    def __add__(self, expr):
        assert isinstance(expr, type(self))
        attachment_expressions = self.attachment_expressions or ()
        attachment_expressions = expr.attachment_expressions or ()
        return type(self)(attachment_expressions)

    def __call__(
        self,
        music,
        music_index=0,
        ):
        assert isinstance(music, scoretools.Container)
        if not self.attachment_expressions:
            return
        for attachment_expression in self.attachment_expressions:
            attachment_expression(music, seed=music_index)

    def __getitem__(self, item):
        return self.attachment_expressions[item]

    def __len__(self):
        return len(self.attachment_expressions)

    @staticmethod
    def _process_score(score):
        from consort import makers
        counter = collections.Counter()
        for voice in iterate(score).by_class(scoretools.Voice):
            for container in voice:
                prototype = makers.MusicSpecifier
                music_specifier = inspect_(container).get_effective(prototype)
                maker = music_specifier.attachment_maker
                if maker is None:
                    continue
                if music_specifier not in counter:
                    seed = music_specifier.seed or 0
                    counter[music_specifier] = seed
                seed = counter[music_specifier]
                maker(container, music_index=seed)
                counter[music_specifier] += 1

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_expressions(self):
        return self._attachment_expressions