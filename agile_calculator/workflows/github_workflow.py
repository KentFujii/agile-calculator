from ..extractors.github.pull_request_extractor import PullRequestExtractor
from ..transformers.lead_time_for_changes_transformer import LeadTimeForChangesTransformer
from ..loaders.matplotlib_loader import MatplotlibLoader

class GitHubWorkflow:
    def pull_request(self, repo_name: str, users: tuple, since_days: int):
        """
        GitHubのPull Requestからデータを抽出します。

        :param repo_name: リポジトリ名 (例: 'owner/repo')
        :param users: 特定のユーザーのPull Requestのみを取得する場合、そのユーザー名 (例: 'A,B,C')
        :param since_days: 何日前からのデータを取得するか
        """
        return PullRequestWorkflow(
            extractor=PullRequestExtractor(repo_name, users, since_days)
        )

class PullRequestWorkflow:
    def __init__(self, extractor):
        self._extractor = extractor

    def lead_time_for_changes(self):
        return LeadTimeForChangesWorkflow(
            extractor=self._extractor,
            transformer=LeadTimeForChangesTransformer()
        )

class LeadTimeForChangesWorkflow:
    def __init__(self, extractor, transformer):
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self):
        MatplotlibLoader().run(
            self._transformer.run(
                self._extractor.run()
            )
        )

