\layout {

    \context {
        \StaffGroup
        \name PianoPerformerGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts Staff
        \override StaffSymbol #'color = #red
    }

    \context {
        \EnsembleGroup
        \accepts PianoPerformerGroup
    }

    \context {
        \Score
        \accepts PianoPerformerGroup
    }

}