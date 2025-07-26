# from unittest.mock import patch, MagicMock
# from src.agile_calculator.clients.jira_client import JiraClient, get_jira_client
# from jira.exceptions import JIRAError

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
        # JiraのAPIを使用してベロシティを取得するコードをここに記述
        # 例: プロジェクトのスプリント情報を取得し、完了したストーリーのポイントを集計する
        pass
