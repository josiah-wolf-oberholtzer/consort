import abjad


class TimespanListMapping(dict):

    ### SPECIAL METHODS ###

    def __illustrate__(self, range_=None, scale=None):
        timespan_inventory = abjad.TimespanList()
        for key, value in self.items():
            timespan_inventory.extend(value)
        return timespan_inventory.__illustrate__(
            key='voice_name',
            range_=range_,
            scale=scale,
            )
