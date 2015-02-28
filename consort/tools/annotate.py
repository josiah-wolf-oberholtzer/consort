# -*- encoding: utf-8 -*-
from abjad import *


def annotate(context):
    annotated_context = mutate(context).copy()
    annotated_context.is_simultaneous = True
    annotation_voices = []
    for voice in iterate(annotated_context).by_class(Voice):
        override(voice).tuplet_bracket.direction = Down
        annotation_voice = Voice()
        manager = override(annotation_voice)
        manager.dots.stencil = False
        manager.flag.stencil = False
        manager.note_column.ignore_collision = True
        manager.note_head.no_ledgers = True
        manager.note_head.stencil = False
        manager.stem.stencil = False
        manager.tuplet_bracket.direction = Up
        manager.tuplet_bracket.full_length_to_extent = True
        manager.tuplet_bracket.positions = schemetools.SchemePair(5, 5)
        manager.tuplet_number.stencil = False
        set_(annotation_voice).tuplet_full_length = True
        for phrase in voice:
            annotation_phrase = Container()
            for division in phrase:
                duration = inspect_(division).get_duration()
                if duration != 1:
                    note = Note(0, 1)
                    annotation_division = Tuplet(duration, (note,))
                else:
                    note = scoretools.Note(0, (1, 2))
                    annotation_division = Tuplet(2, (note,))
                leaves = division.select_leaves()
                if all(isinstance(_, Rest) for _ in leaves):
                    manager = override(annotation_division)
                    manager.tuplet_bracket.dash_fraction = 0.25
                    manager.tuplet_bracket.dash_period = 1
                    manager.tuplet_bracket.style = \
                        schemetools.SchemeSymbol('dashed-line')
                annotation_phrase.append(annotation_division)
            annotation_voice.append(annotation_phrase)
        annotation_voices.append(annotation_voice)
    annotated_context.extend(annotation_voices)
    return annotated_context