from datetime import datetime

from agile_calculator.records.extracted_record import ExtractedRecord

class CommentBase(ExtractedRecord):
    id: int | None = None
    body: str | None = None
    user: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    pull_request_url: str | None = None
    author_association: str | None = None
    url: str | None = None
    html_url: str | None = None
