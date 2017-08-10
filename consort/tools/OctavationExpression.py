from abjad import attach
from abjad import inspect
from abjad import iterate
from abjad.tools import abctools
from abjad.tools import indicatortools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools import spannertools


class OctavationExpression(abctools.AbjadValueObject):
    r'''An octavation expression.
    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(self):
        pass

    ### SPECIAL METHODS ###

    def __call__(self, music, name=None):
        leaves = list(iterate(music).by_leaf())
        weights = []
        weighted_pitches = []
        for leaf in leaves:
            weight = float(inspect(leaf).get_duration())
            if isinstance(leaf, abjad.Note):
                pitch = float(leaf.written_pitch)
                weighted_pitch = pitch * weight
                weights.append(weight)
                weighted_pitches.append(weighted_pitch)
            elif isinstance(leaf, abjad.Chord):
                for pitch in leaf.written_pitches:
                    pitch = float(pitch)
                    weighted_pitch = pitch * weight
                    weighted_pitches.append(weighted_pitch)
                    weights.append(weight)
        sum_of_weights = sum(weights)
        sum_of_weighted_pitches = sum(weighted_pitches)
        weighted_average = sum_of_weighted_pitches / sum_of_weights
        #print(music, weighted_average)
        clef = abjad.inspect(leaves[0]).get_effective(indicatortools.Clef)
        octavation_spanner = None
        if clef == indicatortools.Clef('treble'):
            if int(abjad.NamedPitch('C6')) <= int(weighted_average):
                octavation_spanner = spannertools.OctavationSpanner()
        elif clef == indicatortools.Clef('bass'):
            pass
        if octavation_spanner is not None:
            attach(octavation_spanner, music)
