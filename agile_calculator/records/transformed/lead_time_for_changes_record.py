from datetime import date
from typing import Any

from agile_calculator.records.transformed_record import TransformedRecord


class LeadTimeForChangesRecord(TransformedRecord):
    def __init__(
        self,
        number: int | None = None,
        title: str | None = None,
        merged_date: date | None = None,
        lead_time_seconds: float | None = None,
        **kwargs: Any,
    ) -> None:
        self.merged_date = merged_date
        self.lead_time_seconds = lead_time_seconds

    def x(self) -> date:
        if self.merged_date is None:
            raise ValueError("merged_date is not set")
        return self.merged_date

    def y(self) -> float:
        if self.lead_time_seconds is None:
            raise ValueError("lead_time_seconds is not set")
        return self.lead_time_seconds

    def __repr__(self) -> str:
        return (
            f"<LeadTimeForChangesRecord "
            f"x: merged_date={self.merged_date}>, "
            f"y: lead_time_seconds={self.lead_time_seconds}>"
        )
