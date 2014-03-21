# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject


class AnnotationSpecification(ConsortObject):
    r'''An annotation specification.

    stage 1: no brackets, no notation, no barlines
    stage 2: outer bracket, no barlines, no notation
    stage 3: outer bracket, barlines, no notation
    stage 4: outer bracket, barlines, notation (not rewritten)
    stage 5: outer bracket, barlines, notation (rewritten)
    stage 6: no brackets, barlines, notation (rewritten)

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_show_inner_bracket',
        '_show_stage_1',
        '_show_stage_2',
        '_show_stage_3',
        '_show_stage_4',
        '_show_stage_5',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        show_inner_bracket=None,
        show_stage_1=None,
        show_stage_2=None,
        show_stage_3=None,
        show_stage_4=None,
        show_stage_5=None,
        ):
        self._show_inner_bracket = show_inner_bracket
        self._show_stage_1 = show_stage_1
        self._show_stage_2 = show_stage_2
        self._show_stage_3 = show_stage_3
        self._show_stage_4 = show_stage_4
        self._show_stage_5 = show_stage_5

    ### PUBLIC PROPERTIES ###

    @property
    def show_inner_bracket(self):
        return self._show_inner_bracket

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
