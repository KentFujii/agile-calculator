from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date

from agile_calculator.records.base_record import BaseRecord


@dataclass
class TransformedRecord(BaseRecord, ABC):
    merged_date: date | None = None

    @abstractmethod
    def x(self) -> date:
        pass

    @abstractmethod
    def y(self) -> int | float:
        pass
