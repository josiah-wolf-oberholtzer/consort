# -*- encoding: utf-8 -*-
from abjad import inspect_
from abjad.tools import lilypondnametools
from abjad.tools import pitchtools
from abjad.tools import spannertools


class ConsortTrillSpanner(spannertools.Spanner):
    r'''A complex trill spanner.

    ..  container:: example

        ::

            >>> staff = Staff("c'4 ~ c'8 d'8 r8 e'8 ~ e'8 r8")
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> print(format(staff))
            \new Staff {
                c'4 ~
                c'8
                d'8
                r8
                e'8 ~
                e'8
                r8
            }

        ::

            >>> import consort
            >>> complex_trill = consort.ConsortTrillSpanner(
            ...     interval='P4',
            ...     )
            >>> attach(complex_trill, staff)
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> print(format(staff))
            \new Staff {
                \pitchedTrill
                c'4 ~ \startTrillSpan f'
                c'8
                <> \stopTrillSpan
                \pitchedTrill
                d'8 \startTrillSpan g'
                <> \stopTrillSpan
                r8
                \pitchedTrill
                e'8 ~ \startTrillSpan a'
                e'8
                <> \stopTrillSpan
                r8
            }

    Allows for specifying a trill pitch via a named interval.

    Avoids silences.

    Restarts the trill on every new pitched logical tie.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_interval',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        overrides=None,
        interval=None,
        ):
        spannertools.Spanner.__init__(
            self,
            overrides=overrides,
            )
        if interval is not None:
            interval = pitchtools.NamedInterval(interval)
        self._interval = interval

    ### PRIVATE METHODS ###

    def _copy_keyword_args(self, new):
        new._interval = self.interval

    def _get_lilypond_format_bundle(self, leaf):
        from abjad.tools import scoretools
        lilypond_format_bundle = self._get_basic_lilypond_format_bundle(leaf)
        prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            scoretools.Skip,
            )
        if isinstance(leaf, prototype):
            return lilypond_format_bundle
        logical_tie = inspect_(leaf).get_logical_tie()

        starts_spanner, stops_spanner = False, False
        if leaf is logical_tie.head:
            starts_spanner = True
        after_graces = inspect_(leaf).get_grace_containers('after')
        if leaf is logical_tie.tail and not len(after_graces):
            stops_spanner = True
        elif self._is_my_last_leaf(leaf):
            stops_spanner = True

        if starts_spanner:
            previous_leaf = leaf._get_leaf(-1)
            if previous_leaf is not None:
                after_graces = inspect_(previous_leaf).get_grace_containers(
                    'after')
                if after_graces:
                    grob_override = lilypondnametools.LilyPondGrobOverride(
                        grob_name='TrillSpanner',
                        is_once=True,
                        property_path=(
                            'bound-details',
                            'left',
                            'padding',
                            ),
                        value=2,
                        )
                    string = '\n'.join(grob_override.override_format_pieces)
                    lilypond_format_bundle.grob_overrides.append(string)
            if self.interval is not None:
                string = r'\pitchedTrill'
                lilypond_format_bundle.opening.spanners.append(string)
                if hasattr(leaf, 'written_pitch'):
                    written_pitch = leaf.written_pitch
                elif hasattr(leaf, 'written_pitches'):
                    if 0 < self.interval.semitones:
                        written_pitch = max(leaf.written_pitches)
                    elif self.interval.semitones < 0:
                        written_pitch = min(leaf.written_pitches)
                trill_pitch = written_pitch.transpose(self.interval)
                string = r'\startTrillSpan {!s}'.format(trill_pitch)
            else:
                string = r'\startTrillSpan'
            lilypond_format_bundle.right.trill_pitches.append(string)

        if stops_spanner:
            next_leaf = leaf._get_leaf(1)
            if next_leaf is not None:
                string = r'<> \stopTrillSpan'
                lilypond_format_bundle.after.commands.append(string)
            else:
                string = r'\stopTrillSpan'
                lilypond_format_bundle.right.spanner_stops.append(string)

        return lilypond_format_bundle

    ### PUBLIC PROPERTIES ###

    @property
    def interval(self):
        r'''Gets optional interval of trill spanner.

        ..  container:: example

            ::

                >>> import consort
                >>> staff = Staff("c'4 d'4 e'4 f'4")
                >>> interval = pitchtools.NamedInterval('m3')
                >>> complex_trill = consort.ConsortTrillSpanner(
                ...     interval=interval)
                >>> attach(complex_trill, staff[1:-1])
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> print(format(staff))
                \new Staff {
                    c'4
                    \pitchedTrill
                    d'4 \startTrillSpan f'
                    <> \stopTrillSpan
                    \pitchedTrill
                    e'4 \startTrillSpan g'
                    <> \stopTrillSpan
                    f'4
                }

            ::

                >>> complex_trill.interval
                NamedInterval('+m3')

        '''
        return self._interval
