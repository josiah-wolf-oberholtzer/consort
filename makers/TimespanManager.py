# -*- encoding: utf-8 -*-
from abjad.tools import abctools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import metertools
from abjad.tools import scoretools
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
        if not offset_counter:
            offset_counter[target_duration] += 2
        meters = metertools.Meter.fit_meters_to_expr(
            offset_counter,
            permitted_time_signatures,
            discard_final_orphan_downbeat=False,
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
        for timespan in timespan_inventory:
            voice_name, layer = timespan.voice_name, timespan.layer
            if voice_name not in voicewise_timespans:
                voicewise_timespans[voice_name] = {}
            if layer not in voicewise_timespans[voice_name]:
                voicewise_timespans[voice_name][layer] = \
                    timespantools.TimespanInventory()
            voicewise_timespans[voice_name][layer].append(
                timespan)
            voicewise_timespans[voice_name][layer].sort()
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
        permitted_time_signatures=None,
        segment_session=None,
        target_duration=None,
        score_template=None,
        settings=None,
        ):

        timespan_inventory = TimespanManager._make_timespan_inventory(
            dependent=False,
            score_template=score_template,
            settings=settings,
            target_duration=target_duration,
            )

        meters = TimespanManager._find_meters(
            permitted_time_signatures=permitted_time_signatures,
            target_duration=target_duration,
            timespan_inventory=timespan_inventory,
            )

        segment_session.meters = tuple(meters)

        voicewise_timespans = TimespanManager._make_voicewise_timespans(
            settings_count=len(settings),
            timespan_inventory=timespan_inventory,
            )

        TimespanManager._cleanup_performed_timespans(
            measure_offsets=segment_session.measure_offsets,
            voicewise_timespans=voicewise_timespans,
            )

        timespan_inventory = timespantools.TimespanInventory()
        for voicewise_timespan_inventory in voicewise_timespans.values():
            print(format(voicewise_timespan_inventory))
            timespan_inventory.extend(voicewise_timespan_inventory)

        timespan_inventory = TimespanManager._make_timespan_inventory(
            dependent=True,
            score_template=score_template,
            settings=settings,
            timespan_inventory=timespan_inventory,
            target_duration=target_duration,
            )

        voicewise_timespans = TimespanManager._make_voicewise_timespans(
            settings_count=len(settings),
            timespan_inventory=timespan_inventory,
            )

        TimespanManager._make_silent_timespans(
            measure_offsets=segment_session.measure_offsets,
            score_template=score_template,
            voicewise_timespans=voicewise_timespans,
            )

        segment_session.voicewise_timespans = voicewise_timespans

        return segment_session