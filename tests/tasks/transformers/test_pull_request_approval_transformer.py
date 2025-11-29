import pytest
from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.pull_request_base import Review
from agile_calculator.tasks.transformers.pull_request_approval_transformer import PullRequestApprovalTransformer

class TestPullRequestApprovalTransformer:
    def test_run_aggregates_approvals(self):
        records = [
            PullRequestRecord(
                merged=True,
                reviews=[
                    Review(user="user1", state="APPROVED"),
                    Review(user="user2", state="CHANGES_REQUESTED"),
                ]
            ),
            PullRequestRecord(
                merged=True,
                reviews=[
                    Review(user="user1", state="APPROVED"),
                    Review(user="user3", state="APPROVED"),
                ]
            ),
             PullRequestRecord(
                merged=True,
                reviews=[
                    Review(user="user1", state="COMMENTED"),
                ]
            ),
        ]

        transformer = PullRequestApprovalTransformer()
        result = transformer.run(records)

        assert len(result) == 2

        # user1 approved twice (PR1, PR2). Since we sort descending, user1 (2) comes first.
        # But if count is same, order is undefined. Here counts are 2 and 1.

        # Check by converting to dict for easier assertion
        result_dict = {r.user: r.count for r in result}
        assert result_dict["user1"] == 2
        assert result_dict["user3"] == 1
        assert "user2" not in result_dict

    def test_run_deduplicates_per_pr(self):
        records = [
            PullRequestRecord(
                merged=True,
                reviews=[
                    Review(user="user1", state="APPROVED"),
                    Review(user="user1", state="APPROVED"), # duplicate
                ]
            )
        ]

        transformer = PullRequestApprovalTransformer()
        result = transformer.run(records)

        assert len(result) == 1
        assert result[0].user == "user1"
        assert result[0].count == 1

    def test_run_ignores_unmerged_prs(self):
        records = [
            PullRequestRecord(
                merged=False,
                reviews=[
                    Review(user="user1", state="APPROVED"),
                ]
            ),
             PullRequestRecord(
                merged=True,
                reviews=[
                    Review(user="user1", state="APPROVED"),
                ]
            )
        ]

        transformer = PullRequestApprovalTransformer()
        result = transformer.run(records)

        assert len(result) == 1
        assert result[0].user == "user1"
        assert result[0].count == 1
