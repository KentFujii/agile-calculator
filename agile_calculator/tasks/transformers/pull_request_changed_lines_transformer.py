import logging
from collections import defaultdict
from statistics import mean
from typing import Iterator

from agile_calculator.records.extracted.pull_request_record import (
    PullRequestRecord,
)
from agile_calculator.records.transformed.pull_request_changed_lines_record import (
    PullRequestChangedLinesRecord,
)


class PullRequestChangedLinesTransformer:
    def run(self, records: list[PullRequestRecord]) -> list[PullRequestChangedLinesRecord]:
        mapped_records = list(self._map_records(records))
        reduced_records = list(self._reduce_records(mapped_records))
        return reduced_records

    def _reduce_records(self, records: list[PullRequestChangedLinesRecord]) -> Iterator[PullRequestChangedLinesRecord]:
        merged_dict = defaultdict(list)
        for r in records:
            merged_dict[r.merged_date].append(r.changed_lines)
        sorted_items = sorted((k, mean(x for x in v if x is not None)) for k, v in merged_dict.items())
        for k, v in sorted_items:
            yield PullRequestChangedLinesRecord(merged_date=k, changed_lines=v)

    def _map_records(self, records: list[PullRequestRecord]) -> Iterator[PullRequestChangedLinesRecord]:
        for record in records:
            if not record.merged_at:
                continue
            record = PullRequestChangedLinesRecord(
                merged_date=record.merged_at.date(),
                changed_lines=float(record.changed_lines())
            )
            logging.debug(record)
            yield record
