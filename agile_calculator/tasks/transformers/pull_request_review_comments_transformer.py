import logging
from collections import defaultdict
from statistics import mean
from typing import Iterator

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_review_comments_record import (
    PullRequestReviewCommentsRecord,
)


class PullRequestReviewCommentsTransformer:
    def run(self, records: list[PullRequestRecord]) -> list[PullRequestReviewCommentsRecord]:
        mapped_records = list(self._map_records(records))
        reduced_records = list(self._reduce_records(mapped_records))
        return reduced_records

    def _reduce_records(self, records: list[PullRequestReviewCommentsRecord]) -> Iterator[PullRequestReviewCommentsRecord]:
        merged_dict = defaultdict(list)
        for r in records:
            merged_dict[r.merged_date].append(r.review_comments)
        sorted_items = sorted((k, mean(x for x in v if x is not None)) for k, v in merged_dict.items())
        for k, v in sorted_items:
            yield PullRequestReviewCommentsRecord(merged_date=k, review_comments=int(v))

    def _map_records(self, records: list[PullRequestRecord]) -> Iterator[PullRequestReviewCommentsRecord]:
        for record in records:
            if not record.merged_at:
                continue
            record =  PullRequestReviewCommentsRecord(
                merged_date=record.merged_at.date(),
                review_comments=record.review_comments
            )
            logging.debug(record)
            yield record
