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
        score_template=None,
        voicewise_timespans=None,
        ):
        from consort import makers
        score = score_template()
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
                    silence = makers.SilentTimespan(
                        start_offset=0,
                        stop_offset=shards[0].start_offset,
                        )
                    silence_inventory.append(silence)
                for one, two in sequencetools.iterate_sequence_nwise(shards):
                    silence = makers.SilentTimespan(
                        start_offset=one.stop_offset,
                        stop_offset=two.start_offset,
                        )
                    silence_inventory.append(silence)
                if shards[-1].stop_offset != measure_offsets[-1]:
                    silence = makers.SilentTimespan(
                        start_offset=shards[-1].stop_offset,
                        stop_offset=measure_offsets[-1],
                        )
                    silence_inventory.append(silence)
            else:
                silence = makers.SilentTimespan(
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
        for layer, setting in enumerate(settings, start_index):
            setting(
                layer=layer,
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
        with systemtools.Timer() as timer:
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
        print('\t\tCollecting:', timer.elapsed_time)
        with systemtools.Timer() as timer:
            for voice_name in voicewise_timespans:
                timespan_inventories = voicewise_timespans[voice_name]
                for timespan_inventory in timespan_inventories.values():
                    timespan_inventory.sort()
                timespan_inventory = \
                    TimespanManager._resolve_timespan_inventories(
                        timespan_inventories)
                voicewise_timespans[voice_name] = timespan_inventory
        print('\t\tResolving:', timer.elapsed_time)
        return voicewise_timespans

    @staticmethod
    def _resolve_timespan_inventories(
        timespan_inventories=None,
        ):
        resolved_timespan_inventory = timespantools.TimespanInventory()
        timespan_inventories = [x[1] for x in
            sorted(timespan_inventories.items(),
                key=lambda item: item[0],
                )
            ]
        resolved_timespan_inventory.extend(timespan_inventories[0])
        for timespan_inventory in timespan_inventories[1:]:
            for timespan in timespan_inventory:
                resolved_timespan_inventory -= timespan
            resolved_timespan_inventory.extend(timespan_inventory)
        resolved_timespan_inventory.sort()
        return resolved_timespan_inventory

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

        with systemtools.Timer() as timer:
            timespan_inventory = TimespanManager._make_timespan_inventory(
                dependent=False,
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

        with systemtools.Timer() as timer:
            TimespanManager._cleanup_performed_timespans(
                measure_offsets=segment_session.measure_offsets,
                voicewise_timespans=voicewise_timespans,
                )
        print('\tcleaned-up performed timespans:', timer.elapsed_time)

        timespan_inventory = timespantools.TimespanInventory()
        for voicewise_timespan_inventory in voicewise_timespans.values():
            timespan_inventory.extend(voicewise_timespan_inventory)

        with systemtools.Timer() as timer:
            timespan_inventory = TimespanManager._make_timespan_inventory(
                dependent=True,
                score_template=score_template,
                settings=settings,
                timespan_inventory=timespan_inventory,
                target_duration=target_duration,
                )
        print('\tmade dependent timespans:', timer.elapsed_time)

        with systemtools.Timer() as timer:
            voicewise_timespans = TimespanManager._make_voicewise_timespans(
                settings_count=len(settings),
                timespan_inventory=timespan_inventory,
                )
        print('\tmade voicewise timespans (2/2):', timer.elapsed_time)

        with systemtools.Timer() as timer:
            TimespanManager._make_silent_timespans(
                measure_offsets=segment_session.measure_offsets,
                score_template=score_template,
                voicewise_timespans=voicewise_timespans,
                )
        print('\tmade silent timespans:', timer.elapsed_time)

        segment_session.voicewise_timespans = voicewise_timespans

        return segment_session