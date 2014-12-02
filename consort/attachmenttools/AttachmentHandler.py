# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools import systemtools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class AttachmentHandler(abctools.AbjadValueObject):
    r'''An attachment maker.

    ::

        >>> import consort
        >>> attachment_handler = consort.attachmenttools.AttachmentHandler()
        >>> print(format(attachment_handler))
        consort.attachmenttools.AttachmentHandler()

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
        from consort import attachmenttools
        prototype = attachmenttools.AttachmentExpression
        validated_attachment_expressions = {}
        for name, attachment_expression in attachment_expressions.items():
            if attachment_expression is None:
                continue
            assert isinstance(attachment_expression, prototype), \
                (name, attachment_expression)
            validated_attachment_expressions[name] = attachment_expression
        self._attachment_expressions = validated_attachment_expressions

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music,
        music_index=0,
        ):
        assert isinstance(music, scoretools.Container)
        if not self.attachment_expressions:
            return
        for name, attachment_expression in self.attachment_expressions.items():
            attachment_expression(music, seed=music_index)

    def __getattr__(self, item):
        if item in self.attachment_expressions:
            return self.attachment_expressions[item]
        return object.__getattribute__(self, item)

    ### PRIVATE METHODS ###

    @staticmethod
    def _process_session(segment_session):
        import consort
        score = segment_session.score
        counter = collections.Counter()
        for voice in iterate(score).by_class(scoretools.Voice):
            for container in voice:
                prototype = consort.coretools.MusicSpecifier
                music_specifier = inspect_(container).get_effective(prototype)
                maker = music_specifier.attachment_handler
                if maker is None:
                    continue
                if music_specifier not in counter:
                    seed = music_specifier.seed or 0
                    counter[music_specifier] = seed
                seed = counter[music_specifier]
                maker(container, music_index=seed)
                counter[music_specifier] += 1

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