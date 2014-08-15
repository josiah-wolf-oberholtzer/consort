# -*- encoding: utf-8 -*-
from abjad import *
import consort


crescendi_dynamic_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            consort.makers.DynamicExpression(
                hairpin_start_token='p',
                hairpin_stop_token='f',
                minimum_duration=durationtools.Duration(1, 4),
                ),
            consort.makers.DynamicExpression(
                hairpin_start_token='fp',
                hairpin_stop_token='f',
                minimum_duration=durationtools.Duration(1, 4),
                ),
            consort.makers.DynamicExpression(
                hairpin_start_token='fp',
                hairpin_stop_token='ff',
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