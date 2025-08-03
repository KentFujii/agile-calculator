
from ..records.lead_time_for_changes_record import LeadTimeForChangesRecord
from ..records.pull_request_record import PullRequestRecord


class LeadTimeForChangesTransformer:
    def __init__(self, pull_request: PullRequestRecord):
        self.pull_request = pull_request

    def transform(self) -> 'LeadTimeForChangesRecord':
        lead_time_seconds = (self.pull_request.merged_at - self.pull_request.created_at).total_seconds() if self.pull_request.merged_at else None
        return LeadTimeForChangesRecord(
            number=self.pull_request.number,
            title=self.pull_request.title,
            merged_at=self.pull_request.merged_at,
            lead_time_seconds=lead_time_seconds
        )
