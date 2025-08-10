import os

from github import Github

from ..extractors.github.pull_request_extractor import PullRequestExtractor



# https://g.co/gemini/share/c89f203b9c7a
class GitHubInitializer:
    def __init__(self):
        self.token = os.environ.get("GITHUB_CLASSIC_TOKEN")
        self.client = Github(self.token)

    def pull_request(self):
        """
        GitHubのPull Requestからデータを抽出します。

        :param repo_name: リポジトリ名 (例: 'owner/repo')
        :param since_days: 何日前からのデータを取得するか
        :param users: 特定のユーザーのPull Requestのみを取得する場合、そのユーザー名
        """
        return PullRequestExtractor(initializer=self)


