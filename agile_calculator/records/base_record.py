from abc import ABC, abstractmethod


class BaseRecord(ABC):
    @abstractmethod
    def __repr__(self):
        pass
