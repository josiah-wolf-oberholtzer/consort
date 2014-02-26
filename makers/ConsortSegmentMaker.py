# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import indicatortools
from experimental.tools.segmentmakertools import SegmentMaker


class ConsortSegmentMaker(SegmentMaker):
    r'''A Consort segment-maker.

    ::

        >>> from consort import makers
        >>> segment_maker = makers.ConsortSegmentMaker()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_permitted_time_signatures',
        '_target_duration',
        '_tempo',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        name=None,
        permitted_time_signatures=None,
        target_duration=None,
        tempo=None,
        ):
        SegmentMaker.__init__(
            self,
            name=name,
            )
        if permitted_time_signatures is not None:
            permitted_time_signatures = (
                indicatortools.TimeSignature(x)
                for x in permitted_time_signatures
                )
        self._permitted_time_signatures = permitted_time_signatures
        if target_duration is not None:
            target_duration = durationtools.Duration(target_duration)
        self._target_duration = target_duration
        if tempo is not None:
            tempo = indicatortools.Tempo(tempo)
        self._tempo = tempo

    ### PUBLIC METHODS ###

    ### PUBLIC PROPERTIES ###

    @property
    def permitted_time_signatures(self):
        return self._permitted_time_signatures

    @property
    def target_duration(self):
        return self._target_duration

    @property
    def tempo(self):
        return self._tempo
