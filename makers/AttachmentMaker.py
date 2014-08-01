# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import scoretools
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
            assert all(isinstance(x, prototype) for x in attachment_expressions)
            if len(attachment_expressions):
                attachment_expressions = tuple(attachment_expressions)
            else:
                attachment_expressions = None
        self._attachment_expressions = attachment_expressions

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        assert isinstance(music, scoretools.Container)
        if self.attachment_expressions is None:
            return
        for attachment_expression in self.attachment_expressions:
            attachment_expression(music, seed=seed)

    ### PUBLIC METHODS ###

    def reverse(self):
        attachment_expressions = self.attachment_expressions
        if attachment_expressions is None:
            return new(self)
        attachment_expressions = [
            attachment_expression.reverse()
            for attachment_expression in attachment_expressions
            ]
        return new(self,
            attachment_expressions=attachment_expressions,
            )

    def rotate(self, n=0):
        attachment_expressions = self.attachment_expressions
        attachment_expressions = [
            attachment_expression.rotate(n)
            for attachment_expression in attachment_expressions
            ]
        return new(self,
            attachment_expressions=attachment_expressions,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_expressions(self):
        return self._attachment_expressions