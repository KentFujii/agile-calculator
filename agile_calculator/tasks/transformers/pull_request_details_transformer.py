from typing import List

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_details_record import (
    PullRequestDetailsRecord,
)
from agile_calculator.tasks.transformers.base_transformer import BaseTransformer


class PullRequestDetailsTransformer(BaseTransformer):
    def run(self, records: List[PullRequestRecord]) -> List[PullRequestDetailsRecord]:
        mapped = []
        for record in records:
            mapped.append(PullRequestDetailsRecord.model_validate(record.model_dump()))
        return mapped
