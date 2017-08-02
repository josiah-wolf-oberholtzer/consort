import abjad
from consort.tools.LogicalTieExpression import LogicalTieExpression


class HarmonicExpression(LogicalTieExpression):
    r'''A harmonic expression.

    ::

        >>> harmonic_expression = consort.HarmonicExpression()
        >>> print(format(harmonic_expression))
        consort.tools.HarmonicExpression(
            touch_interval=abjad.NamedInterval('+P4'),
            )

    ::

        >>> staff = abjad.Staff("c'4 d'4 ~ d'4 e'4")
        >>> logical_tie = abjad.inspect(staff[1]).get_logical_tie()
        >>> harmonic_expression(logical_tie)
        >>> print(format(staff))
        \new Staff {
            c'4
            <
                d'
                \tweak style #'harmonic
                g'
            >4 ~
            <
                d'
                \tweak style #'harmonic
                g'
            >4
            e'4
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_touch_interval',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        touch_interval='P4',
        ):
        touch_interval = abjad.NamedInterval(touch_interval)
        self._touch_interval = touch_interval

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        pitch_range=None,
        ):
        for i, leaf in enumerate(logical_tie):
            stopped_pitch = leaf.written_pitch
            touched_pitch = stopped_pitch.transpose(self.touch_interval)
            chord = abjad.Chord(leaf)
            chord.written_pitches = [stopped_pitch, touched_pitch]
            #chord.note_heads[0].is_parenthesized = True
            #chord.note_heads[0].tweak.font_size = -4
            chord.note_heads[1].tweak.style = 'harmonic'
            self._replace(leaf, chord)

    ### PUBLIC PROPERTIES ###

    @property
    def touch_interval(self):
        return self._touch_interval
