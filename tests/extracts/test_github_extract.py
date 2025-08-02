import os

from src.agile_calculator.extracts.github_extract import GitHubExtract


class TestGitHubExtract:
    # DF  (デプロイ頻度)
    # LTFC (リードタイム)
    # CFR (変更失敗率)
    # MTTR (平均復旧時間)
    def test_extract(self):
        token = os.environ.get("GITHUB_CLASSIC_TOKEN")
        github_extract = GitHubExtract(token=token)
        for pull_request in github_extract.extract(repo_name="itandi/nomad-cloud"):
            print(pull_request)
