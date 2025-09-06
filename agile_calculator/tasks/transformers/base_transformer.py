import abc
from typing import List

from agile_calculator.records.base_record import BaseRecord


class BaseTransformer(abc.ABC):

    @abc.abstractmethod
    def run(self, records: List[BaseRecord]) -> List[BaseRecord]:
        raise NotImplementedError
