afterGraceFraction = #(cons 127 128)

\layout {
    \accidentalStyle dodecaphonic
    indent = 0
    ragged-bottom = ##t
    ragged-last = ##t
    ragged-right = ##t

    %%% COMMON %%%

    \context {
        \Voice
        \consists Horizontal_bracket_engraver
        \remove Forbid_line_break_engraver
    }

    \context {
        \Staff
        \remove Time_signature_engraver
    }

    %%% SPECIFIC %%%

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
        \accepts InnerAnnotation
        \accepts OuterAnnotation
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
        \accepts InnerAnnotation
        \accepts OuterAnnotation
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
        \name OuterStaffGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts ViolinStaffGroup
        \accepts ViolaStaffGroup
        \accepts CelloStaffGroup
        \accepts ContrabassStaffGroup
    }

    %%% TIME SIGNATURE CONTEXT %%%

    \context {
        \type Engraver_group
        \name TimeSignatureContext
        \consists Time_signature_engraver
        \consists Axis_group_engraver
        \consists Metronome_mark_engraver
        \consists Mark_engraver
        \consists Bar_number_engraver
        \override BarNumber.X-extent = #'(0 . 0)
        \override BarNumber.Y-extent = #'(0 . 0)
        \override BarNumber.extra-offset = #'(-8 . -4)
        \override BarNumber.font-name = "Didot Italic"
        \override BarNumber.font-size = 2
        \override BarNumber.stencil = #(make-stencil-circler 0.1 0.7 ly:text-interface::print)
        \override MetronomeMark.X-extent = #'(0 . 0)
        \override MetronomeMark.X-offset = 5
        \override MetronomeMark.Y-offset = -2.5
        \override MetronomeMark.break-align-symbols = #'(time-signature)
        \override MetronomeMark.font-size = 3
        \override RehearsalMark.X-extent = #'(0 . 0)
        \override RehearsalMark.Y-offset = 8
        \override RehearsalMark.break-align-symbols = #'(time-signature)
        \override RehearsalMark.break-visibility = #end-of-line-invisible
        \override RehearsalMark.font-name = "Didot"
        \override RehearsalMark.font-size = 10
        \override RehearsalMark.self-alignment-X = #CENTER
        \override TimeSignature.X-extent = #'(0 . 0)
        \override TimeSignature.break-align-symbols = #'(staff-bar)
        \override TimeSignature.break-visibility = #end-of-line-invisible
        \override TimeSignature.font-size = 3
        \override TimeSignature.style = #'numbered
        \override VerticalAxisGroup.staff-staff-spacing = #'(
            (basic-distance . 8)
            (minimum-distance . 8)
            (padding . 9)
            (stretchability . 0)
            )
    }

    %%% SCORE %%%

    \context {
        \Score
        \accepts TimeSignatureContext
        \accepts OuterStaffGroup
        \remove Metronome_mark_engraver
        \remove Mark_engraver
        \remove Bar_number_engraver
        \override BarLine.hair-thickness = 0.5
        \override BarLine.space-alist = #'(
            (time-signature extra-space . 0.0)
            (custos minimum-space . 0.0) 
            (clef minimum-space . 0.0) 
            (key-signature extra-space . 0.0) 
            (key-cancellation extra-space . 0.0) 
            (first-note fixed-space . 0.0) 
            (next-note semi-fixed-space . 0.0) 
            (right-edge extra-space . 0.0)
            )
        \override Beam.beam-thickness = 0.75
        \override Beam.breakable = ##t
        \override Beam.length-fraction = 1.5
        \override DynamicLineSpanner.add-stem-support = ##t
        \override DynamicLineSpanner.outside-staff-padding = 1
        \override Glissando.breakable = ##t
        \override Glissando.thickness = 3
        \override GraceSpacing.common-shortest-duration = #(ly:make-moment 1 16)
        \override NoteCollision.merge-differently-dotted = ##t
        \override NoteColumn.ignore-collision = ##t
        \override OttavaBracket.add-stem-support = ##t
        \override OttavaBracket.padding = 2
        %\override PhrasingSlur.dash-definition = #'((0 1 0.5 0.5))
        %\override Slur.dash-definition = #'((0 1 0.5 0.5))
        \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1 64)
        \override SpacingSpanner.strict-grace-spacing = ##f
        \override SpacingSpanner.strict-note-spacing = ##f
        \override SpacingSpanner.uniform-stretching = ##t
        \override Stem.details.beamed-lengths = #'(6)
        \override Stem.details.lengths = #'(6)
        \override Stem.direction = #DOWN
        \override Stem.stemlet-length = 1.5
        \override StemTremolo.beam-thickness = 0.75
        \override StemTremolo.beam-width = 1.5
        \override StemTremolo.flag-count = 4.0
        \override StemTremolo.length-fraction = 1.5
        \override StemTremolo.slope = 0.5
        \override SustainPedal.self-alignment-X = #LEFT
        \override TextScript.add-stem-support = ##t
        \override TextScript.outside-staff-padding = 1
        \override TextScript.padding = 1
        \override TextScript.staff-padding = 1
        \override TrillPitchAccidental.avoid-slur = #'ignore
        \override TrillPitchAccidental.layer = 1000
        \override TrillPitchAccidental.whiteout = ##t
        \override TrillPitchHead.layer = 1000
        \override TrillPitchHead.whiteout = ##t
        \override TrillSpanner.outside-staff-padding = 1
        \override TrillSpanner.padding = 1
        \override TupletBracket.avoid-scripts = ##t
        \override TupletBracket.direction = #DOWN
        \override TupletBracket.full-length-to-extent = ##t
        \override TupletBracket.outside-staff-padding = 2
        \override TupletBracket.padding = 2
        \override TupletNumber.font-size = 1
        \override TupletNumber.text = #tuplet-number::calc-fraction-text
        \override VerticalAxisGroup.staff-staff-spacing = #'(
            (basic-distance . 6)
            (minimum-distance . 8)
            (padding . 6)
            (stretchability . 30)
            )
        autoBeaming = ##f
        pedalSustainStyle = #'mixed
        proportionalNotationDuration = #(ly:make-moment 1 48)
        tupletFullLength = ##t
    }
}
