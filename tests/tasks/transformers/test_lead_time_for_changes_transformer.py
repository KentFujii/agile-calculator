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
    @pytest.fixture
    def transformer(self):
        return LeadTimeForChangesTransformer()

    def create_pr_record(self, created_at, merged_at):
        """Helper to create a PullRequestRecord with minimal necessary data."""
        return PullRequestRecord(
            number=1,
            title="test pr",
            user="test_user",
            created_at=created_at,
            merged_at=merged_at,
            closed_at=merged_at,
            updated_at=merged_at or created_at,
            merged=bool(merged_at),
            merge_commit_sha="sha" if merged_at else None,
            state="closed",
            base_ref="main",
            head_ref="feature",
            comments=0,
            review_comments=0,
            commits=1,
            additions=10,
            deletions=5,
            changed_files=2,
            draft=False,
        )

    def test_map_records(self, transformer):
        # Arrange
        now = datetime.now()
        pr1_created = now - timedelta(days=1)
        pr1_merged = now
        pr2_created = now - timedelta(days=2)
        # PR that is not merged should be skipped
        pr3_created = now - timedelta(days=3)

        records = [
            self.create_pr_record(created_at=pr1_created, merged_at=pr1_merged),
            self.create_pr_record(created_at=pr2_created, merged_at=None),
            self.create_pr_record(created_at=pr3_created, merged_at=pr1_merged),
        ]

        # Act
        result = list(transformer._map_records(records))

        # Assert
        assert len(result) == 2
        assert isinstance(result[0], LeadTimeForChangesRecord)
        assert result[0].merged_date == pr1_merged.date()
        assert result[0].lead_time_seconds == (pr1_merged - pr1_created).total_seconds()
        assert result[1].merged_date == pr1_merged.date()
        assert result[1].lead_time_seconds == (pr1_merged - pr3_created).total_seconds()

    def test_reduce_records(self, transformer):
        # Arrange
        date1 = date(2023, 1, 1)
        date2 = date(2023, 1, 2)
        records = [
            LeadTimeForChangesRecord(merged_date=date1, lead_time_seconds=100),
            LeadTimeForChangesRecord(merged_date=date1, lead_time_seconds=200),
            LeadTimeForChangesRecord(merged_date=date2, lead_time_seconds=300),
        ]

        # Act
        result = list(transformer._reduce_records(records))

        # Assert
        assert len(result) == 2
        assert result[0].merged_date == date1
        assert result[0].lead_time_seconds == 150  # mean(100, 200)
        assert result[1].merged_date == date2
        assert result[1].lead_time_seconds == 300

    def test_run(self, transformer):
        # Arrange
        now = datetime.now()
        pr1_created = now - timedelta(days=1)
        pr1_merged = now
        pr2_created = now - timedelta(days=2)
        pr2_merged = now
        pr3_created = now - timedelta(days=3)
        pr3_merged = now + timedelta(days=1)

        records = [
            self.create_pr_record(created_at=pr1_created, merged_at=pr1_merged),
            self.create_pr_record(created_at=pr2_created, merged_at=pr2_merged),
            self.create_pr_record(created_at=pr3_created, merged_at=pr3_merged),
            self.create_pr_record(created_at=now, merged_at=None),  # Should be ignored
        ]

        # Act
        result = transformer.run(records)

        # Assert
        assert len(result) == 2
        assert result[0].merged_date == now.date()
        expected_lead_time_date1 = (
            (pr1_merged - pr1_created).total_seconds()
            + (pr2_merged - pr2_created).total_seconds()
        ) / 2
        assert result[0].lead_time_seconds == expected_lead_time_date1

        assert result[1].merged_date == pr3_merged.date()
        assert result[1].lead_time_seconds == (pr3_merged - pr3_created).total_seconds()

    def test_run_with_empty_list(self, transformer):
        # Arrange
        records = []

        # Act
        result = transformer.run(records)

        # Assert
        assert len(result) == 0