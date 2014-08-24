# -*- encoding: utf-8 -*-
from abjad import *


class ChordExpression(abctools.AbjadValueObject):
    r'''A chord expression.

    ::

        >>> from consort import makers
        >>> chord_expression = makers.ChordExpression(
        ...     arpeggio_direction=Down,
        ...     interval_numbers=(-1, 3, 7),
        ...     )
        >>> print(format(chord_expression))
        consort.makers.ChordExpression(
            arpeggio_direction=Down,
            interval_numbers=frozenset([3, -1, 7]),
            )

    ::

        >>> staff = Staff("c'4 d'4 ~ d'4 e'4")
        >>> pitch_range = pitchtools.PitchRange.from_pitches('C3', 'C6')
        >>> attach(pitch_range, staff, scope=Staff)
        >>> logical_tie = inspect_(staff[1]).get_logical_tie()
        >>> chord_expression(logical_tie)
        >>> f(staff)
        \new Staff {
            c'4
            \arpeggioArrowDown
            <cs' f' a'>4 \arpeggio ~
            <cs' f' a'>4
            e'4
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_arpeggio_direction',
        '_interval_numbers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        arpeggio_direction=None,
        interval_numbers=None,
        ):
        assert arpeggio_direction in (Up, Down, Center, None)
        if interval_numbers is not None:
            interval_numbers = frozenset(
                x for x in interval_numbers
                if x != 0
                )
            assert len(interval_numbers)
        self._arpeggio_direction = arpeggio_direction
        self._interval_numbers = interval_numbers

    ### SPECIAL METHODS ###

    def __call__(self, logical_tie):
        assert isinstance(logical_tie, selectiontools.LogicalTie), logical_tie
        interval_numbers = self.interval_numbers or ()
        interval_numbers = sorted(list(interval_numbers))
        head = logical_tie.head
        base_pitch = head.written_pitch
        pitch_range = inspect_(head).get_effective(pitchtools.PitchRange)
        if pitch_range is None:
            pitch_range = pitchtools.PitchRange.from_pitches(-48, 48)
        assert base_pitch in pitch_range
        maximum = max(interval_numbers)
        minimum = min(interval_numbers)
        maximum_pitch = base_pitch.transpose(maximum)
        minimum_pitch = base_pitch.transpose(minimum)
        if maximum_pitch not in pitch_range:
            new_interval_numbers = [x - maximum for x in interval_numbers]
        elif minimum_pitch not in pitch_range:
            new_interval_numbers = [x - minimum for x in interval_numbers]
        else:
            new_interval_numbers = interval_numbers
        pitches = [base_pitch.transpose(x) for x in new_interval_numbers]
        pitches = [pitchtools.NamedPitch(float(x)) for x in pitches]
        assert all(pitch in pitch_range for pitch in pitches), \
            (pitch_range, base_pitch, interval_numbers, pitches)
        for i, leaf in enumerate(logical_tie):
            chord = scoretools.Chord(leaf)
            chord.written_pitches = pitches
            grace_containers = inspect_(leaf).get_grace_containers('after')
            if grace_containers:
                old_grace_container = grace_containers[0]
                grace_notes = old_grace_container.select_leaves()
                detach(scoretools.GraceContainer, leaf)
            mutate(leaf).replace(chord)
            if not i and self.arpeggio_direction is not None:
                arpeggio = indicatortools.Arpeggio(self.arpeggio_direction)
                attach(arpeggio, chord)
            if grace_containers:
                new_grace_container = scoretools.GraceContainer(
                    grace_notes,
                    kind='after',
                    )
                attach(new_grace_container, chord)

    ### PUBLIC PROPERTIES ###

    @property
    def arpeggio_direction(self):
        return self._arpeggio_direction

    @property
    def interval_numbers(self):
        return self._interval_numbers