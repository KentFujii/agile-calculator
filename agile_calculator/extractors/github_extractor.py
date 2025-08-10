import os
from datetime import datetime, timedelta

from github import Github

from ..records.pull_request_record import PullRequestRecord
# from .base_extractor import BaseExtractor


class GitHubExtractor:
    def __init__(self):
        self.client = Github(os.environ.get("GITHUB_CLASSIC_TOKEN"))

    def run(self):
        pass
