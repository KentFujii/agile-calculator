from datetime import date
from typing import Any

from agile_calculator.records.transformed_record import TransformedRecord


class PullRequestCycleTimeRecord(TransformedRecord):
    def __init__(
        self,
        number: int | None = None,
        title: str | None = None,
        merged_date: date | None = None,
        lead_time_hours: float | None = None,
        **kwargs: Any,
    ) -> None:
        self.merged_date = merged_date
        self.lead_time_hours = lead_time_hours

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
