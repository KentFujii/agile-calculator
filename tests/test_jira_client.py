# from unittest.mock import patch, MagicMock
# from src.agile_calculator.clients.jira_client import JiraClient, get_jira_client
# from jira.exceptions import JIRAError
import os

from jira import JIRA


class TestJiraClient:
    # ベロシティ
    # スプリントバーンダウン（進捗状況、残作業量の推移）
    # スプリント完了率（計画した作業のうち完了した割合）
    # ストーリー完了率（ストーリーごとの達成状況）
    # イシュースループット（一定期間内に完了したチケット数）
    # サイクルタイム（チケットが「着手」から「完了」までにかかった時間）
    # ワークインプログレス（WIP）数（同時進行しているチケット数）
    # ブロック率（ブロックされたチケットの割合）
    # リオープン率（完了後に再オープンされたチケットの割合）
    def test_velocity(self):
        server_url = os.environ.get("JIRA_SERVER_URL")
        email = os.environ.get("JIRA_USER_EMAIL")
        token = os.environ.get("JIRA_API_TOKEN")
        jira = JIRA(server_url, basic_auth=(email, token))
        allfields = jira.fields()
        name_map = {field["name"]: field["id"] for field in allfields}
        issues = jira.search_issues(
            'project = "NC" AND assignee = "k_fujii" ORDER BY created DESC'
        )
        for issue in issues:
            print("----------------------")
            print(f"key: {issue.key}")
            print(f"summary: {issue.fields.summary}")
            print(f"status: {issue.fields.status.name}")
            print(f"assignee: {issue.fields.assignee.displayName}")
            print(
                f"story points: {getattr(issue.fields, name_map['Story point estimate'])}"
            )
            print(
                f"sprints: {[sprint.name for sprint in getattr(issue.fields, name_map['Sprint'])]}"
            )
