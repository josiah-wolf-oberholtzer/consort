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
				\mark \markup { \override #'(box-padding . 0.5) \box "C1" }
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
					\context LHStaff = "Violin Staff" {
						\clef "treble"
						\context LHVoice = "Violin Voice" {
							{
								{
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'8 ]
								}
								{
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'16
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
								\times 2/3 {
									r16
									c'8
								}
								{
									c'8 ~ [
									c'16
									c'16 ]
								}
							}
							{
								{
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'16 ~
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'16 ]
								}
								{
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
									c'16 [
									c'16 ~
									c'16
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
									c'8 [
									c'16 ]
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
									c'8. [
									c'16 ]
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
									r8
								}
							}
							{
								\times 2/3 {
									r8
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								{
									c'8 [
									c'16
									c'16 ]
								}
							}
							{
								{
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									c'16 [
									c'8 ]
								}
							}
							{
								{
									r8
								}
								{
									\stopStaff
									\once \override Staff.StaffSymbol.line-count = 1
									\startStaff
									\afterGrace
									R1 * 3/8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\stopStaff
									\startStaff
								}
							}
							{
								{
									c'8 [
									\afterGrace
									c'8 ]
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								{
									c'16 [
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								{
									c'8. [
									c'16 ]
								}
							}
							{
								{
									r16
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
									r4
								}
								{
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									c'16 [
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'16 ]
								}
								{
									c'16 ~ [
									c'16
									c'16 ]
								}
							}
							{
								{
									r8
									r4
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
									r4
								}
							}
							{
								{
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r8.
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									c'16
								}
							}
							{
								{
									\afterGrace
									r8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									c'8 ~ [
									c'16
									c'16 ]
								}
								{
									c'8 [
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
									r8
									c'16
								}
								{
									c'8 [
									c'16
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
									c'16 [
									c'8 ]
								}
							}
							{
								{
									r4
								}
								{
									\afterGrace
									r4
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
							}
							{
								{
									\afterGrace
									c'8 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'8 ]
								}
								{
									\afterGrace
									c'16 [
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'16
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
									\afterGrace
									r16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\afterGrace
									c'8
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
								}
								{
									c'8 ~ [
									\afterGrace
									c'16
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									c'16 ]
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