from typing import Sequence

from agile_calculator.records.transformed_record import TransformedRecord
from agile_calculator.tasks.loaders.base_loader import BaseLoader


class CsvLoader(BaseLoader):

    def run(self, records: Sequence[TransformedRecord]) -> None:
        pass
