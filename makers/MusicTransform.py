# -*- encoding: utf-8 -*-
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
        target_duration,
        timespan_inventory,
        ):
        voice_names = MusicSetting.__call__(
            layer,
            score_template,
            target_duration,
            timespan_inventory,
            )


    def __getattr__(self, name):
        if name in self._transforms:
            return self._transforms[name]
        return object.__getattr__(self, name)

    ### PUBLIC PROPERTIES ###

    @property
    def transforms(self):
        return self.transforms.copy()
