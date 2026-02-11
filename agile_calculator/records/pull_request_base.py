from datetime import datetime

from agile_calculator.records.extracted_record import ExtractedRecord


class PullRequestBase(ExtractedRecord):
    number: int | None = None
    title: str | None = None
    body: str | None = None
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
