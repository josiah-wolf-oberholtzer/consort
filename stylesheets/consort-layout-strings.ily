\layout {

    \context {
        \Voice
        \name StringBowingVoice
        \type Engraver_group
        \alias Voice
    }

    \context {
        \Staff
        \name StringBowingStaff
        \type Engraver_group
        \alias Staff
        \accepts StringBowingVoice
    }

    \context {
        \Voice
        \name StringFingeringVoice
        \type Engraver_group
        \alias Voice
    }

    \context {
        \Staff
        \name StringFingeringStaff
        \type Engraver_group
        \alias Staff
        \accepts StringFingeringVoice
    }

    \context {
        \StaffGroup
        \name StringPerformerStaffGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts StringBowingStaff
        \accepts StringFingeringStaff
    }

    \context{
        \StaffGroup
        \accepts StringPerformerStaffGroup
    }

}
