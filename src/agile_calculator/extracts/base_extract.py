from abc import ABC, abstractmethod


class BaseExtract(ABC):
    @abstractmethod
    def extract(self, project_key: str) -> list:
        pass
