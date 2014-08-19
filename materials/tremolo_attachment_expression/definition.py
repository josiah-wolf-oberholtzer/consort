# -*- encoding: utf-8 -*-
from abjad import *
import consort


tremolo_attachment_expression = consort.makers.AttachmentExpression(
    attachments=consort.makers.ComplexTextSpanner(
        markup=r'\box airtone',
        ),
    selector=selectortools.selects_pitched_runs(),
    )