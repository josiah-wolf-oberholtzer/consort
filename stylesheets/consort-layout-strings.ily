\layout {

    \context {
        \Voice
        \name RHVoice
        \type Engraver_group
        \alias Voice
    }

    \context {
        \Staff
        \name RHStaff
        \type Engraver_group
        \alias Staff
        \accepts RHVoice
    }

    \context {
        \Voice
        \name LHVoice
        \type Engraver_group
        \alias Voice
    }

    \context {
        \Staff
        \name LHStaff
        \type Engraver_group
        \alias Staff
        \accepts LHVoice
    }

    \context {
        \StaffGroup
        \name PerformerStaffGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts RHStaff
        \accepts LHStaff
    }

    \context {
        \StaffGroup
        \name ViolinStaffGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts PerformerStaffGroup
    }

    \context {
        \StaffGroup
        \name ViolaStaffGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts PerformerStaffGroup
    }

    \context {
        \StaffGroup
        \name CelloStaffGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts PerformerStaffGroup
    }

    \context {
        \StaffGroup
        \name ContrabassStaffGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts PerformerStaffGroup
    }

    \context{
        \StaffGroup
        \accepts ViolinStaffGroup
        \accepts ViolaStaffGroup
        \accepts CelloStaffGroup
        \accepts ContrabassStaffGroup
    }

}
