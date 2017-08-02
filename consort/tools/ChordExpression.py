import abjad
from abjad import attach
from abjad.tools import pitchtools
from abjad.tools import selectiontools
from consort.tools.LogicalTieExpression import LogicalTieExpression


class ChordExpression(LogicalTieExpression):
    r'''A chord expression.

    ::

        >>> chord_expression = consort.ChordExpression(
        ...     arpeggio_direction=Down,
        ...     chord_expr=(-1, 3, 7),
        ...     )
        >>> print(format(chord_expression))
        consort.tools.ChordExpression(
            chord_expr=abjad.IntervalSegment(
                (
                    abjad.NumberedInterval(-1),
                    abjad.NumberedInterval(3),
                    abjad.NumberedInterval(7),
                    ),
                item_class=abjad.NumberedInterval,
                ),
            arpeggio_direction=Down,
            )

    ::

        >>> staff = abjad.Staff(r"c'4 d'4 \p -\accent ~ d'4 e'4")
        >>> pitch_range = pitchtools.PitchRange.from_pitches('C3', 'C6')
        >>> abjad.attach(pitch_range, staff, scope=abjad.Staff)
        >>> logical_tie = abjad.inspect(staff[1]).get_logical_tie()
        >>> chord_expression(logical_tie)
        >>> print(format(staff))
        \new Staff {
            c'4
            \arpeggioArrowDown
            <cs' f' a'>4 -\accent \arpeggio \p ~
            <cs' f' a'>4
            e'4
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_arpeggio_direction',
        '_chord_expr',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        chord_expr=None,
        arpeggio_direction=None,
        ):
        assert arpeggio_direction in (Up, Down, Center, None)
        if chord_expr is not None:
            assert len(chord_expr)
            prototype = (abjad.IntervalSegment, abjad.PitchSegment)
            if isinstance(chord_expr, prototype):
                result = chord_expr
            elif isinstance(chord_expr, str):
                result = abjad.PitchSegment(chord_expr)
            else:
                try:
                    result = sorted(chord_expr)
                    result = abjad.IntervalSegment(result)
                except:
                    result = abjad.PitchSegment(chord_expr)
            chord_expr = result
        self._arpeggio_direction = arpeggio_direction
        self._chord_expr = chord_expr

    ### SPECIAL METHODS ###

    def __call__(
        self,
        logical_tie,
        pitch_range=None,
        ):
        assert isinstance(logical_tie, selectiontools.LogicalTie), logical_tie
        if isinstance(self.chord_expr, abjad.IntervalSegment):
            pitches = self._get_pitches_from_intervals(
                logical_tie.head.written_pitch,
                pitch_range,
                logical_tie,
                )
        else:
            pitches = self.chord_expr
        if len(pitches) == 2:
            interval = pitches[0] - pitches[1]
            if interval.quality_string in ('augmented', 'diminished'):
                chord = abjad.Chord(pitches, 1)
                abjad.Accidental.respell_with_sharps(chord)
                pitches = chord.written_pitches
                interval = pitches[0] - pitches[1]
            if interval.quality_string in ('augmented', 'diminished'):
                chord = abjad.Chord(pitches, 1)
                abjad.Accidental.respell_with_flats(chord)
                pitches = chord.written_pitches
        for i, leaf in enumerate(logical_tie):
            chord = abjad.Chord(leaf)
            chord.written_pitches = pitches
            self._replace(leaf, chord)
            if not i and self.arpeggio_direction is not None:
                arpeggio = abjad.Arpeggio(self.arpeggio_direction)
                attach(arpeggio, chord)

    ### PRIVATE METHODS ###

    @staticmethod
    def _score_pitch_set(pitch_set):
        import consort
        buckets = {}
        for pitch in pitch_set:
            if pitch._get_diatonic_pitch_number() not in buckets:
                buckets[pitch._get_diatonic_pitch_number()] = set()
            buckets[pitch._get_diatonic_pitch_number()].add(pitch)
        penalty = 0
        for diatonic_pitch_number, bucket in sorted(buckets.items()):
            penalty = penalty + (len(bucket) - 1)
        for one, two in consort.iterate_nwise(sorted(buckets.items())):
            number_1, bucket_1 = one
            number_2, bucket_2 = two
            if abs(number_1 - number_2) != 1:
                continue
            one_has_flats, one_has_sharps = False, False
            for pitch in bucket_1:
                if pitch._get_alteration() > 0:
                    one_has_sharps = True
                if pitch._get_alteration() < 0:
                    one_has_flats = True
            two_has_flats, two_has_sharps = False, False
            for pitch in bucket_2:
                if pitch._get_alteration() > 0:
                    two_has_sharps = True
                if pitch._get_alteration() < 0:
                    two_has_flats = True
            if one_has_flats and two_has_sharps:
                penalty += 1
            if one_has_sharps and two_has_flats:
                penalty += 1
        return penalty

    @staticmethod
    def _flip_accidental(pitch):
        if not pitch._get_alteration():
            return pitch
        elif 0 < pitch._get_alteration():
            return pitch._respell_with_flats()
        return pitch._respell_with_sharps()

    @staticmethod
    def _reshape_pitch_set(pitch_set):
        altered = {}
        unaltered = {}
        for pitch in pitch_set:
            diatonic_pitch_number = pitch._get_diatonic_pitch_number()
            if pitch._get_alteration():
                if diatonic_pitch_number not in altered:
                    altered[diatonic_pitch_number] = []
                altered[diatonic_pitch_number].append(pitch)
            else:
                unaltered[diatonic_pitch_number] = pitch
        new_altered = {}
        for diatonic_pitch_number, altered_pitches in altered.items():
            while altered_pitches:
                altered_pitch = altered_pitches.pop()
                if diatonic_pitch_number not in unaltered and \
                    diatonic_pitch_number not in new_altered:
                    if diatonic_pitch_number not in new_altered:
                        new_altered[diatonic_pitch_number] = []
                    new_altered[diatonic_pitch_number].append(altered_pitch)
                else:
                    new_pitch = ChordExpression._flip_accidental(altered_pitch)
                    new_diatonic_pitch_number = new_pitch._get_diatonic_pitch_number()
                    if new_diatonic_pitch_number not in new_altered:
                        new_altered[new_diatonic_pitch_number] = []
                    new_altered[new_diatonic_pitch_number].append(new_pitch)
        result = set(unaltered.values())
        for altered_pitches in new_altered.values():
            result.update(altered_pitches)
        result = pitchtools.PitchSet(result)
        return result

    @staticmethod
    def _respell_pitch_set(pitch_set):
        r'''Respell pitch set.

        ::

            >>> pitch_set = pitchtools.PitchSet("c' e' g'")
            >>> consort.ChordExpression._respell_pitch_set(pitch_set)
            PitchSet(["c'", "e'", "g'"])

        ::

            >>> pitch_set = pitchtools.PitchSet("c' e' g' c'' cs'' g''")
            >>> consort.ChordExpression._respell_pitch_set(pitch_set)
            PitchSet(["c'", "e'", "g'", "c''", "df''", "g''"])

        ::

            >>> pitch_set = pitchtools.PitchSet("bf d' f' fs' bf' f''")
            >>> consort.ChordExpression._respell_pitch_set(pitch_set)
            PitchSet(['bf', "d'", "f'", "gf'", "bf'", "f''"])

        ::

            >>> pitch_set = pitchtools.PitchSet("b' c'' cs'' d''")
            >>> consort.ChordExpression._respell_pitch_set(pitch_set)
            PitchSet(["b'", "c''", "cs''", "d''"])

        ::

            >>> pitch_set = pitchtools.PitchSet("cf' c' cs'")
            >>> consort.ChordExpression._respell_pitch_set(pitch_set)
            PitchSet(["c'", "df'", "b'"])

        ::

            >>> pitch_set = pitchtools.PitchSet("e ff f fs g")
            >>> consort.ChordExpression._respell_pitch_set(pitch_set)
            PitchSet(['e', 'f', 'gf', 'g'])

        '''
        initial_score = ChordExpression._score_pitch_set(pitch_set)
        if not initial_score:
            return pitch_set
        flat_pitch_set = pitchtools.PitchSet(
            _._respell_with_flats()
            for _ in pitch_set
            )
        flat_score = ChordExpression._score_pitch_set(flat_pitch_set)
        if not flat_score:
            return flat_pitch_set
        sharp_pitch_set = pitchtools.PitchSet(
            _._respell_with_sharps()
            for _ in pitch_set
            )
        sharp_score = ChordExpression._score_pitch_set(sharp_pitch_set)
        if not sharp_score:
            return sharp_pitch_set
        scored_pitch_sets = [
            (initial_score, pitch_set),
            (flat_score, flat_pitch_set),
            (sharp_score, sharp_pitch_set),
            ]
        scored_pitch_sets.sort()
        reshaped_pitch_set = ChordExpression._reshape_pitch_set(
            scored_pitch_sets[0][1])
        reshaped_score = ChordExpression._score_pitch_set(reshaped_pitch_set)
        scored_pitch_sets.append((reshaped_score, reshaped_pitch_set))
        scored_pitch_sets.sort()
        return scored_pitch_sets[0][1]

    def _get_pitches_from_intervals(self, base_pitch, pitch_range, logical_tie):
        import consort
        chord_expr = self.chord_expr or ()
        new_chord_expr = chord_expr
        if pitch_range is not None:
            sorted_intervals = sorted(chord_expr, key=lambda x: x.semitones)
            maximum = sorted_intervals[-1]
            maximum_pitch = base_pitch.transpose(maximum)
            minimum = sorted_intervals[0]
            minimum_pitch = base_pitch.transpose(minimum)
            if maximum_pitch not in pitch_range:
                new_chord_expr = [x - maximum for x in chord_expr]
            elif minimum_pitch not in pitch_range:
                new_chord_expr = [x - minimum for x in chord_expr]

        pitches = [base_pitch.transpose(x) for x in new_chord_expr]
        pitches = [abjad.NamedPitch(float(x)) for x in pitches]
        if pitch_range is not None:
            # Not exhaustive, but good enough.
            while min(pitches) < pitch_range.start_pitch:
                pitches = [_.transpose(12) for _ in pitches]
            while max(pitches) > pitch_range.stop_pitch:
                pitches = [_.transpose(-12) for _ in pitches]
            if not all(pitch in pitch_range for pitch in pitches):
                print('Voice:', consort.SegmentMaker.logical_tie_to_voice(
                    logical_tie).name)
                print('Pitch range:', pitch_range)
                print('Base pitch:', base_pitch)
                print('Chord expression:', chord_expr)
                print('Resulting pitches:', pitches)
                raise Exception

        pitch_set = self._respell_pitch_set(pitchtools.PitchSet(pitches))
        pitches = abjad.PitchSegment(sorted(pitch_set))

        return pitches

    ### PUBLIC PROPERTIES ###

    @property
    def arpeggio_direction(self):
        return self._arpeggio_direction

    @property
    def chord_expr(self):
        return self._chord_expr
