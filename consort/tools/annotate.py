# -*- encoding: utf-8 -*-
from abjad import *


def make_annotated_phrase(phrase):
    duration = inspect_(phrase).get_duration()
    if duration != 1:
        note = Note("c'''1")
        annotated_phrase = Tuplet(duration, (note,))
    else:
        note = scoretools.Note("c'''2")
        annotated_phrase = Tuplet(2, (note,))
    return annotated_phrase


def make_annotated_division(division):
    duration = inspect_(division).get_duration()
    if duration != 1:
        note = Note("c'''1")
        annotated_division = Tuplet(duration, (note,))
    else:
        note = scoretools.Note("c'''2")
        annotated_division = Tuplet(2, (note,))
    leaves = division.select_leaves()
    if all(isinstance(_, Rest) for _ in leaves):
        manager = override(annotated_division)
        manager.tuplet_bracket.dash_fraction = 0.1
        manager.tuplet_bracket.dash_period = 1.5
        manager.tuplet_bracket.style = \
            schemetools.SchemeSymbol('dashed-line')
    return annotated_division


def annotate(context):
    #annotated_context = mutate(context).copy()
    annotated_context = context
    context_mapping = {}
    for voice in iterate(annotated_context).by_class(Voice):
        division_voice = Voice(context_name='AnnotatedDivisionsVoice')
        phrase_voice = Voice(context_name='AnnotatedPhrasesVoice')
        for phrase in voice:
            for division in phrase:
                annotation_division = make_annotated_division(division)
                division_voice.append(annotation_division)
            annotation_phrase = make_annotated_phrase(phrase)
            phrase_voice.append(annotation_phrase)
        parent = inspect_(voice).get_parentage().parent
        if parent not in context_mapping:
            context_mapping[parent] = []
        context_mapping[parent].append(division_voice)
        context_mapping[parent].append(phrase_voice)
    for context, annotation_voices in context_mapping.items():
        context.is_simultaneous = True
        context.extend(annotation_voices)