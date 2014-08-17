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
        **attachment_expressions
        ):
        from consort import makers
        prototype = makers.AttachmentExpression
        all_expressions = {}
        for name, attachment_expression in attachment_expressions.items():
            if attachment_expression is None:
                continue
            assert isinstance(attachment_expression, prototype)
            all_expressions[name] = attachment_expression
        self._attachment_expressions = all_expressions

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        assert isinstance(music, scoretools.Container)
        if self.attachment_expressions is None:
            return
        for attachment_expression in self.attachment_expressions.values():
            attachment_expression(music, seed=seed)

    ### PRIVATE PROPERTIES ###

    @property
    def _storage_format_specification(self):
        from abjad.tools import systemtools
        manager = systemtools.StorageFormatManager
        keyword_argument_names = manager.get_keyword_argument_names(self)
        keyword_argument_names = list(keyword_argument_names)
        keyword_argument_names.extend(sorted(self.attachment_expressions))
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=keyword_argument_names
            )

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
        return self._attachment_expressions.copy()