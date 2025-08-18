from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)


@pytest.fixture
def mock_github_client():
    with patch("github.Github") as mock_github_class:
        mock_client = mock_github_class.return_value
        yield mock_client


def create_mock_pull_request(
    number,
    title,
    user_login,
    created_at,
    merged_at=None,
    state="closed",
    merged=False,
    base_ref="main",
):
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


def test_run(mock_github_client):
    # Setup mock data
    now = datetime.now(timezone.utc)
    mock_prs = [
        # Should be extracted
        create_mock_pull_request(
            1, "PR 1", "user1", now - timedelta(days=1), merged_at=now, merged=True
        ),
        # Should be filtered out by user
        create_mock_pull_request(
            2, "PR 2", "user2", now - timedelta(days=2), merged_at=now, merged=True
        ),
        # Should be extracted (not merged)
        create_mock_pull_request(3, "PR 3", "user1", now - timedelta(days=3)),
        # Too old, should break the loop
        create_mock_pull_request(
            4, "PR 4", "user1", now - timedelta(days=10), merged_at=now, merged=True
        ),
    ]

    mock_repo = MagicMock()
    mock_repo.get_pulls.return_value = mock_prs
    mock_github_client.get_repo.return_value = mock_repo

    # Instantiate the extractor
    extractor = PullRequestExtractor(
        repo_name="test/repo", users=("user1",), since_days=5
    )
    # We need to manually set the client because the constructor in the test
    # doesn't call the super().__init__ where the client is created.
    # A better approach would be to mock the Github object during extractor's init.
    extractor.client = mock_github_client

    # Execute
    result = extractor.run()

    # Assertions
    assert len(result) == 2
    assert isinstance(result[0], PullRequestRecord)
    assert result[0].number == 1
    assert result[0].user == "user1"
    assert result[1].number == 3
    assert result[1].user == "user1"
    assert not result[1].merged

    mock_github_client.get_repo.assert_called_once_with("test/repo")
    mock_repo.get_pulls.assert_called_once_with(
        state="close", sort="created", direction="desc", base="main"
    )


def test_run_no_user_filter(mock_github_client):
    # Setup mock data
    now = datetime.now(timezone.utc)
    mock_prs = [
        # Should be extracted
        create_mock_pull_request(
            1, "PR 1", "user1", now - timedelta(days=1), merged_at=now, merged=True
        ),
        # Should also be extracted
        create_mock_pull_request(
            2, "PR 2", "user2", now - timedelta(days=2), merged_at=now, merged=True
        ),
    ]

    mock_repo = MagicMock()
    mock_repo.get_pulls.return_value = mock_prs
    mock_github_client.get_repo.return_value = mock_repo

    # Instantiate the extractor with no users filter
    extractor = PullRequestExtractor(repo_name="test/repo", users=(), since_days=5)
    extractor.client = mock_github_client

    # Execute
    result = extractor.run()

    # Assertions
    assert len(result) == 2
    assert result[0].number == 1
    assert result[1].number == 2


def test_run_empty_pull_requests(mock_github_client):
    # Setup mock data
    mock_repo = MagicMock()
    mock_repo.get_pulls.return_value = []
    mock_github_client.get_repo.return_value = mock_repo

    # Instantiate the extractor
    extractor = PullRequestExtractor(
        repo_name="test/repo", users=("user1",), since_days=5
    )
    extractor.client = mock_github_client

    # Execute
    result = extractor.run()

    # Assertions
    assert len(result) == 0