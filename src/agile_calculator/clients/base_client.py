from abc import ABC, abstractmethod


class BaseClient(ABC):
    @abstractmethod
    def get_issues(self, project_key: str):
        pass
