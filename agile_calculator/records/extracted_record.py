from abc import abstractmethod

from agile_calculator.records.base_record import BaseRecord


class ExtractedRecord(BaseRecord):
    @abstractmethod
    def __repr__(self):
        pass
