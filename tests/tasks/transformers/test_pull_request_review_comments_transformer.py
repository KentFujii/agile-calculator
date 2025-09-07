
from datetime import date, datetime, timedelta

import pytest

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_review_comments_record import (
    PullRequestReviewCommentsRecord,
)
from agile_calculator.tasks.transformers.pull_request_review_comments_transformer import (
    PullRequestReviewCommentsTransformer,
)


class TestPullRequestReviewCommentsTransformer:
    @pytest.fixture
    def transformer(self):
        return PullRequestReviewCommentsTransformer()

    def create_pr_record(self, merged_at, review_comments):
        """Helper to create a PullRequestRecord with minimal necessary data."""
        return PullRequestRecord(
            number=1,
            title="test pr",
            user="test_user",
            merged_at=merged_at,
            created_at=datetime(2025, 1, 1),
            updated_at=datetime(2025, 1, 1),
            closed_at=merged_at,
            merged=bool(merged_at),
            merge_commit_sha="sha",
            base_ref="main",
            head_ref="feature",
            comments=0,
            review_comments=review_comments,
            commits=1,
            additions=10,
            deletions=5,
            changed_files=2,
        )

    def test_run_with_valid_data(self, transformer):
        """
        Tests the main `run` method with a typical list of PR records.
        It should map and then reduce them, calculating the mean of review comments per day.
        """
        today = date.today()
        yesterday = today - timedelta(days=1)
        records = [
            self.create_pr_record(datetime.combine(today, datetime.min.time()), 10),
            self.create_pr_record(datetime.combine(today, datetime.min.time()), 20),  # Same day
            self.create_pr_record(datetime.combine(yesterday, datetime.min.time()), 5),
            self.create_pr_record(None, 100),  # Not merged, should be ignored
        ]

        result = transformer.run(records)

        assert len(result) == 2
        assert isinstance(result[0], PullRequestReviewCommentsRecord)
        assert result[0].merged_date == yesterday
        assert result[0].review_comments == 5.0
        assert result[1].merged_date == today
        assert result[1].review_comments == 15.0  # mean(10, 20)

    def test_map_records(self, transformer):
        """
        Tests the internal `_map_records` method to ensure it correctly
        transforms PullRequestRecord to PullRequestReviewCommentsRecord and filters out unmerged PRs.
        """
        today = date.today()
        records = [
            self.create_pr_record(datetime.combine(today, datetime.min.time()), 10),
            self.create_pr_record(None, 5),  # Should be skipped
        ]

        mapped = list(transformer._map_records(records))

        assert len(mapped) == 1
        assert mapped[0].merged_date == today
        assert mapped[0].review_comments == 10

    def test_reduce_records(self, transformer):
        """
        Tests the internal `_reduce_records` method to ensure it correctly
        groups records by date, calculates the mean of comments, and sorts the result.
        """
        today = date.today()
        yesterday = today - timedelta(days=1)
        records = [
            PullRequestReviewCommentsRecord(merged_date=today, review_comments=10),
            PullRequestReviewCommentsRecord(merged_date=yesterday, review_comments=5),
            PullRequestReviewCommentsRecord(merged_date=today, review_comments=20),
        ]

        reduced = list(transformer._reduce_records(records))

        assert len(reduced) == 2
        assert reduced[0].merged_date == yesterday
        assert reduced[0].review_comments == 5.0
        assert reduced[1].merged_date == today
        assert reduced[1].review_comments == 15.0

    def test_run_with_empty_list(self, transformer):
        """
        Tests that running the transformer with an empty list results in an empty list.
        """
        result = transformer.run([])
        assert len(result) == 0

    def test_run_with_no_merged_prs(self, transformer):
        """
        Tests that if no PRs are merged, the result is an empty list.
        """
        records = [
            self.create_pr_record(None, 10),
            self.create_pr_record(None, 20),
        ]
        result = transformer.run(records)
        assert len(result) == 0
