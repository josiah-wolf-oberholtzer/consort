import abjad
from consort.tools.LogicalTieExpression import LogicalTieExpression


class KeyClickExpression(LogicalTieExpression):
    r'''A key-click expression.

    ::

        >>> key_click_expression = consort.KeyClickExpression()
        >>> staff = abjad.Staff("c'4 d'4 ~ d'4 e'4")
        >>> logical_tie = abjad.inspect(staff[1]).get_logical_tie()
        >>> key_click_expression(logical_tie)
        >>> print(format(staff))
        \new Staff {
            c'4
            <
                \parenthesize
                \tweak font-size #-2
                ef
                \tweak style #'cross
                d'
            >4 ~
            <
                \parenthesize
                \tweak font-size #-2
                ef
                \tweak style #'cross
                d'
            >4
            e'4
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(self):
        pass

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        pitch_range=None,
        ):
        assert isinstance(logical_tie, abjad.LogicalTie), logical_tie
        main_pitch = logical_tie[0].written_pitch
        subtone_pitch = main_pitch.transpose('-M7')
        chord_pitches = (subtone_pitch, main_pitch)
        for i, leaf in enumerate(logical_tie):
            chord = abjad.Chord(leaf)
            chord.written_pitches = chord_pitches
            self._replace(leaf, chord)
            for note_head in chord.note_heads:
                if note_head.written_pitch == subtone_pitch:
                    note_head.is_parenthesized = True
                    note_head.tweak.font_size = -2
                else:
                    note_head.tweak.style = 'cross'
