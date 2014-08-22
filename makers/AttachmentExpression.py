# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import sequencetools
from abjad.tools import spannertools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import new
from experimental.tools import selectortools
import collections
import copy


class AttachmentExpression(abctools.AbjadValueObject):
    r'''An attachment specifier.

    ::

        >>> from consort import makers
        >>> attachment_expression = makers.AttachmentExpression(
        ...     attachments=(indicatortools.Articulation('>'),),
        ...     selector=selectortools.Selector().by_leaves().by_run(Note)[0],
        ...     )
        >>> print(format(attachment_expression))
        consort.makers.AttachmentExpression(
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

        >>> attachment_expression = makers.AttachmentExpression(
        ...     attachments=(
        ...         makers.DynamicExpression(
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
            d'8 \sfz
            e'8
            r8
            \override Hairpin #'circled-tip = ##t
            f'8 \> \sfz
            g'8
            a'8 \!
            \revert Hairpin #'circled-tip
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachments',
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
        if selector is not None:
            assert isinstance(selector, selectortools.Selector)
        self._selector = selector

    ### PUBLIC METHODS ###

    def __call__(
        self,
        music,
        seed=0,
        ):
        if not self.attachments or not self.selector:
            return
        all_attachments = datastructuretools.CyclicTuple(self.attachments)
        all_attachments = sequencetools.rotate_sequence(all_attachments, seed)
        selector = self.selector or selectortools.Selector()
        selections = selector(music)
        for i, selection in enumerate(selections, seed):
            attachments = all_attachments[i]
            if attachments is None:
                continue
            if not isinstance(attachments, tuple):
                attachments = (attachments,)
            for attachment in attachments:
                # spanners
                if isinstance(attachment, spannertools.Spanner):
                    attachment = copy.copy(attachment)
                    attach(attachment, selection)
                # expressions
                elif hasattr(attachment, '__call__'):
                    attachment(selection)
                # indicators
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
        hash_values = (type(self), format(self))
        return hash(hash_values)

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