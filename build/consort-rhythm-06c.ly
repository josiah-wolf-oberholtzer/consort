	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "B6c" " " \fontsize #-3 "rotating rhythm patterns (3)" }
				\tempo 8=72
				\time 2/4
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
		\context OuterStaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context PerformerStaffGroup = "Violin Staff Group" <<
					\context LHStaff = "Violin Staff" <<
						\clef "percussion"
						\context LHVoice = "Violin Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
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
								{
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
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
									r16
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
									c'8. [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
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
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8. [
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
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
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
									c'8 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
						}
						\context InnerAnnotation = "Violin Voice Inner Annotation" {
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
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
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
						}
					>>
				>>
			>>
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context PerformerStaffGroup = "Viola Staff Group" <<
					\context LHStaff = "Viola Staff" <<
						\clef "percussion"
						\context LHVoice = "Viola Voice" {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
								}
								{
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8. ]
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
								{
									r8
								}
							}
							{
								\times 2/3 {
									r8
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
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r4
								}
								{
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
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
									r16
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
									c'8. [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
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
									r8
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
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							c'1 * 1/8
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
				\context PerformerStaffGroup = "Cello Staff Group" <<
					\context LHStaff = "Cello Staff" <<
						\clef "percussion"
						\context LHVoice = "Cello Voice" {
							{
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									r16
								}
								{
									r8.
								}
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
									c'8 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
								}
								{
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8. ]
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
									r4
								}
							}
							{
								\times 2/3 {
									r8
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
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r4
								}
								{
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
}

	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "B6c" " " \fontsize #-3 "rotating rhythm patterns (3)" }
				\tempo 8=72
				\time 2/4
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
		\context OuterStaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context PerformerStaffGroup = "Violin Staff Group" <<
					\context LHStaff = "Violin Staff" <<
						\clef "percussion"
						\context LHVoice = "Violin Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
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
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
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
									r16
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
									c'8. [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
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
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
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
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
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
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
						}
						\context InnerAnnotation = "Violin Voice Inner Annotation" {
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
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
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
						}
					>>
				>>
			>>
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context PerformerStaffGroup = "Viola Staff Group" <<
					\context LHStaff = "Viola Staff" <<
						\clef "percussion"
						\context LHVoice = "Viola Voice" {
							{
								{
									r8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
								}
								{
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8. ]
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
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
								\times 2/3 {
									r8
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
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
									r8
								}
							}
							{
								\times 2/3 {
									r16
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
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									r8
									r4
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
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							c'1 * 1/8
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
				\context PerformerStaffGroup = "Cello Staff Group" <<
					\context LHStaff = "Cello Staff" <<
						\clef "percussion"
						\context LHVoice = "Cello Voice" {
							{
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
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
									\stopStaff
									\once \override Staff.StaffSymbol.line-count = 1
									\startStaff
									R1 * 7/16
									\stopStaff
									\startStaff
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
								}
								{
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
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
									r4
								}
							}
							{
								\times 2/3 {
									r8
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
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r4
								}
								{
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
}

	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "B6c" " " \fontsize #-3 "rotating rhythm patterns (3)" }
				\tempo 8=72
				\time 2/4
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
		\context OuterStaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context PerformerStaffGroup = "Violin Staff Group" <<
					\context LHStaff = "Violin Staff" <<
						\clef "percussion"
						\context LHVoice = "Violin Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
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
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
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
									r16
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
									c'8. [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
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
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
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
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
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
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
						}
					>>
				>>
			>>
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context PerformerStaffGroup = "Viola Staff Group" <<
					\context LHStaff = "Viola Staff" <<
						\clef "percussion"
						\context LHVoice = "Viola Voice" {
							{
								{
									r8.
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
								}
								{
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8. ]
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
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
								\times 2/3 {
									r8
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
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r8
									r8
								}
							}
							{
								\times 2/3 {
									r16
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
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
								}
							}
							{
								{
									r8
									r4
								}
							}
						}
					>>
				>>
			>>
			\context CelloStaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context PerformerStaffGroup = "Cello Staff Group" <<
					\context LHStaff = "Cello Staff" <<
						\clef "percussion"
						\context LHVoice = "Cello Voice" {
							{
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
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
									\stopStaff
									\once \override Staff.StaffSymbol.line-count = 1
									\startStaff
									R1 * 7/16
									\stopStaff
									\startStaff
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									r16
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
								}
								{
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									r4
								}
							}
							{
								\times 2/3 {
									r8
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
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16 ~
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r4
								}
								{
									r8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
