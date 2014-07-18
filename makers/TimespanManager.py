# -*- encoding: utf-8 -*-
from consort.makers.ConsortObject import ConsortObject
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import metertools
from abjad.tools import scoretools
from abjad.tools import timespantools
from abjad.tools.topleveltools import iterate


class TimespanManager(ConsortObject):
    r'''A timespan manager.
    '''

    ### PRIVATE METHODS ###

    @staticmethod
    def _cleanup_performed_timespans(
        segment_session=None,
        ):
        measure_offsets = segment_session.measure_offsets
        voicewise_timespan_inventories = segment_session.voicewise_timespan_inventories
        for voice_name in voicewise_timespan_inventories:
            offsets = list(measure_offsets)
            timespan_inventory = voicewise_timespan_inventories[voice_name]
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
            voicewise_timespan_inventories[voice_name] = split_inventory

    @staticmethod
    def _find_meters(
        permitted_time_signatures=None,
        target_duration=None,
        voicewise_timespan_inventories=None,
        ):
        offset_counter = datastructuretools.TypedCounter(
            item_class=durationtools.Offset,
            )
        for timespan_inventory in \
            voicewise_timespan_inventories.values():
            for timespan in timespan_inventory:
                offset_counter[timespan.start_offset] += 1
                offset_counter[timespan.stop_offset] += 1
        if not offset_counter:
            offset_counter[target_duration] += 1
        meters = metertools.Meter.fit_meters_to_expr(
            offset_counter,
            permitted_time_signatures,
            maximum_repetitions=None,
            )
        return meters

    @staticmethod
    def _make_silent_timespans(
        segment_session=None,
        score_template=None,
        ):
        from consort import makers
        measure_offsets = segment_session.measure_offsets
        voicewise_timespan_inventories = segment_session.voicewise_timespan_inventories
        score = score_template()
        for voice in iterate(score).by_class(scoretools.Voice):
            voice_name = voice.name
            if voice_name not in voicewise_timespan_inventories:
                voicewise_timespan_inventories[voice_name] = \
                    timespantools.TimespanInventory()
            timespan_inventory = voicewise_timespan_inventories[voice_name]
            silence_inventory = timespantools.TimespanInventory()
            silence = makers.SilentTimespan(
                start_offset=0,
                stop_offset=measure_offsets[-1],
                )
            silence_inventory.append(silence)
            for timespan in timespan_inventory:
                silence_inventory - timespan
            for shard in silence_inventory.split_at_offsets(measure_offsets):
                timespan_inventory.extend(shard)
                timespan_inventory.sort()

    @staticmethod
    def _make_timespan_inventory(
        score_template=None,
        settings=None,
        target_duration=None,
        ):
        timespan_inventory = timespantools.TimespanInventory()
        for layer, setting in enumerate(settings):
            setting(
                layer=layer,
                score_template=score_template,
                target_duration=target_duration,
                timespan_inventory=timespan_inventory,
                )
        return timespan_inventory

    @staticmethod
    def _make_voicewise_timespan_inventories(
        settings_count=None,
        timespan_inventory=None,
        ):
        voicewise_timespan_inventories = {}
        for timespan in timespan_inventory:
            voice_name, layer = timespan.voice_name, timespan.layer
            if voice_name not in voicewise_timespan_inventories:
                voicewise_timespan_inventories[voice_name] = []
                for _ in range(settings_count):
                    voicewise_timespan_inventories[voice_name].append(
                        timespantools.TimespanInventory())
            voicewise_timespan_inventories[voice_name][layer].append(
                timespan)
            voicewise_timespan_inventories[voice_name][layer].sort()
        for voice_name in voicewise_timespan_inventories:
            timespan_inventories = voicewise_timespan_inventories[voice_name]
            timespan_inventory = \
                TimespanManager._resolve_timespan_inventories(
                    timespan_inventories)
            voicewise_timespan_inventories[voice_name] = timespan_inventory
        return voicewise_timespan_inventories

    @staticmethod
    def _resolve_timespan_inventories(
        timespan_inventories=None,
        ):
        resolved_timespan_inventory = timespantools.TimespanInventory()
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
        permitted_time_signatures=None,
        segment_session=None,
        target_duration=None,
        score_template=None,
        settings=None,
        ):
        timespan_inventory = TimespanManager._make_timespan_inventory(
            score_template=score_template,
            settings=settings,
            target_duration=target_duration,
            )
        segment_session.segment_duration = timespan_inventory.stop_offset

        voicewise_timespan_inventories = \
            TimespanManager._make_voicewise_timespan_inventories(
                settings_count=len(settings),
                timespan_inventory=timespan_inventory,
                )
        segment_session.voicewise_timespan_inventories = \
            voicewise_timespan_inventories

        meters = TimespanManager._find_meters(
            permitted_time_signatures=permitted_time_signatures,
            target_duration=target_duration,
            voicewise_timespan_inventories=voicewise_timespan_inventories,
            )
        segment_session.meters = tuple(meters)
        segment_session.segment_duration = sum(
            x.duration for x in segment_session.time_signatures)

        TimespanManager._cleanup_performed_timespans(
            segment_session=segment_session,
            )

        TimespanManager._make_silent_timespans(
            segment_session=segment_session,
            score_template=score_template,
            )
            
        return segment_session
