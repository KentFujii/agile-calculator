import pytest
import os
from github import Auth
from github import Github

class TestGitHubClient:
    # DF  (デプロイ頻度)
    # LTFC (リードタイム)
    # CFR (変更失敗率)
    # MTTR (平均復旧時間)
    def test_ltfc(self):
        token = os.environ.get("GITHUB_CLASSIC_TOKEN")
        auth = Auth.Token(token)
        g = Github(auth=auth)
        g.get_user().login
        repo = g.get_repo("itandi/nomad-cloud")
        pulls = repo.get_pulls(state='close', sort='created')
        for pr in pulls:
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
            print(f"labels: {[label.name for label in pr.labels]}")
            print(f"assignees: {[assignee.login for assignee in pr.assignees]}")
