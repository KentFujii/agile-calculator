from dataclasses import dataclass
from datetime import date

from agile_calculator.records.transformed_record import TransformedRecord


@dataclass
class PullRequestCycleTimeRecord(TransformedRecord):
    lead_time_hours: float | None = None

    def x(self) -> date:
        if self.merged_date is None:
            raise ValueError("merged_date is not set")
        return self.merged_date

    def y(self) -> float:
        if self.lead_time_hours is None:
            raise ValueError("lead_time_hours is not set")
        return self.lead_time_hours

    def __repr__(self) -> str:
        return (
            f"<PullRequestCycleTimeRecord "
            f"x: merged_date={self.merged_date}>, "
            f"y: lead_time_hours={self.lead_time_hours}>"
        )
