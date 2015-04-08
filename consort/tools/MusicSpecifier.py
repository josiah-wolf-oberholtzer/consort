# -*- encoding: utf-8 -*-
import collections
import os
from abjad import new
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import rhythmmakertools
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

    __slots__ = (
        '_attachment_handler',
        '_color',
        '_grace_handler',
        '_labels',
        '_minimum_phrase_duration',
        '_pitch_handler',
        '_rhythm_maker',
        '_seed',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachment_handler=None,
        color=None,
        grace_handler=None,
        labels=None,
        minimum_phrase_duration=None,
        pitch_handler=None,
        rhythm_maker=None,
        seed=None,
        ):
        import consort
        HashCachingObject.__init__(self)
        if attachment_handler is not None:
            assert isinstance(attachment_handler, consort.AttachmentHandler)
        self._attachment_handler = attachment_handler
        if color is not None:
            color = str(color)
        self._color = color
        if grace_handler is not None:
            assert isinstance(grace_handler, consort.GraceHandler)
        self._grace_handler = grace_handler
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

    ### SPECIAL METHODS ###

    def __illustrate__(self, annotate=False, verbose=True, **kwargs):
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
            >>> illustration = piano_glissando_music_specifier.__illustrate__(
            ...     annotate=True,
            ...     verbose=False,
            ...     )

        Returns LilyPond file.
        """
        import consort
        score_template = consort.StringQuartetScoreTemplate(split=False)
        segment_maker = consort.SegmentMaker(
            desired_duration_in_seconds=10,
            discard_final_silence=True,
            is_annotated=annotate,
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
                counts=(0, 3, 4, 2, 5),
                denominator=16,
                ),
            playing_talea=rhythmmakertools.Talea(
                counts=(6, 8, 4, 5, 6, 6, 4),
                denominator=16,
                ),
            playing_groupings=(2, 1, 2, 3, 1, 1, 2, 2),
            repeat=True,
            silence_talea=rhythmmakertools.Talea(
                counts=(2, 4, 6, 3, 4, 10),
                denominator=16,
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
        lilypond_file.file_initial_user_includes[:] = [consort_stylesheet_path]
        lilypond_file.use_relative_includes = False
        # TODO: fix stylesheet path
        return lilypond_file

    ### PUBLIC METHODS ###

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
                        ratio=mathtools.Ratio(1, 2, 3),
                        ),
                    ),
                )

        Returns new music specifier.
        '''
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
    def grace_handler(self):
        return self._grace_handler

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
    def rhythm_maker(self):
        return self._rhythm_maker

    @property
    def seed(self):
        return self._seed