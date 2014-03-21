\version "2.19.3"
\language "english"

#(ly:set-option 'relative-includes #t)

\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-header.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-paper.ily"

\score {
	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "A8" }
				\tempo 8=72
				\time 2/4
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
		\context OuterStaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context PerformerStaffGroup = "Violin Staff Group" <<
					\context LHStaff = "Violin Staff" {
						\clef "treble"
						\context LHVoice = "Violin Voice" {
							{
								{
									c'8. -\accent
								}
							}
							{
								{
									c'16
								}
							}
							{
								{
									c'8.
								}
							}
							{
								{
									r16
								}
								{
									r8
									r16
								}
							}
							{
								{
									c'16
								}
							}
							{
								{
									c'8 -\accent
								}
							}
							{
								{
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
									c'8 ~ [
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
							{
								{
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
									c'8
								}
							}
							{
								{
									c'8 ~ [
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
									c'8.
								}
							}
							{
								{
									c'16. -\accent
								}
							}
							{
								{
									r32
									r8
								}
							}
							{
								{
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
									c'8 -\accent
								}
							}
							{
								{
									c'8
								}
							}
							{
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
									c'8
								}
							}
							{
								{
									c'8 -\accent ~ [
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
							{
								{
									c'16 ~ [
									c'8 ]
								}
							}
							{
								{
									r8
									r8
								}
							}
							{
								{
									c'8
								}
							}
							{
								{
									c'8. ~ [
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
									c'16 ~ [
									c'8 ]
								}
							}
							{
								{
									r8
									r8
								}
							}
							{
								{
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
									c'16
								}
							}
							{
								{
									c'8 -\accent
								}
							}
							{
								{
									c'16
								}
							}
							{
								{
									c'16 ~ [
									c'8 ]
								}
							}
							{
								{
									r8
									r8
								}
							}
							{
								{
									c'8
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
									c'16. -\accent
								}
							}
							{
								{
									r32
									r8
								}
							}
							{
								{
									c'8.
								}
							}
							{
								{
									r16
								}
								{
									r8
									r16
								}
							}
							{
								{
									c'16
								}
							}
							{
								{
									c'8 -\accent
								}
							}
							{
								{
									r16
								}
							}
							{
								{
									c'8 ~ [
									c'8 ]
								}
							}
							{
								{
									c'8 ~ [
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
									c'8
								}
							}
							{
								{
									c'8 ~ [
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
							{
								{
									c'8.
								}
							}
							{
								{
									c'8 -\accent ~ [
									c'16 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								{
									c'8
								}
							}
							{
								{
									c'8 ~ [
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
					}
				>>
			>>
		>>
	>>
}