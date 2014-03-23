# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject


class AnnotationSpecifier(ConsortObject):
    r'''An annotation specifier.

    Annotated stages:

        stage 1: no brackets, no notation, no barlines
        stage 2: bracket, no barlines, no notation
        stage 3: bracket, barlines, no notation
        stage 4: bracket, barlines, notation (not rewritten)
        stage 5: bracket, barlines, notation (rewritten)
        stage 6: brackets, barlines, notation (rewritten), and all attachments

    Final stage:

        stage X: no brackets, barlines, notation (rewritten)

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_hide_inner_bracket',
        '_show_stage_1',
        '_show_stage_2',
        '_show_stage_3',
        '_show_stage_4',
        '_show_stage_5',
        '_show_annotated_result',
        '_show_unannotated_result',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        hide_inner_bracket=False,
        show_stage_1=False,
        show_stage_2=False,
        show_stage_3=False,
        show_stage_4=False,
        show_stage_5=False,
        show_annotated_result=False,
        show_unannotated_result=True,
        ):
        self._hide_inner_bracket = hide_inner_bracket
        self._show_stage_1 = show_stage_1
        self._show_stage_2 = show_stage_2
        self._show_stage_3 = show_stage_3
        self._show_stage_4 = show_stage_4
        self._show_stage_5 = show_stage_5
        self._show_annotated_result = show_annotated_result
        self._show_unannotated_result = show_unannotated_result

    ### PUBLIC PROPERTIES ###

    @property
    def hide_inner_bracket(self):
        return self._hide_inner_bracket

    @property
    def show_stage_1(self):
        return self._show_stage_1

    @property
    def show_stage_2(self):
        return self._show_stage_2

    @property
    def show_stage_3(self):
        return self._show_stage_3

    @property
    def show_stage_4(self):
        return self._show_stage_4

    @property
    def show_stage_5(self):
        return self._show_stage_5

    @property
    def show_annotated_result(self):
        return self._show_annotated_result

    @property
    def show_unannotated_result(self):
        return self._show_unannotated_result
