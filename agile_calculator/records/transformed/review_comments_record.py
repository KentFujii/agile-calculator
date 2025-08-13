from agile_calculator.records.transformed_record import TransformedRecord


class ReviewCommentsRecord(TransformedRecord):
    def __init__(
        self,
        number=None,
        title=None,
        merged_date=None,
        review_comments=None
    ):
        self.number = number
        self.title = title
        self.merged_date = merged_date
        self.review_comments = review_comments

    def __repr__(self):
        return (
            f"<ReviewCommentsRecord #{self.number} {self.title} "
            f"x: lead_time_seconds={self.lead_time_seconds}>, "
            f"y: merged_date={self.merged_date}>"
        )
