# -*- encoding: utf-8 -*-
from abjad import new
from consort import makers
from consort.segments import rhythm_06 as base


voice_specifier_one = new(base.voice_specifier_one,
    music_specifier__grace_agent=makers.GraceAgent(
        counts=(0, 1, 0, 0, 2),
        ),
    )

segment_maker = new(base.segment_maker,
    rehearsal_mark='C1',
    voice_specifiers=(
        voice_specifier_one,
        ),
    )

__all__ = (
    'segment_maker',
    'voice_specifier_one',
    )
