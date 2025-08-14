from typing import Iterator

from agile_calculator.records.extracted.pull_request_record import (
    PullRequestRecord,
)
from agile_calculator.records.transformed.lead_time_for_changes_record import (
    LeadTimeForChangesRecord,
)


class LeadTimeForChangesTransformer:
    def run(self, records: list[PullRequestRecord]) -> list[LeadTimeForChangesRecord]:
        return list(self._generate_records(records))

    def _generate_records(self, records: list[PullRequestRecord]) -> Iterator[LeadTimeForChangesRecord]:
        for record in records:
            if not record.merged_at:
                continue
            yield LeadTimeForChangesRecord(
                merged_date=record.merged_at.date(),
                lead_time_seconds=record.lead_time_for_changes()
            )
