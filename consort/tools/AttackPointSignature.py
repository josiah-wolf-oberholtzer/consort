# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import iterate


class AttackPointSignature(abctools.AbjadValueObject):
    r'''An attack point signature.

    ::

        >>> from consort import tools
        >>> attack_point_signature = tools.AttackPointSignature(
        ...     division_position=0,
        ...     phrase_position=(1, 2),
        ...     segment_position=(4, 5),
        ...     )
        >>> print(format(attack_point_signature))
        consort.tools.AttackPointSignature(
            division_index=0,
            division_position=durationtools.Multiplier(0, 1),
            logical_tie_index=0,
            phrase_position=durationtools.Multiplier(1, 2),
            segment_position=durationtools.Multiplier(4, 5),
            total_divisions_in_phrase=1,
            total_logical_ties_in_division=1,
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_division_index',
        '_division_position',
        '_logical_tie_index',
        '_phrase_position',
        '_segment_position',
        '_total_divisions_in_phrase',
        '_total_logical_ties_in_division',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        division_index=0,
        division_position=0,
        logical_tie_index=0,
        phrase_position=0,
        segment_position=0,
        total_divisions_in_phrase=1,
        total_logical_ties_in_division=1,
        ):
        division_index = int(division_index)
        division_position = durationtools.Multiplier(division_position)
        logical_tie_index = int(logical_tie_index)
        phrase_position = durationtools.Multiplier(phrase_position)
        segment_position = durationtools.Multiplier(segment_position)
        total_divisions_in_phrase = int(total_divisions_in_phrase)
        total_logical_ties_in_division = int(total_logical_ties_in_division)
        assert 0 <= logical_tie_index < total_logical_ties_in_division
        assert 0 <= division_index < total_divisions_in_phrase
        assert 0 <= division_position <= 1
        assert 0 <= phrase_position <= 1
        assert 0 <= segment_position <= 1
        self._division_index = division_index
        self._division_position = division_position
        self._logical_tie_index = logical_tie_index
        self._phrase_position = phrase_position
        self._segment_position = segment_position
        self._total_divisions_in_phrase = total_divisions_in_phrase
        self._total_logical_ties_in_division = \
            total_logical_ties_in_division

    ### PRIVATE METHODS ###

    @staticmethod
    def _find_position(
        logical_tie_start_offset,
        bounding_start_offset,
        bounding_stop_offset,
        ):
        duration = bounding_stop_offset - bounding_start_offset
        start_offset = logical_tie_start_offset - bounding_start_offset
        if duration == 0:
            return durationtools.Multiplier(0)
        position = start_offset / duration
        assert 0 <= position <= 1
        return position

    ### PUBLIC METHODS ###

    @classmethod
    def from_logical_tie(cls, logical_tie):
        from consort import tools
        logical_tie_start_offset = logical_tie.get_timespan().start_offset
        head = logical_tie.head
        parentage = inspect_(head).get_parentage(include_self=False)
        for i, parent in enumerate(parentage):
            if inspect_(parent).has_indicator(tools.MusicSpecifier):

                phrase = parent
                phrase_timespan = inspect_(phrase).get_timespan()
                phrase_position = cls._find_position(
                    logical_tie_start_offset,
                    phrase_timespan.start_offset,
                    phrase_timespan.stop_offset,
                    )

                division = parentage[i - 1]
                division_index = phrase.index(division)
                total_divisions_in_phrase = len(phrase)

                logical_ties = []
                for leaf in iterate(division).by_class(scoretools.Note):
                    leaf_logical_tie = inspect_(leaf).get_logical_tie()
                    if leaf is not leaf_logical_tie.head:
                        continue
                    logical_ties.append(leaf_logical_tie)

                division_position = cls._find_position(
                    logical_tie_start_offset,
                    logical_ties[0].get_timespan().start_offset,
                    logical_ties[-1].get_timespan().stop_offset,
                    )

                logical_tie_index = logical_ties.index(logical_tie)
                total_logical_ties_in_division = len(logical_ties)

            elif isinstance(parent, scoretools.Voice):
                segment_timespan = inspect_(parent).get_timespan()
                segment_position = cls._find_position(
                    logical_tie_start_offset,
                    segment_timespan.start_offset,
                    segment_timespan.stop_offset,
                    )

        signature = cls(
            division_index=division_index,
            division_position=division_position,
            logical_tie_index=logical_tie_index,
            phrase_position=phrase_position,
            segment_position=segment_position,
            total_divisions_in_phrase=total_divisions_in_phrase,
            total_logical_ties_in_division=total_logical_ties_in_division,
            )
        return signature

    ### PUBLIC PROPERTIES ###

    @property
    def division_index(self):
        return self._division_index

    @property
    def division_position(self):
        return self._division_position

    @property
    def is_first_of_division(self):
        if not self.logical_tie_index:
            return True
        return False

    @property
    def is_first_of_phrase(self):
        if not self.logical_tie_index and not self.division_index:
            return True
        return False

    @property
    def logical_tie_index(self):
        return self._logical_tie_index

    @property
    def phrase_index(self):
        return self._phrase_index

    @property
    def phrase_position(self):
        return self._phrase_position

    @property
    def segment_position(self):
        return self._segment_position

    @property
    def total_divisions_in_phrase(self):
        return self._total_divisions_in_phrase

    @property
    def total_logical_ties_in_division(self):
        return self._total_logical_ties_in_division