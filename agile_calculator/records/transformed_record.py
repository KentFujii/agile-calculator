from abc import abstractmethod
from datetime import date

from agile_calculator.records.base_record import BaseRecord


class TransformedRecord(BaseRecord):
    @abstractmethod
    def x(self) -> date:
        pass

    @abstractmethod
    def y(self) -> int | float:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
