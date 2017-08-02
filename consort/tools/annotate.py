import abjad
import consort
from abjad import attach
from abjad import inspect
from abjad import iterate
from abjad import override
from abjad.tools import scoretools
from abjad.tools import schemetools


def make_annotated_phrase(phrase, color=None):
    duration = abjad.inspect(phrase).get_duration()
    durations = [inspect(_).get_duration() for _ in phrase]
    leaves = scoretools.LeafMaker()([0], durations)
    annotated_phrase = scoretools.Tuplet.from_duration(duration, leaves)
    if color:
        override(annotated_phrase).tuplet_bracket.color = color
    return annotated_phrase


def make_annotated_division(division, color=None):
    duration = abjad.inspect(division).get_duration()
    if duration != 1:
        note = abjad.Note("c'''1")
        annotated_division = abjad.Tuplet(duration, (note,))
    else:
        note = abjad.Note("c'''2")
        annotated_division = abjad.Tuplet(2, (note,))
    leaves = list(iterate(division).by_leaf())
    prototype = (abjad.Rest, abjad.MultimeasureRest)
    if all(isinstance(_, prototype) for _ in leaves):
        manager = override(annotated_division)
        manager.tuplet_bracket.dash_fraction = 0.1
        manager.tuplet_bracket.dash_period = 1.5
        manager.tuplet_bracket.style = \
            schemetools.SchemeSymbol('dashed-line')
    if color:
        override(annotated_division).tuplet_bracket.color = color
    return annotated_division


def make_empty_phrase_divisions(phrase):
    inner_container = abjad.Container()
    outer_container = abjad.Container()
    for division in phrase:
        duration = abjad.inspect(division).get_duration()
        multiplier = abjad.Multiplier(duration)
        inner_skip = abjad.Skip(1)
        outer_skip = abjad.Skip(1)
        attach(multiplier, inner_skip)
        attach(multiplier, outer_skip)
        inner_container.append(inner_skip)
        outer_container.append(outer_skip)
    return inner_container, outer_container


def annotate(context, nonsilence=None):
    prototype = consort.MusicSpecifier
    silence_specifier = consort.MusicSpecifier()
    annotated_context = context
    context_mapping = {}
    for voice in iterate(annotated_context).by_class(abjad.Voice):
        if voice.context_name == 'Dynamics':
            continue
        division_voice = abjad.Context(
            context_name='AnnotatedDivisionsVoice',
            )
        phrase_voice = abjad.Context(
            context_name='AnnotatedPhrasesVoice',
            )
        for phrase in voice:
            color = None
            if nonsilence:
                music_specifier = abjad.inspect(phrase).get_indicator(prototype)
                if music_specifier == silence_specifier:
                    inner_container, outer_container = \
                        make_empty_phrase_divisions(phrase)
                    division_voice.append(inner_container)
                    phrase_voice.append(outer_container)
                    continue
                if music_specifier:
                    color = music_specifier.color
            for division in phrase:
                annotation_division = make_annotated_division(division, color)
                division_voice.append(annotation_division)
            annotation_phrase = make_annotated_phrase(phrase, color)
            phrase_voice.append(annotation_phrase)
        parent = abjad.inspect(voice).get_parentage().parent
        if parent not in context_mapping:
            context_mapping[parent] = []
        context_mapping[parent].append(division_voice)
        context_mapping[parent].append(phrase_voice)
    for context, annotation_voices in context_mapping.items():
        context.is_simultaneous = True
        context.extend(annotation_voices)
