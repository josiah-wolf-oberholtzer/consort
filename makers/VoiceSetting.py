# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject
from abjad.tools.topleveltools import new


class VoiceSetting(ConsortObject):
    r'''A voice setting.

    ::

        >>> from consort import makers
        >>> voice_setting = makers.VoiceSetting(
        ...     voice_identifier=r'Violin \d+ LH Voice',
        ...     key='rhythm_maker',
        ...     value=rhythmmakertools.NoteRhythmMaker(),
        ...     )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_color',
        '_key',
        '_value',
        '_voice_identifiers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        color=None,
        key=None,
        value=None,
        voice_identifier=None,
        ):
        if voice_identifier is not None:
            if isinstance(voice_identifier, str):
                voice_identifier = (voice_identifier,)
            if not isinstance(voice_identifier, tuple):
                voice_identifier = tuple(voice_identifier)
        self._voice_identifiers = voice_identifier
        if color is not None:
            color = str(color)
        self._color = color
        self._key = key
        self._value = value

    ### SPECIAL METHODS ###

    def __call__(
        self,
        segment_duration=None,
        template=None,
        timespan_inventory_mapping=None,
        ):
        from consort import makers
        voice_names = makers.ConsortSegmentMaker._find_voice_names(
            template=template,
            voice_identifier=self.voice_identifier,
            )
        for voice_name in voice_names:
            if voice_name not in timespan_inventory_mapping:
                continue
            timespan_inventory = timespan_inventory_mapping[voice_name]
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
            kwargs = {key: value}
            music_specifier = new(
                music_specifier,
                **kwargs
                )
            timespan_inventory.remove(timespan)
            timespan = new(
                timespan,
                music_specifier=music_specifier,
                )
            timespan_inventory.append(timespan)
        timespan_inventory.sort()

    def _is_applicable_timespan(
        self,
        segment_duration=None,
        timespan=None,
        ):
        if self.color is not None:
            return self.color == timespan.color
        return True

    ### PUBLIC PROPERTIES ###

    @property
    def color(self):
        return self._color

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def voice_identifier(self):
        return self._voice_identifiers