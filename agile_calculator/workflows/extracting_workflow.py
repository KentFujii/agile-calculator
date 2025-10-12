import logging

from agile_calculator.tasks.extractors.jira.issue_extractor import (
    IssueExtractor,
)
from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.extractors.github.comment_extractor import (
    CommentExtractor,
)
from agile_calculator.workflows.transforming.pull_request_workflow import (
    PullRequestWorkflow,
)
from agile_calculator.workflows.transforming.comment_workflow import (
    CommentWorkflow,
)


class ExtractingWorkflow:
    def __init__(self, log_level: str = "INFO") -> None:
        level = getattr(logging, log_level.upper(), logging.INFO)
        logging.basicConfig(level=level)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("matplotlib").setLevel(logging.WARNING)

    def jira_issues(self, project_key: str) -> IssueExtractor:
        """
        JiraのIssueからデータを抽出します。

        :param project_key: プロジェクトキー (例: 'PROJECT-1')
        """
        issue_extractor = IssueExtractor()
        for issue in issue_extractor.run(project_key):
            logging.info(f"Extracted issue: {issue.key} - {issue.summary} - {issue.sprint}")

    def pull_requests(self, repo_name: str, users: tuple, since_days: int) -> PullRequestWorkflow:
        """
        GitHubのPull Requestからデータを抽出します。

        :param repo_name: リポジトリ名 (例: 'owner/repo')
        :param users: 特定のユーザーのPull Requestのみを取得する場合、そのユーザー名 (例: 'BBKing,albert-king,freddie_king')
        :param since_days: 何日前からのデータを取得するか (例: 7)
        """
        return PullRequestWorkflow(
            extractor=PullRequestExtractor(repo_name, users, since_days),
        )

    def comments(self, repo_name: str, users: tuple, since_days: int) -> CommentWorkflow:
        """
        GitHubのCommentからデータを抽出します。

        :param repo_name: リポジトリ名 (例: 'owner/repo')
        :param users: 特定のユーザーのCommentのみを取得する場合、そのユーザー名 (例: 'BBKing,albert-king,freddie_king')
        :param since_days: 何日前からのデータを取得するか (例: 7)
        """
        return CommentWorkflow(
            extractor=CommentExtractor(repo_name, users, since_days),
        )
