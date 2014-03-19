# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import metertools
from abjad.tools import scoretools
from abjad.tools import timespantools
from abjad.tools.topleveltools import iterate


class TimespanManager(abctools.AbjadObject):
    r'''A timespan manager.
    '''

    ### PRIVATE METHODS ###

    @staticmethod
    def _apply_voice_settings(
        segment_product=None,
        voice_settings=None,
        ):
        if voice_settings is not None:
            for context_setting in voice_settings:
                context_setting(segment_product)

    @staticmethod
    def _cleanup_performed_timespans(
        segment_product=None,
        ):
        measure_offsets = segment_product.measure_offsets
        timespan_inventory_mapping = segment_product.timespan_inventory_mapping
        for voice_name in timespan_inventory_mapping:
            offsets = list(measure_offsets)
            timespan_inventory = timespan_inventory_mapping[voice_name]
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
            split_inventory.sort()
            timespan_inventory_mapping[voice_name] = split_inventory

    @staticmethod
    def _find_meters(
        permitted_time_signatures=None,
        segment_product=None,
        target_duration=None,
        ):
        offset_counter = datastructuretools.TypedCounter(
            item_class=durationtools.Offset,
            )
        for timespan_inventory in \
            segment_product.timespan_inventory_mapping.values():
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
        segment_product.meters = tuple(meters)
        segment_product.segment_duration = sum(
            x.duration for x in segment_product.time_signatures)

    @staticmethod
    def _make_silent_timespans(
        segment_product=None,
        template=None,
        ):
        from consort import makers
        measure_offsets = segment_product.measure_offsets
        timespan_inventory_mapping = segment_product.timespan_inventory_mapping
        score = template()
        for voice in iterate(score).by_class(scoretools.Voice):
            voice_name = voice.name
            if voice_name not in timespan_inventory_mapping:
                timespan_inventory_mapping[voice_name] = \
                    timespantools.TimespanInventory()
            timespan_inventory = timespan_inventory_mapping[voice_name]
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
    def _make_timespan_inventory_mapping(
        segment_product=None,
        target_duration=None,
        template=None,
        voice_specifiers=None,
        ):
        timespan_inventory_mapping = {}
        segment_duration = durationtools.Duration(0)
        for layer, voice_specifier in enumerate(voice_specifiers):
            timespan_inventory, final_duration = voice_specifier(
                layer=layer,
                target_duration=target_duration,
                template=template,
                )
            if segment_duration < final_duration:
                segment_duration = final_duration
            for timespan in timespan_inventory:
                voice_name, layer = timespan.voice_name, timespan.layer
                if voice_name not in timespan_inventory_mapping:
                    timespan_inventory_mapping[voice_name] = []
                    for _ in range(len(voice_specifiers)):
                        timespan_inventory_mapping[voice_name].append(
                            timespantools.TimespanInventory())
                timespan_inventory_mapping[voice_name][layer].append(
                    timespan)
                timespan_inventory_mapping[voice_name][layer].sort()
        for voice_name in timespan_inventory_mapping:
            timespan_inventories = timespan_inventory_mapping[voice_name]
            timespan_inventory = \
                TimespanManager._resolve_timespan_inventories(
                    timespan_inventories)
            timespan_inventory_mapping[voice_name] = timespan_inventory
        segment_product.segment_duration = segment_duration
        segment_product.timespan_inventory_mapping = timespan_inventory_mapping

    @staticmethod
    def _resolve_timespan_inventories(
        timespan_inventories=None,
        ):
        resolved_timespan_inventory = timespantools.TimespanInventory()
        resolved_timespan_inventory.extend(timespan_inventories[0])
        for timespan_inventory in timespan_inventories[1:]:
            for timespan in timespan_inventory:
                resolved_timespan_inventory -= timespan
        return resolved_timespan_inventory

    ### PUBLIC METHODS ###

    @staticmethod
    def execute(
        permitted_time_signatures=None,
        segment_product=None,
        target_duration=None,
        template=None,
        voice_settings=None,
        voice_specifiers=None,
        ):
        TimespanManager._make_timespan_inventory_mapping(
            segment_product=segment_product,
            target_duration=target_duration,
            template=template,
            voice_specifiers=voice_specifiers,
            )
        TimespanManager._find_meters(
            permitted_time_signatures=permitted_time_signatures,
            segment_product=segment_product,
            target_duration=target_duration,
            )
        TimespanManager._cleanup_performed_timespans(
            segment_product=segment_product,
            )
        TimespanManager._make_silent_timespans(
            segment_product=segment_product,
            template=template,
            )
        #TimespanManager._create_dependent_timespans(segment_product)
        #TimespanManager._remove_empty_trailing_measures(segment_product)
        TimespanManager._apply_voice_settings(
            segment_product=segment_product,
            voice_settings=voice_settings,
            )
        return segment_product
