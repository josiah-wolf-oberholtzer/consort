# -*- encoding: utf-8 -*-
from abjad import *
import consort


overpressure_attachment_expression = consort.makers.AttachmentExpression(
    attachments=datastructuretools.TypedList(
        [
            consort.makers.ComplexTextSpanner(
                markup=markuptools.Markup(
                    contents=(
                        markuptools.MarkupCommand(
                            'filled-box',
                            schemetools.SchemePair(-1, 1),
                            schemetools.SchemePair(-1, 1),
                            1
                            ),
                        ),
                    ),
                ),
            ]
        ),
    selector=selectortools.Selector(),
    )