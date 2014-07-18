# -*- encoding: utf-8 -*-
from abjad.tools import timespantools
from abjad.tools.topleveltools import new
from consort.makers.MusicSetting import MusicSetting


class MusicTransform(MusicSetting):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_transforms',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        color=None,
        timespan_identifier=None,
        voice_identifier=None,
        **kwargs
        ):
        MusicSetting.__init__(
            self,
            color=color,
            timespan_identifier=timespan_identifier,
            voice_identifier=voice_identifier,
            )
        self._transforms = dict(kwargs)

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer,
        score_template,
        target_timespan,
        timespan_inventory=None,
        ):
        from consort import makers
        target_timespans, voice_names, timespan_inventory = \
            MusicSetting.__call__(
                self,
                layer,
                score_template,
                target_timespan,
                timespan_inventory,
                )
        for target_timespan in target_timespans:
            inequality = timespantools.timespan_2_intersects_timespan_1(
                timespan_1=target_timespan,
                )
            intersecting_timespans = []
            for timespan in timespan_inventory:
                if not isinstance(timespan, makers.PerformedTimespan):
                    continue
                if not inequality(timespan_2=timespan):
                    continue
                if self.color and timespan.color != self.color:
                    continue
                intersecting_timespans.append(timespan)
            for timespan in intersecting_timespans:
                timespan_inventory.remove(timespan)
                music_specifier = timespan.music_specifier
                transformed_music_specifier = self._transform_music_specifier(
                    music_specifier)
                timespan = new(timespan,
                    layer=layer,
                    music_specifier=transformed_music_specifier,
                    )
                timespan_inventory.append(timespan)
        timespan_inventory.sort()
        return timespan_inventory

    def __getattr__(self, name):
        if name in self._transforms:
            return self._transforms[name]
        return object.__getattr__(self, name)

    ### PRIVATE PROPERTIES ###

    def _transform_music_specifier(self, music_specifier):
        from consort import makers
        kwargs = {}
        for key, value in self.transforms.items():
            if isinstance(value, makers.Transform):
                parts = key.split('__')
                object_ = music_specifier
                while parts:
                    part = parts.pop(0)
                    object_ = getattr(object_, part)
                value = value(object_)
            kwargs[key] = value
        music_specifier = new(
            music_specifier,
            **kwargs
            )
        return music_specifier

    ### PUBLIC PROPERTIES ###

    @property
    def transforms(self):
        return self.transforms.copy()