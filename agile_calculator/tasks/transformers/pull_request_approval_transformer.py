from typing import Sequence

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.approval_count_record import (
    ApprovalCountRecord,
)
from agile_calculator.tasks.transformers.base_transformer import BaseTransformer


class PullRequestApprovalTransformer(BaseTransformer):
    def run(self, records: Sequence[PullRequestRecord]) -> list[ApprovalCountRecord]:
        user_counts: dict[str, int] = {}

        for record in records:
            if not record.merged:
                continue

            if not record.reviews:
                continue

            # Use a set to count unique approvers per PR
            approvers = set()
            for review in record.reviews:
                if review.state == 'APPROVED':
                    approvers.add(review.user)

            for user in approvers:
                user_counts[user] = user_counts.get(user, 0) + 1

        # Convert to list of records
        result = [
            ApprovalCountRecord(user=user, count=count)
            for user, count in user_counts.items()
        ]

        # Sort by count descending
        result.sort(key=lambda x: x.count, reverse=True)

        return result
