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
                ratio=mathtools.Ratio((1,)),
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
        music_specifier,
        pitch_choices,
        previous_pitch,
        seed_session,
        ):
        pitch = self._get_pitch(
            attack_point_signature,
            pitch_choices,
            previous_pitch,
            seed_session.current_phrased_voicewise_logical_tie_seed,
            )
        pitch = self._apply_deviation(
            pitch,
            seed_session.current_unphrased_voicewise_logical_tie_seed,
            )
        return pitch

    ### PRIVATE METHODS ###

    def _get_pitch(
        self,
        attack_point_signature,
        pitch_choices,
        previous_pitch,
        seed,
        ):
        pitch = pitch_choices[seed]
        if pitch_choices and \
            1 < len(set(pitch_choices)) and \
            self.forbid_repetitions:
            if self.pitch_application_rate == 'phrase':
                if attack_point_signature.is_first_of_phrase:
                    while pitch == previous_pitch:
                        seed += 1
                        pitch = pitch_choices[seed]
            elif self.pitch_application_rate == 'division':
                if attack_point_signature.is_first_of_division:
                    while pitch == previous_pitch:
                        seed += 1
                        pitch = pitch_choices[seed]
            else:
                while pitch == previous_pitch:
                    seed += 1
                    pitch = pitch_choices[seed]
        return pitch