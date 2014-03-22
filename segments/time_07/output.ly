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
				\mark \markup { \override #'(box-padding . 0.5) \box "A7" " " \fontsize #-3 "desynchronizing blue timespan releases" }
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
				\time 5/8
				s1 * 5/8
			}
			{
				\time 5/16
				s1 * 5/16
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
						\context LHVoice = "Violin Voice" \with {
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
								}
								{
									r8
									r16
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16.
								}
							}
							{
								{
									r32
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
									c'8
								}
							}
							{
								{
									r8.
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
									c'8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
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
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/32
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\times 1/8 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/32
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
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
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\times 1/8 {
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
									\set stemRightBeamCount = 1
									c'8
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
									c'8
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\set stemRightBeamCount = 3
									c'32
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
							}
							{
								{
									c'4
								}
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\times 1/8 {
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
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/32 {
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\times 1/8 {
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/32 {
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
									\set stemRightBeamCount = 2
									c'16.
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
									\set stemRightBeamCount = 1
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
									\set stemRightBeamCount = 2
									c'16
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
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
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
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
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
									c'8
								}
							}
							{
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. ~ [
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
									c'8
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/32 {
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
							\times 1/8 {
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/32 {
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
							\times 1/8 {
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
				\mark \markup { \override #'(box-padding . 0.5) \box "A7" " " \fontsize #-3 "desynchronizing blue timespan releases" }
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
				\time 5/8
				s1 * 5/8
			}
			{
				\time 5/16
				s1 * 5/16
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
								}
								{
									r8
									r16
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16.
								}
							}
							{
								{
									r32
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
									c'8
								}
							}
							{
								{
									r8.
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
									c'8
								}
							}
							{
								{
									\set stemRightBeamCount = 1
									c'8
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
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/32
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\times 1/8 {
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
							c'1 * 1/8
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/32
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
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
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\times 1/8 {
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
									c'8
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
									c'8
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\set stemRightBeamCount = 3
									c'32
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
							}
							{
								{
									c'4
								}
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\times 1/8 {
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
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/32 {
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\times 1/8 {
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\times 1/32 {
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
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
									\set stemRightBeamCount = 2
									c'16.
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
									\set stemRightBeamCount = 1
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
									\set stemRightBeamCount = 2
									c'16
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
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
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
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
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
									c'8
								}
							}
							{
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. ~ [
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
									c'8
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/32 {
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
							\times 1/8 {
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0.7 . 0)
							\times 1/16 {
								c'1
							}
							\revert TupletBracket #'color
							\revert TupletBracket #'edge-height
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
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 3/16
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
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #red
							\override TupletBracket #'edge-height = #'(0 . 0.7)
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 5/32 {
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
							\times 1/8 {
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
				\mark \markup { \override #'(box-padding . 0.5) \box "A7" " " \fontsize #-3 "desynchronizing blue timespan releases" }
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
				\time 5/8
				s1 * 5/8
			}
			{
				\time 5/16
				s1 * 5/16
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
								}
								{
									r8
									r16
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
									c'8 -\accent
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
									r8
								}
							}
							{
								{
									\set stemRightBeamCount = 2
									c'16. -\accent
								}
							}
							{
								{
									r32
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
									c'8 -\accent
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
									c'8 -\accent
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
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context PerformerStaffGroup = "Viola Staff Group" <<
					\context LHStaff = "Viola Staff" <<
						\clef "percussion"
						\context LHVoice = "Viola Voice" {
							{
								{
									\set stemRightBeamCount = 1
									c'8 -\accent
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
									c'8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
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
									c'8 -\accent
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent ~ [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\set stemRightBeamCount = 3
									c'32
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
									c'4
								}
								{
									\set stemLeftBeamCount = -1
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
									\set stemRightBeamCount = 2
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
									\set stemRightBeamCount = 1
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
									\set stemRightBeamCount = 2
									c'16
								}
							}
							{
								{
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
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
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
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
									c'8 -\accent
								}
							}
							{
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent ~ [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. ~ [
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
									c'8 -\accent
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