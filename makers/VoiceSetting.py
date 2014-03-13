# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools.topleveltools import new


class VoiceSetting(abctools.AbjadObject):
    r'''A voice setting.

    ::

        >>> from consort import makers
        >>> voice_setting = makers.VoiceSetting(
        ...     voice_identifiers=r'Violin \d+ LH Voice',
        ...     key='rhythm_maker',
        ...     value=rhythmmakertools.NoteRhythmMaker(),
        ...     )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_voice_identifiers',
        '_key',
        '_value',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        voice_identifiers=None,
        key=None,
        value=None,
        ):
        if voice_identifiers is not None:
            if isinstance(voice_identifiers, str):
                voice_identifiers = (voice_identifiers,)
            if not isinstance(voice_identifiers, tuple):
                voice_identifiers = tuple(voice_identifiers)
        self._voice_identifiers = voice_identifiers
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
        voice_names = makers.ConsortSegmentMaker.find_voice_names(
            template=template,
            voice_identifiers=self.voice_identifiers,
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
    def voice_identifiers(self):
        return self._voice_identifiers

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value