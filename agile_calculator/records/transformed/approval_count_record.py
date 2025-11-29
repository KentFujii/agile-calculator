from agile_calculator.records.base_record import BaseRecord


class ApprovalCountRecord(BaseRecord):
    user: str
    count: int
