from agile_calculator.records.extracted.pull_request_record import PullRequestRecord


class PassthroughTransformer:
    def __init__(self, records: PullRequestRecord):
        self.records = records
