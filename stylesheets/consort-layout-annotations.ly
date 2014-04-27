\layout {

    \context {
        \Voice
        \name InnerAnnotation
        \type Engraver_group
        \alias Voice
        \override Accidental.stencil = ##f
        \override Dots.stencil = ##f
        \override Flag.stencil = ##f
        \override NoteColumn.ignore-collision = ##t
        \override NoteHead.no-ledgers = ##t
        \override NoteHead.stencil = ##f
        \override Stem.stencil = ##f
        \override TupletBracket.dash-fraction = 0.125
        \override TupletBracket.dash-period = 1.0
        \override TupletBracket.outside-staff-padding = 1
        \override TupletBracket.outside-staff-priority = 999
        \override TupletBracket.style = #'dashed-line
        \override TupletNumber.stencil = ##f
    }

    \context {
        \Voice
        \name OuterAnnotation
        \type Engraver_group
        \alias Voice
        \override Accidental.stencil = ##f
        \override Dots.stencil = ##f
        \override Flag.stencil = ##f
        \override NoteHead.no-ledgers = ##t
        \override NoteHead.stencil = ##f
        \override Stem.stencil = ##f
        \override TupletNumber.stencil = ##f
        \override TupletBracket.outside-staff-padding = 1
        \override TupletBracket.outside-staff-priority = 1000
        \override NoteColumn.ignore-collision = ##t
    }

    \context {
        \Staff
        \accepts InnerAnnotation
        \accepts OuterAnnotation
    }

}
