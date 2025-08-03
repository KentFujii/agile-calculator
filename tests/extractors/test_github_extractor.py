import os

from src.agile_calculator.extractors.github_extractor import GitHubExtractor


class TestGitHubExtractor:
    # DF  (デプロイ頻度)
    # LTFC (リードタイム)
    # CFR (変更失敗率)
    # MTTR (平均復旧時間)
    def test_extract(self):
        token = os.environ.get("GITHUB_CLASSIC_TOKEN")
        github_extractor = GitHubExtractor(token=token)
        for pull_request in github_extractor.extract(repo_name="itandi/nomad-cloud"):
            print(pull_request)
