# -*- encoding: utf-8 -*-
from __future__ import print_function
import collections
import itertools
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import metertools
from abjad.tools import rhythmmakertools
from abjad.tools import scoretools
from abjad.tools import spannertools
from abjad.tools import timespantools
from abjad.tools.topleveltools import attach
from abjad.tools.topleveltools import inspect_
from abjad.tools.topleveltools import mutate
from abjad.tools.topleveltools import new
from supriya.tools import timetools


class TimeManager(abctools.AbjadValueObject):

    ### PUBLIC METHODS ###

    @staticmethod
    def consolidate_demultiplexed_timespans(demultiplexed_timespans):
        for voice_name in demultiplexed_timespans:
            timespans = demultiplexed_timespans[voice_name]
            consolidated_timespans = TimeManager.consolidate_timespans(
                timespans)
            demultiplexed_timespans[voice_name] = consolidated_timespans

    @staticmethod
    def consolidate_timespans(timespans):
        consolidated_timespans = timespantools.TimespanInventory()
        for music_specifier, grouped_timespans in \
            TimeManager.group_timespans(timespans):
            if music_specifier is None:
                continue
            divisions = tuple(_.duration for _ in grouped_timespans)
            first_timespan = grouped_timespans[0]
            last_timespan = grouped_timespans[-1]
            consolidated_timespan = new(
                first_timespan,
                divisions=divisions,
                stop_offset=last_timespan.stop_offset,
                original_stop_offset=last_timespan.original_stop_offset,
                )
            consolidated_timespans.append(consolidated_timespan)
        consolidated_timespans.sort()
        return consolidated_timespans

    @staticmethod
    def demultiplex_timespans(multiplexed_timespans):
        demultiplexed_timespans = {}
        for timespan in multiplexed_timespans:
            voice_name, layer = timespan.voice_name, timespan.layer
            if voice_name not in demultiplexed_timespans:
                demultiplexed_timespans[voice_name] = {}
            if layer not in demultiplexed_timespans[voice_name]:
                demultiplexed_timespans[voice_name][layer] = \
                    timespantools.TimespanInventory()
            demultiplexed_timespans[voice_name][layer].append(
                timespan)
            demultiplexed_timespans[voice_name][layer]
        for voice_name in demultiplexed_timespans:
            timespan_inventories = demultiplexed_timespans[voice_name]
            timespan_inventory = \
                TimeManager.resolve_timespan_inventories(
                    timespan_inventories)
            demultiplexed_timespans[voice_name] = timespan_inventory
        return demultiplexed_timespans

    @staticmethod
    def execute(
        discard_final_silence=None,
        permitted_time_signatures=None,
        segment_session=None,
        target_duration=None,
        score_template=None,
        settings=None,
        ):

        score = score_template()
        multiplexed_timespans = timespantools.TimespanInventory()

        # populate independent timespans
        TimeManager._populate_multiplexed_timespans(
            dependent=False,
            score=score,
            score_template=score_template,
            settings=settings,
            target_duration=target_duration,
            timespan_inventory=multiplexed_timespans,
            )

        # find meters
        segment_session.meters = TimeManager.find_meters(
            discard_final_silence=discard_final_silence,
            permitted_time_signatures=permitted_time_signatures,
            target_duration=target_duration,
            timespan_inventory=multiplexed_timespans,
            )

        # demultiplex
        demultiplexed_timespans = TimeManager.demultiplex_timespans(
            multiplexed_timespans)

        # split performed timespans by meter offsets
        TimeManager.split_demultiplexed_timespans(
            segment_session.measure_offsets,
            demultiplexed_timespans,
            )

        # consolidate performed timespans by music specifier
        TimeManager.consolidate_demultiplexed_timespans(
            segment_session.measure_offsets,
            demultiplexed_timespans,
            )

        # inscribe grouped performed timespans with rhythms

            # rebuild performed timespans without silence divisions
            # (the inscription process should do the rebuilding)

        # make dependent timespans

        # make (pre-split) silent timespans

        # rewrite meters? (magic)

        # populate score

        # perform other rhythmic processing

        # collect attack points

    @staticmethod
    def find_meters(
        discard_final_silence=None,
        permitted_time_signatures=None,
        target_duration=None,
        timespan_inventory=None,
        ):
        offset_counter = datastructuretools.TypedCounter(
            item_class=durationtools.Offset,
            )
        for timespan in timespan_inventory:
            offset_counter[timespan.start_offset] += 2
            offset_counter[timespan.stop_offset] += 1
        offset_counter[target_duration] += 100
        if discard_final_silence is None:
            discard_final_silence = False
        else:
            discard_final_silence = bool(discard_final_silence)
        meters = metertools.Meter.fit_meters_to_expr(
            offset_counter,
            permitted_time_signatures,
            discard_final_orphan_downbeat=discard_final_silence,
            maximum_repetitions=2,
            )
        return tuple(meters)

    @staticmethod
    def get_rhythm_maker(music_specifier):
        if music_specifier is None:
            rhythm_maker = rhythmmakertools.NoteRhythmMaker(
                output_masks=[
                    rhythmmakertools.BooleanPattern(
                        indices=[0],
                        period=1,
                        )
                    ],
                )
        elif music_specifier.rhythm_maker is None:
            rhythm_maker = rhythmmakertools.NoteRhythmMaker(
                beam_specifier=rhythmmakertools.BeamSpecifier(
                    beam_each_division=False,
                    beam_divisions_together=False,
                    ),
                tie_specifier=rhythmmakertools.TieSpecifier(
                    tie_across_divisions=True,
                    ),
                )
        else:
            rhythm_maker = music_specifier.rhythm_maker
        return rhythm_maker

    @staticmethod
    def group_timespans(timespans):
        def grouper(timespan):
            music_specifier = None
            if isinstance(timespan, consort.PerformedTimespan):
                music_specifier = timespan.music_specifier
                if music_specifier is None:
                    music_specifier = consort.MusicSpecifier()
            return music_specifier
        import consort
        for music_specifier, grouped_timespans in itertools.groupby(
            timespans, grouper):
            grouped_timespans = timespantools.TimespanInventory(
                grouped_timespans)
            yield music_specifier, grouped_timespans

    @staticmethod
    def make_simple_music(rhythm_maker, durations, seed):
        music = rhythm_maker(durations, seeds=seed)
        for i, x in enumerate(music):
            if len(x) == 1 and isinstance(x[0], scoretools.Tuplet):
                music[i] = x[0]
            else:
                music[i] = scoretools.Container(x)
        music = scoretools.Container(music)
        for x in music[:]:
            if isinstance(x, scoretools.Tuplet) and x.multiplier == 1:
                mutate(x).swap(scoretools.Container())
        # TODO: perform rest consolidation here
        return music

    @staticmethod
    def division_is_silent(division):
        r'''Is true when division only contains rests, at any depth.

        ::

            >>> import consort

        ::

            >>> division = Container("c'4 d'4 e'4 f'4")
            >>> consort.TimeManager.division_is_silent(division)
            False

        ::

            >>> division = Container('r4 r8 r16 r32')
            >>> consort.TimeManager.division_is_silent(division)
            True

        ::

            >>> division = Container(r"c'4 \times 2/3 { d'8 r8 e'8 } f'4")
            >>> consort.TimeManager.division_is_silent(division)
            False

        ::

            >>> division = Container(r'\times 2/3 { r4 \times 2/3 { r8. } }')
            >>> consort.TimeManager.division_is_silent(division)
            True

        Returns boolean.
        '''
        rest_prototype = (
            scoretools.Rest,
            scoretools.MultimeasureRest,
            )
        leaves = division.select_leaves()
        return all(isinstance(leaf, rest_prototype) for leaf in leaves)

    @staticmethod
    def group_nonsilent_divisions(music):
        group = []
        for division in reversed(music):
            if TimeManager.division_is_silent(division):
                if group:
                    yield reversed(group)
                    group = []
            else:
                group.append(division)
        if group:
            yield reversed(group)

    @staticmethod
    def populate_timespan(timespan, seed=None):
        populated_timespans = timespantools.TimespanInventory()
        rhythm_maker = TimeManager.get_rhythm_maker(timespan.music_specifier)
        durations = timespan.divisions[:]
        music = TimeManager.make_simple_music(
            rhythm_maker,
            durations,
            seed,
            )
        assert inspect_(music).get_duration() == timespan.duration
        for group in TimeManager.group_nonsilent_divisions(music):
            start_offset = inspect_(group[0]).get_timespan().start_offset
            stop_offset = inspect_(group[-1]).get_timespan().stop_offset
            start_offset += timespan.start_offset
            stop_offset += timespan.stop_offset
            container = scoretools.Container(group)
            beam = spannertools.GeneralizedBeam(
                durations=[division._get_duration() for division in music],
                include_long_duration_notes=True,
                include_long_duration_rests=False,
                isolated_nib_direction=None,
                use_stemlets=False,
                )
            attach(beam, container)
            populated_timespan = new(
                timespan,
                divisions=None,
                music=container,
                start_offset=start_offset,
                stop_offset=stop_offset,
                )
            populated_timespans.append(populated_timespan)
        return populated_timespans

    @staticmethod
    def populate_timespans(
        demultiplexed_timespans,
        score_template,
        ):
        counter = collections.Counter()
        voice_names = demultiplexed_timespans.keys()
        voice_names = TimeManager.sort_voice_names(
            score_template=score_template,
            voice_names=voice_names,
            )
        for voice_name in voice_names:
            populated_timespans = timespantools.TimespanInventory()
            for timespan in demultiplexed_timespans[voice_name]:
                music_specifier = timespan.music_specifier
                if music_specifier not in counter:
                    if music_specifier is None:
                        seed = 0
                    else:
                        seed = music_specifier.seed or 0
                    counter[music_specifier] = seed
                result = TimeManager.populate_timespan(timespan, seed=seed)
                populated_timespans.extend(result)
            demultiplexed_timespans[voice_name] = populated_timespans

    @staticmethod
    def populate_multiplexed_timespans(
        dependent=False,
        score=None,
        score_template=None,
        settings=None,
        target_duration=None,
        timespan_inventory=None,
        ):
        target_timespan = timespantools.Timespan(0, target_duration)
        if timespan_inventory is None:
            timespan_inventory = timespantools.TimespanInventory()
        independent_settings = [setting for setting in settings
            if not setting.timespan_maker.is_dependent
            ]
        dependent_settings = [setting for setting in settings
            if setting.timespan_maker.is_dependent
            ]
        if dependent:
            settings = dependent_settings
            start_index = len(independent_settings)
        else:
            settings = independent_settings
            start_index = 0
        for layer, music_setting in enumerate(settings, start_index):
            music_setting(
                layer=layer,
                score=score,
                score_template=score_template,
                target_timespan=target_timespan,
                timespan_inventory=timespan_inventory,
                )

    @staticmethod
    def resolve_timespan_inventories(
        timespan_inventories=None,
        ):
        import consort
        timespan_inventories = [x[1] for x in
            sorted(timespan_inventories.items(),
                key=lambda item: item[0],
                )
            ]
        resolved_inventory = timetools.TimespanCollection()
        for timespan in timespan_inventories[0]:
            if isinstance(timespan, consort.SilentTimespan):
                continue
            resolved_inventory.insert(timespan)
        for timespan_inventory in timespan_inventories[1:]:
            resolved_inventory = TimeManager.subtract_timespan_inventories(
                resolved_inventory,
                timespan_inventory,
                )
            for timespan in timespan_inventory:
                if isinstance(timespan, consort.SilentTimespan):
                    continue
                resolved_inventory.append(timespan)
            resolved_inventory.sort()
        resolved_inventory = timespantools.TimespanInventory(
            resolved_inventory[:],
            )
        return resolved_inventory

    @staticmethod
    def split_demultiplexed_timespans(
        measure_offsets=None,
        demultiplexed_timespans=None,
        ):
        for voice_name in demultiplexed_timespans:
            timespan_inventory = demultiplexed_timespans[voice_name]
            split_inventory = TimeManager.split_timespans(
                measure_offsets,
                timespan_inventory,
                )
            demultiplexed_timespans[voice_name] = split_inventory

    @staticmethod
    def split_timespans(offsets, timespan_inventory):
        offsets = list(offsets)
        timespan_inventory.sort()
        split_inventory = timespantools.TimespanInventory()
        for timespan in timespan_inventory:
            current_offsets = []
            while offsets and offsets[0] <= timespan.start_offset:
                offsets.pop(0)
            while offsets and offsets[0] < timespan.stop_offset:
                current_offsets.append(offsets.pop(0))
            if current_offsets and timespan.can_split:
                shards = timespan.split_at_offsets(current_offsets)
                for shard in shards:
                    if shard.minimum_duration:
                        if shard.minimum_duration <= shard.duration:
                            split_inventory.append(shard)
                    else:
                        split_inventory.append(shard)
            else:
                if timespan.minimum_duration:
                    if timespan.minimum_duration <= timespan.duration:
                        split_inventory.append(timespan)
                else:
                    split_inventory.append(timespan)
        split_inventory.sort()
        return split_inventory

    @staticmethod
    def subtract_timespan_inventories(inventory_one, inventory_two):
        r'''Subtracts `inventory_two` from `inventory_one`.

        ::

            >>> inventory_one = timespantools.TimespanInventory([
            ...     timespantools.Timespan(0, 10),
            ...     timespantools.Timespan(10, 20),
            ...     timespantools.Timespan(40, 80),
            ...     ])

        ::

            >>> inventory_two = timespantools.TimespanInventory([
            ...     timespantools.Timespan(5, 15),
            ...     timespantools.Timespan(25, 35),
            ...     timespantools.Timespan(35, 45),
            ...     timespantools.Timespan(55, 65),
            ...     timespantools.Timespan(85, 95),
            ...     ])

        ::

            >>> import consort
            >>> manager = consort.TimeManager
            >>> result = manager.subtract_timespan_inventories(
            ...      inventory_one,
            ...      inventory_two,
            ...      )
            >>> print(format(result))
            timespantools.TimespanInventory(
                [
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(0, 1),
                        stop_offset=durationtools.Offset(5, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(15, 1),
                        stop_offset=durationtools.Offset(20, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(45, 1),
                        stop_offset=durationtools.Offset(55, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(65, 1),
                        stop_offset=durationtools.Offset(80, 1),
                        ),
                    ]
                )

        ::

            >>> result = manager.subtract_timespan_inventories(
            ...      inventory_two,
            ...      inventory_one,
            ...      )
            >>> print(format(result))
            timespantools.TimespanInventory(
                [
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(25, 1),
                        stop_offset=durationtools.Offset(35, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(35, 1),
                        stop_offset=durationtools.Offset(40, 1),
                        ),
                    timespantools.Timespan(
                        start_offset=durationtools.Offset(85, 1),
                        stop_offset=durationtools.Offset(95, 1),
                        ),
                    ]
                )

        '''
        resulting_timespans = timetools.TimespanCollection()
        if not inventory_one or not inventory_two:
            return resulting_timespans
        subtractee_index = 0
        subtractor_index = 0
        subtractee = None
        subtractor = None
        subtractee_is_modified = False
        while subtractee_index < len(inventory_one) and \
            subtractor_index < len(inventory_two):
            if subtractee is None:
                subtractee = inventory_one[subtractee_index]
                subtractee_is_modified = False
            if subtractor is None:
                subtractor = inventory_two[subtractor_index]
            if subtractee.intersects_timespan(subtractor):
                subtraction = subtractee - subtractor
                if len(subtraction) == 1:
                    subtractee = subtraction[0]
                    subtractee_is_modified = True
                elif len(subtraction) == 2:
                    resulting_timespans.insert(subtraction[0])
                    subtractee = subtraction[1]
                    subtractee_is_modified = True
                else:
                    subtractee = None
                    subtractee_index += 1
            else:
                if subtractee.stops_before_or_at_offset(
                    subtractor.start_offset):
                    resulting_timespans.insert(subtractee)
                    subtractee = None
                    subtractee_index += 1
                else:
                    subtractor = None
                    subtractor_index += 1
        if subtractee_is_modified:
            if subtractee:
                resulting_timespans.insert(subtractee)
            resulting_timespans.insert(inventory_one[subtractee_index + 1:])
        else:
            resulting_timespans.insert(inventory_one[subtractee_index:])
        resulting_timespans = timespantools.TimespanInventory(
            resulting_timespans)
        return resulting_timespans