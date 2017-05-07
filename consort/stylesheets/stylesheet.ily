#(set-default-paper-size "letter" 'landscape)
#(set-global-staff-size 11)

#(define-markup-command (overlay layout props args)
  (markup-list?)
  (apply ly:stencil-add (interpret-markup-list layout props args)))

#(define-markup-command (vstrut layout props) ()
    (let ((ref-mrkp (interpret-markup layout props "fp")))
    (ly:make-stencil 
        (ly:stencil-expr empty-stencil)
        empty-interval
        (ly:stencil-extent ref-mrkp Y))))

parenthesizeDynamic =
#(define-event-function (parser location dyn) (ly:event?)
    (make-dynamic-script
        #{ \markup \concat {
            \normal-text \italic \fontsize #2 (
            \pad-x #0.2 #(ly:music-property dyn 'text)
            \normal-text \italic \fontsize #2 )
        }
        #}))

colorSpan =
#(define-music-function (parser location y-lower y-upper color) 
     (number? number? color?)
    #{
      \once\override PhrasingSlur.stencil =
        $(lambda (grob)
          (let* (
            (area (ly:slur::print grob))
              (X-ext (ly:stencil-extent area X))
              (Y-ext (ly:stencil-extent area Y)))
            (set! Y-ext (cons y-lower y-upper))
            (ly:grob-set-property! grob 'layer -10)
            (ly:make-stencil (list 'color color
              (ly:stencil-expr (ly:round-filled-box X-ext Y-ext 0))
              X-ext Y-ext))))
      \once\override PhrasingSlur.Y-offset = #0
      \once\override PhrasingSlur.shorten-pair = #'(-.95 . -1.65)
    #})

\paper {

    %%% MARGINS %%%

    bottom-margin = 10\mm
    left-margin = 30\mm
    right-margin = 10\mm
    top-margin = 10\mm

    %%% HEADERS AND FOOTERS %%%

    evenFooterMarkup = \markup \fill-line {
        " "
        \concat {
            \bold \fontsize #3
            \on-the-fly #print-page-number-check-first
            \fromproperty #'page:page-number-string
            %\hspace #18
        }
    }
    evenHeaderMarkup = \markup \fill-line { " " }
    oddFooterMarkup = \markup \fill-line {
        " "
        \concat {
            \bold \fontsize #3
            \on-the-fly #print-page-number-check-first
            \fromproperty #'page:page-number-string
            %\hspace #18
        }
    }
    oddHeaderMarkup = \markup \fill-line { " " }
    print-first-page-number = ##f
    print-page-number = ##t

    %%% PAGE BREAKING %%%

    page-breaking = #ly:minimal-breaking
    ragged-bottom = ##f
    ragged-last-bottom = ##f

    %%% SPACING DETAILS %%%%

    markup-system-spacing = #'(
        (basic-distance . 0)
        (minimum-distance . 0)
        (padding . 2)
        (stretchability . 0)
        )

    system-system-spacing = #'(
        (basic-distance . 0)
        (minimum-distance . 0)
        (padding . 2)
        (stretchability . 0)
        )

    top-markup-spacing = #'(
        (basic-distance . 0)
        (minimum-distance . 0)
        (padding . 0)
        (stretchability . 0)
        )
}

afterGraceFraction = #(cons 127 128)

\layout {

    \accidentalStyle modern-cautionary
    indent = 0
    ragged-bottom = ##t
    ragged-last = ##t
    ragged-right = ##t

    %%% ANNOTATIONS %%%

    \context {
        \Voice
        \name AnnotatedDivisionsVoice
        \type Engraver_group
        \alias Voice
        \override Accidental.stencil = ##f
        \override Beam.stencil = ##f
        \override Dots.stencil = ##f
        \override Flag.stencil = ##f
        \override NoteCollision.merge-differently-dotted = ##t
        \override NoteCollision.merge-differently-headed = ##t
        \override NoteColumn.ignore-collision = ##t
        \override NoteHead.no-ledgers = ##t
        \override NoteHead.transparent = ##t
        \override Stem.stencil = ##f
        \override TupletBracket.direction = #down
        \override TupletBracket.outside-staff-padding = 1
        \override TupletBracket.outside-staff-priority = 999
        \override TupletBracket.thickness = 2
        \override TupletNumber.stencil = ##f
    }

    \context {
        \Voice
        \name AnnotatedPhrasesVoice
        \type Engraver_group
        \alias Voice
        \override Accidental.stencil = ##f
        \override Beam.stencil = ##f
        \override Dots.stencil = ##f
        \override Flag.stencil = ##f
        \override NoteCollision.merge-differently-dotted = ##t
        \override NoteCollision.merge-differently-headed = ##t
        \override NoteColumn.ignore-collision = ##t
        \override NoteHead.no-ledgers = ##t
        \override NoteHead.transparent = ##t
        \override Stem.stencil = ##f
        \override TupletBracket.direction = #down
        \override TupletBracket.outside-staff-padding = 1
        \override TupletBracket.outside-staff-priority = 1000
        \override TupletBracket.thickness = 2
        \override TupletNumber.stencil = ##f
    }

    %%% COMMON %%%

    \context {
        \Voice
        \consists Horizontal_bracket_engraver
        \remove Forbid_line_break_engraver
    }

    \context {
        \Staff
        \remove Time_signature_engraver
        \accepts AnnotatedDivisionsVoice
        \accepts AnnotatedPhrasesVoice
    }

    %%% TIME SIGNATURE CONTEXT %%%

    \context {
        \name TimeSignatureContext
        \type Engraver_group
        \consists Axis_group_engraver
        \consists Bar_number_engraver
        \consists Mark_engraver
        \consists Metronome_mark_engraver
        \consists Script_engraver
        \consists Text_engraver
        \consists Text_spanner_engraver
        \consists Time_signature_engraver
        \override BarNumber.extra-offset = #'(-6 . -4)
        \override BarNumber.font-name = "Didot Italic"
        \override BarNumber.font-size = 1
        \override BarNumber.padding = 4
        \override MetronomeMark.X-extent = #'(0 . 0)
        \override MetronomeMark.Y-extent = #'(0 . 0)
        \override MetronomeMark.break-align-symbols = #'(left-edge)
        \override MetronomeMark.extra-offset = #'(0 . 4)
        \override MetronomeMark.font-size = 3
        \override RehearsalMark.X-extent = #'(0 . 0)
        \override RehearsalMark.X-offset = 6
        \override RehearsalMark.Y-offset = -2.25
        \override RehearsalMark.break-align-symbols = #'(time-signature)
        \override RehearsalMark.break-visibility = #end-of-line-invisible
        \override RehearsalMark.font-name = "Didot"
        \override RehearsalMark.font-size = 10
        \override RehearsalMark.outside-staff-priority = 500
        \override RehearsalMark.self-alignment-X = #center
        \override Script.extra-offset = #'(4 . -9)
        \override Script.font-size = 6
        \override TextScript.font-size = 3
        \override TextScript.outside-staff-priority = 600
        \override TextScript.padding = 6
        \override TextSpanner.bound-details.right.attach-dir = #LEFT
        \override TextSpanner.padding = 6.75
        \override TimeSignature.X-extent = #'(0 . 0)
        \override TimeSignature.break-align-symbol = #'left-edge
        \override TimeSignature.break-visibility = #end-of-line-invisible
        \override TimeSignature.font-size = 3
        \override TimeSignature.space-alist.clef = #'(extra-space . 0.5)
        \override TimeSignature.style = #'numbered
        \override VerticalAxisGroup.default-staff-staff-spacing = #'(
            (basic-distance . 0)
            (minimum-distance . 14)
            (padding . 0)
            (stretchability . 0)
        )
        \override VerticalAxisGroup.minimum-Y-extent = #'(-20 . 20)
    }

    %%% SINGLE PERFORMER GROUP %%%

    \context {
        \StaffGroup
        \name PerformerGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts Staff
    }

    %%% MULTIPLE PERFORMER GROUP %%%

    \context {
        \StaffGroup
        \name EnsembleGroup
        \type Engraver_group
        \alias StaffGroup
        \accepts PerformerGroup
    }

    %%% STRINGS %%%

    \context {
        \Staff
        \name StringStaff
        \type Engraver_group
        \alias Staff
        \override Beam.positions = #'(-9 . -9)
        \override DynamicLineSpanner.staff-padding = 11
        \override TupletBracket.staff-padding = 6
    }

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
        \accepts StringStaff
    }

    \context {
        \EnsembleGroup
        \accepts StringPerformerGroup
    }

    \context {
        \Score
        \accepts StringPerformerGroup
    }

    %%% SCORE %%%

    \context {
        \Score
        \accepts PercussionSectionStaffGroup
        \accepts StringSectionStaffGroup
        \accepts TimeSignatureContext
        \accepts WindSectionStaffGroup
        \remove Bar_number_engraver
        \remove Mark_engraver
        \remove Metronome_mark_engraver
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
        \override Beam.direction = #down
        \override Beam.breakable = ##t
        \override Beam.length-fraction = 1.5
        \override Glissando.breakable = ##t
        \override Glissando.thickness = 3
        \override Hairpin.bound-padding = 1.5
        \override NoteCollision.merge-differently-dotted = ##t
        \override NoteColumn.ignore-collision = ##t
        \shape #'((-1.5 . 0) (-1 . 0) (-0.5 . 0) (0 . 0)) RepeatTie                 
        \override RepeatTie.X-extent = ##f
        \override SpacingSpanner.strict-grace-spacing = ##t
        \override SpacingSpanner.strict-note-spacing = ##f
        \override SpacingSpanner.uniform-stretching = ##t
        \override StaffSymbol.color = #(x11-color 'grey50)
        \override Stem.details.beamed-lengths = #'(6)
        \override Stem.details.lengths = #'(6)
        \override Stem.direction = #down
        \override Stem.stemlet-length = 1.5
        \override StemTremolo.beam-width = 1.5
        \override StemTremolo.flag-count = 4
        \override StemTremolo.slope = 0.5
        \override SustainPedal.self-alignment-X = #CENTER
        \override SustainPedalLineSpanner.padding = 2
        \override SustainPedalLineSpanner.outside-staff-padding = 2
        \override SustainPedalLineSpanner.to-barline = ##t
        \override SystemStartSquare.thickness = 2

        \override TextScript.parent-alignment-X = #center
        \override TextScript.self-alignment-X = #center

        \override TextSpanner.padding = 1
        \override TupletBracket.breakable = ##t
        \override TupletBracket.direction = #down
        \override TupletBracket.full-length-to-extent = ##f
        \override TupletBracket.padding = 1.5
        \override TupletBracket.outside-staff-padding = 0.75
        \override TupletNumber.font-size = 1
        \override TupletNumber.text = #tuplet-number::calc-fraction-text
        \override StaffGrouper.staffgroup-staff-spacing = #'(
            (basic-distance . 20)
            (minimum-distance . 20)
            (padding . 5)
            (stretchability . 0)
            )
        \override StaffGrouper.staff-staff-spacing = #'(
            (basic-distance . 20)
            (minimum-distance . 20)
            (padding . 5)
            (stretchability . 0)
            )
        autoBeaming = ##f
        %doubleRepeatType = #":|.|:"
        pedalSustainStyle = #'mixed
        proportionalNotationDuration = #(ly:make-moment 1 32)
        tupletFullLength = ##t
    }

}
