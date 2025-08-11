from collections import namedtuple

from jira import JIRA


class JiraExtractor:
    def __init__(self, server: str, email: str, token: str):
        self.server = server
        self.email = email
        self.token = token
        self.client = JIRA(self.server, basic_auth=(self.email, self.token))

    def run(self, project_key: str, assignee: str):
        allfields = self.client.fields()
        name_map = {field["name"]: field["id"] for field in allfields}
        issue_info = self._get_issueinfo_namedtuple()
        issues = self.client.search_issues(
            f'project = "{project_key}" AND assignee = "{assignee}" ORDER BY created DESC'
        )
        for issue in issues:
            yield issue_info(
                key=issue.key,
                summary=issue.fields.summary,
                status=issue.fields.status.name,
                assignee=issue.fields.assignee.displayName if issue.fields.assignee else None,
                story_points=getattr(issue.fields, name_map['Story point estimate'], None),
                sprints=[sprint.name for sprint in getattr(issue.fields, name_map['Sprint'], [])],
            )

    def _get_issueinfo_namedtuple(self):
        return namedtuple(
            "IssueInfo",
            [
                "key",
                "summary",
                "status",
                "assignee",
                "story_points",
                "sprints",
            ]
        )
