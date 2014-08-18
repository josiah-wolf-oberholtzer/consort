# -*- encoding: utf-8 -*-
from abjad import *
import consort


staff_lines_spanner = spannertools.StaffLinesSpanner(lines=1)
override(staff_lines_spanner).note_head.style = schemetools.Scheme(
    'cross', quoting="'"),

percussion_staff_attachment_expression = consort.makers.AttachmentExpression(
    attachments=(
        (
            consort.makers.ClefSpanner('percussion'),
            staff_lines_spanner,
            ),
        ),
    selector=selectortools.Selector(),
    )