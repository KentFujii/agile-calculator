from datetime import date

from agile_calculator.records.transformed.pull_request_review_comments_record import PullRequestReviewCommentsRecord


class TestPullRequestReviewCommentsRecord:
    def test_init(self):
        merged_date = date(2023, 1, 1)
        record = PullRequestReviewCommentsRecord(
            merged_date=merged_date,
            review_comments=10
        )
        assert record.merged_date == merged_date
        assert record.review_comments == 10

    def test_x(self):
        merged_date = date(2023, 1, 1)
        record = PullRequestReviewCommentsRecord(merged_date=merged_date)
        assert record.x() == merged_date

    def test_y(self):
        record = PullRequestReviewCommentsRecord(review_comments=5)
        assert record.y() == 5
