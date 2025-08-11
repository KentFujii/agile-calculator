from agile_calculator.records.pull_request_record import PullRequestRecord


class PassThroughTransformer:
    def __init__(self, records: PullRequestRecord):
        self.records = records
