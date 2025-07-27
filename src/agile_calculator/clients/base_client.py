from abc import ABC, abstractmethod


class BaseClient(ABC):
    @abstractmethod
    def to_pandas(self, project_key: str) -> list:
        pass

    @abstractmethod
    def to_csv(self, project_key: str) -> list:
        pass
