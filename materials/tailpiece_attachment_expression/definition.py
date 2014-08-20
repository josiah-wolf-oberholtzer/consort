# -*- encoding: utf-8 -*-
from abjad import *
import consort


staff_lines_spanner = spannertools.StaffLinesSpanner(lines=1)
override(staff_lines_spanner).note_head.style = 'cross'

tailpiece_attachment_expression = consort.makers.AttachmentExpression(
    attachments=(
        (
            consort.makers.ClefSpanner('percussion'),
            staff_lines_spanner,
            consort.makers.ComplexTextSpanner(
                markup=Markup('tailpiece').pad_around(0.5).with_box(),
                ),
            ),
        ),
    selector=selectortools.selects_pitched_runs(),
    )