from abjad.tools import datastructuretools


class HarmonicField(datastructuretools.TypedList):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        items=None,
        ):
        import consort
        mapping = {}
        items = items or []
        entries = [self._item_callable(x) for x in items]
        for entry in entries:
            mapping[float(entry.structural_pitch)] = entry
        items = list(mapping.values())
        datastructuretools.TypedList.__init__(
            self,
            items=items,
            item_class=consort.makers.HarmonicFieldEntry,
            keep_sorted=True,
            )

    ### PRIVATE METHODS ###

    def _find_matching_entries(
        self,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        from abjad.tools import pitchtools
        matching_entries, nonmatching_entries = self[:], []
        if structural_pitch_class_subset:
            pitch_clas_set = pitchtools.PitchClassSet(
                items=structural_pitch_class_subset,
                item_class=pitchtools.NumberedPitchClass,
                )
            for entry in tuple(matching_entries):
                structural_pitch = entry.structural_pitch
                structural_pitch_class = structural_pitch.numbered_pitch_class
                if structural_pitch_class not in pitch_clas_set:
                    matching_entries.remove(entry)
                    nonmatching_entries.append(entry)
        if structural_pitch_range:
            pitch_range = pitchtools.PitchRange(structural_pitch_range)
            for entry in tuple(matching_entries):
                structural_pitch = entry.structural_pitch
                if structural_pitch not in pitch_range:
                    matching_entries.remove(entry)
                    nonmatching_entries.append(entry)
        return matching_entries, nonmatching_entries

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import systemtools
        return systemtools.AttributeManifest()

    @property
    def _item_callable(self):
        import consort
        return consort.makers.HarmonicFieldEntry

    ### PUBLIC METHODS ###

    def invert(
        self,
        axis=None,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        from abjad.tools import pitchtools
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        axis = axis or pitchtools.NamedPitch("c'")
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.invert(axis=axis)
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + matching_entries
        return type(self)(all_entries)

    def invert_ornamental_pitches(
        self,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.invert_ornamental_pitches()
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + matching_entries
        return type(self)(all_entries)

    def retrograde(
        self,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.retrograde()
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + matching_entries
        return type(self)(all_entries)

    def rotate_pitch_classes(
        self,
        expr,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.rotate_pitch_classes(expr)
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + matching_entries
        return type(self)(all_entries)

    def transpose(
        self,
        expr,
        structural_pitch_class_subset=None,
        structural_pitch_range=None,
        ):
        matching_entries, nonmatching_entries = self._find_matching_entries(
            structural_pitch_class_subset=structural_pitch_class_subset,
            structural_pitch_range=structural_pitch_range,
            )
        altered_entries = []
        for entry in matching_entries:
            altered_entry = entry.transpose(expr)
            altered_entries.append(altered_entry)
        all_entries = nonmatching_entries + matching_entries
        return type(self)(all_entries)

    ### PUBLIC PROPERTIES ###

    @property
    def pitches(self):
        pitches = []
        for entry in self:
            pitches.extend(entry.pitches)
        return tuple(pitches)

    @property
    def pitch_range(self):
        from abjad.tools import pitchtools
        pitches = self.pitches
        minimum = min(pitches)
        maximum = max(pitches)
        pitch_range = pitchtools.PitchRange.from_pitches(minimum, maximum)
        return pitch_range