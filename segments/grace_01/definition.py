# -*- encoding: utf-8 -*-
from abjad import new
from consort import makers
from consort.segments import rhythm_08 as base


voice_specifier_one = new(base.voice_specifier_one,
    music_specifier__grace_agent=makers.GraceAgent(
        counts=(1,),
        ),
    )


voice_specifier_two = new(base.voice_specifier_two,
    )


segment_maker = new(base.segment_maker,
    rehearsal_mark='C1',
    voice_specifiers=(
        voice_specifier_one,
        voice_specifier_two,
        ),
    )

__all__ = (
    'segment_maker',
    'voice_specifier_one',
    'voice_specifier_two',
    )
