import os
from typing import Any

from github import Github


class GitHubExtractor:
    def __init__(self) -> None:
        self.client = Github(os.environ.get("GITHUB_CLASSIC_TOKEN"))

    def run(self) -> list[Any]:
        raise NotImplementedError
