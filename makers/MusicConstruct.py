# -*- encoding: utf-8 -*-
from consort.makers.MusicSetting import MusicSetting


class MusicConstruct(MusicSetting):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_music_specifier',
        '_timespan_maker',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        color=None,
        music_specifier=None,
        timespan_identifier=None,
        timespan_maker=None,
        voice_identifier=None,
        ):
        MusicSetting.__init__(
            self,
            color=color,
            timespan_identifier=timespan_identifier,
            voice_identifier=voice_identifier,
            )
        assert isinstance(music_specifier, makers.MusicSpecifier)
        self._music_specifier = music_specifier
        assert isinstance(timespan_maker, makers.TimespanMaker)
        self._timespan_maker = timespan_maker

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer,
        score_template,
        target_duration,
        timespan_inventory,
        ):
        target_timespans, voice_names = MusicSetting.__call__(
            layer,
            score_template,
            target_duration,
            timespan_inventory,
            )
        timespan_inventory = self.timespan_maker(
            color=self.color,
            layer=layer,
            music_specifier=self.music_specifier,
            target_duration=target_duration,
            timespan_inventory=timespan_inventory,
            voice_names=voice_names,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def music_specifier(self):
        return self._music_specifier

    @property
    def timespan_maker(self):
        return self._timespan_maker

