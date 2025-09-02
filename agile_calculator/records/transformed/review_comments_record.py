from dataclasses import dataclass
from datetime import date

from agile_calculator.records.transformed_record import TransformedRecord


@dataclass
class ReviewCommentsRecord(TransformedRecord):
    review_comments: int | None = None

    def x(self) -> date:
        if self.merged_date is None:
            raise ValueError("merged_date is not set")
        return self.merged_date

    def y(self) -> int:
        if self.review_comments is None:
            raise ValueError("review_comments is not set")
        return self.review_comments

    def __repr__(self) -> str:
        return (
            f"<ReviewCommentsRecord "
            f"x: merged_date={self.merged_date}>, "
            f"y: review_comments={self.review_comments}>"
        )
