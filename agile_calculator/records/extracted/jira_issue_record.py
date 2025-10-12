from agile_calculator.records.extracted_record import ExtractedRecord

class JiraIssueRecord(ExtractedRecord):
    key: str
    summary: str
    status: str
    assignee: str | None
    story_points: float | None
    sprints: list[str]
