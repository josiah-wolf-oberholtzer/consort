import abjad
import collections
from consort.tools.HashCachingObject import HashCachingObject


class CompositeMusicSpecifier(HashCachingObject):
    r'''A composite music specifier.

    ::

        >>> music_specifier = consort.CompositeMusicSpecifier(
        ...     primary_music_specifier='one',
        ...     primary_voice_name='Viola 1 RH',
        ...     rotation_indices=(0, 1, -1),
        ...     secondary_voice_name='Viola 1 LH',
        ...     secondary_music_specifier=consort.MusicSpecifierSequence(
        ...         application_rate='phrase',
        ...         music_specifiers=('two', 'three', 'four'),
        ...         ),
        ...     )
        >>> print(format(music_specifier))
        consort.tools.CompositeMusicSpecifier(
            primary_music_specifier=consort.tools.MusicSpecifierSequence(
                music_specifiers=('one',),
                ),
            primary_voice_name='Viola 1 RH',
            rotation_indices=(0, 1, -1),
            secondary_music_specifier=consort.tools.MusicSpecifierSequence(
                application_rate='phrase',
                music_specifiers=('two', 'three', 'four'),
                ),
            secondary_voice_name='Viola 1 LH',
            )

    ::

        >>> durations = [1, 2]
        >>> timespans = music_specifier(
        ...     durations=durations,
        ...     layer=1,
        ...     )
        >>> print(format(timespans))
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 1),
                    layer=1,
                    music_specifier='two',
                    voice_name='Viola 1 LH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 1),
                    layer=1,
                    music_specifier='one',
                    voice_name='Viola 1 RH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=1,
                    music_specifier='two',
                    voice_name='Viola 1 LH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=1,
                    music_specifier='one',
                    voice_name='Viola 1 RH',
                    ),
                ]
            )

    ::

        >>> durations = [1, 2]
        >>> timespans = music_specifier(
        ...     durations=durations,
        ...     layer=2,
        ...     seed=1,
        ...     )
        >>> print(format(timespans))
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 1),
                    layer=2,
                    music_specifier='one',
                    voice_name='Viola 1 RH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(2, 1),
                    layer=2,
                    music_specifier='three',
                    voice_name='Viola 1 LH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=2,
                    music_specifier='one',
                    voice_name='Viola 1 RH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(2, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=2,
                    music_specifier='three',
                    voice_name='Viola 1 LH',
                    ),
                ]
            )

    ::

        >>> durations = [1, 2]
        >>> timespans = music_specifier(
        ...     durations=durations,
        ...     layer=3,
        ...     padding=1,
        ...     seed=2,
        ...     )
        >>> print(format(timespans))
        abjad.TimespanList(
            [
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 1),
                    stop_offset=abjad.Offset(0, 1),
                    layer=3,
                    voice_name='Viola 1 RH',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(-1, 1),
                    stop_offset=abjad.Offset(0, 1),
                    layer=3,
                    voice_name='Viola 1 LH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 1),
                    layer=3,
                    music_specifier='one',
                    voice_name='Viola 1 RH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(2, 1),
                    layer=3,
                    music_specifier='four',
                    voice_name='Viola 1 LH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=3,
                    music_specifier='one',
                    voice_name='Viola 1 RH',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(2, 1),
                    stop_offset=abjad.Offset(3, 1),
                    layer=3,
                    music_specifier='four',
                    voice_name='Viola 1 LH',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 1),
                    stop_offset=abjad.Offset(4, 1),
                    layer=3,
                    voice_name='Viola 1 RH',
                    ),
                consort.tools.SilentTimespan(
                    start_offset=abjad.Offset(3, 1),
                    stop_offset=abjad.Offset(4, 1),
                    layer=3,
                    voice_name='Viola 1 LH',
                    ),
                ]
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_discard_inner_offsets',
        '_primary_music_specifier',
        '_primary_voice_name',
        '_rotation_indices',
        '_secondary_music_specifier',
        '_secondary_voice_name',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        discard_inner_offsets=None,
        primary_music_specifier=None,
        primary_voice_name=None,
        rotation_indices=None,
        secondary_music_specifier=None,
        secondary_voice_name=None,
        ):
        import consort
        HashCachingObject.__init__(self)
        prototype = consort.MusicSpecifierSequence
        if discard_inner_offsets is not None:
            discard_inner_offsets = bool(discard_inner_offsets)
        self._discard_inner_offsets = discard_inner_offsets
        if not isinstance(primary_music_specifier, prototype):
            primary_music_specifier = consort.MusicSpecifierSequence(
                music_specifiers=primary_music_specifier,
                )
        self._primary_music_specifier = primary_music_specifier
        if primary_voice_name is not None:
            primary_voice_name = str(primary_voice_name)
        self._primary_voice_name = primary_voice_name
        if rotation_indices is not None:
            if not isinstance(rotation_indices, collections.Sequence):
                rotation_indices = int(rotation_indices)
                rotation_indices = (rotation_indices,)
            rotation_indices = tuple(rotation_indices)
        self._rotation_indices = rotation_indices
        if not isinstance(secondary_music_specifier, prototype):
            secondary_music_specifier = consort.MusicSpecifierSequence(
                music_specifiers=secondary_music_specifier,
                )
        self._secondary_music_specifier = secondary_music_specifier
        if secondary_voice_name is not None:
            secondary_voice_name = str(secondary_voice_name)
        self._secondary_voice_name = secondary_voice_name

    ### PUBLIC METHODS ###

    def __call__(
        self,
        durations=None,
        layer=None,
        division_masks=None,
        division_mask_seed=None,
        padding=None,
        seed=None,
        start_offset=None,
        timespan_specifier=None,
        voice_name=None,
        ):
        import consort
        seed = seed or 0
        rotation_indices = self.rotation_indices or (0,)
        rotation_indices = abjad.CyclicTuple(rotation_indices)
        primary_durations = durations
        start_offset = start_offset or 0
        if self.discard_inner_offsets:
            secondary_durations = [sum(primary_durations)]
        else:
            secondary_durations = consort.rotate(
                primary_durations,
                rotation_indices[seed],
                )
        primary_timespans = self.primary_music_specifier(
            durations=primary_durations,
            layer=layer,
            division_masks=division_masks,
            division_mask_seed=division_mask_seed,
            padding=padding,
            seed=seed,
            start_offset=start_offset,
            timespan_specifier=timespan_specifier,
            voice_name=self.primary_voice_name,
            )
        secondary_timespans = self.secondary_music_specifier(
            durations=secondary_durations,
            layer=layer,
            division_masks=division_masks,
            division_mask_seed=division_mask_seed,
            padding=padding,
            seed=seed,
            start_offset=start_offset,
            timespan_specifier=timespan_specifier,
            voice_name=self.secondary_voice_name,
            )
        timespans = primary_timespans[:] + secondary_timespans[:]
        timespans = abjad.TimespanList(timespans)
        timespans.sort()
        return timespans

    ### PUBLIC PROPERTIES ###

    @property
    def discard_inner_offsets(self):
        return self._discard_inner_offsets

    @property
    def primary_music_specifier(self):
        return self._primary_music_specifier

    @property
    def primary_voice_name(self):
        return self._primary_voice_name

    @property
    def rotation_indices(self):
        return self._rotation_indices

    @property
    def secondary_music_specifier(self):
        return self._secondary_music_specifier

    @property
    def secondary_voice_name(self):
        return self._secondary_voice_name
