import logging

from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.workflows.transforming.pull_request_workflow import (
    PullRequestWorkflow,
)


class ExtractingWorkflow:
    def __init__(self, log_level: str = "INFO") -> None:
        level = getattr(logging, log_level.upper(), logging.INFO)
        logging.basicConfig(level=level)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("matplotlib").setLevel(logging.WARNING)

    def pull_requests(
        self, repo_name: str, users: tuple, since_days: int, base_branch: str = "main"
    ) -> PullRequestWorkflow:
        """
        GitHubのPull Requestからデータを抽出します。

        :param repo_name: リポジトリ名 (例: 'owner/repo')
        :param users: 特定のユーザーのPull Requestのみを取得する場合、そのユーザー名 (例: 'BBKing,albert-king,freddie_king')
        :param since_days: 何日前からのデータを取得するか (例: 7)
        :param base_branch: PRのマージ先ベースブランチ (例: 'main')
        """
        return PullRequestWorkflow(
            extractor=PullRequestExtractor(repo_name, users, since_days, base_branch),
        )
