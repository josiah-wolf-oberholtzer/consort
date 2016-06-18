# -*- encoding: utf-8 -*-
from abjad import new
from abjad.tools import instrumenttools
from abjad.tools import markuptools
from abjad.tools import systemtools


class Instrument(instrumenttools.Instrument):
    r'''A fancy instrument indicator.

    ::

        >>> import consort
        >>> instrument_one = consort.Instrument(
        ...     instrument_name_markup='Bassoon',
        ...     short_instrument_name_markup='Bsn.',
        ...     instrument_change_markup='B!',
        ...     )
        >>> instrument_two = consort.Instrument(
        ...     instrument_name_markup='Cuica',
        ...     short_instrument_name_markup='Cu.',
        ...     instrument_change_markup='C!',
        ...     )

    ::

        >>> staff = Staff("c'4 d'4 e'4 f'4 g'4 a'4 b'4 c''4")
        >>> attach(instrument_one, staff[0])
        >>> attach(instrument_two, staff[2])
        >>> attach(instrument_two, staff[4])
        >>> attach(instrument_one, staff[6])
        >>> print(format(staff))
        \new Staff {
            \set Staff.instrumentName = \markup { Bassoon }
            \set Staff.shortInstrumentName = \markup { Bsn. }
            c'4
            d'4
            \set Staff.instrumentName = \markup { Cuica }
            \set Staff.shortInstrumentName = \markup { Cu. }
            e'4 ^ \markup { C! }
            f'4
            g'4
            a'4
            \set Staff.instrumentName = \markup { Bassoon }
            \set Staff.shortInstrumentName = \markup { Bsn. }
            b'4 ^ \markup { B! }
            c''4
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_instrument_change_markup',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        instrument_name=None,
        short_instrument_name=None,
        instrument_name_markup=None,
        short_instrument_name_markup=None,
        allowable_clefs=None,
        pitch_range=None,
        sounding_pitch_of_written_middle_c=None,
        instrument_change_markup=None,
        ):
        instrument_name_markup = markuptools.Markup(
            instrument_name_markup, direction=None,
            )
        short_instrument_name_markup = markuptools.Markup(
            short_instrument_name_markup, direction=None,
            )
        instrumenttools.Instrument.__init__(
            self,
            instrument_name=instrument_name,
            short_instrument_name=short_instrument_name,
            instrument_name_markup=instrument_name_markup,
            short_instrument_name_markup=short_instrument_name_markup,
            allowable_clefs=allowable_clefs,
            pitch_range=pitch_range,
            sounding_pitch_of_written_middle_c=sounding_pitch_of_written_middle_c,
            )
        self._instrument_change_markup = markuptools.Markup(
            instrument_change_markup, direction=Up,
            )

    ### PRIVATE METHODS ###

    def _get_lilypond_format_bundle(self, component):
        bundle = systemtools.LilyPondFormatBundle()
        previous_instrument = component._get_effective(type(self), n=-1)
        if previous_instrument == self:
            return bundle
        previous_leaf = component._get_leaf(-1)
        if (
            self.instrument_change_markup and
            (previous_leaf or previous_instrument)
            ):
            bundle.right.markup.append(self.instrument_change_markup)
        line_one = r'\set {!s}.instrumentName = {!s}'
        line_one = line_one.format(
            self._scope_name,
            new(self.instrument_name_markup, direction=None),
            )
        line_two = r'\set {!s}.shortInstrumentName = {!s}'
        line_two = line_two.format(
            self._scope_name,
            new(self.short_instrument_name_markup, direction=None),
            )
        bundle.context_settings.extend([line_one, line_two])
        return bundle

    ### PUBLIC PROPERTIES ###

    @property
    def instrument_change_markup(self):
        return self._instrument_change_markup
