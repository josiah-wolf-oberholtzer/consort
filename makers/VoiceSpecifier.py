# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import durationtools


class VoiceSpecifier(ConsortObject):
    r'''A voice specifier.

    Voice specifiers bundle three things:

    - a music specifier
    - a timespan maker
    - a sequence of voice identifiers

    They represent the complete logic for how a collection of timespans should
    be arranged in time, on what voices, with what music specifiers to
    inscribe them with.

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
        ...     voice_identifiers=(
        ...         'Violin \\d+ Bowing Voice',
        ...         'Viola Bowing Voice',
        ...         ),
        ...     )
        >>> print(format(voice_specifier))
        makers.VoiceSpecifier(
            music_specifier=makers.MusicSpecifier(),
            timespan_maker=makers.TimespanMaker(
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
            voice_identifiers=(
                'Violin \\d+ Bowing Voice',
                'Viola Bowing Voice',
                ),
            )

    ::


        >>> layer = 1
        >>> target_duration = durationtools.Duration(1)
        >>> score_template = makers.ConsortScoreTemplate(
        ...     violin_count=2,
        ...     viola_count=1,
        ...     cello_count=1,
        ...     contrabass_count=1,
        ...     )
        >>> timespan_inventory, final_duration = voice_specifier(
        ...     layer=layer,
        ...     target_duration=target_duration,
        ...     score_template=score_template,
        ...     )

    ::

        >>> print(final_duration)
        1

    ::

        >>> print(format(timespan_inventory))
        timespantools.TimespanInventory(
            [
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 4),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(0, 1),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Viola Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 4),
                    stop_offset=durationtools.Offset(1, 2),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(1, 2),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin 1 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Violin 2 Bowing Voice',
                    ),
                makers.PerformedTimespan(
                    layer=1,
                    minimum_duration=durationtools.Duration(1, 8),
                    music_specifier=makers.MusicSpecifier(),
                    start_offset=durationtools.Offset(3, 4),
                    stop_offset=durationtools.Offset(1, 1),
                    voice_name='Viola Bowing Voice',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_color',
        '_music_specifier',
        '_timespan_maker',
        '_voice_identifiers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        color=None,
        music_specifier=None,
        timespan_maker=None,
        voice_identifiers=None,
        ):
        from consort import makers
        if color is not None:
            color = str(color)
        self._color = color
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
        score_template=None,
        ):
        from consort import makers
        if layer is None:
            layer = 0
        layer = int(layer)
        target_duration = durationtools.Duration(target_duration)
        assert 0 < target_duration
        assert score_template is not None
        voice_names = makers.ConsortSegmentMaker._find_voice_names(
            score_template=score_template,
            voice_identifiers=self.voice_identifiers,
            )
        assert voice_names, voice_names
        timespan_inventory, final_offset = self.timespan_maker(
            color=self.color,
            layer=layer,
            music_specifier=self.music_specifier,
            target_duration=target_duration,
            voice_names=voice_names,
            )
        return timespan_inventory, final_offset

    ### PUBLIC PROPERTIES ###

    @property
    def color(self):
        return self._color

    @property
    def music_specifier(self):
        return self._music_specifier

    @property
    def timespan_maker(self):
        return self._timespan_maker

    @property
    def voice_identifiers(self):
        return self._voice_identifiers