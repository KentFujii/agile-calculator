from agile_calculator.records.transformed_record import TransformedRecord


class ReviewCommentsRecord(TransformedRecord):
    def __init__(
        self,
        number=None,
        title=None,
        merged_date=None,
        review_comments=None
    ):
        self.merged_date = merged_date
        self.review_comments = review_comments

    def x(self):
        return merged_date

    def y(self):
        return review_comments

    def __repr__(self):
        return (
            f"<ReviewCommentsRecord "
            f"x: merged_date={self.merged_date}>, "
            f"y: review_comments={self.review_comments}>"
        )
