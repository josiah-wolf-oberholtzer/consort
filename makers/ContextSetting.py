# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools.topleveltools import iterate
from abjad.tools.topleveltools import new


class ContextSetting(abctools.AbjadObject):
    r'''A context setting.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_context_identifier',
        '_key',
        '_value',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        context_identifier=None,
        key=None,
        value=None,
        ):
        if context_identifier is not None:
            if isinstance(context_identifier, str):
                context_identifier = (context_identifier,)
            if not isinstance(context_identifier, tuple):
                context_identifier = tuple(context_identifier)
        self._context_identifier = context_identifier
        self._key = key
        self._value = value

    ### SPECIAL METHODS ###

    def __call__(self, segment_product):
        from consort import makers
        prototype = makers.ConsortSegmentMaker.SegmentProduct
        assert isinstance(segment_product, prototype)
        assert segment_product.timespan_inventory_mapping is not None
        score = segment_product.segment_maker.score_template()
        context_names = set()
        for context_name in self.context_identifier:
            context = score[context_name]
            if isinstance(context, scoretools.Voice):
                context_names.add(context_name)
            else:
                for voice in iterate(context).by_class(scoretools.Voice):
                    context_names.add(voice.name)
        segment_duration = segment_product.segment_duration
        timespan_inventory_mapping = segment_product.timespan_inventory_mapping
        for context_name in context_names:
            if context_name not in timespan_inventory_mapping:
                continue
            timespan_inventory = timespan_inventory_mapping[context_name]
            self._apply_setting(
                segment_duration=segment_duration,
                timespan_inventory=timespan_inventory,
                )

    ### PRIVATE METHODS ###

    def _apply_setting(
        self,
        segment_duration=None,
        timespan_inventory=None,
        ):
        from consort import makers
        for timespan in timespan_inventory[:]:
            if not isinstance(timespan, makers.PerformedTimespan):
                continue
            elif not self._is_applicable_timespan(
                segment_duration=segment_duration,
                timespan=timespan,
                ):
                continue
            music_specifier = timespan.music_specifier
            key = self._key
            value = self._value
            if isinstance(self.value, makers.Transform):
                parts = key.split('__')
                object_ = music_specifier
                while parts:
                    part = parts.pop(0)
                    object_ = getattr(object_, part)
                value = value(object_)
            music_specifier = new(
                music_specifier,
                key=value,
                )
            timespan_inventory.remove(timespan)
            timespan = new(
                timespan,
                music_specifier=music_specifier,
                )
            timespan_inventory.append(timespan)

    def _is_applicable_timespan(
        self,
        segment_duration=None,
        timespan=None,
        ):
        return True

    ### PUBLIC PROPERTIES ###

    @property
    def context_identifier(self):
        return self._context_identifier

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value
