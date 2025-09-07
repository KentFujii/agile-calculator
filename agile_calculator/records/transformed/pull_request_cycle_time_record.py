from datetime import date

from agile_calculator.records.transformed_record import TransformedRecord


class PullRequestCycleTimeRecord(TransformedRecord):
    merged_date: date | None = None
    lead_time_hours: float | None = None

    def x(self) -> date:
        if self.merged_date is None:
            raise ValueError("merged_date is not set")
        return self.merged_date

    def y(self) -> float:
        if self.lead_time_hours is None:
            raise ValueError("lead_time_hours is not set")
        return self.lead_time_hours
