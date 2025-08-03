from ..extractors.github_extractor import GitHubExtractor
from ..transformers.lead_time_for_changes_transformer import LeadTimeForChangesTransformer
from ..loaders.matplotlib_loader import MatplotlibLoader

class LeadTimeForChangesWorkflow:
    def __init__(self, github_token, repo_name):
        self.extractor = GitHubExtractor(github_token)
        self.repo_name = repo_name

    def run(self):
        # データ抽出
        pull_requests = list(self.extractor.extract(self.repo_name))
        # 変換
        records = [LeadTimeForChangesTransformer(pr).transform() for pr in pull_requests if pr.merged_at]
        # ロード
        loader = MatplotlibLoader(records)
        loader.load()
        return records
