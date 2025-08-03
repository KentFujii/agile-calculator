from .base_record import BaseRecorder


class LeadTimeForChangesRecord(BaseRecorder):
    def __init__(
        self,
        number=None,
        title=None,
        created_at=None,
        merged_at=None,
        lead_time=None
    ):
        self.number = number
        self.title = title
        self.created_at = created_at
        self.merged_at = merged_at
        self.lead_time = lead_time

    def __repr__(self):
        return f"<LeadTimeForChangesRecord #{self.number} {self.title} lead_time={self.lead_time}>"
