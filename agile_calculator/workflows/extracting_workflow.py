import logging

from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.workflows.transforming.pull_request_workflow import (
    PullRequestWorkflow,
)


class ExtractingWorkflow:
    def __init__(self, log_level="INFO"):
        level = getattr(logging, log_level.upper(), logging.INFO)
        logging.basicConfig(level=level)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("matplotlib").setLevel(logging.WARNING)

    def pull_requests(self, repo_name: str, users: tuple, since_days: int):
        """
        GitHubのPull Requestからデータを抽出します。

        :param repo_name: リポジトリ名 (例: 'owner/repo')
        :param users: 特定のユーザーのPull Requestのみを取得する場合、そのユーザー名 (例: 'BBKing,albert-king,freddie_king')
        :param since_days: 何日前からのデータを取得するか (例: 7)
        """
        return PullRequestWorkflow(
            extractor=PullRequestExtractor(repo_name, users, since_days),
        )
