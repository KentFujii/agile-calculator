import logging
from collections import defaultdict
from statistics import mean
from typing import Iterator

from agile_calculator.records.extracted.pull_request_record import (
    PullRequestRecord,
)
from agile_calculator.records.transformed.lead_time_for_changes_record import (
    LeadTimeForChangesRecord,
)


class LeadTimeForChangesTransformer:
    def run(self, records: list[PullRequestRecord]) -> list[LeadTimeForChangesRecord]:
        mapped_records = list(self._map_records(records))
        reduced_records = list(self._reduce_records(mapped_records))
        return reduced_records

    def _reduce_records(self, records: list[LeadTimeForChangesRecord]) -> Iterator[LeadTimeForChangesRecord]:
        merged_dict = defaultdict(list)
        for r in records:
            merged_dict[r.merged_date].append(r.lead_time_seconds)
        sorted_items = sorted((k, mean(x for x in v if x is not None)) for k, v in merged_dict.items())
        for k, v in sorted_items:
            yield LeadTimeForChangesRecord(merged_date=k, lead_time_seconds=v)

    def _map_records(self, records: list[PullRequestRecord]) -> Iterator[LeadTimeForChangesRecord]:
        for record in records:
            if not record.merged_at:
                continue
            record = LeadTimeForChangesRecord(
                merged_date=record.merged_at.date(),
                lead_time_seconds=record.lead_time_for_changes()
            )
            logging.debug(record)
            yield record
