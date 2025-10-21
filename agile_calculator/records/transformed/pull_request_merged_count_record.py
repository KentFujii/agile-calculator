from datetime import date

from agile_calculator.records.transformed_record import TransformedRecord


class PullRequestMergedCountRecord(TransformedRecord):
    merged_date: date | None = None
    merged_count: int | None = None

    def x(self) -> date:
        if self.merged_date is None:
            raise ValueError("merged_date is not set")
        return self.merged_date

    def y(self) -> int:
        if self.merged_count is None:
            raise ValueError("merged_count is not set")
        return self.merged_count
