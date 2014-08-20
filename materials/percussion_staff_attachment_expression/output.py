# -*- encoding: utf-8 -*-
from abjad import *
import consort


percussion_staff_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            (
                consort.makers.ClefSpanner(
                    clef=indicatortools.Clef(
                        name='percussion',
                        ),
                    ),
                spannertools.StaffLinesSpanner(
                    lines=(4, -4),
                    overrides={
                        'note_head__no_ledgers': True,
                        'note_head__style': 'cross',
                        },
                    ),
                ),
            ]
        ),
    selector=selectortools.Selector(),
    )