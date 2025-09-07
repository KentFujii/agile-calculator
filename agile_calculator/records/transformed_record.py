from abc import ABC, abstractmethod
from datetime import date

from agile_calculator.records.base_record import BaseRecord


class TransformedRecord(BaseRecord, ABC):
    @abstractmethod
    def x(self) -> date:
        pass

    @abstractmethod
    def y(self) -> int | float:
        pass
