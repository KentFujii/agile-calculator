from datetime import date, datetime

import pytest

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_changed_lines_record import (
    PullRequestChangedLinesRecord,
)
from agile_calculator.tasks.transformers.pull_request_changed_lines_transformer import (
    PullRequestChangedLinesTransformer,
)


class TestPullRequestChangedLinesTransformer:
    def test_run(self):
        # Setup mock data
        pr1_merged = datetime(2024, 1, 10, 10, 0, 0)

        # PR1: 10 + 5 = 15
        pr1 = PullRequestRecord(
            number=1,
            title="PR 1",
            user="user1",
            created_at=datetime(2024, 1, 9, 10, 0, 0),
            merged_at=pr1_merged,
            merged=True,
            additions=10,
            deletions=5
        )

        # PR2: 20 + 10 = 30
        pr2 = PullRequestRecord(
            number=2,
            title="PR 2",
            user="user2",
            created_at=datetime(2024, 1, 8, 10, 0, 0),
            merged_at=pr1_merged,
            merged=True,
            additions=20,
            deletions=10
        )

        # PR3: 5 + 5 = 10 (Different Date)
        pr3_merged = datetime(2024, 1, 4, 10, 0, 0)
        pr3 = PullRequestRecord(
            number=3,
            title="PR 3",
            user="user1",
            created_at=datetime(2024, 1, 3, 10, 0, 0),
            merged_at=pr3_merged,
            merged=True,
            additions=5,
            deletions=5
        )

        # PR4: Not merged
        pr4 = PullRequestRecord(
            number=4,
            title="PR 4",
            user="user1",
            created_at=datetime(2024, 1, 2, 10, 0, 0),
            merged_at=None,
            merged=False,
            additions=100,
            deletions=100
        )

        records = [pr1, pr2, pr3, pr4]

        # Instantiate the transformer
        transformer = PullRequestChangedLinesTransformer()

        # Execute
        result = transformer.run(records)

        # Assertions
        assert len(result) == 2
        assert isinstance(result[0], PullRequestChangedLinesRecord)
        assert isinstance(result[1], PullRequestChangedLinesRecord)

        # Assert the older date comes first
        assert result[0].merged_date == pr3_merged.date()
        assert result[1].merged_date == pr1_merged.date()

        # Assert changed lines for single PR
        # PR3: 10
        assert result[0].changed_lines == 10.0

        # Assert average changed lines for two PRs on same date
        # PR1: 15, PR2: 30. Avg: 22.5
        assert result[1].changed_lines == 22.5

    def test_run_with_missing_additions_deletions(self):
        # PR with None additions/deletions
        pr1_merged = datetime(2024, 1, 10, 10, 0, 0)
        pr1 = PullRequestRecord(
            number=1,
            title="PR 1",
            user="user1",
            created_at=datetime(2024, 1, 9, 10, 0, 0),
            merged_at=pr1_merged,
            merged=True,
            additions=None,
            deletions=None
        )

        transformer = PullRequestChangedLinesTransformer()
        result = transformer.run([pr1])

        assert len(result) == 1
        assert result[0].changed_lines == 0.0

    def test_run_with_no_merged_prs(self):
        records = [
            PullRequestRecord(
                number=1,
                title="PR 1",
                user="user1",
                created_at=datetime.now(),
                merged_at=None,
                merged=False,
            )
        ]
        transformer = PullRequestChangedLinesTransformer()
        result = transformer.run(records)
        assert len(result) == 0

    def test_run_with_empty_list(self):
        transformer = PullRequestChangedLinesTransformer()
        result = transformer.run([])
        assert len(result) == 0
