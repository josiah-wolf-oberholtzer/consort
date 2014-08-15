# -*- encoding: utf-8 -*-
from abjad import *
import consort


midground_dynamic_attachment_expression = consort.makers.AttachmentExpression(
    attachments=(
        consort.makers.DynamicExpression('mf'),
        consort.makers.DynamicExpression('mp'),
        ),
    selector=selectortools.selects_pitched_runs(),
    )