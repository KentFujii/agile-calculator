from datetime import datetime, timedelta

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.tasks.extractors.github_extractor import GitHubExtractor


class PullRequestExtractor(GitHubExtractor):
    def __init__(self, repo_name: str, users: tuple, since_days: int):
        super().__init__()
        self.repo_name = repo_name
        self.users = users
        self.since_days = since_days

    # TODO: .github.PullRequestExtractorに継承させる
    # https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#get-a-pull-request
    def run(self):
        repo = self.client.get_repo(self.repo_name)
        pull_requests = repo.get_pulls(state="close", sort="created", direction="desc", base='main')
        return list(self._extract_request_records(pull_requests))

    def _extract_request_records(self, pull_requests):
        for pr in pull_requests:
            if self.users and pr.user.login not in self.users:
                continue
            if pr.created_at < datetime.now(pr.created_at.tzinfo) - timedelta(days=self.since_days):
                break
            # TODO: 後でloggerに出力することを検討
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
