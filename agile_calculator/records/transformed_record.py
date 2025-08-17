from abc import abstractmethod

from agile_calculator.records.base_record import BaseRecord


class TransformedRecord(BaseRecord):
    @abstractmethod
    def x(self):
        pass

    @abstractmethod
    def y(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
