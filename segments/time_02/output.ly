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
				\mark \markup { \override #'(box-padding . 0.5) \box "A2" }
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
									c'4
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
									r4
								}
							}
							{
								{
									c'4
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
									r4
								}
							}
							{
								{
									c'4
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
									r4
								}
							}
						}
						\context InnerAnnotation = "Violin Voice Inner Annotation" {
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
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
									c'4
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
									r4
								}
							}
							{
								{
									c'4
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
									r4
								}
							}
							{
								{
									c'4
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
									r4
								}
							}
						}
						\context InnerAnnotation = "Viola Voice Inner Annotation" {
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
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
									c'4
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
									r4
								}
							}
							{
								{
									c'4
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
									r4
								}
							}
							{
								{
									c'4
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
									r4
								}
							}
						}
						\context InnerAnnotation = "Cello Voice Inner Annotation" {
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\times 1/4 {
								c'1
							}
							c'1 * 1/4
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							c'1 * 1/4
							\times 1/8 {
								c'1
							}
							c'1 * 1/4
							\bar "||"
						}
					>>
				>>
			>>
		>>
	>>
}