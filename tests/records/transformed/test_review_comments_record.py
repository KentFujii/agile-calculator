from datetime import date

from agile_calculator.records.transformed.review_comments_record import ReviewCommentsRecord


def test_init():
    merged_date = date(2023, 1, 1)
    record = ReviewCommentsRecord(
        merged_date=merged_date,
        review_comments=10
    )
    assert record.merged_date == merged_date
    assert record.review_comments == 10


def test_x():
    merged_date = date(2023, 1, 1)
    record = ReviewCommentsRecord(merged_date=merged_date)
    assert record.x() == merged_date


def test_y():
    record = ReviewCommentsRecord(review_comments=5)
    assert record.y() == 5
