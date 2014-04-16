# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import lilypondnametools
from abjad.tools import schemetools
from abjad.tools import spannertools
from abjad.tools.topleveltools import inspect_


class BowSpanner(spannertools.Spanner):

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(
        self,
        overrides=None,
        ):
        spannertools.Spanner.__init__(
            self,
            overrides=overrides,
            )

    ### PRIVATE METHODS ###

    def _get_lilypond_format_bundle(self, leaf):
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)
        bow_hair_contact_point = inspect_(leaf).get_indicator(
            indicatortools.BowHairContactPoint)
        bow_pressure = inspect_(leaf).get_indicator(
            indicatortools.BowPressure)
        bow_technique = inspect_(leaf).get_indicator(
            indicatortools.BowTechnique)
        string_contact_point = inspect_(leaf).get_indicator(
            indicatortools.StringContactPoint)
        if self._is_my_only_leaf(leaf):
            return lilypond_format_bundle
        self._make_bow_hair_contact_point_overrides(
            bow_hair_contact_point=bow_hair_contact_point,
            lilypond_format_bundle=lilypond_format_bundle,
            )
        if not self._is_my_last_leaf(leaf):
            lilypond_format_bundle.right.spanner_starts.append(r'\glissando')
            self._make_glissando_overrides(
                bow_pressure=bow_pressure,
                bow_technique=bow_technique,
                lilypond_format_bundle=lilypond_format_bundle,
                string_contact_point=string_contact_point,
                )

        return lilypond_format_bundle

    def _make_bow_hair_contact_point_overrides(
        self,
        lilypond_format_bundle=None,
        bow_hair_contact_point=None,
        ):
        bow_hair_contact_point = bow_hair_contact_point.markup
        stencil_override = lilypondnametools.LilyPondGrobOverride(
            grob_name='NoteHead',
            is_once=True,
            property_path='stencil',
            value=schemetools.Scheme('ly:text-interface::print'),
            )
        text_override = lilypondnametools.LilyPondGrobOverride(
            grob_name='NoteHead',
            is_once=True,
            property_path='text',
            value=bow_hair_contact_point.markup,
            )
        stencil_override_string = '\n'.join(
            stencil_override.override_format_pieces)
        text_override_string = '\n'.join(text_override.override_format_pieces)
        lilypond_format_bundle.grob_overrides.append(stencil_override_string)
        lilypond_format_bundle.grob_overrides.append(text_override_string)

    def _make_glissando_overrides(
        self,
        bow_pressure=None,
        bow_technique=None,
        lilypond_format_bundle=None,
        string_contact_point=None,
        ):
        pass
