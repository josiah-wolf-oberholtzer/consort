# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject
from abjad.tools.topleveltools import new


class MusicSpecifierTransform(ConsortObject):
    r'''A voice setting.

    ::

        >>> from consort import makers
        >>> voice_setting = makers.MusicSpecifierTransform(
        ...     key='rhythm_maker',
        ...     value=rhythmmakertools.NoteRhythmMaker(),
        ...     )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_key',
        '_value',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        key=None,
        value=None,
        ):
        self._key = key
        self._value = value

    ### SPECIAL METHODS ###

    def __call__(
        self,
        segment_duration=None,
        template=None,
        voicewise_timespans=None,
        ):
        from consort import makers
        voice_names = makers.SegmentMaker._find_voice_names(
            template=template,
            voice_identifier=self.voice_identifier,
            )
        for voice_name in voice_names:
            if voice_name not in voicewise_timespans:
                continue
            timespan_inventory = voicewise_timespans[voice_name]
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
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value
