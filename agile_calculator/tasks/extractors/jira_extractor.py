import logging
from typing import Iterator, NamedTuple

from jira import JIRA
from jira.resources import Issue


class IssueInfo(NamedTuple):
    key: str
    summary: str
    status: str
    assignee: str | None
    story_points: float | None
    sprints: list[str]


class JiraExtractor:
    def __init__(self, server: str, email: str, token: str) -> None:
        self.server = server
        self.email = email
        self.token = token
        self.client = JIRA(self.server, basic_auth=(self.email, self.token))

    def run(self, project_key: str, assignee: str) -> Iterator[IssueInfo]:
        allfields = self.client.fields()
        name_map = {field["name"]: field["id"] for field in allfields}
        search_results = self.client.search_issues(
            f'project = "{project_key}" AND assignee = "{assignee}" ORDER BY created DESC'
        )
        if isinstance(search_results, str):
            logging.error(f"Jira API returned an error: {search_results}")
            return
        if isinstance(search_results, dict):
            logging.error(f"Jira API returned a dict: {search_results}")
            return
        issues: list[Issue] = search_results
        for issue in issues:
            yield IssueInfo(
                key=issue.key,
                summary=issue.fields.summary,
                status=issue.fields.status.name,
                assignee=issue.fields.assignee.displayName if issue.fields.assignee else None,
                story_points=getattr(issue.fields, name_map['Story point estimate'], None),
                sprints=[sprint.name for sprint in getattr(issue.fields, name_map['Sprint'], [])],
            )

