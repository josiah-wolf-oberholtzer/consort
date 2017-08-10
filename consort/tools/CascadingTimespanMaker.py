import abjad
import collections
from abjad.tools import rhythmmakertools
from consort.tools.TimespanMaker import TimespanMaker


class CascadingTimespanMaker(TimespanMaker):
    """
    A cascading timespan maker.

    ::

        >>> timespan_maker = consort.CascadingTimespanMaker()
        >>> print(format(timespan_maker))
        consort.tools.CascadingTimespanMaker(
            cascade_pattern=(1,),
            playing_talea=rhythmmakertools.Talea(
                counts=[4],
                denominator=16,
                ),
            playing_groupings=(1,),
            repeat=True,
            silence_talea=rhythmmakertools.Talea(
                counts=[4],
                denominator=16,
                ),
            )

    ::

        >>> import collections
        >>> music_specifiers = collections.OrderedDict([
        ...     ('A', None),
        ...     ('B', None),
        ...     ('C', None),
        ...     ('D', None),
        ...     ])
        >>> target_timespan = abjad.Timespan(0, 2)
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 4),
                    stop_offset=abjad.Offset(1, 2),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(1, 1),
                    voice_name='D',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(5, 4),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(5, 4),
                    stop_offset=abjad.Offset(3, 2),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 2),
                    stop_offset=abjad.Offset(7, 4),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 4),
                    stop_offset=abjad.Offset(2, 1),
                    voice_name='D',
                    ),
                ]
            )

    ::

        >>> timespan_maker = abjad.new(
        ...     timespan_maker,
        ...     playing_groupings=(1, 2),
        ...     cascade_pattern=(2, -1),
        ...     )
        >>> timespan_inventory = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> print(format(timespan_inventory))
        abjad.TimespanList(
            [
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(0, 1),
                    stop_offset=abjad.Offset(1, 4),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 4),
                    stop_offset=abjad.Offset(3, 4),
                    original_stop_offset=abjad.Offset(1, 2),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 2),
                    stop_offset=abjad.Offset(3, 4),
                    voice_name='B',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 4),
                    stop_offset=abjad.Offset(5, 4),
                    original_stop_offset=abjad.Offset(1, 1),
                    voice_name='D',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(1, 1),
                    stop_offset=abjad.Offset(5, 4),
                    voice_name='C',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(5, 4),
                    stop_offset=abjad.Offset(7, 4),
                    original_stop_offset=abjad.Offset(3, 2),
                    voice_name='A',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(3, 2),
                    stop_offset=abjad.Offset(7, 4),
                    voice_name='D',
                    ),
                consort.tools.PerformedTimespan(
                    start_offset=abjad.Offset(7, 4),
                    stop_offset=abjad.Offset(2, 1),
                    voice_name='B',
                    ),
                ]
            )


    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_cascade_pattern',
        '_fuse_groups',
        '_playing_talea',
        '_playing_groupings',
        '_repeat',
        '_silence_talea',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        cascade_pattern=(1,),
        division_masks=None,
        fuse_groups=None,
        padding=None,
        playing_talea=rhythmmakertools.Talea(
            counts=[4],
            denominator=16,
            ),
        playing_groupings=(1,),
        seed=None,
        repeat=True,
        silence_talea=rhythmmakertools.Talea(
            counts=[4],
            denominator=16,
            ),
        timespan_specifier=None,
        ):
        TimespanMaker.__init__(
            self,
            division_masks=division_masks,
            padding=padding,
            seed=seed,
            timespan_specifier=timespan_specifier,
            )
        self._initialize_cascade_pattern(cascade_pattern)
        self._initialize_fuse_groups(fuse_groups)
        self._initialize_playing_talea(playing_talea)
        self._initialize_playing_groupings(playing_groupings)
        self._initialize_repeat(repeat)
        self._initialize_silence_talea(silence_talea)

    ### PRIVATE METHODS ###

    def _initialize_cascade_pattern(self, cascade_pattern):
        if not isinstance(cascade_pattern, collections.Sequence):
            cascade_pattern = (cascade_pattern,)
        cascade_pattern = tuple(int(_) for _ in cascade_pattern)
        assert all(_ != 0 for _ in cascade_pattern)
        self._cascade_pattern = cascade_pattern

    def _initialize_fuse_groups(self, fuse_groups):
        if fuse_groups is not None:
            fuse_groups = bool(fuse_groups)
        self._fuse_groups = fuse_groups

    def _initialize_playing_talea(self, playing_talea):
        assert isinstance(playing_talea, rhythmmakertools.Talea)
        assert playing_talea.counts
        assert all(0 < x for x in playing_talea.counts)
        self._playing_talea = playing_talea

    def _initialize_repeat(self, repeat):
        if repeat is not None:
            repeat = bool(repeat)
        self._repeat = repeat

    def _initialize_silence_talea(self, silence_talea):
        assert isinstance(silence_talea, rhythmmakertools.Talea)
        assert silence_talea.counts
        assert all(0 <= x for x in silence_talea.counts)
        self._silence_talea = silence_talea

    def _initialize_playing_groupings(self, playing_groupings):
        if not isinstance(playing_groupings, collections.Sequence):
            playing_groupings = (playing_groupings,)
        playing_groupings = tuple(int(x) for x in playing_groupings)
        assert len(playing_groupings)
        assert all(0 < x for x in playing_groupings)
        self._playing_groupings = playing_groupings

    def _make_timespans(
        self,
        layer=None,
        music_specifiers=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        import consort
        # setup state
        context_names = abjad.CyclicTuple(music_specifiers)
        context_index = self.seed or 0
        cascade_pattern = self.cascade_pattern
        playing_talea = consort.Cursor(self.playing_talea)
        playing_groupings = consort.Cursor(self.playing_groupings)
        silence_talea = consort.Cursor(self.silence_talea)
        if self.seed is not None and 0 < self.seed:
            for _ in range(self.seed):
                next(playing_talea)
                next(playing_groupings)
                next(silence_talea)
        context_seeds = collections.Counter()
        timespan_inventory = abjad.TimespanList()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        can_continue = True
        division_mask_seed = 0
        # start the engine
        new_timespan_mapping = {}
        while start_offset < stop_offset and can_continue:
            for cascade_step in cascade_pattern:
                context_name = context_names[context_index]
                music_specifier = music_specifiers[context_name]
                grouping = next(playing_groupings)
                valid_durations = []
                for duration in (next(playing_talea) for _ in range(grouping)):
                    offset = start_offset + duration + sum(valid_durations)
                    if stop_offset < offset:
                        playing_talea.backtrack()
                        break
                    valid_durations.append(duration)
                if self.fuse_groups:
                    valid_durations = [sum(valid_durations)]
                new_timespans = music_specifier(
                    durations=valid_durations,
                    layer=layer,
                    division_masks=self.division_masks,
                    padding=self.padding,
                    seed=context_seeds[context_name],
                    division_mask_seed=division_mask_seed,
                    start_offset=start_offset,
                    timespan_specifier=self.timespan_specifier,
                    voice_name=context_name,
                    )
                if all(isinstance(_, consort.SilentTimespan)
                    for _ in new_timespans):
                    new_timespans[:] = []
                if context_name not in new_timespan_mapping:
                    new_timespan_mapping[context_name] = \
                        abjad.TimespanList()
                new_timespan_mapping[context_name].extend(new_timespans)
                context_index += cascade_step
                context_seeds[context_name] += 1
                division_mask_seed += 1
                start_offset += next(silence_talea)
                if not can_continue:
                    break
            if not self.repeat:
                if len(music_specifiers) == len(new_timespan_mapping):
                    # dangerous...
                    break
        for context_name, timespans in new_timespan_mapping.items():
            timespans.compute_logical_or()
            timespan_inventory.extend(timespans)
        return timespan_inventory

    ### PUBLIC PROPERTIES ###

    @property
    def cascade_pattern(self):
        return self._cascade_pattern

    @property
    def fuse_groups(self):
        return self._fuse_groups

    @property
    def playing_groupings(self):
        return self._playing_groupings

    @property
    def playing_talea(self):
        return self._playing_talea

    @property
    def repeat(self):
        return self._repeat

    @property
    def silence_talea(self):
        return self._silence_talea
