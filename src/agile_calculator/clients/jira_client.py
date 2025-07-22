import os
from jira import JIRA, JIRAError
from .base_client import BaseClient

class JiraClient(BaseClient):
    def __init__(self, server: str, token: str):
        self.server = server
        self.token = token
        try:
            self.client = JIRA(server=self.server, token_auth=self.token)
        except JIRAError as e:
            raise ConnectionError(f"Failed to connect to Jira: {e.message}")

    def get_issues(self, project_key: str) -> list:
        try:
            issues = self.client.search_issues(f'project={project_key}')
            return issues
        except JIRAError as e:
            print(f"Failed to get issues from Jira: {e.message}")
            return []

def get_jira_client() -> JiraClient:
    server = os.environ.get("JIRA_SERVER")
    token = os.environ.get("JIRA_TOKEN")
    if not server or not token:
        raise ValueError("JIRA_SERVER and JIRA_TOKEN environment variables must be set")
    return JiraClient(server, token)
