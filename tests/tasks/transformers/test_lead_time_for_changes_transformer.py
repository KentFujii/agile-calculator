from datetime import date, datetime, timedelta

import pytest

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.lead_time_for_changes_record import (
    LeadTimeForChangesRecord,
)
from agile_calculator.tasks.transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)


class TestLeadTimeForChangesTransformer:
    def test_run(self):
        # Setup mock data
        # Use fixed dates to make the test deterministic
        # Using a Wednesday as a reference point
        pr1_merged = datetime(2024, 1, 10, 10, 0, 0)  # Wed
        pr1_created = datetime(2024, 1, 9, 10, 0, 0)  # Tue. lead time = 24h

        pr2_created = datetime(2024, 1, 8, 10, 0, 0)  # Mon
        pr2_merged = datetime(2024, 1, 10, 10, 0, 0)  # Wed. lead time = 48h

        pr3_created = datetime(2024, 1, 3, 10, 0, 0)  # Wed
        pr3_merged = datetime(2024, 1, 4, 10, 0, 0)  # Thu. lead time = 24h

        pr4_created = datetime(2024, 1, 2, 10, 0, 0)  # Not merged, Tue

        records = [
            PullRequestRecord(
                number=1,
                title="PR 1",
                user="user1",
                created_at=pr1_created,
                merged_at=pr1_merged,
                merged=True,
                # other fields are not relevant for this test
            ),
            PullRequestRecord(
                number=2,
                title="PR 2",
                user="user2",
                created_at=pr2_created,
                merged_at=pr2_merged,
                merged=True,
            ),
            PullRequestRecord(
                number=3,
                title="PR 3",
                user="user1",
                created_at=pr3_created,
                merged_at=pr3_merged,
                merged=True,
            ),
            PullRequestRecord(
                number=4,
                title="PR 4",
                user="user1",
                created_at=pr4_created,
                merged_at=None,
                merged=False,
            ),
        ]

        # Instantiate the transformer
        transformer = LeadTimeForChangesTransformer()

        # Execute
        result = transformer.run(records)

        # Assertions
        assert len(result) == 2
        assert isinstance(result[0], LeadTimeForChangesRecord)
        assert isinstance(result[1], LeadTimeForChangesRecord)

        # Assert the older date comes first
        assert result[0].merged_date == pr3_merged.date()
        assert result[1].merged_date == pr1_merged.date()

        # Assert lead time for the single PR merged on pr3_merged.date()
        expected_lead_time_3 = (pr3_merged - pr3_created).total_seconds() / 3600
        assert result[0].lead_time_seconds == pytest.approx(expected_lead_time_3)

        # Assert average lead time for the two PRs merged on pr1_merged.date()
        lead_time_1 = (pr1_merged - pr1_created).total_seconds() / 3600
        lead_time_2 = (pr2_merged - pr2_created).total_seconds() / 3600
        expected_avg_lead_time = (lead_time_1 + lead_time_2) / 2
        assert result[1].lead_time_seconds == pytest.approx(expected_avg_lead_time)

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
        transformer = LeadTimeForChangesTransformer()
        result = transformer.run(records)
        assert len(result) == 0

    def test_run_with_empty_list(self):
        transformer = LeadTimeForChangesTransformer()
        result = transformer.run([])
        assert len(result) == 0