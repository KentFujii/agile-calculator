from agile_calculator.records.base_record import BaseRecord
from abc import abstractmethod

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
