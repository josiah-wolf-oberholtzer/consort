# -*- encoding: utf-8 -*-
import consort
from abjad import attach
from abjad import inspect_
from abjad import iterate
from abjad import override
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import schemetools


def make_annotated_phrase(phrase):
    duration = inspect_(phrase).get_duration()
    if duration != 1:
        note = scoretools.Note("c'''1")
        annotated_phrase = scoretools.Tuplet(duration, (note,))
    else:
        note = scoretools.Note("c'''2")
        annotated_phrase = scoretools.Tuplet(2, (note,))
    return annotated_phrase


def make_annotated_division(division):
    duration = inspect_(division).get_duration()
    if duration != 1:
        note = scoretools.Note("c'''1")
        annotated_division = scoretools.Tuplet(duration, (note,))
    else:
        note = scoretools.Note("c'''2")
        annotated_division = scoretools.Tuplet(2, (note,))
    leaves = division.select_leaves()
    prototype = (scoretools.Rest, scoretools.MultimeasureRest)
    if all(isinstance(_, prototype) for _ in leaves):
        manager = override(annotated_division)
        manager.tuplet_bracket.dash_fraction = 0.1
        manager.tuplet_bracket.dash_period = 1.5
        manager.tuplet_bracket.style = \
            schemetools.SchemeSymbol('dashed-line')
    return annotated_division


def make_empty_phrase(phrase):
    skip = scoretools.Skip(1)
    duration = inspect_(phrase).get_duration()
    multiplier = durationtools.Multiplier(duration)
    attach(multiplier, skip)
    container = scoretools.Container([skip])
    return container


def annotate(context, nonsilence=None):
    prototype = consort.MusicSpecifier
    silence_specifier = consort.MusicSpecifier()
    annotated_context = context
    context_mapping = {}
    for voice in iterate(annotated_context).by_class(scoretools.Voice):
        if voice.context_name == 'Dynamics':
            continue
        division_voice = scoretools.Context(
            context_name='AnnotatedDivisionsVoice',
            )
        phrase_voice = scoretools.Context(
            context_name='AnnotatedPhrasesVoice',
            )
        for phrase in voice:
            if nonsilence:
                music_specifier = inspect_(phrase).get_indicator(prototype)
                if music_specifier == silence_specifier:
                    annotated_divisions = make_empty_phrase(phrase)
                    division_voice.append(annotated_divisions)
                    annotated_phrase = make_empty_phrase(phrase)
                    phrase_voice.append(annotated_phrase)
                    continue
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