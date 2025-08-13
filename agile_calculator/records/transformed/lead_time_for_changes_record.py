from agile_calculator.records.transformed_record import TransformedRecord


class LeadTimeForChangesRecord(TransformedRecord):
    def __init__(
        self,
        number=None,
        title=None,
        merged_date=None,
        lead_time_seconds=None
    ):
        self.number = number
        self.title = title
        self.merged_date = merged_date
        self.lead_time_seconds = lead_time_seconds

    def x(self):
        return lead_time_seconds

    def y(self):
        return merged_date

    def __repr__(self):
        return (
            f"<LeadTimeForChangesRecord #{self.number} {self.title} "
            f"x: lead_time_seconds={self.lead_time_seconds}>, "
            f"y: merged_date={self.merged_date}>"
        )
