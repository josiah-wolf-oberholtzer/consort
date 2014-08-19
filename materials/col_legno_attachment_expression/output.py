# -*- encoding: utf-8 -*-
from abjad import *
import consort


col_legno_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            consort.makers.ComplexTextSpanner(
                markup=markuptools.Markup(
                    contents=(
                        markuptools.MarkupCommand(
                            'box',
                            ['col', 'legno']
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