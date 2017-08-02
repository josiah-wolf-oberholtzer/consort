import abjad
import collections
from abjad.tools import abctools
from abjad.tools import mathtools
from abjad.tools import rhythmmakertools


class MusicSpecifierSequence(abctools.AbjadValueObject):
    r'''A music specifier sequence.

    ::

        >>> sequence_a = consort.MusicSpecifierSequence(
        ...     music_specifiers='music',
        ...     )
        >>> print(format(sequence_a))
        consort.tools.MusicSpecifierSequence(
            music_specifiers=('music',),
            )

    ::

        >>> sequence_b = consort.MusicSpecifierSequence(
        ...     application_rate='phrase',
        ...     music_specifiers=['one', 'two', 'three'],
        ...     )
        >>> print(format(sequence_b))
        consort.tools.MusicSpecifierSequence(
            application_rate='phrase',
            music_specifiers=('one', 'two', 'three'),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_application_rate',
        '_music_specifiers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        application_rate=None,
        music_specifiers=None,
        ):
        if application_rate is not None:
            application_rate = application_rate or 'phrase'
            assert application_rate in ('division', 'phrase')
        if music_specifiers is None:
            music_specifiers = [None]
        if not isinstance(music_specifiers, collections.Sequence) or \
            isinstance(music_specifiers, str):
            music_specifiers = [music_specifiers]
        music_specifiers = tuple(music_specifiers)
        #music_specifiers = abjad.CyclicTuple(music_specifiers)
        assert len(music_specifiers)
        self._application_rate = application_rate
        self._music_specifiers = music_specifiers

    ### SPECIAL METHODS ###

    def __call__(
        self,
        durations=None,
        layer=None,
        division_mask_seed=0,
        division_masks=None,
        padding=None,
        seed=None,
        start_offset=None,
        timespan_specifier=None,
        voice_name=None,
        ):
        import consort
        timespans = abjad.TimespanList()
        timespan_specifier = timespan_specifier or \
            consort.TimespanSpecifier()
        seed = seed or 0
        division_mask_seed = division_mask_seed or 0
        durations = [_ for _ in durations if _]
        offsets = mathtools.cumulative_sums(durations, start_offset)
        if not offsets:
            return timespans
        offset_pair_count = len(offsets) - 1
        if offset_pair_count == 1:
            offset_pair_count = 2  # make patterns happy
        iterator = consort.iterate_nwise(offsets)
        for i, offset_pair in enumerate(iterator):
            start_offset, stop_offset = offset_pair
            music_specifier = self[seed % len(self)]
            timespan = consort.PerformedTimespan(
                forbid_fusing=timespan_specifier.forbid_fusing,
                forbid_splitting=timespan_specifier.forbid_splitting,
                layer=layer,
                minimum_duration=timespan_specifier.minimum_duration,
                music_specifier=music_specifier,
                start_offset=start_offset,
                stop_offset=stop_offset,
                voice_name=voice_name,
                )
            if not division_masks:
                timespans.append(timespan)
            else:
                output_mask = division_masks.get_matching_pattern(
                    i, offset_pair_count + 1, rotation=division_mask_seed)
                if output_mask is None:
                    timespans.append(timespan)
                elif isinstance(output_mask, rhythmmakertools.SustainMask):
                    timespans.append(timespan)
                elif isinstance(output_mask, rhythmmakertools.SilenceMask):
                    pass
            division_mask_seed += 1
            if self.application_rate == 'division':
                seed += 1

        if padding:
            silent_timespans = abjad.TimespanList()
            for shard in timespans.partition(True):
                silent_timespan_one = consort.SilentTimespan(
                    layer=layer,
                    start_offset=shard.start_offset - padding,
                    stop_offset=shard.start_offset,
                    voice_name=voice_name,
                    )
                silent_timespans.append(silent_timespan_one)
                silent_timespan_two = consort.SilentTimespan(
                    layer=layer,
                    start_offset=shard.stop_offset,
                    stop_offset=shard.stop_offset + padding,
                    voice_name=voice_name,
                    )
                silent_timespans.append(silent_timespan_two)
            silent_timespans.compute_logical_or()
            for timespan in timespans:
                silent_timespans - timespan
            timespans.extend(silent_timespans)
            timespans.sort()

        return timespans

    def __getitem__(self, item):
        return self._music_specifiers[item]

    def __len__(self):
        return len(self._music_specifiers)

    ### PUBLIC METHODS ###

    def transpose(self, expr):
        music_specifiers = [_.transpose(expr) for _ in self.music_specifiers]
        return abjad.new(
            self,
            music_specifiers=music_specifiers,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def application_rate(self):
        return self._application_rate

    @property
    def music_specifiers(self):
        return self._music_specifiers
