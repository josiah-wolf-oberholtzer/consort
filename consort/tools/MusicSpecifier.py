# -*- encoding: utf-8 -*-
import collections
import os
from abjad import new
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import instrumenttools
from abjad.tools import lilypondfiletools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools import rhythmmakertools
from abjad.tools import stringtools
from consort.tools.HashCachingObject import HashCachingObject


class MusicSpecifier(HashCachingObject):
    r'''A music specifier.

    ::

        >>> import consort
        >>> music_specifier = consort.MusicSpecifier()
        >>> print(format(music_specifier))
        consort.tools.MusicSpecifier()

    ..  container:: example

        MusicSpecifier can accept CompositeRhythmMakers in their `rhythm_maker`
        slot:

        ::

            >>> music_specifier = consort.MusicSpecifier(
            ...     rhythm_maker=consort.CompositeRhythmMaker(),
            ...     )

    '''

    ### CLASS VARIABLES ###

    __is_terminal_ajv_list_item__ = True

    __slots__ = (
        '_attachment_handler',
        '_color',
        '_comment',
        '_grace_handler',
        '_instrument',
        '_labels',
        '_minimum_phrase_duration',
        '_pitch_handler',
        '_register_handler',
        '_rhythm_maker',
        '_seed',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachment_handler=None,
        color=None,
        comment=None,
        grace_handler=None,
        instrument=None,
        labels=None,
        minimum_phrase_duration=None,
        pitch_handler=None,
        register_handler=None,
        rhythm_maker=None,
        seed=None,
        ):
        import consort
        HashCachingObject.__init__(self)
        if attachment_handler is not None:
            assert isinstance(attachment_handler, consort.AttachmentHandler)
        self._attachment_handler = attachment_handler
        self._color = color
        if grace_handler is not None:
            assert isinstance(grace_handler, consort.GraceHandler)
        self._grace_handler = grace_handler
        if instrument is not None:
            assert isinstance(instrument, instrumenttools.Instrument)
        self._instrument = instrument
        if labels is not None:
            if isinstance(labels, str):
                labels = (labels,)
            labels = tuple(str(_) for _ in labels)
        self._labels = labels
        if minimum_phrase_duration is not None:
            minimum_phrase_duration = \
                durationtools.Duration(minimum_phrase_duration)
            assert 0 <= minimum_phrase_duration
        self._minimum_phrase_duration = minimum_phrase_duration
        if pitch_handler is not None:
            assert isinstance(pitch_handler, consort.PitchHandler)
        self._pitch_handler = pitch_handler
        if register_handler is not None:
            assert isinstance(register_handler, consort.RegisterHandler)
        self._register_handler = register_handler
        if rhythm_maker is not None:
            prototype = (
                rhythmmakertools.RhythmMaker,
                consort.CompositeRhythmMaker,
                )
            assert isinstance(rhythm_maker, prototype)
        self._rhythm_maker = rhythm_maker
        if seed is not None:
            seed = int(seed)
        self._seed = seed
        if comment is not None:
            comment = str(comment)
        self._comment = comment

    ### SPECIAL METHODS ###

    def __illustrate__(
        self,
        annotate=False,
        verbose=True,
        package_name=None,
        **kwargs
        ):
        r"""Illustrates music specifier.

        ::

            >>> piano_glissando_music_specifier = consort.MusicSpecifier(
            ...     attachment_handler=consort.AttachmentHandler(
            ...         glissando=spannertools.Glissando(),
            ...         ),
            ...     color=None,
            ...     labels=[],
            ...     pitch_handler=consort.AbsolutePitchHandler(
            ...         pitch_specifier="c' f' c'' f'' c''' c'' c' c'''",
            ...         ),
            ...     rhythm_maker=consort.CompositeRhythmMaker(
            ...         last=rhythmmakertools.IncisedRhythmMaker(
            ...             incise_specifier=rhythmmakertools.InciseSpecifier(
            ...                 prefix_counts=[0],
            ...                 suffix_talea=[1],
            ...                 suffix_counts=[1],
            ...                 talea_denominator=16,
            ...                 ),
            ...             ),
            ...         default=rhythmmakertools.EvenDivisionRhythmMaker(
            ...             denominators=(4,),
            ...             duration_spelling_specifier=rhythmmakertools.DurationSpellingSpecifier(
            ...                 decrease_durations_monotonically=True,
            ...                 forbidden_written_duration=(1, 4),
            ...                 forbid_meter_rewriting=True,
            ...                 ),
            ...             ),
            ...         ),
            ...     )

        ::

            >>> illustration = piano_glissando_music_specifier.__illustrate__(
            ...     annotate=True,
            ...     verbose=False,
            ...     )

        Returns LilyPond file.
        """
        import consort
        score_template = consort.StringQuartetScoreTemplate(
            split=False,
            without_instruments=False,
            )
        segment_maker = consort.SegmentMaker(
            desired_duration_in_seconds=10,
            discard_final_silence=True,
            annotate_colors=True,
            annotate_phrasing=annotate,
            permitted_time_signatures=[
                (3, 8),
                (4, 8),
                (5, 8),
                (6, 8),
                (7, 8),
                ],
            score_template=score_template,
            tempo=indicatortools.Tempo((1, 4), 72),
            timespan_quantization=(1, 8),
            )
        timespan_maker = consort.TaleaTimespanMaker(
            initial_silence_talea=rhythmmakertools.Talea(
                counts=[0, 2, 1],
                denominator=8,
                ),
            playing_talea=rhythmmakertools.Talea(
                counts=[3, 2, 1, 4, 5, 3, 1, 2],
                denominator=8,
                ),
            playing_groupings=[2, 1, 2, 3, 1, 3, 4, 1, 2, 3],
            repeat=True,
            silence_talea=rhythmmakertools.Talea(
                counts=[1, 2, 3, 1, 2, 4],
                denominator=8,
                ),
            step_anchor=Right,
            synchronize_groupings=False,
            synchronize_step=False,
            timespan_specifier=consort.TimespanSpecifier(
                minimum_duration=durationtools.Duration(1, 8),
                ),
            )
        segment_maker.add_setting(
            timespan_maker=timespan_maker,
            violin_1=self,
            violin_2=self,
            viola=self,
            cello=self,
            )
        segment_metadata = collections.OrderedDict(
            segment_count=1,
            segment_number=1,
            )
        lilypond_file, segment_metadata = segment_maker(
            segment_metadata=segment_metadata,
            verbose=verbose,
            )
        consort_stylesheet_path = os.path.join(
            consort.__path__[0],
            'stylesheets',
            'stylesheet.ily',
            )
        consort_stylesheet_path = os.path.abspath(consort_stylesheet_path)
        lilypond_file = new(
            lilypond_file,
            includes=[consort_stylesheet_path],
            use_relative_includes=False,
            date_time_token=False,
            )
        if package_name is not None:
            header = lilypondfiletools.Block('header')
            title = stringtools.to_space_delimited_lowercase(package_name)
            title = title.title()
            title = markuptools.Markup(title).override(('font-name', 'Didot'))
            header.title = title
            header.tagline = markuptools.Markup('""')
            lilypond_file.items.insert(0, header)
        return lilypond_file

    ### PUBLIC METHODS ###

    def rotate(self, rotation):
        seed = self.seed or 0
        seed = seed + rotation
        return new(self, seed=seed)

    def transpose(self, expr):
        r'''Transposes music specifier.

        ::

            >>> music_specifier = consort.MusicSpecifier(
            ...     pitch_handler=consort.AbsolutePitchHandler(
            ...         pitch_specifier = consort.PitchSpecifier(
            ...             pitch_segments=(
            ...                 "c' e' g'",
            ...                 "fs' gs'",
            ...                 "b",
            ...                 ),
            ...             ratio=(1, 2, 3),
            ...             ),
            ...         ),
            ...     )
            >>> transposed_music_specifier = music_specifier.transpose('-M2')
            >>> print(format(transposed_music_specifier))
            consort.tools.MusicSpecifier(
                pitch_handler=consort.tools.AbsolutePitchHandler(
                    pitch_specifier=consort.tools.PitchSpecifier(
                        pitch_segments=(
                            pitchtools.PitchSegment(
                                (
                                    pitchtools.NamedPitch('bf'),
                                    pitchtools.NamedPitch("d'"),
                                    pitchtools.NamedPitch("f'"),
                                    ),
                                item_class=pitchtools.NamedPitch,
                                ),
                            pitchtools.PitchSegment(
                                (
                                    pitchtools.NamedPitch("e'"),
                                    pitchtools.NamedPitch("fs'"),
                                    ),
                                item_class=pitchtools.NamedPitch,
                                ),
                            pitchtools.PitchSegment(
                                (
                                    pitchtools.NamedPitch('a'),
                                    ),
                                item_class=pitchtools.NamedPitch,
                                ),
                            ),
                        ratio=mathtools.Ratio((1, 2, 3)),
                        ),
                    ),
                )

        Returns new music specifier.
        '''
        if isinstance(expr, str):
            try:
                pitch = pitchtools.NamedPitch(expr)
                expr = pitchtools.NamedPitch('C4') - pitch
            except:
                expr = pitchtools.NamedInterval(expr)
        pitch_handler = self.pitch_handler
        if pitch_handler is not None:
            pitch_handler = pitch_handler.transpose(expr)
        return new(
            self,
            pitch_handler=pitch_handler,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_handler(self):
        return self._attachment_handler

    @property
    def color(self):
        return self._color

    @property
    def comment(self):
        return self._comment

    @property
    def grace_handler(self):
        return self._grace_handler

    @property
    def instrument(self):
        return self._instrument

    @property
    def labels(self):
        return self._labels

    @property
    def minimum_phrase_duration(self):
        return self._minimum_phrase_duration

    @property
    def pitch_handler(self):
        return self._pitch_handler

    @property
    def register_handler(self):
        return self._register_handler

    @property
    def rhythm_maker(self):
        return self._rhythm_maker

    @property
    def seed(self):
        return self._seed
