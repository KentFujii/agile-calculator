from __future__ import annotations

from datetime import datetime
from typing import Any, Sequence

from agile_calculator.records.base_record import BaseRecord


class PullRequestDetailRecord(BaseRecord):
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
    ):
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

    def fields(self) -> Sequence[str]:
        """
        レコードのフィールド名を返す
        """
        return [
            "number",
            "title",
            "draft",
            "user",
            "created_at",
            "updated_at",
            "merged_at",
            "closed_at",
            "state",
            "base_ref",
            "head_ref",
            "merged",
            "merge_commit_sha",
            "comments",
            "review_comments",
            "commits",
            "additions",
            "deletions",
            "changed_files",
        ]

    def values(self) -> Sequence[Any]:
        """
        レコードのフィールド値を返す
        """
        return [
            self.number,
            self.title,
            self.draft,
            self.user,
            self.created_at,
            self.updated_at,
            self.merged_at,
            self.closed_at,
            self.state,
            self.base_ref,
            self.head_ref,
            self.merged,
            self.merge_commit_sha,
            self.comments,
            self.review_comments,
            self.commits,
            self.additions,
            self.deletions,
            self.changed_files,
        ]

    def __repr__(self) -> str:
        return f"<PullRequestDetailRecord #{self.number} {self.title}>"
