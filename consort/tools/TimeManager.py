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
        pass