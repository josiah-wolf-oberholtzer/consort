# -*- encoding: utf-8 -*-
from abjad import *
import consort


col_legno_attachment_expression = consort.makers.AttachmentExpression(
    attachments=consort.makers.ComplexTextSpanner(
        markup=r'\box { col legno }',
        ),
    selector=selectortools.selects_pitched_runs(),
    )