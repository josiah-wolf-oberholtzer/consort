# -*- encoding: utf-8 -*-
from abjad import *
from consort import makers


crescendi_dynamic_attachment_expression = makers.AttachmentExpression(
    attachments=(
        makers.DynamicExpression('p', 'f'),
        makers.DynamicExpression('fp', 'f'),
        makers.DynamicExpression('fp', 'ff'),
        ),
    selector=selectortools.selects_pitched_runs(),
    )