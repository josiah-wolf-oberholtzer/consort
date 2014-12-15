# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import scoretools
from abjad.tools import sequencetools
from abjad.tools import spannertools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import new
from experimental.tools import selectortools
import collections
import copy


class AttachmentExpression(abctools.AbjadValueObject):
    r'''An attachment specifier.

    ..  container:: example

        ::

            >>> import consort
            >>> attachment_expression = consort.AttachmentExpression(
            ...     attachments=(indicatortools.Articulation('>'),),
            ...     selector=selectortools.Selector().by_leaves().by_run(Note)[0],
            ...     )
            >>> print(format(attachment_expression))
            consort.tools.AttachmentExpression(
                attachments=datastructuretools.TypedList(
                    [
                        indicatortools.Articulation('>'),
                        ]
                    ),
                selector=selectortools.Selector(
                    callbacks=(
                        selectortools.PrototypeSelectorCallback(
                            prototype=scoretools.Leaf,
                            ),
                        selectortools.RunSelectorCallback(
                            prototype=scoretools.Note,
                            ),
                        selectortools.ItemSelectorCallback(
                            item=0,
                            apply_to_each=True,
                            ),
                        ),
                    ),
                )

        ::

            >>> attachment_expression = consort.AttachmentExpression(
            ...     attachments=(
            ...         consort.DynamicExpression(
            ...             hairpin_start_token='sfz',
            ...             hairpin_stop_token='o',
            ...             ),
            ...         ),
            ...     selector=selectortools.Selector().by_leaves().by_run(Note),
            ...     )

        ::

            >>> staff = Staff("c'8 r8 d'8 e'8 r8 f'8 g'8 a'8")
            >>> attachment_expression(staff)
            >>> print(format(staff))
            \new Staff {
                c'8 \sfz
                r8
                \override Hairpin #'circled-tip = ##t
                d'8 \> \sfz
                e'8 \!
                \revert Hairpin #'circled-tip
                r8
                \override Hairpin #'circled-tip = ##t
                f'8 \> \sfz
                g'8
                a'8 \!
                \revert Hairpin #'circled-tip
            }

    ..  container:: example

        ::

            >>> attachment_expression = consort.AttachmentExpression(
            ...     attachments=spannertools.Slur(),
            ...     )
            >>> staff = Staff("c'4 d'4 e'4 f'4")
            >>> attachment_expression(staff)
            >>> print(format(staff))
            \new Staff {
                c'4 (
                d'4
                e'4
                f'4 )
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachments',
        '_hash',
        '_selector',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachments=None,
        selector=None,
        ):
        if attachments is not None:
            if not isinstance(attachments, collections.Sequence):
                attachments = (attachments,)
            attachments = datastructuretools.TypedList(attachments)
        self._attachments = attachments
        self._hash = None
        if selector is not None:
            assert isinstance(selector, selectortools.Selector)
        self._selector = selector

    ### PUBLIC METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        if not self.attachments:
            return
        all_attachments = datastructuretools.CyclicTuple(self.attachments)
        selector = self.selector
        if selector is None:
            selector = selectortools.Selector()
        selections = selector(music)
        for i, selection in enumerate(selections, seed):
            attachments = all_attachments[i]
            #print(i, selection)
            if attachments is None:
                continue
            if not isinstance(attachments, tuple):
                attachments = (attachments,)
            for attachment in attachments:
                #print('\t' + repr(attachment))
                # spanners
                if isinstance(attachment, spannertools.Spanner):
                    attachment = copy.copy(attachment)
                    attach(attachment, selection)
                elif isinstance(attachment, type) and \
                    issubclass(attachment, spannertools.Spanner):
                    attachment = attachment()
                    attach(attachment, selection)
                # expressions
                elif hasattr(attachment, '__call__'):
                    try:
                        attachment(selection, seed=seed)
                    except TypeError:
                        attachment(selection)
                # indicators
                else:
                    if isinstance(selection, scoretools.Leaf):
                        attachment = copy.copy(attachment)
                        attach(attachment, selection)
                    else:
                        for component in selection:
                            attachment = copy.copy(attachment)
                            attach(attachment, component)

    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            if format(self) == format(expr):
                return True
        return False

    def __hash__(self):
        if self._hash is None:
            hash_values = (type(self), format(self))
            self._hash = hash(hash_values)
        return self._hash

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='attachments',
                display_string='attachments',
                command='at',
                editor=datastructuretools.TypedList,
                ),
            systemtools.AttributeDetail(
                name='selector',
                display_string='selector',
                command='se',
                editor=selectortools.Selector,
                ),
            )

    ### PUBLIC METHODS ###

    def reverse(self):
        attachments = sequencetools.Sequence(*self.attachments)
        return new(self,
            attachments=attachments.reverse(),
            )

    def rotate(self, n=0):
        attachments = sequencetools.Sequence(*self.attachments)
        return new(self,
            attachments=attachments.rotate(n),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachments(self):
        return self._attachments

    @property
    def selector(self):
        return self._selector