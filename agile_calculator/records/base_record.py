from abc import ABC, abstractmethod


class BaseRecorder(ABC):
    @abstractmethod
    def __repr__(self):
        pass
