# -*- encoding: utf-8 -*-
from abjad import *
import consort


overpressure_attachment_expression = consort.makers.AttachmentExpression(
    attachments=consort.makers.ComplexTextSpanner(
        markup=r"\filled-box #'(-1 . 1) #'(-1 . 1) #1",
        ),
    selector=selectortools.Selector(),
    )