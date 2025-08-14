from agile_calculator.records.transformed_record import TransformedRecord


class LeadTimeForChangesRecord(TransformedRecord):
    def __init__(
        self,
        number=None,
        title=None,
        merged_date=None,
        lead_time_seconds=None
    ):
        self.merged_date = merged_date
        self.lead_time_seconds = lead_time_seconds

    def x(self):
        return merged_date

    def y(self):
        return lead_time_seconds

    def __repr__(self):
        return (
            f"<LeadTimeForChangesRecord "
            f"x: merged_date={self.merged_date}>, "
            f"y: lead_time_seconds={self.lead_time_seconds}>"
        )
