# -*- encoding: utf-8 -*-
from __future__ import print_function
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import metertools
from abjad.tools import scoretools
from abjad.tools import sequencetools
from abjad.tools import systemtools
from abjad.tools import timespantools
from abjad.tools.topleveltools import iterate
from supriya.tools import timetools


class TimespanManager(abctools.AbjadValueObject):
    r'''A timespan manager.
    '''

    ### PRIVATE METHODS ###

    @staticmethod
    def _cleanup_performed_timespans(
        measure_offsets=None,
        voicewise_timespans=None,
        ):
        for voice_name in voicewise_timespans:
            offsets = list(measure_offsets)
            timespan_inventory = voicewise_timespans[voice_name]
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
            voicewise_timespans[voice_name] = split_inventory

    @staticmethod
    def _find_meters(
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
        return meters

    @staticmethod
    def _make_silent_timespans(
        measure_offsets=None,
        score=None,
        voicewise_timespans=None,
        ):
        import consort
        for voice in iterate(score).by_class(scoretools.Voice):
            voice_name = voice.name
            if voice_name not in voicewise_timespans:
                voicewise_timespans[voice_name] = \
                    timespantools.TimespanInventory()
            timespan_inventory = voicewise_timespans[voice_name]
            silence_inventory = timespantools.TimespanInventory()
            shards = tuple(timespan_inventory.partition(
                include_tangent_timespans=True,
                ))
            if shards:
                if shards[0].start_offset != 0:
                    silence = consort.SilentTimespan(
                        start_offset=0,
                        stop_offset=shards[0].start_offset,
                        )
                    silence_inventory.append(silence)
                for one, two in sequencetools.iterate_sequence_nwise(shards):
                    silence = consort.SilentTimespan(
                        start_offset=one.stop_offset,
                        stop_offset=two.start_offset,
                        )
                    silence_inventory.append(silence)
                if shards[-1].stop_offset != measure_offsets[-1]:
                    silence = consort.SilentTimespan(
                        start_offset=shards[-1].stop_offset,
                        stop_offset=measure_offsets[-1],
                        )
                    silence_inventory.append(silence)
            else:
                silence = consort.SilentTimespan(
                    start_offset=0,
                    stop_offset=measure_offsets[-1],
                    )
                silence_inventory.append(silence)
            for shard in silence_inventory.split_at_offsets(measure_offsets):
                timespan_inventory.extend(shard)
            timespan_inventory.sort()

    @staticmethod
    def _make_timespan_inventory(
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
        return timespan_inventory

    @staticmethod
    def _make_voicewise_timespans(
        settings_count=None,
        timespan_inventory=None,
        ):
        voicewise_timespans = {}
        for timespan in timespan_inventory:
            voice_name, layer = timespan.voice_name, timespan.layer
            if voice_name not in voicewise_timespans:
                voicewise_timespans[voice_name] = {}
            if layer not in voicewise_timespans[voice_name]:
                voicewise_timespans[voice_name][layer] = \
                    timespantools.TimespanInventory()
            voicewise_timespans[voice_name][layer].append(
                timespan)
            voicewise_timespans[voice_name][layer]
        for voice_name in voicewise_timespans:
            timespan_inventories = voicewise_timespans[voice_name]
            timespan_inventory = \
                TimespanManager._resolve_timespan_inventories(
                    timespan_inventories)
            voicewise_timespans[voice_name] = timespan_inventory
        return voicewise_timespans

    @staticmethod
    def _resolve_timespan_inventories(
        timespan_inventories=None,
        ):
        import consort
        manager = consort.TimespanManager
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
            resolved_inventory = manager._subtract_timespan_inventories(
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
    def _subtract_timespan_inventories(inventory_one, inventory_two):
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
            >>> manager = consort.TimespanManager
            >>> result = manager._subtract_timespan_inventories(
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

            >>> result = manager._subtract_timespan_inventories(
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

    ### PUBLIC METHODS ###

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

        with systemtools.Timer() as timer:
            timespan_inventory = TimespanManager._make_timespan_inventory(
                dependent=False,
                score=score,
                score_template=score_template,
                settings=settings,
                target_duration=target_duration,
                )
        print('\tmade independent timespans:', timer.elapsed_time)

        with systemtools.Timer() as timer:
            meters = TimespanManager._find_meters(
                discard_final_silence=discard_final_silence,
                permitted_time_signatures=permitted_time_signatures,
                target_duration=target_duration,
                timespan_inventory=timespan_inventory,
                )
        print('\tfound meters:', timer.elapsed_time)

        segment_session.meters = tuple(meters)

        with systemtools.Timer() as timer:
            voicewise_timespans = TimespanManager._make_voicewise_timespans(
                settings_count=len(settings),
                timespan_inventory=timespan_inventory,
                )
        print('\tmade voicewise timespans (1/2):', timer.elapsed_time)

        for voice_name, voicewise_timespan_inventory in \
            voicewise_timespans.items():
            if not voicewise_timespan_inventory.all_are_nonoverlapping:
                print(voice_name)
                for timespan in voicewise_timespan_inventory:
                    print(
                        '\t',
                        timespan.layer,
                        ':',
                        timespan.start_offset,
                        timespan.stop_offset,
                        type(timespan)
                        )

        with systemtools.Timer() as timer:
            TimespanManager._cleanup_performed_timespans(
                measure_offsets=segment_session.measure_offsets,
                voicewise_timespans=voicewise_timespans,
                )
        print('\tcleaned-up performed timespans:', timer.elapsed_time)

        timespan_inventory = timespantools.TimespanInventory()
        for voicewise_timespan_inventory in voicewise_timespans.values():
            timespan_inventory.extend(voicewise_timespan_inventory)

        for voicewise_timespan_inventory in voicewise_timespans.values():
            assert voicewise_timespan_inventory.all_are_nonoverlapping

        with systemtools.Timer() as timer:
            timespan_inventory = TimespanManager._make_timespan_inventory(
                dependent=True,
                score=score,
                score_template=score_template,
                settings=settings,
                timespan_inventory=timespan_inventory,
                target_duration=target_duration,
                )
        print('\tmade dependent timespans:', timer.elapsed_time)

        for voicewise_timespan_inventory in voicewise_timespans.values():
            assert voicewise_timespan_inventory.all_are_nonoverlapping

        with systemtools.Timer() as timer:
            voicewise_timespans = TimespanManager._make_voicewise_timespans(
                settings_count=len(settings),
                timespan_inventory=timespan_inventory,
                )
        print('\tmade voicewise timespans (2/2):', timer.elapsed_time)

        for voicewise_timespan_inventory in voicewise_timespans.values():
            assert voicewise_timespan_inventory.all_are_nonoverlapping

        with systemtools.Timer() as timer:
            TimespanManager._make_silent_timespans(
                measure_offsets=segment_session.measure_offsets,
                score=score,
                voicewise_timespans=voicewise_timespans,
                )
        print('\tmade silent timespans:', timer.elapsed_time)

        durations = set()
        for voicewise_timespan_inventory in voicewise_timespans.values():
            duration = voicewise_timespan_inventory.duration
            durations.add(duration)
            assert voicewise_timespan_inventory.all_are_nonoverlapping
        assert len(durations) == 1
        segment_session.voicewise_timespans = voicewise_timespans

        return segment_session