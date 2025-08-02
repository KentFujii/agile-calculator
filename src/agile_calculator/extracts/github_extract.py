from github import Github

from .base_extract import BaseExtract


class GitHubExtract(BaseExtract):
    def __init__(self, token: str):
        self.token = token
        self.client = Github(self.token)

    def to_pandas(self, repo_name: str) -> list:
        return []

    def to_csv(self, repo_name: str) -> list:
        return []

    def df(self, repo_name: str):
        """デプロイ頻度 (DF) を取得する"""
        pass

    def ltfc(self, repo_name: str):
        """リードタイム (LTFC) を取得する"""
        self.client.get_user().login
        repo = self.client.get_repo(repo_name)
        pulls = repo.get_pulls(state="close", sort="created")
        for pr in pulls:
            print("----------------------")
            print(f"number: {pr.number}")
            print(f"title: {pr.title}")
            print(f"draft: {pr.draft}")
            print(f"user: {pr.user.login}")
            print(f"created_at: {pr.created_at}")
            print(f"updated_at: {pr.updated_at}")
            print(f"merged_at: {pr.merged_at}")
            print(f"closed_at: {pr.closed_at}")
            print(f"state: {pr.state}")
            print(f"base_ref: {pr.base.ref}")
            print(f"head_ref: {pr.head.ref}")
            print(f"merged: {pr.merged}")
            print(f"merge_commit_sha: {pr.merge_commit_sha}")
            print(f"comments: {pr.comments}")
            print(f"review_comments: {pr.review_comments}")
            print(f"commits: {pr.commits}")
            print(f"additions: {pr.additions}")
            print(f"deletions: {pr.deletions}")
            print(f"changed_files: {pr.changed_files}")
            # print(f"labels: {[label.name for label in pr.labels]}")
            # print(f"assignees: {[assignee.login for assignee in pr.assignees]}")

    def cfr(self, repo_name: str):
        """変更失敗率 (CFR) を取得する"""
        pass

    def mttr(self, repo_name: str):
        """平均復旧時間 (MTTR) を取得する"""
        pass
