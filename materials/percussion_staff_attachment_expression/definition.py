# -*- encoding: utf-8 -*-
from abjad import *
import consort


staff_lines_spanner = spannertools.StaffLinesSpanner(
    lines=(4, -4),
    )
override(staff_lines_spanner).note_head.no_ledgers = True
override(staff_lines_spanner).note_head.style = 'cross'

percussion_staff_attachment_expression = consort.makers.AttachmentExpression(
    attachments=(
        (
            consort.makers.ClefSpanner('percussion'),
            staff_lines_spanner,
            ),
        ),
    selector=selectortools.Selector(),
    )