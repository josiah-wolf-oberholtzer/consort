# -*- encoding: utf-8 -*-
from abjad import *
import consort


foreground_dynamic_attachment_expression = consort.makers.AttachmentExpression(
    attachments=(
        consort.makers.DynamicExpression('fff'),
        consort.makers.DynamicExpression('f'),
        consort.makers.DynamicExpression('ff'),
        consort.makers.DynamicExpression('mf'),
        ),
    selector=selectortools.selects_pitched_runs(),
    )