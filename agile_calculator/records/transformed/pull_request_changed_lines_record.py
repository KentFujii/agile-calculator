from datetime import date

from agile_calculator.records.transformed_record import TransformedRecord


class PullRequestChangedLinesRecord(TransformedRecord):
    merged_date: date | None = None
    changed_lines: float | None = None

    def x(self) -> date:
        if self.merged_date is None:
            raise ValueError("merged_date is not set")
        return self.merged_date

    def y(self) -> float:
        if self.changed_lines is None:
            raise ValueError("changed_lines is not set")
        return self.changed_lines
