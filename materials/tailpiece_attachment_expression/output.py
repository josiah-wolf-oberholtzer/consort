# -*- encoding: utf-8 -*-
from abjad import *
import consort


tailpiece_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            (
                consort.makers.ClefSpanner(
                    clef=indicatortools.Clef(
                        name='percussion',
                        ),
                    ),
                spannertools.StaffLinesSpanner(
                    lines=1,
                    overrides={
                        'note_head__style': 'cross',
                        },
                    ),
                consort.makers.ComplexTextSpanner(
                    markup=markuptools.Markup(
                        contents=(
                            markuptools.MarkupCommand(
                                'box',
                                markuptools.MarkupCommand(
                                    'pad-around',
                                    0.5,
                                    'tailpiece'
                                    )
                                ),
                            ),
                        ),
                    ),
                ),
            ]
        ),
    selector=selectortools.Selector(
        callbacks=(
            selectortools.PrototypeSelectorCallback(
                prototype=scoretools.Leaf,
                ),
            selectortools.RunSelectorCallback(
                prototype=(
                    scoretools.Note,
                    scoretools.Chord,
                    ),
                ),
            ),
        ),
    )