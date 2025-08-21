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
        created_at = datetime(2023, 1, 1, 10, 0, 0)
        merged_at = datetime(2023, 1, 1, 12, 0, 0)
        record = PullRequestRecord(created_at=created_at, merged_at=merged_at)
        # (12 - 10) * 3600 / 3600 = 2.0
        assert record.lead_time_for_changes() == 2.0

        created_at_day = datetime(2023, 1, 1, 0, 0, 0)
        merged_at_day = datetime(2023, 1, 2, 0, 0, 0)
        record_day = PullRequestRecord(created_at=created_at_day, merged_at=merged_at_day)
        assert record_day.lead_time_for_changes() == 24.0
