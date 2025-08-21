from datetime import date

from agile_calculator.records.transformed.lead_time_for_changes_record import LeadTimeForChangesRecord


def test_init():
    merged_date = date(2023, 1, 1)
    record = LeadTimeForChangesRecord(
        merged_date=merged_date,
        lead_time_seconds=3600
    )
    assert record.merged_date == merged_date
    assert record.lead_time_seconds == 3600


def test_x():
    merged_date = date(2023, 1, 1)
    record = LeadTimeForChangesRecord(merged_date=merged_date)
    assert record.x() == merged_date


def test_y():
    record = LeadTimeForChangesRecord(lead_time_seconds=7200)
    assert record.y() == 7200
