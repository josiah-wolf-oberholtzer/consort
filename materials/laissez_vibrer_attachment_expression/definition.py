# -*- encoding: utf-8 -*-
from abjad import *
import consort


laissez_vibrer_attachment_expression = consort.makers.AttachmentExpression(
    attachments=(
        (
            indicatortools.LaissezVibrer(),
            markuptools.Markup('L.V.', Up).caps().pad_around(0.5).with_box(),
            ),
        ),
    selector=selectortools.selects_pitched_runs()[-1],
    )