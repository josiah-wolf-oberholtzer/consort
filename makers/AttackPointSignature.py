# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_


class AttackPointSignature(abctools.AbjadValueObject):
    r'''An attack point signature.

    ::

        >>> from consort import makers
        >>> attack_point_signature = makers.AttackPointSignature(
        ...     division_position=0,
        ...     phrase_position=(1, 2),
        ...     segment_position=(4, 5),
        ...     )
        >>> print(format(attack_point_signature))
        consort.makers.AttackPointSignature(
            division_position=durationtools.Multiplier(0, 1),
            phrase_position=durationtools.Multiplier(1, 2),
            segment_position=durationtools.Multiplier(4, 5),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_division_position',
        '_phrase_position',
        '_segment_position',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        division_position=0,
        phrase_position=0,
        segment_position=0,
        ):
        self._division_position = durationtools.Multiplier(division_position)
        self._phrase_position = durationtools.Multiplier(phrase_position)
        self._segment_position = durationtools.Multiplier(segment_position)

    ### PRIVATE METHODS ###

    @staticmethod
    def _find_position(
        tie_start_offset,
        bounding_start_offset,
        bounding_stop_offset,
        ):
        start_offset = tie_start_offset - bounding_start_offset
        duration = bounding_start_offset - bounding_stop_offset
        if duration == 0:
            return durationtools.Multiplier(0)
        position = start_offset / duration
        return position

    ### PUBLIC METHODS ###

    @classmethod
    def from_logical_tie(cls, logical_tie):
        from consort import makers
        tie_start_offset = logical_tie.get_timespan().start_offset
        head = logical_tie.head
        parentage = inspect_(head).get_parentage(include_self=False)
        for i, parent in enumerate(parentage):
            if inspect_(parent).has_indicator(makers.MusicSpecifier):
                phrase = parent
                phrase_timespan = inspect_(phrase).get_timespan()
                phrase_position = cls._find_position(
                    tie_start_offset,
                    phrase_timespan.start_offset,
                    phrase_timespan.stop_offset,
                    )
                division = parentage[i - 1]
                division_timespan = inspect_(division).get_timespan()
                last_leaf = division.select_leaves()[-1]
                last_logical_tie = inspect_(last_leaf).get_logical_tie()
                bounding_stop_offset = \
                    last_logical_tie.get_timespan().start_offset
                division_position = cls._find_position(
                    tie_start_offset,
                    division_timespan.start_offset,
                    bounding_stop_offset,
                    )
            elif isinstance(parent, scoretools.Voice):
                segment_timespan = inspect_(parent).get_timespan()
                segment_position = cls._find_position(
                    tie_start_offset,
                    segment_timespan.start_offset,
                    segment_timespan.stop_offset,
                    )
        signature = cls(
            division_position=division_position,
            phrase_position=phrase_position,
            segment_position=segment_position,
            )
        return signature

    ### PUBLIC PROPERTIES ###

    @property
    def division_position(self):
        return self._division_position

    @property
    def phrase_position(self):
        return self._phrase_position

    @property
    def segment_position(self):
        return self._segment_position