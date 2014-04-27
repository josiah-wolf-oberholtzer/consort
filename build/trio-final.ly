	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 2/4
				\tempo 8=72
				\mark \markup { \override #'(box-padding . 0.5) \box "F" " " \fontsize #-3 "a string trio" }
				s1 * 1/2
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
				\time 5/16
				s1 * 5/16
			}
		}
		\context StaffGroup = "Outer Staff Group" <<
			\context StaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context StringPerformerStaffGroup = "Violin Staff Group" <<
					\context FingeringStaff = "Violin Staff" <<
						\clef "treble"
						\context FingeringVoice = "Violin Voice" {
							{
								\times 4/5 {
									\override Hairpin #'circled-tip = ##t
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 -\accent [ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									cs''8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									b'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									f''16 ] ] \! )
									\revert Hairpin #'circled-tip
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
									\pitchedTrill
									cs''16 \ppp ~ [ \startTrillSpan fs''
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									cs''16 ]
									<> \stopTrillSpan
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									cs''8 ] ] )
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									cs''16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									cs''16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									b'16 ] ] )
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\pitchedTrill
									e'''8 \ppp ~ [ \startTrillSpan a'''
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									e'''8 ]
									<> \stopTrillSpan
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									b'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									a'8 ] ] )
								}
							}
							{
								{
									r4
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									b'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									a'8 ] ] )
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									d'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									af'8 ] ] )
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\pitchedTrill
									cs''8 \ppp ~ [ \startTrillSpan fs''
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									cs''16 ]
									<> \stopTrillSpan
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									d'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									af'8 ] ] )
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									f''8 ] ] )
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
									\pitchedTrill
									e'''16 \ppp ~ [ \startTrillSpan a'''
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									e'''16 ]
									<> \stopTrillSpan
								}
							}
							{
								{
									r16
									r8
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									f''16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									f''16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									ef'16 ] ] )
								}
							}
							{
								{
									r8.
									r16
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									f''8 ] ] )
								}
							}
							{
								{
									r16
								}
							}
							{
								{
									\pitchedTrill
									cs''4 \ppp \startTrillSpan fs''
									<> \stopTrillSpan
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
						\clef "alto"
						\context FingeringVoice = "Viola Voice" {
							{
								{
									r8
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									cs'8 ] ] )
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
									\pitchedTrill
									cs'8. \ppp \startTrillSpan fs'
									<> \stopTrillSpan
								}
							}
							{
								{
									r8
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									cs'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									cs'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									b16 ] ] )
								}
							}
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
									\set stemRightBeamCount = 1
									\pitchedTrill
									e''8 \ppp \startTrillSpan a''
									<> \stopTrillSpan
								}
							}
							{
								{
									r8
									r16
								}
							}
							{
								\times 4/5 {
									\override Hairpin #'circled-tip = ##t
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									b16 -\accent [ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									a8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									b16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									a16 ] ] \! )
									\revert Hairpin #'circled-tip
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									b16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									a16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									a16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									b16 ] ] )
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
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\pitchedTrill
									cs'8 \ppp ~ [ \startTrillSpan fs'
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									cs'8 ]
									<> \stopTrillSpan
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									d16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									f'8 ] ] )
								}
							}
							{
								{
									r8
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									f'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									f'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									ef16 ] ] )
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
									\pitchedTrill
									e''16 \ppp ~ [ \startTrillSpan a''
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									e''8 ]
									<> \stopTrillSpan
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									f'8 ] ] )
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 4/5 {
									\override Hairpin #'circled-tip = ##t
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c16 -\accent [ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									f'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									ef16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] \! )
									\revert Hairpin #'circled-tip
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									f16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									ef'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									ef'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c16 ] ] )
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
									\pitchedTrill
									cs'8 \ppp \startTrillSpan fs'
									<> \stopTrillSpan
								}
							}
							{
								{
									r16
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									f'8 ] ] )
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
						\clef "bass"
						\context FingeringVoice = "Cello Voice" {
							{
								{
									r4
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									c,16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									cs16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									cs16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									b,16 ] ] )
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
								{
									\set stemRightBeamCount = 1
									f8 -\accent \fp
								}
							}
							{
								{
									r8
								}
							}
							{
								\times 4/5 {
									\override Hairpin #'circled-tip = ##t
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									d,8 -\accent [ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									ef8.
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									b,16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									a,8 ] ] \! )
									\revert Hairpin #'circled-tip
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
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									b,16 -\accent [ [ \< \fp (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									a,16 ~
								}
								\times 4/5 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									a,16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									f8.
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									e,16 ] ] \fff )
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
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									d,8 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									af,16 ] ] )
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #2
									ef16 -\accent \fp [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c,8 ] ] )
								}
							}
							{
								{
									r8
								}
							}
							{
								{
									\override Hairpin #'circled-tip = ##t
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									f,8 -\accent [ ~ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									f,16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									ef16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c,8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									f16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									ef,16 ] ] \! )
									\revert Hairpin #'circled-tip
								}
							}
							{
								{
									r8.
									r16
								}
							}
							{
								\times 2/3 {
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #0
									\set stemRightBeamCount = #1
									c8 -\accent [ [ \< \fp (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									f,16 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									f,16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									f,16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									ef16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c,16 ] ] \fff )
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

