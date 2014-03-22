# -*- encoding: utf-8 -*-
from abjad import new
from consort import makers
from consort.segments import rhythm_08 as base


voice_specifier_one = new(base.voice_specifier_one,
    music_specifier__grace_agent=makers.GraceAgent(
        counts=(0, 1, 0, 0, 2, 0, 0, 0, 1, 2),
        ),
    )


voice_specifier_two = new(base.voice_specifier_two,
    )


segment_maker = new(base.segment_maker,
    annotation_specifier=makers.AnnotationSpecification(
        show_stage_3=True,
        show_stage_4=True,
        show_stage_5=True,
        ),
    name='adding grace notes (a longer pattern)',
    rehearsal_mark='C3',
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
