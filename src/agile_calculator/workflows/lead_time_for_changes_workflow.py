from ..extractors.github_extractor import GitHubExtractor
from ..loaders.matplotlib_loader import MatplotlibLoader
from ..transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)


class LeadTimeForChangesWorkflow:
    def __init__(self, github_token, repo_name, since_days=None, users=None):
        self.extractor = GitHubExtractor(github_token)
        self.repo_name = repo_name
        self.since_days = since_days
        self.users = users

    def run(self):
        # データ抽出
        pull_requests = list(self.extractor.extract(self.repo_name, users=self.users, since_days=self.since_days))
        # 変換
        records = [LeadTimeForChangesTransformer(pr).transform() for pr in pull_requests if pr.merged_at]
        # ロード
        loader = MatplotlibLoader(records)
        loader.load()
        return records
