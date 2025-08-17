from collections import defaultdict
from statistics import mean
from typing import Iterator

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.review_comments_record import (
    ReviewCommentsRecord,
)


class ReviewCommentsTransformer:
    def run(self, records: list[PullRequestRecord]) -> list[ReviewCommentsRecord]:
        mapped_records = list(self._map_records(records))
        reduced_records = list(self._reduce_records(mapped_records))
        return reduced_records

    def _reduce_records(self, records: list[ReviewCommentsRecord]) -> Iterator[ReviewCommentsRecord]:
        merged_dict = defaultdict(list)
        for r in records:
            merged_dict[r.merged_date].append(r.review_comments)
        sorted_items = sorted((k, mean(v)) for k, v in merged_dict.items())
        for k, v in sorted_items:
            yield ReviewCommentsRecord(merged_date=k, review_comments=v)

    def _map_records(self, records: list[PullRequestRecord]) -> Iterator[ReviewCommentsRecord]:
        for record in records:
            if not record.merged_at:
                continue
            yield ReviewCommentsRecord(
                merged_date=record.merged_at.date(),
                review_comments=record.review_comments
            )
