from datetime import date, datetime

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
        # This was created and merged on a Sunday (2023-01-01), so lead time should be 0.
        created_at = datetime(2023, 1, 1, 10, 0, 0)
        merged_at = datetime(2023, 1, 1, 12, 0, 0)
        record = PullRequestRecord(created_at=created_at, merged_at=merged_at)
        assert record.lead_time_for_changes() == 0.0

        # This was created on Sunday and merged on Monday.
        # The time on Sunday should not be counted. The total duration is 24h.
        # The time on Sunday is 24h. So lead time is 24 - 24 = 0.
        created_at_day = datetime(2023, 1, 1, 0, 0, 0)
        merged_at_day = datetime(2023, 1, 2, 0, 0, 0)
        record_day = PullRequestRecord(created_at=created_at_day, merged_at=merged_at_day)
        assert record_day.lead_time_for_changes() == 0.0

    def test_lead_time_for_changes_with_weekend(self):
        # Friday 5 PM to Monday 5 PM = 72 hours.
        # Weekend days are Saturday and Sunday. 2 days * 24 hours = 48 hours.
        # Lead time should be 72 - 48 = 24 hours.
        created_at = datetime(2024, 1, 5, 17, 0, 0)  # This is a Friday
        merged_at = datetime(2024, 1, 8, 17, 0, 0)  # This is a Monday
        record = PullRequestRecord(created_at=created_at, merged_at=merged_at)
        assert record.lead_time_for_changes() == 24.0

    def test_lead_time_for_changes_on_weekend(self):
        # Saturday 10 AM to Saturday 11 AM = 1 hour.
        # Weekend days is 1. 1 day * 24 hours = 24 hours.
        # Lead time should be max(0, 1 - 24) = 0 hours.
        created_at = datetime(2024, 1, 6, 10, 0, 0)  # This is a Saturday
        merged_at = datetime(2024, 1, 6, 11, 0, 0)  # This is a Saturday
        record = PullRequestRecord(created_at=created_at, merged_at=merged_at)
        assert record.lead_time_for_changes() == 0.0
