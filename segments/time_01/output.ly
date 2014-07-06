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
	\context Score = "Score" \with {
		\override BarLine #'transparent = ##t
		\override Beam #'transparent = ##t
		\override Dots #'transparent = ##t
		\override Flag #'transparent = ##t
		\override NoteHead #'transparent = ##t
		\override Rest #'transparent = ##t
		\override SpanBar #'transparent = ##t
		\override Stem #'transparent = ##t
		\override Tie #'transparent = ##t
		\override TupletBracket #'transparent = ##t
		\override TupletNumber #'transparent = ##t
	} <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 2/4
				\tempo 8=72
				\mark \markup { \override #'(box-padding . 0.5) \box "A1" " " \fontsize #-3 "spans of time" }
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\bar "||"
						}
					>>
				>>
			>>
		>>
	>>
}

\score {
	\context Score = "Score" \with {
		\override BarLine #'transparent = ##t
		\override Beam #'transparent = ##t
		\override Dots #'transparent = ##t
		\override Flag #'transparent = ##t
		\override NoteHead #'transparent = ##t
		\override Rest #'transparent = ##t
		\override SpanBar #'transparent = ##t
		\override Stem #'transparent = ##t
		\override Tie #'transparent = ##t
		\override TupletNumber #'transparent = ##t
	} <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 2/4
				\tempo 8=72
				\mark \markup { \override #'(box-padding . 0.5) \box "A1" " " \fontsize #-3 "spans of time" }
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\bar "||"
						}
					>>
				>>
			>>
		>>
	>>
}

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
				\time 2/4
				\tempo 8=72
				\mark \markup { \override #'(box-padding . 0.5) \box "A1" " " \fontsize #-3 "spans of time" }
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
				\mark \markup { \override #'(box-padding . 0.5) \box "A1" " " \fontsize #-3 "spans of time" }
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Viola Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
									c'4
								}
							}
							{
								{
									r4
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
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
						}
						\context OuterAnnotation = "Cello Voice Outer Annotation" {
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/4 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
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
				\mark \markup { \override #'(box-padding . 0.5) \box "A1" " " \fontsize #-3 "spans of time" }
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
				s1 * 1/2
			}
			{
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
									c'4
								}
							}
							{
								{
									r4
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
									c'4
								}
							}
							{
								{
									r4
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
									c'4
								}
							}
							{
								{
									r4
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