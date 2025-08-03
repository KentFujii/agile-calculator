from ..records.pull_request_record import PullRequestRecord


class LeadTimeForChangesTransformer:
    def __init__(self):
        pass

    def transform(self, pull_request: PullRequestRecord) -> dict:
        return {
            "number": pull_request.number,
            "title": pull_request.title,
            "created_at": pull_request.created_at,
            "merged_at": pull_request.merged_at,
            "lead_time": (pull_request.merged_at - pull_request.created_at).total_seconds if pull_request.merged_at else None
        }
