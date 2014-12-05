# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import rhythmmakertools


class MusicSpecifier(abctools.AbjadValueObject):
    r'''A music specifier.

    ::

        >>> import consort
        >>> music_specifier = consort.MusicSpecifier()
        >>> print(format(music_specifier))
        consort.tools.MusicSpecifier()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachment_handler',
        '_grace_handler',
        '_hash',
        '_is_sentinel',
        '_labels',
        '_pitch_handler',
        '_pitches_are_nonsemantic',
        '_rhythm_maker',
        '_seed',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        attachment_handler=None,
        grace_handler=None,
        is_sentinel=None,
        labels=None,
        pitch_handler=None,
        pitches_are_nonsemantic=None,
        rhythm_maker=None,
        seed=None,
        ):
        import consort
        if attachment_handler is not None:
            assert isinstance(attachment_handler, consort.AttachmentHandler)
        self._attachment_handler = attachment_handler
        if grace_handler is not None:
            assert isinstance(grace_handler, consort.GraceHandler)
        self._grace_handler = grace_handler
        self._hash = None
        if is_sentinel is not None:
            is_sentinel = bool(is_sentinel)
        self._is_sentinel = is_sentinel
        if labels is not None:
            if isinstance(labels, str):
                labels = (labels,)
            labels = tuple(str(_) for _ in labels)
        self._labels = labels
        if pitch_handler is not None:
            assert isinstance(pitch_handler, consort.PitchHandler)
        self._pitch_handler = pitch_handler
        if pitches_are_nonsemantic is not None:
            pitches_are_nonsemantic = bool(pitches_are_nonsemantic)
        self._pitches_are_nonsemantic = pitches_are_nonsemantic
        if rhythm_maker is not None:
            assert isinstance(rhythm_maker, rhythmmakertools.RhythmMaker)
        self._rhythm_maker = rhythm_maker
        if seed is not None:
            seed = int(seed)
        self._seed = seed

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            if format(self) == format(expr):
                return True
        return False

    def __hash__(self):
        if self._hash is None:
            hash_values = (type(self), format(self))
            self._hash = hash(hash_values)
        return self._hash

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        r'''Attribute manifest.

        ::
            
            >>> import consort
            >>> music_specifier = consort.MusicSpecifier()
            >>> print(format(music_specifier._attribute_manifest))
            systemtools.AttributeManifest()

        '''
        from abjad.tools import systemtools
        from scoremanager import idetools
        import consort
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='attachment_handler',
                display_string='attachment maker',
                command='am',
                editor=consort.AttachmentHandler,
                ),
            systemtools.AttributeDetail(
                name='grace_handler',
                display_string='grace maker',
                command='gm',
                editor=consort.GraceHandler,
                ),
            systemtools.AttributeDetail(
                name='labels',
                display_string='labels',
                command='l',
                editor=idetools.getters.get_strings,
                ),
            systemtools.AttributeDetail(
                name='pitch_handler',
                display_string='pitch maker',
                command='pm',
                editor=consort.PitchHandler,
                ),
            systemtools.AttributeDetail(
                name='rhythm_maker',
                display_string='rhythm maker',
                command='rm',
                editor=rhythmmakertools.RhythmMaker,
                ),
            systemtools.AttributeDetail(
                name='seed',
                display_string='seed',
                command='se',
                editor=idetools.getters.get_integer,
                ),
            )

    ### PUBLIC PROPERTIES ###

    @property
    def attachment_handler(self):
        return self._attachment_handler

    @property
    def grace_handler(self):
        return self._grace_handler

    @property
    def is_sentinel(self):
        return self._is_sentinel

    @property
    def labels(self):
        return self._labels

    @property
    def pitch_handler(self):
        return self._pitch_handler

    @property
    def pitches_are_nonsemantic(self):
        return self._pitches_are_nonsemantic

    @property
    def rhythm_maker(self):
        return self._rhythm_maker

    @property
    def seed(self):
        return self._seed