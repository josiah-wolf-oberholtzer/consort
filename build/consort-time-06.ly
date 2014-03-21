	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "A6" }
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
		\context OuterStaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context PerformerStaffGroup = "Violin Staff Group" <<
					\context LHStaff = "Violin Staff" <<
						\clef "percussion"
						\context LHVoice = "Violin Voice" {
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
						\context InnerAnnotation = "Violin Voice Inner Annotation" {
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/8 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/8
							\times 1/4 {
								c'1
							}
							\times 1/8 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							\times 1/4 {
								c'1
							}
							c'1 * 1/16
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/16
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\times 1/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/8 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
								c'1
							}
							c'1 * 1/16
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/16
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
									\set stemRightBeamCount = 1
									c'8. -\accent
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
						\context InnerAnnotation = "Viola Voice Inner Annotation" {
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							\times 1/4 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							\times 1/8 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/16
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/4 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/16
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/16 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/16
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/16
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
								}
							}
						}
						\context InnerAnnotation = "Cello Voice Inner Annotation" {
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/16
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/4 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							\times 1/4 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							\times 1/8 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/16
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/16 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\times 1/8 {
								c'1
							}
							c'1 * 1/8
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\times 1/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/8
							\bar "||"
						}
					>>
				>>
			>>
		>>
	>>
