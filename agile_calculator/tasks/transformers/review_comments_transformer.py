from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.review_comments_record import (
    ReviewCommentsRecord,
)


class ReviewCommentsTransformer:
    def run(self, records: list[PullRequestRecord]) -> list[ReviewCommentsRecord]:
        return list(self._generate_records(records))

    def _generate_records(self, records: list[PullRequestRecord]):
        for record in records:
            yield ReviewCommentsRecord(
                number=record.number,
                title=record.title,
                merged_date=record.merged_at.date(),
                review_comments=record.review_comments
            )
