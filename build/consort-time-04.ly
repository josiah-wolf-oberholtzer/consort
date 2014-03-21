	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "A4" }
				\tempo 8=72
				\time 7/16
				s1 * 7/16
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				s1 * 3/8
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
					\context LHStaff = "Violin Staff" {
						\clef "treble"
						\context LHVoice = "Violin Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8. ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									r4
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
									\set stemRightBeamCount = 1
									c'8 ~
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
									c'4
								}
							}
						}
					}
				>>
			>>
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context PerformerStaffGroup = "Viola Staff Group" <<
					\context LHStaff = "Viola Staff" {
						\clef "alto"
						\context LHVoice = "Viola Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8. ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									r4
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
									\set stemRightBeamCount = 1
									c'8 ~
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
									c'4
								}
							}
						}
					}
				>>
			>>
			\context CelloStaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context PerformerStaffGroup = "Cello Staff Group" <<
					\context LHStaff = "Cello Staff" {
						\clef "bass"
						\context LHVoice = "Cello Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8. ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									c'16
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
									r4
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
									\set stemRightBeamCount = 1
									c'8 ~
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
									c'4
									\bar "||"
								}
							}
						}
					}
				>>
			>>
		>>
	>>
