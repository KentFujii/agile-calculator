from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def extract(self) -> list:
        pass
