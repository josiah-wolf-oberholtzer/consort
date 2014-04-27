	\context Score = "Score" \with {
		\override Beam #'transparent = ##t
		\override Dots #'transparent = ##t
		\override Flag #'transparent = ##t
		\override NoteHead #'transparent = ##t
		\override Rest #'transparent = ##t
		\override Stem #'transparent = ##t
		\override Tie #'transparent = ##t
		\override TupletNumber #'transparent = ##t
	} <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "A6" " " \fontsize #-3 "overlaying red timespans with blue" }
				\tempo 8=72
				\time 3/4
				s1 * 3/4
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
				s1 * 1/2
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
				\time 5/16
				s1 * 5/16
			}
		}
		\context StaffGroup = "Outer Staff Group" <<
			\context StaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context StringPerformerStaffGroup = "Violin Staff Group" <<
					\context FingeringStaff = "Violin Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Violin Voice" \with {
							\override TupletBracket #'transparent = ##t
						} {
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8. ]
								}
							}
							{
								{
									r16
									r8.
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
									\set stemRightBeamCount = 1
									c'8.
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
								{
									\set stemRightBeamCount = 1
									c'8.
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
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
									r16
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
								{
									c'4
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
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									r4
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
								{
									\set stemRightBeamCount = 1
									c'8.
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
									r16
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
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
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
							\override TupletBracket #'color = #red
							\times 1/4 {
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
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
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
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/16
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
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
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
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
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
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
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/16
						}
					>>
				>>
			>>
			\context StaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context StringPerformerStaffGroup = "Viola Staff Group" <<
					\context FingeringStaff = "Viola Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Viola Voice" \with {
							\override TupletBracket #'transparent = ##t
						} {
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16
								}
								{
									c'4
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
								{
									\set stemRightBeamCount = 1
									c'8.
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
									\set stemRightBeamCount = 2
									c'16
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
									c'8 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									r4
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
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8.
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									r16
								}
							}
						}
						\context InnerAnnotation = "Viola Voice Inner Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							\times 1/16 {
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
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/16
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/4 {
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
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/16
						}
					>>
				>>
			>>
			\context StaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context StringPerformerStaffGroup = "Cello Staff Group" <<
					\context FingeringStaff = "Cello Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Cello Voice" \with {
							\override TupletBracket #'transparent = ##t
						} {
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
									r8.
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
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									c'4
								}
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
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16
								}
								{
									c'4
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
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									r16
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
								{
									\set stemRightBeamCount = 1
									c'8.
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
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
						}
						\context InnerAnnotation = "Cello Voice Inner Annotation" {
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							\times 1/16 {
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
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/4 {
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
							\bar "||"
						}
					>>
				>>
			>>
		>>
	>>

	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "A6" " " \fontsize #-3 "overlaying red timespans with blue" }
				\tempo 8=72
				\time 3/4
				s1 * 3/4
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
				s1 * 1/2
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
				\time 5/16
				s1 * 5/16
			}
		}
		\context StaffGroup = "Outer Staff Group" <<
			\context StaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context StringPerformerStaffGroup = "Violin Staff Group" <<
					\context FingeringStaff = "Violin Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Violin Voice" {
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8. ]
								}
							}
							{
								{
									r16
									r8.
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
									\set stemRightBeamCount = 1
									c'8.
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
								{
									\set stemRightBeamCount = 1
									c'8.
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
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
									r16
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
								}
								{
									c'4
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
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									r4
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
								{
									\set stemRightBeamCount = 1
									c'8.
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
									r16
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
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
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
							\override TupletBracket #'color = #red
							\times 1/4 {
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
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
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
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/16
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
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
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
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
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
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
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/16
						}
					>>
				>>
			>>
			\context StaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context StringPerformerStaffGroup = "Viola Staff Group" <<
					\context FingeringStaff = "Viola Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Viola Voice" {
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16
								}
								{
									c'4
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
								{
									\set stemRightBeamCount = 1
									c'8.
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
									\set stemRightBeamCount = 2
									c'16
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
									c'8 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									r4
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
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8.
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									r16
								}
							}
						}
						\context InnerAnnotation = "Viola Voice Inner Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							\times 1/16 {
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
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/16
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/4 {
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
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/16
						}
					>>
				>>
			>>
			\context StaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context StringPerformerStaffGroup = "Cello Staff Group" <<
					\context FingeringStaff = "Cello Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Cello Voice" {
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
									r8.
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
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									c'4
								}
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
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16
								}
								{
									c'4
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
									\set stemRightBeamCount = 1
									c'8.
								}
							}
							{
								{
									r16
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
								{
									\set stemRightBeamCount = 1
									c'8.
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
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
						}
						\context InnerAnnotation = "Cello Voice Inner Annotation" {
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							\times 1/16 {
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
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
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
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
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
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/4 {
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
							\bar "||"
						}
					>>
				>>
			>>
		>>
	>>

	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "A6" " " \fontsize #-3 "overlaying red timespans with blue" }
				\tempo 8=72
				\time 3/4
				s1 * 3/4
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
				s1 * 1/2
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
				\time 5/16
				s1 * 5/16
			}
		}
		\context StaffGroup = "Outer Staff Group" <<
			\context StaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context StringPerformerStaffGroup = "Violin Staff Group" <<
					\context FingeringStaff = "Violin Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Violin Voice" {
							{
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8. ]
								}
							}
							{
								{
									r16
									r8.
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
									\set stemRightBeamCount = 1
									c'8. -\accent
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
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
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
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
								}
							}
							{
								{
									r16
								}
								{
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8
								}
								{
									c'4
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
									c'8. -\accent
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
									r4
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
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
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
									r16
								}
							}
						}
					>>
				>>
			>>
			\context StaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context StringPerformerStaffGroup = "Viola Staff Group" <<
					\context FingeringStaff = "Viola Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Viola Voice" {
							{
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16
								}
								{
									c'4
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
									\set stemRightBeamCount = 1
									c'8. -\accent
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
									\set stemRightBeamCount = 1
									c'8. -\accent
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
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
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
									r4
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
									\set stemRightBeamCount = 1
									c'8. -\accent
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8.
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
									c'8. -\accent
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
									r16
								}
							}
						}
					>>
				>>
			>>
			\context StaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context StringPerformerStaffGroup = "Cello Staff Group" <<
					\context FingeringStaff = "Cello Staff" <<
						\clef "percussion"
						\context FingeringVoice = "Cello Voice" {
							{
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
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
									r16
									r8.
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
									\set stemRightBeamCount = 1
									c'8. -\accent
								}
							}
							{
								{
									c'4
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8.
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
									c'8. -\accent
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16
								}
								{
									c'4
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
									\set stemRightBeamCount = 1
									c'8. -\accent
								}
							}
							{
								{
									r16
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
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
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
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8. -\accent
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

