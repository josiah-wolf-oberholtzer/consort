import abc
import abjad
import collections
from abjad.tools import abctools
from abjad.tools import lilypondfiletools
from abjad.tools import metertools
from abjad.tools import markuptools


class TimespanMaker(abctools.AbjadValueObject):
    r'''Abstract base class for timespan makers.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_output_masks',
        '_padding',
        '_seed',
        '_timespan_specifier',
        )

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(
        self,
        division_masks=None,
        padding=None,
        seed=None,
        timespan_specifier=None,
        ):
        import consort
        if division_masks is not None:
            if isinstance(division_masks, abjad.Pattern):
                division_masks = (division_masks,)
            division_masks = abjad.PatternList(
                items=division_masks,
                )
        self._output_masks = division_masks
        if padding is not None:
            padding = abjad.Duration(padding)
        self._padding = padding
        if seed is not None:
            seed = int(seed)
        self._seed = seed
        if timespan_specifier is not None:
            assert isinstance(timespan_specifier, consort.TimespanSpecifier)
        self._timespan_specifier = timespan_specifier

    ### SPECIAL METHODS ###

    def __call__(
        self,
        layer=None,
        music_specifiers=None,
        rotation=None,
        silenced_context_names=None,
        target_timespan=None,
        timespan_inventory=None,
        ):
        if not isinstance(timespan_inventory, abjad.TimespanList):
            timespan_inventory = abjad.TimespanList(
                timespan_inventory,
                )
        if target_timespan is None:
            if timespan_inventory:
                target_timespan = timespan_inventory.timespan
            else:
                raise TypeError
        assert isinstance(timespan_inventory, abjad.TimespanList)
        if not music_specifiers:
            return timespan_inventory
        music_specifiers = self._coerce_music_specifiers(music_specifiers)
        new_timespans = self._make_timespans(
            layer=layer,
            music_specifiers=music_specifiers,
            target_timespan=target_timespan,
            timespan_inventory=timespan_inventory,
            )
        self._cleanup_silent_timespans(
            layer=layer,
            silenced_context_names=silenced_context_names,
            timespans=new_timespans,
            )
        timespan_inventory.extend(new_timespans)
        timespan_inventory.sort()
        return timespan_inventory

    def __illustrate__(self, scale=None, target_timespan=None, **kwargs):
        target_timespan = target_timespan or abjad.Timespan(0, 16)
        assert isinstance(target_timespan, abjad.Timespan)
        assert 0 < target_timespan.duration
        scale = scale or 1.5
        music_specifiers = collections.OrderedDict([
            ('A', 'A music'),
            ('B', 'B music'),
            ('C', 'C music'),
            ('D', 'D music'),
            ('E', 'E music'),
            ('F', 'F music'),
            ('G', 'G music'),
            ('H', 'H music'),
            ('I', 'I music'),
            ('J', 'J music'),
            ])
        timespan_inventory = self(
            layer=0,
            music_specifiers=music_specifiers,
            target_timespan=target_timespan,
            )
        ti_lilypond_file = timespan_inventory.__illustrate__(
            key='voice_name',
            range_=target_timespan,
            scale=scale,
            )
        ti_markup = ti_lilypond_file.items[-1]
        offset_counter = metertools.OffsetCounter(timespan_inventory)
        oc_lilypond_file = offset_counter.__illustrate__(
            range_=target_timespan,
            scale=scale,
            )
        oc_markup = oc_lilypond_file.items[-1]
        lilypond_file = lilypondfiletools.LilyPondFile.new(
            default_paper_size=['tabloid', 'landscape'],
            date_time_token=False,
            )
        lilypond_file.items.extend([
            abjad.String.normalize('''
            % Backport for pre 2.19.20 versions of LilyPond
            #(define-markup-command (overlay layout props args)
                (markup-list?)
                (apply ly:stencil-add (interpret-markup-list layout props args)))
            '''),
            ti_markup,
            markuptools.Markup.null().pad_around(2),
            oc_markup,
            ])
        lilypond_file.header_block.tagline = False
        return lilypond_file

    ### PRIVATE METHODS ###

    @staticmethod
    def _coerce_music_specifiers(music_specifiers):
        import consort
        result = collections.OrderedDict()
        prototype = (
            consort.MusicSpecifierSequence,
            consort.CompositeMusicSpecifier,
            )
        for context_name, music_specifier in music_specifiers.items():
            if music_specifier is None:
                music_specifier = [None]
            if not isinstance(music_specifier, prototype):
                music_specifier = consort.MusicSpecifierSequence(
                    music_specifiers=music_specifier,
                    )
            result[context_name] = music_specifier
        return result

    def _cleanup_silent_timespans(
        self,
        layer,
        silenced_context_names,
        timespans,
        ):
        import consort
        if not silenced_context_names or not timespans:
            return

        silent_timespans_by_context = {}
        for context_name in silenced_context_names:
            if context_name not in silent_timespans_by_context:
                silent_timespans_by_context[context_name] = \
                    abjad.TimespanList()

        sounding_timespans_by_context = {}
        sounding_timespans = abjad.TimespanList()

        for timespan in timespans:
            voice_name = timespan.voice_name
            if isinstance(timespan, consort.PerformedTimespan):
                if voice_name not in sounding_timespans_by_context:
                    sounding_timespans_by_context[voice_name] = \
                        abjad.TimespanList()
                sounding_timespans_by_context[voice_name].append(timespan)
                sounding_timespans.append(timespan)
            else:
                if voice_name not in silent_timespans_by_context:
                    silent_timespans_by_context[voice_name] = \
                        abjad.TimespanList()
                silent_timespans_by_context[voice_name].append(timespan)

        sounding_timespans.sort()
        sounding_timespans.compute_logical_or()

        # Create silences.
        for shard in sounding_timespans.partition(True):
            for context_name in silenced_context_names:
                timespan = consort.SilentTimespan(
                    layer=layer,
                    voice_name=context_name,
                    start_offset=shard.start_offset,
                    stop_offset=shard.stop_offset,
                    )
                silent_timespans_by_context[context_name].append(timespan)

        # Remove any overlap between performed and silent timespans.
        # Then add the silent timespans into the original timespan inventory.
        for context_name, silent_timespans in \
            sorted(silent_timespans_by_context.items()):
            silent_timespans.sort()
            if context_name in sounding_timespans_by_context:
                for timespan in sounding_timespans_by_context[context_name]:
                    silent_timespans - timespan
            timespans.extend(silent_timespans)

    ### PUBLIC METHODS ###

    def rotate(self, rotation):
        seed = self.seed or 0
        seed = seed + rotation
        return abjad.new(self, seed=seed)

    ### PUBLIC PROPERTIES ###

    @property
    def is_dependent(self):
        return False

    @property
    def division_masks(self):
        return self._output_masks

    @property
    def padding(self):
        return self._padding

    @property
    def seed(self):
        return self._seed

    @property
    def timespan_specifier(self):
        return self._timespan_specifier
