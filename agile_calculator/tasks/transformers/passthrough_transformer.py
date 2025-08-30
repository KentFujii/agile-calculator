from typing import Sequence

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_detail_record import (
    PullRequestDetailRecord,
)


class PassthroughTransformer:
    def run(
        self, records: Sequence[PullRequestRecord]
    ) -> Sequence[PullRequestDetailRecord]:
        """
        PullRequestRecordをPullRequestDetailRecordに変換する
        """
        return [
            PullRequestDetailRecord(
                number=record.number,
                title=record.title,
                draft=record.draft,
                user=record.user,
                created_at=record.created_at,
                updated_at=record.updated_at,
                merged_at=record.merged_at,
                closed_at=record.closed_at,
                state=record.state,
                base_ref=record.base_ref,
                head_ref=record.head_ref,
                merged=record.merged,
                merge_commit_sha=record.merge_commit_sha,
                comments=record.comments,
                review_comments=record.review_comments,
                commits=record.commits,
                additions=record.additions,
                deletions=record.deletions,
                changed_files=record.changed_files,
            )
            for record in records
        ]
