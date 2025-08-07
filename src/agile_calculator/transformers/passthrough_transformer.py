from ..records.lead_time_for_changes_record import LeadTimeForChangesRecord
from ..records.pull_request_record import PullRequestRecord


class PassThroughTransformer:
    def __init__(self, records: PullRequestRecord):
        self.records = records
