from datetime import date

from agile_calculator.records.transformed_record import TransformedRecord


class PullRequestReviewCommentsRecord(TransformedRecord):
    merged_date: date | None = None
    review_comments: int | None = None

    def x(self) -> date:
        if self.merged_date is None:
            raise ValueError("merged_date is not set")
        return self.merged_date

    def y(self) -> int:
        if self.review_comments is None:
            raise ValueError("review_comments is not set")
        return self.review_comments
