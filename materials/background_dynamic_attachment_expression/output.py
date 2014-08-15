# -*- encoding: utf-8 -*-
from abjad import *
import consort


background_dynamic_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            consort.makers.DynamicExpression(
                hairpin_start_token='ppp',
                minimum_duration=durationtools.Duration(1, 4),
                ),
            consort.makers.DynamicExpression(
                hairpin_start_token='p',
                minimum_duration=durationtools.Duration(1, 4),
                ),
            consort.makers.DynamicExpression(
                hairpin_start_token='pp',
                minimum_duration=durationtools.Duration(1, 4),
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