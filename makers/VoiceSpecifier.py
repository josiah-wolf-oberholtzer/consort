# -*- encoding: utf-8 -*-
import re
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import timespantools
from abjad.tools.topleveltools import iterate


class VoiceSpecifier(abctools.AbjadObject):
    r'''A context specifier.

    ::

        >>> from consort import makers
        >>> voice_specifier = makers.VoiceSpecifier(
        ...     music_specifier=makers.MusicSpecifier(),
        ...     timespan_maker=makers.TimespanMaker(
        ...         initial_silence_durations=(
        ...             durationtools.Duration(0, 1),
        ...             durationtools.Duration(1, 4),
        ...             ),
        ...         playing_durations=(
        ...             durationtools.Duration(1, 4),
        ...             durationtools.Duration(1, 2),
        ...             durationtools.Duration(1, 4),
        ...             ),
        ...         ),
        ...     voice_identifiers=('Violin \\d+ LH Voice', 'Viola LH Voice'),
        ...     )
        >>> print format(voice_specifier)
        makers.VoiceSpecifier(
            music_specifier=makers.MusicSpecifier(),
            timespan_maker=makers.TimespanMaker(
                can_shift=False,
                can_split=False,
                initial_silence_durations=(
                    durationtools.Duration(0, 1),
                    durationtools.Duration(1, 4),
                    ),
                minimum_duration=durationtools.Duration(1, 8),
                playing_durations=(
                    durationtools.Duration(1, 4),
                    durationtools.Duration(1, 2),
                    durationtools.Duration(1, 4),
                    ),
                playing_groupings=(1,),
                repeat=True,
                silence_durations=(
                    durationtools.Duration(1, 4),
                    ),
                step_anchor=Right,
                synchronize_groupings=False,
                synchronize_step=False,
                ),
            voice_identifiers=('Violin \\d+ LH Voice', 'Viola LH Voice'),
            )

    ::

        >>> from consort import templates
        >>> template = templates.ConsortScoreTemplate(
        ...     violin_count=2,
        ...     viola_count=1,
        ...     cello_count=1,
        ...     contrabass_count=1,
        ...     )
        >>> voice_specifier.find_voice_names(template=template)
        ('Violin 1 LH Voice', 'Violin 2 LH Voice', 'Viola LH Voice')

    ::

        >>> layer = 1
        >>> target_duration = durationtools.Duration(1)
        >>> timespan_inventory, final_duration = voice_specifier(
        ...     layer=layer,
        ...     target_duration=target_duration,
        ...     template=template,
        ...     )

    ::

        >>> print final_duration
        1

    ::

        >>> print format(timespan_inventory)
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Violin 1 LH Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Viola LH Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Violin 2 LH Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin 1 LH Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin 2 LH Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola LH Voice',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_music_specifier',
        '_timespan_maker',
        '_voice_identifiers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        music_specifier=None,
        timespan_maker=None,
        voice_identifiers=None,
        ):
        from consort import makers
        assert isinstance(music_specifier, makers.MusicSpecifier)
        self._music_specifier = music_specifier
        assert isinstance(timespan_maker, makers.TimespanMaker)
        self._timespan_maker = timespan_maker
        if isinstance(voice_identifiers, str):
            voice_identifiers = (voice_identifiers,)
        assert isinstance(voice_identifiers, tuple)
        assert len(voice_identifiers)
        assert all(isinstance(x, str) for x in voice_identifiers)
        self._voice_identifiers = voice_identifiers

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer=None,
        target_duration=None,
        template=None,
        ):
        if layer is None:
            layer = 0
        layer = int(layer)
        target_duration = durationtools.Duration(target_duration)
        assert 0 < target_duration
        assert template is not None
        voice_names = self.find_voice_names(
            template=template,
            )
        timespan_inventory, final_offset = self.timespan_maker(
            layer=layer,
            music_specifier=self.music_specifier,
            target_duration=target_duration,
            voice_names=voice_names,
            )
        return timespan_inventory, final_offset

    ### PUBLIC METHODS ###

    def find_voice_names(
        self,
        template=None,
        ):
        score = template()
        all_voice_names = [voice.name for voice in
            iterate(score).by_class(scoretools.Voice)]
        matched_voice_names = set()
        for voice_identifier in self.voice_identifiers:
            pattern = re.compile(voice_identifier)
            for voice_name in all_voice_names:
                match = pattern.match(voice_name)
                if match:
                    matched_voice_names.add(voice_name)
        selected_voice_names = []
        for voice_name in all_voice_names:
            if voice_name in matched_voice_names:
                selected_voice_names.append(voice_name)
        selected_voice_names = tuple(selected_voice_names)
        return selected_voice_names

    ### PUBLIC PROPERTIES ###

    @property
    def music_specifier(self):
        return self._music_specifier

    @property
    def timespan_maker(self):
        return self._timespan_maker

    @property
    def voice_identifiers(self):
        return self._voice_identifiers
