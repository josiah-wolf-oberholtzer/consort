# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import scoretools


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

    def __call__(
        self,
        music,
        seed=0,
        ):
        assert isinstance(music, scoretools.Container)
        if not self.attachment_expressions:
            return
        for attachment_expression in self.attachment_expressions:
            attachment_expression(music, seed=seed)

    ### PUBLIC METHODS ###

    def reverse(self):
        new_attachment_expressions = {}
        for name, attachment_expression in self.attachment_expressions:
            new_attachment_expressions[name] = attachment_expression.reverse()
        return type(self)(**new_attachment_expressions)

    def rotate(self, n=0):
        new_attachment_expressions = {}
        for name, attachment_expression in self.attachment_expressions:
            new_attachment_expressions[name] = attachment_expression.rotate(n)
        return type(self)(**new_attachment_expressions)

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_expressions(self):
        return self._attachment_expressions