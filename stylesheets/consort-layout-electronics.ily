\layout {

    \context {
        \Voice
        \name BowingVoice
        \type Engraver_group
        \alias Voice
    }

    \context {
        \Staff
        \name BowingStaff
        \type Engraver_group
        \alias Staff
        \accepts BowingVoice
    }

    \context {
        \Voice
        \name FingeringVoice
        \type Engraver_group
        \alias Voice
    }

    \context {
        \Staff
        \name FingeringStaff
        \type Engraver_group
        \alias Staff
        \accepts FingeringVoice
    }

    \context {
        \StaffGroup
        \name StringPerformerStaffGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts BowingStaff
        \accepts FingeringStaff
    }

    \context{
        \StaffGroup
        \accepts StringPerformerStaffGroup
    }

}
