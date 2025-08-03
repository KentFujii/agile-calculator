import os

from src.agile_calculator.extractors.jira_extractor import JiraExtractor


class TestJiraExtractor:
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
        email = os.environ.get("JIRA_EMAIL")
        token = os.environ.get("JIRA_TOKEN")
        assignee = "k_fujii"
        project_key = "NC"
        jira_extractor = JiraExtractor(server=server_url, email=email, token=token)
        for issue in jira_extractor.extract(project_key=project_key, assignee=assignee):
            print(issue)
