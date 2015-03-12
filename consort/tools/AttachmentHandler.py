# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad import inspect_
from abjad import iterate
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools import systemtools


class AttachmentHandler(abctools.AbjadValueObject):
    r'''An attachment maker.

    ::

        >>> import consort
        >>> attachment_handler = consort.AttachmentHandler()
        >>> print(format(attachment_handler))
        consort.tools.AttachmentHandler()

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
        import consort
        prototype = consort.AttachmentExpression
        validated_attachment_expressions = {}
        for name, attachment_expression in attachment_expressions.items():
            if attachment_expression is None:
                continue
            if not isinstance(attachment_expression, prototype):
                attachment_expression = consort.AttachmentExpression(
                    attachments=attachment_expression,
                    )
            validated_attachment_expressions[name] = attachment_expression
        self._attachment_expressions = validated_attachment_expressions

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        assert isinstance(music, scoretools.Container)
        if not self.attachment_expressions:
            return
        items = self.attachment_expressions.items()
        for name, attachment_expression in items:
            attachment_expression(
                music,
                name=name,
                seed=seed,
                )

    def __getattr__(self, item):
        if item in self.attachment_expressions:
            return self.attachment_expressions[item]
        return object.__getattribute__(self, item)

    ### PRIVATE METHODS ###

    @staticmethod
    def _process_session(segment_maker):
        import consort
        score = segment_maker.score
        counter = collections.Counter()
        for voice in iterate(score).by_class(scoretools.Voice):
            for container in voice:
                prototype = consort.MusicSpecifier
                music_specifier = inspect_(container).get_effective(prototype)
                maker = music_specifier.attachment_handler
                if maker is None:
                    continue
                if music_specifier not in counter:
                    seed = music_specifier.seed or 0
                    counter[music_specifier] = seed
                seed = counter[music_specifier]
                maker(container, seed=seed)
                counter[music_specifier] -= 1

    ### PRIVATE PROPERTIES ###

    @property
    def _storage_format_specification(self):
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=sorted(self.attachment_expressions.keys()),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_expressions(self):
        return self._attachment_expressions.copy()