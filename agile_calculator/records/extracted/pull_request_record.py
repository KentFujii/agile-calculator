from dataclasses import dataclass
from datetime import date, datetime

from agile_calculator.records.extracted_record import ExtractedRecord


@dataclass
class PullRequestRecord(ExtractedRecord):
    number: int | None = None
    title: str | None = None
    draft: bool | None = None
    user: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    merged_at: datetime | None = None
    closed_at: datetime | None = None
    state: str | None = None
    base_ref: str | None = None
    head_ref: str | None = None
    merged: bool | None = None
    merge_commit_sha: str | None = None
    comments: int | None = None
    review_comments: int | None = None
    commits: int | None = None
    additions: int | None = None
    deletions: int | None = None
    changed_files: int | None = None

    def merged_date(self) -> date | None:
        return self.merged_at.date() if self.merged_at else None

    HOURS_PER_WEEKEND_DAY = 24

    def _get_weekend_days(self, start_dt: datetime, end_dt: datetime) -> int:
        start_date = start_dt.date()
        end_date = end_dt.date()

        if start_date > end_date:
            return 0

        total_days = (end_date - start_date).days + 1
        start_weekday = start_date.weekday()

        num_full_weeks = total_days // 7
        weekend_days = num_full_weeks * 2

        remaining_days = total_days % 7
        current_weekday = start_weekday
        for _ in range(remaining_days):
            if current_weekday >= 5:  # Saturday or Sunday
                weekend_days += 1
            current_weekday = (current_weekday + 1) % 7

        return weekend_days

    def lead_time_for_changes(self) -> float:
        if self.merged_at is None or self.created_at is None:
            return 0.0

        total_seconds = (self.merged_at - self.created_at).total_seconds()

        weekend_days = self._get_weekend_days(self.created_at, self.merged_at)
        weekend_seconds = weekend_days * self.HOURS_PER_WEEKEND_DAY * 3600

        lead_time_seconds = total_seconds - weekend_seconds

        return max(0, lead_time_seconds) / 3600

    def __repr__(self) -> str:
        return f"<PullRequestRecord #{self.number} {self.title}>"
