import os
from jira import JIRA
from jira.resources import Issue


class JiraExtractor:
    def __init__(self) -> None:
        self.server = os.environ.get("JIRA_SERVER_URL")
        self.email = os.environ.get("JIRA_EMAIL")
        self.token = os.environ.get("JIRA_TOKEN")
        self.client = JIRA(self.server, basic_auth=(self.email, self.token))
