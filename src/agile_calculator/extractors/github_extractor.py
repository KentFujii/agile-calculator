from datetime import datetime, timedelta

from github import Github

from ..records.pull_request_record import PullRequestRecord
from .base_extractor import BaseExtractor


class GitHubExtractor(BaseExtractor):
    def __init__(self, token: str):
        self.token = token
        self.client = Github(self.token)

    def run(self):
        pass