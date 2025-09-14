from datetime import datetime, date

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord


class TestPullRequestRecord:
    def test_init(self):
        created_at = datetime(2023, 1, 1, 10, 0, 0)
        merged_at = datetime(2023, 1, 1, 12, 0, 0)
        record = PullRequestRecord(
            number=1,
            title="Test PR",
            created_at=created_at,
            merged_at=merged_at
        )
        assert record.number == 1
        assert record.title == "Test PR"
        assert record.created_at == created_at
        assert record.merged_at == merged_at

    def test_merged_date(self):
        record = PullRequestRecord(merged_at=datetime(2023, 1, 1, 12, 0, 0))
        assert record.merged_date() == date(2023, 1, 1)

        record_none = PullRequestRecord(merged_at=None)
        assert record_none.merged_date() is None

    def test_lead_time_for_changes(self):
        # Test case 1: Same day, 2 hours difference
        created_at = datetime(2023, 1, 1, 10, 0, 0)
        merged_at = datetime(2023, 1, 1, 12, 0, 0)
        record = PullRequestRecord(created_at=created_at, merged_at=merged_at)
        assert record.lead_time_for_changes() == 2.0

        # Test case 2: Next day, 24 hours difference
        created_at_day = datetime(2023, 1, 1, 0, 0, 0)
        merged_at_day = datetime(2023, 1, 2, 0, 0, 0)
        record_day = PullRequestRecord(created_at=created_at_day, merged_at=merged_at_day)
        assert record_day.lead_time_for_changes() == 24.0

        # Test case 3: Over a weekend, 72 hours difference
        created_at_weekend = datetime(2024, 1, 5, 17, 0, 0)  # This is a Friday
        merged_at_weekend = datetime(2024, 1, 8, 17, 0, 0)  # This is a Monday
        record_weekend = PullRequestRecord(created_at=created_at_weekend, merged_at=merged_at_weekend)
        assert record_weekend.lead_time_for_changes() == 72.0

        # Test case 4: On a weekend, 1 hour difference
        created_at_on_weekend = datetime(2024, 1, 6, 10, 0, 0)  # This is a Saturday
        merged_at_on_weekend = datetime(2024, 1, 6, 11, 0, 0)  # This is a Saturday
        record_on_weekend = PullRequestRecord(created_at=created_at_on_weekend, merged_at=merged_at_on_weekend)
        assert record_on_weekend.lead_time_for_changes() == 1.0

        # Test case 5: No merge date
        record_none = PullRequestRecord(created_at=created_at, merged_at=None)
        assert record_none.lead_time_for_changes() is None
