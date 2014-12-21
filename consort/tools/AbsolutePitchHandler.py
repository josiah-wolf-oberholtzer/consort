# -*- encoding: utf-8 -*-
from __future__ import print_function
from consort.tools.PitchHandler import PitchHandler


class AbsolutePitchHandler(PitchHandler):
    r'''Absolute pitch maker.

    ::

        >>> import consort
        >>> pitch_handler = consort.AbsolutePitchHandler(
        ...     pitch_specifier="c' d' e' f'",
        ...     )
        >>> print(format(pitch_handler))
        consort.tools.AbsolutePitchHandler(
            pitch_specifier=consort.tools.PitchSpecifier(
                pitch_segments=(
                    pitchtools.PitchSegment(
                        (
                            pitchtools.NamedPitch("c'"),
                            pitchtools.NamedPitch("d'"),
                            pitchtools.NamedPitch("e'"),
                            pitchtools.NamedPitch("f'"),
                            ),
                        item_class=pitchtools.NamedPitch,
                        ),
                    ),
                ratio=mathtools.Ratio(1),
                ),
            )

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    def __call__(
        self,
        attack_point_signature,
        logical_tie,
        phrase_seed,
        pitch_choices,
        pitch_range,
        previous_pitch,
        seed,
        transposition,
        ):
        pitch = self._get_pitch(
            pitch_choices,
            previous_pitch,
            seed,
            )
        self._process_logical_tie(
            logical_tie,
            pitch,
            pitch_range,
            seed,
            )
        return pitch

    ### PRIVATE METHODS ###

    def _get_pitch(
        self,
        pitch_choices,
        previous_pitch,
        seed,
        ):
        pitch = pitch_choices[seed]
        if pitch_choices and \
            1 < len(set(pitch_choices)) and \
            self.forbid_repetitions:
            while pitch == previous_pitch:
                seed += 1
                pitch = pitch_choices[seed]
        return pitch