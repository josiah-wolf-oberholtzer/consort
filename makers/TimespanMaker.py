# -*- encoding: utf-8 -*-
from abjad import *


class TimespanMaker(abctools.AbjadObject):
    r'''A timespan maker.

    ::

        >>> from consort import makers
        >>> timespan_maker = makers.TimespanMaker()
        >>> print format(timespan_maker)
        makers.TimespanMaker(
            can_shift=False,
            can_split=False,
            initial_silence_durations=(),
            minimum_duration=durationtools.Duration(1, 8),
            playing_durations=(
                durationtools.Duration(1, 4),
                ),
            playing_groupings=(1,),
            repeat=True,
            silence_durations=(
                durationtools.Duration(1, 4),
                ),
            step_anchor=Right,
            synchronize_step=False,
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_can_shift',
        '_can_split',
        '_initial_silence_durations',
        '_minimum_duration',
        '_playing_durations',
        '_playing_groupings',
        '_repeat',
        '_silence_durations',
        '_step_anchor',
        '_synchronize_step',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        can_shift=False,
        can_split=False,
        initial_silence_durations=(),
        minimum_duration=durationtools.Duration(1, 8),
        playing_durations=(
            durationtools.Duration(1, 4),
            ),
        playing_groupings=(1,),
        repeat=True,
        silence_durations=(
            durationtools.Duration(1, 4),
            ),
        step_anchor=Right,
        synchronize_step=False,
        ):
        self._can_shift = bool(can_shift)
        self._can_split = bool(can_split)
        initial_silence_durations = tuple(Duration(x)
            for x in initial_silence_durations)
        assert all(0 <= x for x in initial_silence_durations)
        self._initial_silence_durations = initial_silence_durations
        self._minimum_duration = durationtools.Duration(minimum_duration)
        playing_durations = tuple(Duration(x) for x in playing_durations)
        assert len(playing_durations)
        assert all(0 < x for x in playing_durations)
        self._playing_durations = playing_durations
        playing_groupings = tuple(int(x) for x in playing_groupings)
        assert len(playing_groupings)
        assert all(0 < x for x in playing_groupings)
        self._playing_groupings = playing_groupings
        self._repeat = bool(repeat)
        silence_durations = tuple(Duration(x) for x in silence_durations)
        assert len(silence_durations)
        assert all(0 < x for x in silence_durations)
        self._silence_durations = silence_durations
        assert step_anchor in (Left, Right)
        self._step_anchor = step_anchor
        self._synchronize_step = bool(synchronize_step)

    ### SPECIAL METHODS ###

    def __call__(
        self,
        music_specifier=None,
        score_template=None,
        target_duration=None,
        voice_specifier=None,
        ):
        timespan_inventory = timespantools.TimespanInventory()

        initial_silence_durations = datastructuretools.StatalServer(
            self.initial_silence_durations)()
        playing_durations = datastructuretools.StatalServer(
            self.playing_durations)()
        playing_groupings = datastructuretools.StatalServer(
            self.playing_groupings)()
        silence_durations = datastructuretools.StatalServer(
            self.silence_durations)()

        if self.synchronize_step:
            current_offset = Offset(0)
            if initial_silence_durations:
                current_offset += initial_silence_durations()[0]
            while current_offset < target_duration:
                grouping = playing_groupings()[0]
                playing_durations = playing_durations(grouping)
                silence_duration = silence_durations()[0]
                if not self.repeat:
                    break

        else:
            for voice_name in voice_specifier:
                current_offset = Offset(0)
                if initial_silence_durations:
                    current_offset += initial_silence_durations()[0]
                while current_offset < target_duration:
                    grouping = playing_groupings()[0]
                    playing_durations = playing_durations(grouping)
                    silence_duration = silence_durations()[0]
                    if not self.repeat:
                        break

        stop_offset = current_offset
        return timespan_inventory, stop_offset

    ### PUBLIC PROPERTIES ###

    @property
    def can_shift(self):
        return self._can_shift

    @property
    def can_split(self):
        return self._can_split

    @property
    def initial_silence_durations(self):
        return self._initial_silence_durations

    @property
    def minimum_duration(self):
        return self._minimum_duration

    @property
    def playing_durations(self):
        return self._playing_durations

    @property
    def playing_groupings(self):
        return self._playing_groupings

    @property
    def repeat(self):
        return self._repeat

    @property
    def silence_durations(self):
        return self._silence_durations

    @property
    def step_anchor(self):
        return self._step_anchor

    @property
    def synchronize_step(self):
        return self._synchronize_step
