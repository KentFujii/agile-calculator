from agile_calculator.records.base_record import BaseRecord
from abc import abstractmethod

class TransformedRecord(BaseRecord):
    @abstractmethod
    def __repr__(self):
        pass
