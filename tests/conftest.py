from datetime import timedelta
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_pull_request_factory():
    """
    Fixture that returns a factory function for creating mock pull requests.
    This allows creating multiple, customized mock PRs within a single test.
    """

    def _create_mock_pull_request(
        number,
        title,
        user_login,
        created_at,
        merged_at=None,
        state="closed",
        merged=False,
        base_ref="main",
    ):
        """Helper function to create a mock pull request with specified attributes."""
        mock_pr = MagicMock()
        mock_pr.number = number
        mock_pr.title = title
        mock_pr.draft = False
        mock_pr.user.login = user_login
        mock_pr.created_at = created_at
        mock_pr.updated_at = created_at + timedelta(hours=1)
        mock_pr.merged_at = merged_at
        mock_pr.closed_at = merged_at or (created_at + timedelta(hours=2))
        mock_pr.state = state
        mock_pr.base.ref = base_ref
        mock_pr.head.ref = f"feature/branch-{number}"
        mock_pr.merged = merged
        mock_pr.merge_commit_sha = "sha" if merged else None
        mock_pr.comments = 1
        mock_pr.review_comments = 2
        mock_pr.commits = 3
        mock_pr.additions = 100
        mock_pr.deletions = 50
        mock_pr.changed_files = 5
        return mock_pr

    return _create_mock_pull_request
