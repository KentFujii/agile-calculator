from datetime import date, datetime

from agile_calculator.records.pull_request_base import PullRequestBase


class PullRequestRecord(PullRequestBase):
    def merged_date(self) -> date | None:
        return self.merged_at.date() if self.merged_at else None

    def lead_time_for_changes(self) -> float | None:
        """Get lead time for changes in hours.

        This is the time from when a pull request is created to when it is merged.
        """
        if self.merged_at is None or self.created_at is None:
            return None

        total_seconds = (self.merged_at - self.created_at).total_seconds()

        return total_seconds / 3600
