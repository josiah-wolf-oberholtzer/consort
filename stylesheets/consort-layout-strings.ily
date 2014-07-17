\layout {

    \context {
        \Staff
        \name BowingStaff
        \type Engraver_group
        \alias Staff
    }

    \context {
        \Voice
        \name FingeringStaff
        \type Engraver_group
        \alias Staff
    }

    \context {
        \StaffGroup
        \name StringPerformerGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts BowingStaff
        \accepts FingeringStaff
    }

    \context {
        \EnsembleGroup
        \accepts StringPerformerGroup
    }

    \context {
        \Score
        \accepts StringPerformerGroup
    }

}