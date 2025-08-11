import os
from datetime import datetime, timedelta

from github import Github

from agile_calculator.records.pull_request_record import PullRequestRecord


class GitHubExtractor:
    def __init__(self):
        self.client = Github(os.environ.get("GITHUB_CLASSIC_TOKEN"))

    def run(self):
        pass
