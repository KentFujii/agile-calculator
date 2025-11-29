from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)

@pytest.fixture
def mock_github_client(mocker):
    """Mocks the Github client used by the PullRequestExtractor."""
    mock_github_class = mocker.patch(
        "agile_calculator.tasks.extractors.github_extractor.Github"
    )
    mock_client = mock_github_class.return_value
    return mock_client

class TestPullRequestExtractor:
    def test_extracts_merged_pull_request_in_date_range(self, mock_github_client, mock_pull_request_factory):
        """Tests that a basic, merged PR within the date range is extracted."""
        now = datetime.now(timezone.utc)
        mock_pr = mock_pull_request_factory(
            1, "PR 1", "user1", now - timedelta(days=2), merged_at=now - timedelta(days=1), merged=True
        )
        mock_repo = MagicMock()
        mock_repo.get_pulls.return_value = [mock_pr]
        mock_github_client.get_repo.return_value = mock_repo

        extractor = PullRequestExtractor(repo_name="test/repo", users=("user1",), since_days=5)
        result = extractor.run()

        assert len(result) == 1
        assert result[0].number == 1

    def test_filters_by_user(self, mock_github_client, mock_pull_request_factory):
        """Tests that PRs from users not in the 'users' list are filtered out."""
        now = datetime.now(timezone.utc)
        mock_pr_user1 = mock_pull_request_factory(1, "PR 1", "user1", now - timedelta(days=1), merged=True)
        mock_pr_user2 = mock_pull_request_factory(2, "PR 2", "user2", now - timedelta(days=1), merged=True)
        mock_repo = MagicMock()
        mock_repo.get_pulls.return_value = [mock_pr_user1, mock_pr_user2]
        mock_github_client.get_repo.return_value = mock_repo

        extractor = PullRequestExtractor(repo_name="test/repo", users=("user1",), since_days=5)
        result = extractor.run()

        assert len(result) == 1
        assert result[0].user == "user1"

    def test_stops_fetching_when_pr_is_too_old(self, mock_github_client, mock_pull_request_factory):
        """Tests that the extractor stops fetching when it encounters a PR older than 'since_days'."""
        now = datetime.now(timezone.utc)
        mock_prs = [
            mock_pull_request_factory(1, "PR 1", "user1", now - timedelta(days=1)), # Should be included
            mock_pull_request_factory(2, "PR 2", "user1", now - timedelta(days=10)), # Should cause loop to break
            mock_pull_request_factory(3, "PR 3", "user1", now - timedelta(days=11)), # Should not be processed
        ]
        mock_repo = MagicMock()
        mock_repo.get_pulls.return_value = mock_prs
        mock_github_client.get_repo.return_value = mock_repo

        extractor = PullRequestExtractor(repo_name="test/repo", users=("user1",), since_days=5)
        result = extractor.run()

        assert len(result) == 1
        assert result[0].number == 1

    def test_extracts_unmerged_pull_request(self, mock_github_client, mock_pull_request_factory):
        """Tests that a non-merged (but closed) PR is still extracted."""
        now = datetime.now(timezone.utc)
        mock_pr = mock_pull_request_factory(1, "Unmerged PR", "user1", now - timedelta(days=2), merged=False)
        mock_repo = MagicMock()
        mock_repo.get_pulls.return_value = [mock_pr]
        mock_github_client.get_repo.return_value = mock_repo

        extractor = PullRequestExtractor(repo_name="test/repo", users=("user1",), since_days=5)
        result = extractor.run()

        assert len(result) == 1
        assert result[0].number == 1
        assert not result[0].merged


    def test_run_no_user_filter(self, mock_github_client, mock_pull_request_factory):
        # Setup mock data
        now = datetime.now(timezone.utc)
        mock_prs = [
            # Should be extracted
            mock_pull_request_factory(
                1, "PR 1", "user1", now - timedelta(days=1), merged_at=now, merged=True
            ),
            # Should also be extracted
            mock_pull_request_factory(
                2, "PR 2", "user2", now - timedelta(days=2), merged_at=now, merged=True
            ),
        ]

        mock_repo = MagicMock()
        mock_repo.get_pulls.return_value = mock_prs
        mock_github_client.get_repo.return_value = mock_repo

        # Instantiate the extractor with no users filter
        extractor = PullRequestExtractor(repo_name="test/repo", users=(), since_days=5)

        # Execute
        result = extractor.run()

        # Assertions
        assert len(result) == 2
        assert result[0].number == 1
        assert result[1].number == 2


    def test_run_empty_pull_requests(self, mock_github_client):
        # Setup mock data
        mock_repo = MagicMock()
        mock_repo.get_pulls.return_value = []
        mock_github_client.get_repo.return_value = mock_repo

        # Instantiate the extractor
        extractor = PullRequestExtractor(
            repo_name="test/repo", users=("user1",), since_days=5
        )

        # Execute
        result = extractor.run()

        # Assertions
        assert len(result) == 0

    def test_extracts_reviews(self, mock_github_client, mock_pull_request_factory):
        """Tests that reviews are correctly extracted."""
        now = datetime.now(timezone.utc)
        reviews_data = [
            {"user": "reviewer1", "state": "APPROVED"},
            {"user": "reviewer2", "state": "CHANGES_REQUESTED"},
        ]
        mock_pr = mock_pull_request_factory(
            1, "PR 1", "user1", now - timedelta(days=1), merged_at=now, merged=True, reviews=reviews_data
        )
        mock_repo = MagicMock()
        mock_repo.get_pulls.return_value = [mock_pr]
        mock_github_client.get_repo.return_value = mock_repo

        extractor = PullRequestExtractor(repo_name="test/repo", users=("user1",), since_days=5)
        result = extractor.run()

        assert len(result) == 1
        assert len(result[0].reviews) == 2
        assert result[0].reviews[0].user == "reviewer1"
        assert result[0].reviews[0].state == "APPROVED"
        assert result[0].reviews[1].user == "reviewer2"
        assert result[0].reviews[1].state == "CHANGES_REQUESTED"