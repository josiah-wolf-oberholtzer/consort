	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 2/4
				\tempo 8=72
				\mark \markup { \override #'(box-padding . 0.5) \box "D" " " \fontsize #-3 "a string trio" }
				s1 * 1/2
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				s1 * 7/16
			}
			{
				\time 2/4
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				\time 7/16
				s1 * 7/16
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				\time 2/4
				s1 * 1/2
			}
			{
				\time 5/16
				s1 * 5/16
			}
		}
		\context StaffGroup = "Outer Staff Group" <<
			\context StaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context StringPerformerStaffGroup = "Violin Staff Group" <<
					\context FingeringStaff = "Violin Staff" <<
						\clef "treble"
						\context FingeringVoice = "Violin Voice" {
							{
								\times 4/5 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r16
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
									r8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									c'8 [ ~ [
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									c'8 [ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
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
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r8
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
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ]
								}
							}
							{
								{
									r16
								}
								{
									r8.
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
									r16
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
									r8
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									c'8 [ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ]
								}
							}
							{
								{
									r8.
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r16
								}
							}
							{
								{
									c'4
								}
							}
							{
								{
									r16
								}
							}
						}
						\context InnerAnnotation = "Violin Voice Inner Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
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
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
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
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
						}
					>>
				>>
			>>
			\context StaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context StringPerformerStaffGroup = "Viola Staff Group" <<
					\context FingeringStaff = "Viola Staff" <<
						\clef "alto"
						\context FingeringVoice = "Viola Voice" {
							{
								{
									r8
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
									r16
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
									r8
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r8
								}
								{
									r16
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
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r8
								}
								{
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									c'8 [ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r8
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/5 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ]
								}
							}
							{
								{
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r16
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
									r16
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
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							c'1 * 3/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\override TupletBracket #'color = #blue
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/8 {
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
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
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
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							c'1 * 3/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #blue
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/8 {
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
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
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
							c'1 * 1/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
						}
					>>
				>>
			>>
			\context StaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context StringPerformerStaffGroup = "Cello Staff Group" <<
					\context FingeringStaff = "Cello Staff" <<
						\clef "bass"
						\context FingeringVoice = "Cello Voice" {
							{
								{
									r4
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									c'8 [ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ]
								}
							}
							{
								{
									r16
								}
								{
									r8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									c'8 [ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/5 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8.
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r4
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r8
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
									r16
								}
								{
									r8.
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									c'8 [ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ]
								}
							}
							{
								{
									r8.
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 [ ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16
								}
								\times 2/3 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ]
								}
							}
							{
								{
									r8
								}
							}
						}
						\context InnerAnnotation = "Cello Voice Inner Annotation" {
							c'1 * 1/4
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
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							c'1 * 1/4
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
							\bar "||"
						}
					>>
				>>
			>>
		>>
	>>

