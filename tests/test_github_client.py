import os

from github import Auth, Github
from src.agile_calculator.clients.github_client import GitHubClient


class TestGitHubClient:
    # DF  (デプロイ頻度)
    # LTFC (リードタイム)
    # CFR (変更失敗率)
    # MTTR (平均復旧時間)
    def test_ltfc(self):
        token = os.environ.get("GITHUB_CLASSIC_TOKEN")
        client = GitHubClient(token=token)
        repo_name = "itandi/nomad-cloud"
        client.ltfc(repo_name=repo_name)
