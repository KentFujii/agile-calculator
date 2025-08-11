import os
from datetime import datetime, timedelta

from github import Github

class GitHubExtractor:
    def __init__(self):
        self.client = Github(os.environ.get("GITHUB_CLASSIC_TOKEN"))

    def run(self):
        pass
