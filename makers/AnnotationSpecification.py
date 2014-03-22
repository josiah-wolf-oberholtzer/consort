# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject


class AnnotationSpecification(ConsortObject):
    r'''An annotation specification.

    Annotated stages:

        stage 1: no brackets, no notation, no barlines
        stage 2: outer bracket, no barlines, no notation
        stage 3: outer bracket, barlines, no notation
        stage 4: outer bracket, barlines, notation (not rewritten)
        stage 5: outer bracket, barlines, notation (rewritten)
        stage 6: brackets, barlines, notation (rewritten), and all attachments

    Final stage:

        stage 6: no brackets, barlines, notation (rewritten)

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_hide_inner_bracket',
        '_show_stage_1',
        '_show_stage_2',
        '_show_stage_3',
        '_show_stage_4',
        '_show_stage_5',
        '_show_stage_6',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        hide_inner_bracket=None,
        show_stage_1=True,
        show_stage_2=True,
        show_stage_3=True,
        show_stage_4=True,
        show_stage_5=True,
        show_stage_6=True,
        ):
        self._hide_inner_bracket = hide_inner_bracket
        self._show_stage_1 = show_stage_1
        self._show_stage_2 = show_stage_2
        self._show_stage_3 = show_stage_3
        self._show_stage_4 = show_stage_4
        self._show_stage_5 = show_stage_5
        self._show_stage_6 = show_stage_6

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
    def show_stage_6(self):
        return self._show_stage_6
