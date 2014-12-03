from abjad.tools import abctools


class TimeManager(abctools.AbjadValueObject):

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

        # make independent timespans
        timespan_inventory = TimespanManager._make_multiplexed_timespans(
            dependent=False,
            score=score,
            score_template=score_template,
            settings=settings,
            target_duration=target_duration,
            )

        # find meters

        # split performed timespans by meter offsets

        # group performed timespans by music specifier

        # inscribe grouped performed timespans with rhythms

            # rebuild performed timespans without silence divisions
            # (the inscription process should do the rebuilding)

        # make dependent timespans

        # make (pre-split) silent timespans

        # rewrite meters? (magic)

        # populate score

        # perform other rhythmic processing

        # collect attack points