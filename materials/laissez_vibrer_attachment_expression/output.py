# -*- encoding: utf-8 -*-
from abjad import *
import consort


laissez_vibrer_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            (
                indicatortools.LaissezVibrer(),
                markuptools.Markup(
                    contents=(
                        markuptools.MarkupCommand(
                            'box',
                            markuptools.MarkupCommand(
                                'pad-around',
                                0.5,
                                markuptools.MarkupCommand(
                                    'caps',
                                    'L.V.'
                                    )
                                )
                            ),
                        ),
                    direction=Up,
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
            selectortools.ItemSelectorCallback(
                item=-1,
                apply_to_each=True,
                ),
            ),
        ),
    )