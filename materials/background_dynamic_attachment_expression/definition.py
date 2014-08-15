# -*- encoding: utf-8 -*-
from abjad import *
import consort


background_dynamic_attachment_expression = consort.makers.AttachmentExpression(
    attachments=(
        consort.makers.DynamicExpression('ppp'),
        consort.makers.DynamicExpression('p'),
        consort.makers.DynamicExpression('pp'),
        ),
    selector=selectortools.selects_pitched_runs(),
    )