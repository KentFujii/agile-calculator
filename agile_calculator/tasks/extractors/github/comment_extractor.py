import logging
from datetime import datetime, timedelta

from agile_calculator.records.extracted.comment_record import CommentRecord
from agile_calculator.tasks.extractors.github_extractor import GitHubExtractor

class CommentExtractor(GitHubExtractor):
    def __init__(self, repo_name: str, users: tuple, since_days: int):
        super().__init__()
        self.repo_name = repo_name
        self.users = users
        self.since_days = since_days

    # def run(self) -> list[CommentRecord]:
    def run(self):
        repo = self.client.get_repo(self.repo_name)
        pull_requests = repo.get_pulls(state="close", sort="created", direction="desc", base='main')
        return list(self._extract_comment_records(pull_requests))

    def _extract_comment_records(self, pull_requests):
        for pr in pull_requests:
            if pr.created_at < datetime.now(pr.created_at.tzinfo) - timedelta(days=self.since_days):
                break
            for comment in pr.get_comments():
                if self.users and comment.user.login not in self.users:
                    continue
                record = CommentRecord(
                    id=comment.id,
                    body=comment.body,
                    user=comment.user.login,
                    created_at=comment.created_at,
                    updated_at=comment.updated_at,
                    pull_request_url=comment.pull_request_url,
                    author_association=comment.author_association,
                    url=comment.url,
                    html_url=comment.html_url,
                )
                logging.debug(record)
                yield record
