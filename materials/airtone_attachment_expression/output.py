# -*- encoding: utf-8 -*-
from abjad import *
import consort


airtone_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            spannertools.StemTremoloSpanner(),
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