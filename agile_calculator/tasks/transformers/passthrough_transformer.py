from typing import List

from agile_calculator.records.base_record import BaseRecord
from agile_calculator.tasks.transformers.base_transformer import BaseTransformer


class PassthroughTransformer(BaseTransformer):

    def run(self, records: List[BaseRecord]) -> List[BaseRecord]:
        return records
