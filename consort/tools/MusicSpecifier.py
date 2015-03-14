# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
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

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_handler(self):
        return self._attachment_handler

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