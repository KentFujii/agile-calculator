from datetime import date, datetime

from agile_calculator.records.extracted_record import ExtractedRecord


class PullRequestRecord(ExtractedRecord):
    def __init__(
        self,
        number: int | None = None,
        title: str | None = None,
        draft: bool | None = None,
        user: str | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        merged_at: datetime | None = None,
        closed_at: datetime | None = None,
        state: str | None = None,
        base_ref: str | None = None,
        head_ref: str | None = None,
        merged: bool | None = None,
        merge_commit_sha: str | None = None,
        comments: int | None = None,
        review_comments: int | None = None,
        commits: int | None = None,
        additions: int | None = None,
        deletions: int | None = None,
        changed_files: int | None = None,
    ) -> None:
        self.number = number
        self.title = title
        self.draft = draft
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at
        self.merged_at = merged_at
        self.closed_at = closed_at
        self.state = state
        self.base_ref = base_ref
        self.head_ref = head_ref
        self.merged = merged
        self.merge_commit_sha = merge_commit_sha
        self.comments = comments
        self.review_comments = review_comments
        self.commits = commits
        self.additions = additions
        self.deletions = deletions
        self.changed_files = changed_files

    def merged_date(self) -> date | None:
        return self.merged_at.date() if self.merged_at else None

    def lead_time_for_changes(self) -> float:
        # TODO: テストを書く
        # TODO: 土日を考慮する
        if self.merged_at is None or self.created_at is None:
            return 0.0
        return (self.merged_at - self.created_at).total_seconds() / 3600

    def __repr__(self) -> str:
        return f"<PullRequestRecord #{self.number} {self.title}>"
