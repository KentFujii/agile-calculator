from collections import namedtuple

from jira import JIRA

from .base_extractor import BaseExtractor


class JiraExtractor(BaseExtractor):
    def __init__(self, server: str, email: str, token: str):
        self.server = server
        self.email = email
        self.token = token
        self.client = JIRA(self.server, basic_auth=(self.email, self.token))

    def extract(self, project_key: str, assignee: str):
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

    # def to_pandas(self, project_key: str) -> list:
    #     return []

    # def to_csv(self, project_key: str) -> list:
    #     return []

    # def velocity(self, project_key: str, assignee: str):
    #     """ベロシティを取得する"""
    #     try:
    #         allfields = self.client.fields()
    #         name_map = {field["name"]: field["id"] for field in allfields}
    #         issues = self.client.search_issues(
    #             f'project = "{project_key}" AND assignee = "{assignee}" ORDER BY created DESC'
    #         )
    #         for issue in issues:
    #             print("----------------------")
    #             print(f"key: {issue.key}")
    #             print(f"summary: {issue.fields.summary}")
    #             print(f"status: {issue.fields.status.name}")
    #             print(f"assignee: {issue.fields.assignee.displayName}")
    #             print(
    #                 f"story points: {getattr(issue.fields, name_map['Story point estimate'])}"
    #             )
    #             print(
    #                 f"sprints: {[sprint.name for sprint in getattr(issue.fields, name_map['Sprint'])]}"
    #             )
    #     except JIRAError as e:
    #         print(f"Failed to get velocity from Jira: {e.text}")
    #         return []

    # def sprint_burndown(self, project_key: str, sprint_id: str):
    #     """スプリントバーンダウン（進捗状況、残作業量の推移）を取得する"""
    #     pass

    # def sprint_completion_rate(self, project_key: str, sprint_id: str):
    #     """スプリント完了率（計画した作業のうち完了した割合）を取得する"""
    #     pass

    # def story_completion_rate(self, project_key: str, sprint_id: str):
    #     """ストーリー完了率（ストーリーごとの達成状況）を取得する"""
    #     pass

    # def issue_throughput(self, project_key: str, period: str):
    #     """イシュースループット（一定期間内に完了したチケット数）を取得する"""
    #     pass

    # def cycle_time(self, project_key: str, issue_id: str):
    #     """サイクルタイム（チケットが「着手」から「完了」までにかかった時間）を取得する"""
    #     pass

    # def wip_count(self, project_key: str):
    #     """ワークインプログレス（WIP）数（同時進行しているチケット数）を取得する"""
    #     pass

    # def block_rate(self, project_key: str, period: str):
    #     """ブロック率（ブロックされたチケットの割合）を取得する"""
    #     pass

    # def reopen_rate(self, project_key: str, period: str):
    #     """リオープン率（完了後に再オープンされたチケットの割合）を取得する"""
    #     pass
