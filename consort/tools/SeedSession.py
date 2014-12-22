# -*- encoding: utf-8 -*-
from abjad import abctools


class SeedSession(abctools.AbjadObject):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_current_timewise_logical_tie_seed',
        '_current_timewise_phrase_seed',
        '_current_voicewise_logical_tie_seed',
        '_current_timewise_music_specifier_seed',
        '_timewise_logical_tie_seeds',
        '_timewise_music_specifier_seeds',
        '_timewise_phrase_seeds',
        '_voicewise_logical_tie_seeds',
        )

    ### INITIALIZER ###

    def __init__(self):
        self._current_timewise_logical_tie_seed = 0
        self._current_timewise_phrase_seed = 0
        self._current_voicewise_logical_tie_seed = 0
        self._current_timewise_music_specifier_seed = 0
        self._timewise_music_specifier_seeds = {}
        self._timewise_logical_tie_seeds = {}
        self._timewise_phrase_seeds = {}
        self._voicewise_logical_tie_seeds = {}

    ### SPECIAL METHODS ###

    def __call__(
        self,
        application_rate,
        attack_point_signature,
        music_specifier,
        voice,
        ):
        voicewise_logical_tie_seed = self._get_voicewise_logical_tie_seed(
            attack_point_signature,
            music_specifier,
            application_rate,
            voice,
            )
        timewise_phrase_seed = self._get_timewise_phrase_seed(
            attack_point_signature,
            music_specifier,
            voice,
            )
        timewise_music_specifier_seed = \
            self._get_timewise_music_specifier_seed(
                music_specifier,
                )
        self._current_timewise_phrase_seed = timewise_phrase_seed
        self._current_voicewise_logical_tie_seed = voicewise_logical_tie_seed
        self._current_timewise_music_specifier_seed = \
            timewise_music_specifier_seed

    ### PRIVATE METHODS ###

    def _get_timewise_music_specifier_seed(
        self,
        music_specifier,
        ):
        if music_specifier not in self._timewise_music_specifier_seeds:
            self._timewise_music_specifier_seeds[music_specifier] = 0
        seed = self._timewise_music_specifier_seeds[music_specifier]
        self._timewise_music_specifier_seeds[music_specifier] += 1
        return seed

    def _get_timewise_phrase_seed(
        self,
        attack_point_signature,
        music_specifier,
        voice,
        ):
        key = (voice, music_specifier)
        if attack_point_signature.is_first_of_phrase:
            if key not in self._timewise_phrase_seeds:
                phrase_seed = (music_specifier.seed or 0) - 1
                self._timewise_phrase_seeds[key] = phrase_seed
            self._timewise_phrase_seeds[key] += 1
        phrase_seed = self._timewise_phrase_seeds[key]
        return phrase_seed

    def _get_voicewise_logical_tie_seed(
        self,
        attack_point_signature,
        music_specifier,
        application_rate,
        voice,
        ):
        if music_specifier not in self._timewise_logical_tie_seeds:
            seed = (music_specifier.seed or 0) - 1
            self._timewise_logical_tie_seeds[music_specifier] = seed
            self._voicewise_logical_tie_seeds[voice] = seed
        if application_rate == 'phrase':
            if attack_point_signature.is_first_of_phrase:
                self._timewise_logical_tie_seeds[music_specifier] += 1
                seed = self._timewise_logical_tie_seeds[music_specifier]
                self._voicewise_logical_tie_seeds[voice] = seed
            else:
                seed = self._voicewise_logical_tie_seeds[voice]
        elif application_rate == 'division':
            if attack_point_signature.is_first_of_division:
                self._timewise_logical_tie_seeds[music_specifier] += 1
                seed = self._timewise_logical_tie_seeds[music_specifier]
                self._voicewise_logical_tie_seeds[voice] = seed
            else:
                seed = self._voicewise_logical_tie_seeds[voice]
        else:
            self._timewise_logical_tie_seeds[music_specifier] += 1
            seed = self._timewise_logical_tie_seeds[music_specifier]
        return seed

    ### PUBLIC PROPERTIES ###

    @property
    def current_timewise_music_specifier_seed(self):
        return self._current_timewise_music_specifier_seed

    @property
    def current_timewise_phrase_seed(self):
        return self._current_timewise_phrase_seed

    @property
    def current_voicewise_logical_tie_seed(self):
        return self._current_voicewise_logical_tie_seed