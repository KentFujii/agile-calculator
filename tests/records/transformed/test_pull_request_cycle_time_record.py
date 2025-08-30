from datetime import date

from agile_calculator.records.transformed.pull_request_cycle_time_record import PullRequestCycleTimeRecord


class TestPullRequestCycleTimeRecord:
    def test_init(self):
        merged_date = date(2023, 1, 1)
        record = PullRequestCycleTimeRecord(
            merged_date=merged_date,
            lead_time_seconds=3600
        )
        assert record.merged_date == merged_date
        assert record.lead_time_seconds == 3600

    def test_x(self):
        merged_date = date(2023, 1, 1)
        record = PullRequestCycleTimeRecord(merged_date=merged_date)
        assert record.x() == merged_date

    def test_y(self):
        record = PullRequestCycleTimeRecord(lead_time_seconds=7200)
        assert record.y() == 7200
