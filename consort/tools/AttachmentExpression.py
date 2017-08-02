import abjad
import collections
import copy
try:
    import funcsigs
except ImportError:
    import inspect as funcsigs
from abjad import attach
from consort.tools.HashCachingObject import HashCachingObject


class AttachmentExpression(HashCachingObject):
    r'''An attachment specifier.

    ..  container:: example

        ::

            >>> attachment_expression = consort.AttachmentExpression(
            ...     attachments=(abjad.Articulation('>'),),
            ...     selector=abjad.Selector().by_leaf().by_run(abjad.Note)[0],
            ...     )
            >>> print(format(attachment_expression))
            consort.tools.AttachmentExpression(
                attachments=abjad.TypedList(
                    [
                        abjad.Articulation('>'),
                        ]
                    ),
                selector=abjad.Selector(
                    callbacks=(
                        abjad.PrototypeSelectorCallback(
                            prototype=abjad.Leaf,
                            ),
                        abjad.RunSelectorCallback(
                            prototype=abjad.Note,
                            ),
                        abjad.ItemSelectorCallback(
                            item=0,
                            apply_to_each=True,
                            ),
                        ),
                    ),
                )

        ::

            >>> attachment_expression = consort.AttachmentExpression(
            ...     attachments=(
            ...         consort.SimpleDynamicExpression(
            ...             hairpin_start_token='sfz',
            ...             hairpin_stop_token='niente',
            ...             ),
            ...         ),
            ...     selector=abjad.Selector().by_leaf().by_run(abjad.Note),
            ...     )

        ::

            >>> staff = abjad.Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
            >>> attachment_expression(staff)
            >>> print(format(staff))
            \new Staff {
                c'8 \sfz
                r8
                \override Hairpin.circled-tip = ##t
                d'8 \> \sfz
                \revert Hairpin.circled-tip
                e'8 \!
                r8
                \override Hairpin.circled-tip = ##t
                f'8 \> \sfz
                g'8
                \revert Hairpin.circled-tip
                a'8 \!
            }

    ..  container:: example

        ::

            >>> attachment_expression = consort.AttachmentExpression(
            ...     attachments=abjad.Slur(),
            ...     )
            >>> staff = abjad.Staff("c'4 d'4 e'4 f'4")
            >>> attachment_expression(staff)
            >>> print(format(staff))
            \new Staff {
                c'4 (
                d'4
                e'4
                f'4 )
            }

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 f'4")
            >>> attachment_expression = consort.AttachmentExpression(
            ...     attachments=[
            ...         [
            ...             abjad.Articulation('accent'),
            ...             abjad.Articulation('staccato'),
            ...             ],
            ...         ],
            ...     selector=abjad.Selector().by_logical_tie()[0]
            ...     )
            >>> attachment_expression(staff)
            >>> print(format(staff))
            \new Staff {
                c'4 -\accent -\staccato
                d'4 -\accent -\staccato
                e'4 -\accent -\staccato
                f'4 -\accent -\staccato
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachments',
        '_scope',
        '_selector',
        '_is_annotation',
        '_is_destructive',
        '_use_only_first_attachment',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachments=None,
        selector=None,
        scope=None,
        is_annotation=None,
        is_destructive=None,
        use_only_first_attachment=None,
        ):
        HashCachingObject.__init__(self)
        if attachments is not None:
            if not isinstance(attachments, collections.Sequence):
                attachments = (attachments,)
            attachments = abjad.TypedList(attachments)
        self._attachments = attachments
        if selector is not None:
            assert isinstance(selector, abjad.Selector)
        self._selector = selector
        if scope is not None:
            if isinstance(scope, type):
                assert issubclass(scope, abjad.Component)
            else:
                assert isinstance(scope, (abjad.Component, str))
        self._scope = scope
        if is_annotation is not None:
            is_annotation = bool(is_annotation)
        self._is_annotation = is_annotation
        if is_destructive is not None:
            is_destructive = bool(is_destructive)
        self._is_destructive = is_destructive
        if use_only_first_attachment is not None:
            use_only_first_attachment = bool(use_only_first_attachment)
        self._use_only_first_attachment = use_only_first_attachment

    ### PUBLIC METHODS ###

    def __call__(
        self,
        music,
        name=None,
        rotation=0,
        ):
        selector = self.selector
        if selector is None:
            selector = abjad.Selector()
        selections = selector(music, rotation=rotation)
        self._apply_attachments(
            selections,
            name=name,
            rotation=rotation,
            )

    ### PRIVATE METHODS ###

    def _apply_attachments(self, selections, name=None, rotation=None):
        if not self.attachments:
            return
        all_attachments = abjad.CyclicTuple(self.attachments)
        if self.use_only_first_attachment:
            attachments = all_attachments[rotation]
        for i, selection in enumerate(selections, rotation):
            if not self.use_only_first_attachment:
                attachments = all_attachments[i]
            # print(i, selection, attachments)
            if attachments is None:
                continue
            if not isinstance(attachments, collections.Sequence):
                attachments = (attachments,)
            for attachment in attachments:
                # print('\t' + repr(attachment))
                # spanners
                if isinstance(attachment, abjad.Spanner):
                    attachment = copy.copy(attachment)
                    attach(attachment, selection, name=name)
                elif isinstance(attachment, type) and \
                    issubclass(attachment, abjad.Spanner):
                    attachment = attachment()
                    attach(attachment, selection, name=name)
                # expressions
                elif hasattr(attachment, '__call__'):
                    signature = funcsigs.signature(attachment.__call__)
                    if 'seed' in signature.parameters:
                        attachment(selection, seed=rotation, name=name)
                    elif 'rotation' in signature.parameters:
                        attachment(selection, rotation=rotation, name=name)
                    elif 'name' in signature.parameters:
                        attachment(selection, name=name)
                    else:
                        attachment(selection)
                # indicators
                else:
                    if isinstance(selection, abjad.Leaf):
                        selection = (selection,)
                    for component in selection:
                        attachment = copy.copy(attachment)
                        attach(
                            attachment,
                            component,
                            name=name,
                            scope=self.scope,
                            is_annotation=self.is_annotation,
                            )

    ### PUBLIC METHODS ###

    def reverse(self):
        attachments = abjad.Sequence(*self.attachments)
        return abjad.new(
            self,
            attachments=attachments.reverse(),
            )

    def rotate(self, n=0):
        attachments = abjad.Sequence(*self.attachments)
        return abjad.new(
            self,
            attachments=attachments.rotate(n),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachments(self):
        return self._attachments

    @property
    def is_annotation(self):
        return self._is_annotation

    @property
    def is_destructive(self):
        return self._is_destructive

    @property
    def scope(self):
        return self._scope

    @property
    def selector(self):
        return self._selector

    @property
    def use_only_first_attachment(self):
        return self._use_only_first_attachment
