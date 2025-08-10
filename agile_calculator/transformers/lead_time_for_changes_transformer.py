from ..records.lead_time_for_changes_record import LeadTimeForChangesRecord
from ..records.pull_request_record import PullRequestRecord


class LeadTimeForChangesTransformer:
    def run(self, records):
        for record in records:
            lead_time_seconds = (record.merged_at - record.created_at).total_seconds()
            yield LeadTimeForChangesRecord(
                number=record.number,
                title=record.title,
                merged_date=record.merged_at.date(),
                lead_time_seconds=lead_time_seconds
        )
