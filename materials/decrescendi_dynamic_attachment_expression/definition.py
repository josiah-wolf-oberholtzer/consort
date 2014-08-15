# -*- encoding: utf-8 -*-
from abjad import *
import consort


decrescendi_dynamic_attachment_expression = consort.makers.AttachmentExpression(
    attachments=(
        consort.makers.DynamicExpression('f', 'p'),
        consort.makers.DynamicExpression('mf', 'o'),
        consort.makers.DynamicExpression('fp', 'o'),
        ),
    selector=selectortools.selects_pitched_runs(),
    )