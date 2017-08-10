import abjad
from abjad.tools import abctools
from abjad.tools import scoretools
from abjad.tools import systemtools


class StopTrillSpan(abctools.AbjadValueObject):

    __slots__ = ()

    def _get_lilypond_format_bundle(self, component):
        import consort
        parentage = abjad.inspect(component).get_parentage()
        prototype = scoretools.GraceContainer
        grace_container = None
        for parent in parentage:
            if isinstance(parent, prototype):
                grace_container = parent
                break
        if grace_container is None:
            return
        prototype = consort.ConsortTrillSpanner
        carrier = grace_container._carrier
        spanners = abjad.inspect(carrier).get_spanners(prototype)
        if not spanners:
            return
        bundle = systemtools.LilyPondFormatBundle()
        bundle.right.spanner_stops.append(r'\stopTrillSpan')
        return bundle
