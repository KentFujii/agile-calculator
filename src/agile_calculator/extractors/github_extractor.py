from datetime import datetime, timedelta
from github import Github

from ..records.pull_request_record import PullRequestRecord
from .base_extractor import BaseExtractor


class GitHubExtractor(BaseExtractor):
    def __init__(self, token: str):
        self.token = token
        self.client = Github(self.token)

    def extract(self, repo_name: str):
        self.client.get_user().login
        repo = self.client.get_repo(repo_name)
        # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html?highlight=get_pulls#github.Repository.Repository.get_pulls
        pull_requests = repo.get_pulls(state="close", sort="created", direction="desc", base='main')
        for pr in pull_requests:
            if pr.created_at < datetime.now(pr.created_at.tzinfo) - timedelta(days=30):
                break
            print(pr)
            yield PullRequestRecord(
                number=pr.number,
                title=pr.title,
                draft=pr.draft,
                user=pr.user.login,
                created_at=pr.created_at,
                updated_at=pr.updated_at,
                merged_at=pr.merged_at,
                closed_at=pr.closed_at,
                state=pr.state,
                base_ref=pr.base.ref,
                head_ref=pr.head.ref,
                merged=pr.merged,
                merge_commit_sha=pr.merge_commit_sha,
                comments=pr.comments,
                review_comments=pr.review_comments,
                commits=pr.commits,
                additions=pr.additions,
                deletions=pr.deletions,
                changed_files=pr.changed_files,
            )
