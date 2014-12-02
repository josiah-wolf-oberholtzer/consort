\layout {

    \context {
        \StaffGroup
        \name PianoPerformerGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts Staff
        systemStartDelimiter = #'SystemStartBrace
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