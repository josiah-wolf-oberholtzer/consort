# -*- encoding: utf-8 -*-
from abjad import *
import consort


tremolo_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            consort.makers.ComplexTextSpanner(
                markup=markuptools.Markup(
                    contents=(
                        markuptools.MarkupCommand(
                            'box',
                            'airtone'
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