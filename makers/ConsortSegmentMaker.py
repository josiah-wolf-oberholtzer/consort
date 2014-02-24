# -*- encoding: utf-8 -*-
from experimental.tools.segmentmakertools import SegmentMaker


class ConsortSegmentMaker(SegmentMaker):
    r'''A Consort segment-maker.

    ::

        >>> from consort import makers
        >>> segment_maker = makers.ConsortSegmentMaker()

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        name=None,
        ):
        SegmentMaker.__init__(
            self,
            name=name,
            )

    ### PUBLIC METHODS ###

    ### PUBLIC PROPERTIES ###
