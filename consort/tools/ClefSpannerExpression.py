# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad import attach
from abjad import inspect_
from abjad.tools import abctools
from abjad.tools import scoretools


class ClefSpannerExpression(abctools.AbjadValueObject):
    r'''A clef spanner expression.
    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(self):
        pass

    ### SPECIAL METHODS ###

    def __call__(self, music, name=None):
        import consort
        leaves = music.select_leaves()
        weights = []
        weighted_pitches = []
        for leaf in leaves:
            weight = float(inspect_(leaf).get_duration())
            if isinstance(leaf, scoretools.Note):
                pitch = float(leaf.written_pitch)
                weighted_pitch = pitch * weight
                weights.append(weight)
                weighted_pitches.append(weighted_pitch)
            elif isinstance(leaf, scoretools.Chord):
                for pitch in leaf.written_pitches:
                    pitch = float(pitch)
                    weighted_pitch = pitch * weight
                    weighted_pitches.append(weighted_pitch)
                weights.append(weight)
        sum_of_weights = sum(weights)
        sum_of_weighted_pitches = sum(weighted_pitches)
        weighted_average = sum_of_weighted_pitches / sum_of_weights
        if weighted_average < 0:
            clef_spanner = consort.ClefSpanner('bass')
        else:
            clef_spanner = consort.ClefSpanner('treble')
        attach(clef_spanner, music, name=name)
