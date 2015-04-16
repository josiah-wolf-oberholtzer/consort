# -*- encoding: utf-8 -*-
from abjad import attach
from abjad import inspect_
from abjad import mutate
from abjad import select
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from consort.tools.HashCachingObject import HashCachingObject


class LeafExpression(HashCachingObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachments',
        '_leaf',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        leaf=None,
        attachments=None,
        ):
        HashCachingObject.__init__(self)
        prototype = scoretools.Leaf
        if leaf is not None:
            if isinstance(leaf, prototype):
                leaf = mutate(leaf).copy()
            elif issubclass(leaf, prototype):
                leaf = leaf()
            else:
                raise ValueError(leaf)
        self._leaf = leaf
        if attachments is not None:
            attachments = tuple(attachments)
        self._attachments = attachments

    ### SPECIAL METHODS ###

    def __call__(self, expr):
        if isinstance(expr, scoretools.Leaf):
            expr = select(expr)
        assert isinstance(expr, selectiontools.Selection)
        for i, old_leaf in enumerate(expr):
            assert isinstance(old_leaf, scoretools.Leaf)
            new_leaf = self._make_new_leaf(old_leaf)

            timespan = old_leaf._timespan
            start_offset = old_leaf._start_offset
            stop_offset = old_leaf._stop_offset
            mutate(old_leaf).replace(new_leaf)
            new_leaf._timespan = timespan
            new_leaf._start_offset = start_offset
            new_leaf._stop_offset = stop_offset

            if i == 0 and self.attachments:
                for attachment in self.attachments:
                    attach(attachment, new_leaf)

    ### PRIVATE METHODS ###

    def _make_new_leaf(self, old_leaf):
        duration = old_leaf.written_duration
        if isinstance(self.leaf, scoretools.Note):
            new_leaf = scoretools.Note(self.leaf.written_pitch, duration)
        elif isinstance(self.leaf, scoretools.Chord):
            new_leaf = scoretools.Chord(self.leaf.written_pitches, duration)
        elif isinstance(self.leaf, scoretools.Rest):
            new_leaf = scoretools.Rest(duration)
        elif isinstance(self.leaf, scoretools.Skip):
            new_leaf = scoretools.Skip(duration)
        prototype = durationtools.Multiplier
        if inspect_(old_leaf).has_indicator(prototype):
            multiplier = inspect_(old_leaf).get_indicator(prototype)
            attach(multiplier, new_leaf)
        return new_leaf

    ### PUBLIC PROPERTIES ###

    @property
    def attachments(self):
        return self._attachments

    @property
    def leaf(self):
        return self._leaf