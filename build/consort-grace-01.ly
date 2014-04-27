	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "C1" " " \fontsize #-3 "adding grace notes (every red attack)" }
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
		\context StaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context PerformerStaffGroup = "Violin Staff Group" <<
					\context LHStaff = "Violin Staff" <<
						\clef "percussion"
						\context LHVoice = "Violin Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\times 2/3 {
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
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\times 2/3 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r32
									r8
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
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/16
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
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/32
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
						}
						\context OuterAnnotation = "Violin Voice Outer Annotation" {
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/16
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/8
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
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
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/32 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 5/32
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
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
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
								\times 2/3 {
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
									\set stemRightBeamCount = 1
									c'8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r8
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
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
									\set stemRightBeamCount = 1
									c'8
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
							c'1 * 1/4
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
							c'1 * 3/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
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
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
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
							c'1 * 3/16
							\override TupletBracket #'color = #blue
							\times 1/8 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r32
									r8
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\times 2/3 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\times 2/3 {
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
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
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
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
							c'1 * 5/16
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
							c'1 * 1/4
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
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
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
							c'1 * 5/16
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
							c'1 * 1/4
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
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
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 7/16 {
								c'1
							}
							\revert TupletBracket #'color
							\override TupletBracket #'color = #blue
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/16 {
								c'1
							}
							\revert TupletBracket #'color
							c'1 * 1/16
							\override TupletBracket #'color = #red
							\tweak #'text #tuplet-number::calc-fraction-text
							\times 3/8 {
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

	\context Score = "Score" <<
		\tag #'(Violin Viola Cello)
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\mark \markup { \override #'(box-padding . 0.5) \box "C1" " " \fontsize #-3 "adding grace notes (every red attack)" }
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
		\context StaffGroup = "Outer Staff Group" <<
			\context ViolinStaffGroup = "Violin Staff Group" <<
				\tag #'Violin
				\context PerformerStaffGroup = "Violin Staff Group" <<
					\context LHStaff = "Violin Staff" <<
						\clef "percussion"
						\context LHVoice = "Violin Voice" {
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\times 2/3 {
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
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\times 2/3 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r32
									r8
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
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 0
									c'8 ]
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
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
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
								\times 2/3 {
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
									\set stemRightBeamCount = 1
									c'8
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r8
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
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
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
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									\afterGrace
									c'8.
									{
										\override Flag #'stroke-style = #"grace"
										\override Script #'font-size = #0.5
										\override Stem #'length = #8
										c'16
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
									\set stemRightBeamCount = 1
									c'8
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r32
									r8
								}
							}
							{
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									r16
								}
								{
									r4
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16. -\accent [
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
								}
							}
							{
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\times 2/3 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
								\tweak #'text #tuplet-number::calc-fraction-text
								\times 3/4 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 2
									c'16 ~ [
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
								\times 2/3 {
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
								\times 4/5 {
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
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
									c'16 ]
								}
							}
							{
								{
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
									c'8 -\accent ~ [
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 3
									c'32
									\set stemLeftBeamCount = 3
									\set stemRightBeamCount = 0
									c'32 ]
								}
							}
							{
								{
									r16
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
										\revert Flag #'stroke-style
										\revert Script #'font-size
										\revert Stem #'length
									}
									\set stemLeftBeamCount = 0
									\set stemRightBeamCount = 1
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
								}
								{
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 1
									c'8 ~
									\set stemLeftBeamCount = 1
									\set stemRightBeamCount = 2
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
									\set stemLeftBeamCount = 2
									\set stemRightBeamCount = 0
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
					>>
				>>
			>>
		>>
	>>
