from typing import Iterator
from agile_calculator.tasks.extractors.jira_extractor import JiraExtractor
from agile_calculator.records.extracted.jira_issue_record import JiraIssueRecord

class IssueExtractor(JiraExtractor):
    def __init__(self):
        super().__init__()

    def run(self, project_key: str) -> Iterator[JiraIssueRecord]:
        allfields = self.client.fields()
        name_map = {field["name"]: field["id"] for field in allfields}
        search_results = self.client.enhanced_search_issues(
            # f'project = "{project_key}" AND assignee = "{assignee}" ORDER BY created DESC'
            f'project = "{project_key}" ORDER BY created DESC'
        )
        issues: list[Issue] = search_results
        for issue in issues:
            breakpoint()
            yield JiraIssueRecord(
                key=issue.key,
                summary=issue.fields.summary,
                status=issue.fields.status.name,
                assignee=issue.fields.assignee.displayName if issue.fields.assignee else None,
                story_point=getattr(issue.fields, name_map['Story point estimate'], None),
                sprints=[sprint.name for sprint in (getattr(issue.fields, name_map['Sprint']) or [])],
            )
