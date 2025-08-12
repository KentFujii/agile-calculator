from agile_calculator.records.transformed.review_comments_record import (
    ReviewCommentsRecord,
)


class LeadTimeForChangesTransformer:
    def run(self, records):
        for record in records:
            yield LeadTimeForChangesRecord(
                number=record.number,
                title=record.title,
                merged_date=record.merged_at.date(),
                review_comments=review_comments
        )
