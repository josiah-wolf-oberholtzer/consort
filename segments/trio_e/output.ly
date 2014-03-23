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
				\time 2/4
				\tempo 8=72
				\mark \markup { \override #'(box-padding . 0.5) \box "E" " " \fontsize #-3 "a string trio" }
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
		\context OuterStaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context PerformerStaffGroup = "Violin Staff Group" <<
					\context LHStaff = "Violin Staff" <<
						\clef "treble"
						\context LHVoice = "Violin Voice" {
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
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] \! )
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
									c'16 \ppp ~ [ \startTrillSpan f'
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
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
									c'8 ] ] )
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
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] )
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\pitchedTrill
									c'8 \ppp ~ [ \startTrillSpan f'
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
									<> \stopTrillSpan
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
									c'8 ] ] )
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ] )
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ] )
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									\pitchedTrill
									c'8 \ppp ~ [ \startTrillSpan f'
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
									<> \stopTrillSpan
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
									c'8 ] ] )
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
									c'8 ] ] )
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
									c'16 \ppp ~ [ \startTrillSpan f'
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
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
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] )
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
									c'8 ] ] )
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
									c'4 \ppp \startTrillSpan f'
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
			\context ViolaStaffGroup = "Viola Staff Group" <<
				\tag #'Viola
				\context PerformerStaffGroup = "Viola Staff Group" <<
					\context LHStaff = "Viola Staff" <<
						\clef "alto"
						\context LHVoice = "Viola Voice" {
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ] )
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
									c'8. \ppp \startTrillSpan f'
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] )
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
									c'8 \ppp \startTrillSpan f'
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
									c'16 -\accent [ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] )
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
									c'8 \ppp ~ [ \startTrillSpan f'
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
									<> \stopTrillSpan
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
									c'8 ] ] )
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] )
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
									c'16 \ppp ~ [ \startTrillSpan f'
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
									<> \stopTrillSpan
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
									c'8 ] ] )
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
									c'16 -\accent [ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] )
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
									c'8 \ppp \startTrillSpan f'
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ] )
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
						\clef "bass"
						\context LHVoice = "Cello Voice" {
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
									c'16 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] )
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
									c'8 -\accent \fp
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
									c'8 -\accent [ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8.
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ] \! )
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
									c'16 -\accent [ [ \< \fp (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16 ~
								}
								\times 4/5 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8.
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] \fff )
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
									c'8 -\accent \sfz [ [ (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] )
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
									c'16 -\accent \fp [ [ (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #0
									c'8 ] ] )
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
									c'8 -\accent [ ~ [ \> \sfz (
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16
								}
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #1
									c'8
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] \! )
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
									c'8 -\accent [ [ \< \fp (
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 1
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #1
									c'16 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #1
									\set stemRightBeamCount = #2
									c'16 ~
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #2
									c'16
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									\set stemLeftBeamCount = #2
									\set stemRightBeamCount = #0
									c'16 ] ] \fff )
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