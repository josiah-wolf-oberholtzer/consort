# -*- encoding: utf-8 -*-
from abjad import abctools
from abjad import durationtools
from abjad import rhythmmakertools


class CompositeRhythmMaker(abctools.AbjadValueObject):
    r'''A composite rhythm-maker.

    ::

        >>> import consort
        >>> composite_rhythm_maker = consort.CompositeRhythmMaker(
        ...     first=rhythmmakertools.NoteRhythmMaker(),
        ...     last=rhythmmakertools.IncisedRhythmMaker(
        ...         incise_specifier=rhythmmakertools.InciseSpecifier(
        ...             prefix_counts=[0],
        ...             suffix_talea=[1],
        ...             suffix_counts=[1],
        ...             talea_denominator=16,
        ...             ),
        ...         ),
        ...     only=rhythmmakertools.EvenDivisionRhythmMaker(
        ...         denominators=[32],
        ...         ),
        ...     rest=rhythmmakertools.EvenDivisionRhythmMaker(),
        ...     )
        >>> print(format(composite_rhythm_maker))
        consort.tools.CompositeRhythmMaker(
            first=rhythmmakertools.NoteRhythmMaker(),
            last=rhythmmakertools.IncisedRhythmMaker(
                incise_specifier=rhythmmakertools.InciseSpecifier(
                    prefix_counts=(0,),
                    suffix_talea=(1,),
                    suffix_counts=(1,),
                    talea_denominator=16,
                    ),
                ),
            only=rhythmmakertools.EvenDivisionRhythmMaker(
                denominators=(32,),
                ),
            rest=rhythmmakertools.EvenDivisionRhythmMaker(
                denominators=(8,),
                ),
            )

    ..  container:: example

        ::

            >>> divisions = [(1, 4), (1, 4), (1, 4), (1, 4)]
            >>> result = composite_rhythm_maker(divisions)
            >>> staff = Staff()
            >>> for x in result:
            ...     staff.extend(x)
            ...
            >>> print(format(staff))
            \new Staff {
                c'4
                {
                    c'8 [
                    c'8 ]
                }
                {
                    c'8 [
                    c'8 ]
                }
                c'8. [
                c'16 ]
            }

    ..  container:: example

        ::

            >>> divisions = [(1, 4), (1, 4)]
            >>> result = composite_rhythm_maker(divisions)
            >>> staff = Staff()
            >>> for x in result:
            ...     staff.extend(x)
            ...
            >>> print(format(staff))
            \new Staff {
                c'4
                c'8. [
                c'16 ]
            }

    ..  container:: example

        ::

            >>> divisions = [(1, 4)]
            >>> result = composite_rhythm_maker(divisions)
            >>> staff = Staff()
            >>> for x in result:
            ...     staff.extend(x)
            ...
            >>> print(format(staff))
            \new Staff {
                {
                    c'32 [
                    c'32
                    c'32
                    c'32
                    c'32
                    c'32
                    c'32
                    c'32 ]
                }
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_first',
        '_last',
        '_only',
        '_rest',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        first=None,
        last=None,
        only=None,
        rest=None,
        ):
        if first is not None:
            assert isinstance(first, rhythmmakertools.RhythmMaker)
        if last is not None:
            assert isinstance(last, rhythmmakertools.RhythmMaker)
        if only is not None:
            assert isinstance(only, rhythmmakertools.RhythmMaker)
        assert isinstance(rest, rhythmmakertools.RhythmMaker)
        self._first = first
        self._last = last
        self._only = only
        self._rest = rest

    ### SPECIAL METHODS ###

    def __call__(self, divisions, seeds=None):
        divisions = [durationtools.Division(x) for x in divisions]
        result = []
        if not divisions:
            pass
        elif len(divisions) == 1:
            if self.only:
                result.extend(self.only(divisions, seeds=seeds))
            elif self.last:
                result.extend(self.last(divisions, seeds=seeds))
            elif self.first:
                result.extend(self.first(divisions, seeds=seeds))
            else:
                result.extend(self.rest(divisions, seeds=seeds))
        elif len(divisions) == 2:
            if self.first and self.last:
                first = self.first(divisions=[divisions[0]], seeds=seeds)
                last = self.last(divisions=[divisions[1]], seeds=seeds)
                result.extend(first)
                result.extend(last)
            elif self.first:
                first = self.first(divisions=[divisions[0]], seeds=seeds)
                rest = self.rest(divisions=[divisions[1]], seeds=seeds)
                result.extend(first)
                result.extend(rest)
            elif self.last:
                rest = self.rest(divisions=[divisions[0]], seeds=seeds)
                last = self.last(divisions=[divisions[1]], seeds=seeds)
                result.extend(rest)
                result.extend(last)
            else:
                rest = self.rest(divisions=divisions, seeds=seeds)
                result.extend(rest)
        else:
            if self.first and self.last:
                first = self.first(divisions=[divisions[0]], seeds=seeds)
                rest = self.rest(divisions=divisions[1:-1], seeds=seeds)
                last = self.last(divisions=[divisions[-1]], seeds=seeds)
                result.extend(first)
                result.extend(rest)
                result.extend(last)
            elif self.first:
                first = self.first(divisions=[divisions[0]], seeds=seeds)
                rest = self.rest(divisions=divisions[1:], seeds=seeds)
                result.extend(first)
                result.extend(rest)
            elif self.last:
                rest = self.rest(divisions=divisions[:-1], seeds=seeds)
                last = self.last(divisions=[divisions[-1]], seeds=seeds)
                result.extend(rest)
                result.extend(last)
            else:
                rest = self.rest(divisions=divisions, seeds=seeds)
                result.extend(rest)
        return result


    ### PUBLIC PROPERTIES ###

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    @property
    def only(self):
        return self._only

    @property
    def rest(self):
        return self._rest