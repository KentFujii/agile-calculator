from datetime import datetime, date

import pytest

from agile_calculator.tasks.transformers.pull_request_merged_count_transformer import PullRequestMergedCountTransformer
from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_merged_count_record import PullRequestMergedCountRecord

class TestPullRequestMergedCountTransformer:
    def test_run_with_valid_records(self):
        """Tests that the run method correctly transforms and aggregates pull request records."""
        records = [
            PullRequestRecord(
                title="PR 1",
                number=1,
                state="closed",
                created_at=datetime(2023, 1, 1, 10, 0, 0),
                merged_at=datetime(2023, 1, 2, 12, 0, 0),
                closed_at=datetime(2023, 1, 2, 12, 0, 0),
                additions=10,
                deletions=5,
                author="user1"
            ),
            PullRequestRecord(
                title="PR 2",
                number=2,
                state="closed",
                created_at=datetime(2023, 1, 2, 11, 0, 0),
                merged_at=datetime(2023, 1, 2, 18, 0, 0),
                closed_at=datetime(2023, 1, 2, 18, 0, 0),
                additions=20,
                deletions=10,
                author="user2"
            ),
            PullRequestRecord(
                title="PR 3",
                number=3,
                state="closed",
                created_at=datetime(2023, 1, 3, 9, 0, 0),
                merged_at=datetime(2023, 1, 4, 15, 0, 0),
                closed_at=datetime(2023, 1, 4, 15, 0, 0),
                additions=5,
                deletions=2,
                author="user1"
            )
        ]

        transformer = PullRequestMergedCountTransformer()
        result = transformer.run(records)

        assert len(result) == 2
        assert result[0] == PullRequestMergedCountRecord(merged_date=date(2023, 1, 2), merged_count=2)
        assert result[1] == PullRequestMergedCountRecord(merged_date=date(2023, 1, 4), merged_count=1)

    def test_run_with_unmerged_records(self):
        """Tests that the run method filters out pull requests that have not been merged."""
        records = [
            PullRequestRecord(
                title="PR 1",
                number=1,
                state="closed",
                created_at=datetime(2023, 1, 1, 10, 0, 0),
                merged_at=None,
                closed_at=datetime(2023, 1, 2, 12, 0, 0),
                additions=10,
                deletions=5,
                author="user1"
            ),
            PullRequestRecord(
                title="PR 2",
                number=2,
                state="closed",
                created_at=datetime(2023, 1, 2, 11, 0, 0),
                merged_at=datetime(2023, 1, 2, 18, 0, 0),
                closed_at=datetime(2023, 1, 2, 18, 0, 0),
                additions=20,
                deletions=10,
                author="user2"
            )
        ]

        transformer = PullRequestMergedCountTransformer()
        result = transformer.run(records)

        assert len(result) == 1
        assert result[0] == PullRequestMergedCountRecord(merged_date=date(2023, 1, 2), merged_count=1)

    def test_run_with_empty_records(self):
        """Tests that the run method returns an empty list when given no records."""
        transformer = PullRequestMergedCountTransformer()
        result = transformer.run([])

        assert len(result) == 0

    def test_map_and_reduce_records(self):
        """Tests the _map_records and _reduce_records methods individually."""
        transformer = PullRequestMergedCountTransformer()
        records = [
            PullRequestRecord(
                title="PR 1",
                number=1,
                state="closed",
                created_at=datetime(2023, 1, 1, 10, 0, 0),
                merged_at=datetime(2023, 1, 2, 12, 0, 0),
                closed_at=datetime(2023, 1, 2, 12, 0, 0),
                additions=10,
                deletions=5,
                author="user1"
            ),
            PullRequestRecord(
                title="PR 2",
                number=2,
                state="closed",
                created_at=datetime(2023, 1, 2, 11, 0, 0),
                merged_at=datetime(2023, 1, 2, 18, 0, 0),
                closed_at=datetime(2023, 1, 2, 18, 0, 0),
                additions=20,
                deletions=10,
                author="user2"
            ),
            PullRequestRecord(
                title="PR 3",
                number=3,
                state="closed",
                created_at=datetime(2023, 1, 1, 10, 0, 0),
                merged_at=None, # Should be skipped
                closed_at=datetime(2023, 1, 2, 12, 0, 0),
                additions=10,
                deletions=5,
                author="user1"
            ),
        ]

        # Test _map_records
        mapped_records = list(transformer._map_records(records))
        assert len(mapped_records) == 2
        assert mapped_records[0] == PullRequestMergedCountRecord(merged_date=date(2023, 1, 2), merged_count=1)
        assert mapped_records[1] == PullRequestMergedCountRecord(merged_date=date(2023, 1, 2), merged_count=1)

        # Test _reduce_records
        reduced_records = list(transformer._reduce_records(mapped_records))
        assert len(reduced_records) == 1
        assert reduced_records[0] == PullRequestMergedCountRecord(merged_date=date(2023, 1, 2), merged_count=2)
