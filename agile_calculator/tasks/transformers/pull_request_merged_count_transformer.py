from collections import defaultdict
from typing import Iterator

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_merged_count_record import (
    PullRequestMergedCountRecord,
)


class PullRequestMergedCountTransformer:
    def run(self, records: list[PullRequestRecord]) -> list[PullRequestMergedCountRecord]:
        mapped_records = list(self._map_records(records))
        reduced_records = list(self._reduce_records(mapped_records))
        return reduced_records

    def _reduce_records(self, records: list[PullRequestMergedCountRecord]) -> Iterator[PullRequestMergedCountRecord]:
        merged_dict = defaultdict(int)
        for r in records:
            merged_dict[r.merged_date] += 1
        for k in sorted(merged_dict.keys()):
            yield PullRequestMergedCountRecord(merged_date=k, merged_count=merged_dict[k])

    def _map_records(self, records: list[PullRequestRecord]) -> Iterator[PullRequestMergedCountRecord]:
        for record in records:
            if not record.merged_at:
                continue
            yield PullRequestMergedCountRecord(
                merged_date=record.merged_at.date(),
                merged_count=1,
            )
