\version "2.19.6"
\language "english"

#(ly:set-option 'relative-includes #t)

\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-header.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout-annotations.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout-brass.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout-keyboards.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout-percussion.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout-strings.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout-winds.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-paper.ily"

\score {
	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 2/4
				\tempo 8=72
				\mark \markup { \override #'(box-padding . 0.5) \box "C1" " " \fontsize #-3 "adding grace notes (every red attack)" }
				s1 * 1/2
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 2/4
				s1 * 1/2
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 2/4
				s1 * 1/2
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 2/4
				s1 * 1/2
			}
		}
		\context StaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context StringPerformerStaffGroup = "Violin Staff Group" <<
					\context FingeringStaff = "Violin Staff" <<
						\clef "treble"
						\context FingeringVoice = "Violin Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									\afterGrace
									c'32 ]
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 4/5 {
									\afterGrace
									r8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
								}
								{
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								\times 4/5 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
								}
								{
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r32
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 4/5 {
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemRightBeamCount = 1
									c'8.
								}
							}
						}
						\context InnerAnnotation = "Violin Voice Inner Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/32
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/32
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
						}
					>>
				>>
			>>
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context StringPerformerStaffGroup = "Viola Staff Group" <<
					\context FingeringStaff = "Viola Staff" <<
						\clef "alto"
						\context FingeringVoice = "Viola Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									\afterGrace
									c'32 ]
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
								}
								\times 4/5 {
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 4/5 {
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
								}
								\times 4/5 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
									r8
								}
								{
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									r8
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\afterGrace
									r8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									r8
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
							}
						}
						\context InnerAnnotation = "Viola Voice Inner Annotation" {
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
						}
					>>
				>>
			>>
			\context CelloStaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context StringPerformerStaffGroup = "Cello Staff Group" <<
					\context FingeringStaff = "Cello Staff" <<
						\clef "bass"
						\context FingeringVoice = "Cello Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r32
									r8
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r4
								}
							}
							{
								\times 2/3 {
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									r4
								}
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\times 2/3 {
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
								}
							}
						}
						\context InnerAnnotation = "Cello Voice Inner Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/32
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/32
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\bar "||"
						}
					>>
				>>
			>>
		>>
	>>
}

\score {
	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 2/4
				\tempo 8=72
				\mark \markup { \override #'(box-padding . 0.5) \box "C1" " " \fontsize #-3 "adding grace notes (every red attack)" }
				s1 * 1/2
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 2/4
				s1 * 1/2
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 2/4
				s1 * 1/2
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 2/4
				s1 * 1/2
			}
		}
		\context StaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context StringPerformerStaffGroup = "Violin Staff Group" <<
					\context FingeringStaff = "Violin Staff" <<
						\clef "treble"
						\context FingeringVoice = "Violin Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									\afterGrace
									c'32 ]
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 4/5 {
									\afterGrace
									r8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								\times 4/5 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
								}
								{
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r32
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 4/5 {
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemRightBeamCount = 1
									c'8.
								}
							}
						}
					>>
				>>
			>>
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context StringPerformerStaffGroup = "Viola Staff Group" <<
					\context FingeringStaff = "Viola Staff" <<
						\clef "alto"
						\context FingeringVoice = "Viola Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									\afterGrace
									c'32 ]
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16 ~
								}
								\times 4/5 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 4/5 {
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
								}
								\times 4/5 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
									r8
								}
								{
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									r8
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\afterGrace
									r8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									r8
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
							}
						}
					>>
				>>
			>>
			\context CelloStaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context StringPerformerStaffGroup = "Cello Staff Group" <<
					\context FingeringStaff = "Cello Staff" <<
						\clef "bass"
						\context FingeringVoice = "Cello Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r32
									r8
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r4
								}
							}
							{
								\times 2/3 {
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									r4
								}
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\times 2/3 {
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
									\bar "||"
								}
							}
						}
					>>
				>>
			>>
		>>
	>>
}