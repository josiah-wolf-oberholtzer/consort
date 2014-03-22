\version "2.19.3"
\language "english"

#(ly:set-option 'relative-includes #t)

\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-header.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-layout.ily"
\include "/Users/josiah/Documents/Scores/consort/stylesheets/consort-paper.ily"

\score {
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
				\mark \markup { \override #'(box-padding . 0.5) \box "A3" " " \fontsize #-3 "different silences: 1/4 and 1/8" }
				\tempo 8=72
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
						\context LHVoice = "Violin Voice" \with {
							\override TupletBracket #'transparent = ##t
						} {
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
						}
						\context InnerAnnotation = "Violin Voice Inner Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
						}
					>>
				>>
			>>
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context PerformerStaffGroup = "Viola Staff Group" <<
					\context LHStaff = "Viola Staff" <<
						\clef "percussion"
						\context LHVoice = "Viola Voice" \with {
							\override TupletBracket #'transparent = ##t
						} {
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
						}
						\context InnerAnnotation = "Viola Voice Inner Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
						}
					>>
				>>
			>>
			\context CelloStaffGroup = "Cello Staff Group" <<
				\tag #'Cello
				\context PerformerStaffGroup = "Cello Staff Group" <<
					\context LHStaff = "Cello Staff" <<
						\clef "percussion"
						\context LHVoice = "Cello Voice" \with {
							\override TupletBracket #'transparent = ##t
						} {
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
						}
						\context InnerAnnotation = "Cello Voice Inner Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
								\bar "||"
							}
							\revert TupletBracket #'color
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
				\mark \markup { \override #'(box-padding . 0.5) \box "A3" " " \fontsize #-3 "different silences: 1/4 and 1/8" }
				\tempo 8=72
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
						}
						\context InnerAnnotation = "Violin Voice Inner Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
						}
						\context InnerAnnotation = "Viola Voice Inner Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
								}
							}
						}
						\context InnerAnnotation = "Cello Voice Inner Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
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
							c'1 * 1/4
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
								\bar "||"
							}
							\revert TupletBracket #'color
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
				\mark \markup { \override #'(box-padding . 0.5) \box "A3" " " \fontsize #-3 "different silences: 1/4 and 1/8" }
				\tempo 8=72
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
									r8
								}
							}
							{
								{
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8.
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