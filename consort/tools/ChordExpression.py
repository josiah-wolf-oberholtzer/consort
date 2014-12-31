# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad import attach
from abjad.tools import indicatortools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from consort.tools.LogicalTieExpression import LogicalTieExpression


class ChordExpression(LogicalTieExpression):
    r'''A chord expression.

    ::

        >>> import consort
        >>> chord_expression = consort.ChordExpression(
        ...     arpeggio_direction=Down,
        ...     chord_expr=(-1, 3, 7),
        ...     )
        >>> print(format(chord_expression))
        consort.tools.ChordExpression(
            chord_expr=pitchtools.IntervalSegment(
                (
                    pitchtools.NumberedInterval(-1),
                    pitchtools.NumberedInterval(3),
                    pitchtools.NumberedInterval(7),
                    ),
                item_class=pitchtools.NumberedInterval,
                ),
            arpeggio_direction=Down,
            )

    ::

        >>> staff = Staff("c'4 d'4 ~ d'4 e'4")
        >>> pitch_range = pitchtools.PitchRange.from_pitches('C3', 'C6')
        >>> attach(pitch_range, staff, scope=Staff)
        >>> logical_tie = inspect_(staff[1]).get_logical_tie()
        >>> chord_expression(logical_tie)
        >>> print(format(staff))
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
        '_chord_expr',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        chord_expr=None,
        arpeggio_direction=None,
        ):
        assert arpeggio_direction in (Up, Down, Center, None)
        if chord_expr is not None:
            assert len(chord_expr)
            prototype = (pitchtools.IntervalSegment, pitchtools.PitchSegment)
            if isinstance(chord_expr, prototype):
                result = chord_expr
            else:
                try:
                    result = sorted(chord_expr)
                    result = pitchtools.IntervalSegment(result)
                except:
                    result = pitchtools.PitchSegment(chord_expr)
            chord_expr = result
        self._arpeggio_direction = arpeggio_direction
        self._chord_expr = chord_expr

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        pitch_range=None,
        ):
        assert isinstance(logical_tie, selectiontools.LogicalTie), logical_tie
        if isinstance(self.chord_expr, pitchtools.IntervalSegment):
            pitches = self._get_pitches_from_intervals(
                logical_tie, pitch_range)
        else:
            pitches = self.chord_expr
        for i, leaf in enumerate(logical_tie):
            chord = scoretools.Chord(leaf)
            chord.written_pitches = pitches
            self._replace(leaf, chord)
            if not i and self.arpeggio_direction is not None:
                arpeggio = indicatortools.Arpeggio(self.arpeggio_direction)
                attach(arpeggio, chord)

    ### PRIVATE METHODS ###

    def _get_pitches_from_intervals(self, logical_tie, pitch_range):
        chord_expr = self.chord_expr or ()
        head = logical_tie.head
        base_pitch = head.written_pitch
        new_chord_expr = chord_expr
        if pitch_range is not None:
            assert base_pitch in pitch_range
            maximum = max(chord_expr)
            minimum = min(chord_expr)
            maximum_pitch = base_pitch.transpose(maximum)
            minimum_pitch = base_pitch.transpose(minimum)
            if maximum_pitch not in pitch_range:
                new_chord_expr = [x - maximum for x in chord_expr]
            elif minimum_pitch not in pitch_range:
                new_chord_expr = [x - minimum for x in chord_expr]
        pitches = [base_pitch.transpose(x) for x in new_chord_expr]
        pitches = [pitchtools.NamedPitch(float(x)) for x in pitches]
        if pitch_range is not None:
            assert all(pitch in pitch_range for pitch in pitches), \
                (pitch_range, base_pitch, chord_expr, pitches)
        return pitches

    ### PUBLIC PROPERTIES ###

    @property
    def arpeggio_direction(self):
        return self._arpeggio_direction

    @property
    def chord_expr(self):
        return self._chord_expr