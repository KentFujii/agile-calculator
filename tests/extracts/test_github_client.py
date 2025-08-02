import os

from src.agile_calculator.extracts.github_extract import GitHubExtract


class TestGitHubClient:
    # DF  (デプロイ頻度)
    # LTFC (リードタイム)
    # CFR (変更失敗率)
    # MTTR (平均復旧時間)
    def test_ltfc(self):
        token = os.environ.get("GITHUB_CLASSIC_TOKEN")
        extract = GitHubExtract(token=token)
        repo_name = "itandi/nomad-cloud"
        extract.ltfc(repo_name=repo_name)
