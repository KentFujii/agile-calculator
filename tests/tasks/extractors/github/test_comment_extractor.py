from datetime import datetime, timedelta
from unittest.mock import MagicMock
import pytest

from agile_calculator.tasks.extractors.github.comment_extractor import CommentExtractor
from agile_calculator.records.extracted.comment_record import CommentRecord

@pytest.fixture
def mock_github_client():
    """Mocks the GitHub client and its chain of calls."""
    mock_client = MagicMock()

    mock_comment1 = MagicMock()
    mock_comment1.id = 1
    mock_comment1.body = "This is a comment"
    mock_comment1.user.login = "test_user"
    mock_comment1.created_at = datetime.now()
    mock_comment1.updated_at = datetime.now()
    mock_comment1.pull_request_url = "https://github.com/test/repo/pull/1"
    mock_comment1.author_association = "OWNER"
    mock_comment1.url = "https://api.github.com/repos/test/repo/pulls/comments/1"
    mock_comment1.html_url = "https://github.com/test/repo/pull/1#discussion_r1"

    mock_comment2 = MagicMock()
    mock_comment2.id = 2
    mock_comment2.body = "Another comment"
    mock_comment2.user.login = "another_user"
    mock_comment2.created_at = datetime.now() - timedelta(days=2)
    mock_comment2.updated_at = datetime.now() - timedelta(days=2)
    mock_comment2.pull_request_url = "https://github.com/test/repo/pull/1"
    mock_comment2.author_association = "CONTRIBUTOR"
    mock_comment2.url = "https://api.github.com/repos/test/repo/pulls/comments/2"
    mock_comment2.html_url = "https://github.com/test/repo/pull/1#discussion_r2"

    mock_pr1 = MagicMock()
    mock_pr1.created_at = datetime.now()
    mock_pr1.get_comments.return_value = [mock_comment1, mock_comment2]

    mock_pr2 = MagicMock()
    mock_pr2.created_at = datetime.now() - timedelta(days=10)
    mock_pr2.get_comments.return_value = []

    mock_repo = MagicMock()
    mock_repo.get_pulls.return_value = [mock_pr1, mock_pr2]
    mock_client.get_repo.return_value = mock_repo
    return mock_client

def test_run_returns_comment_records(mocker, mock_github_client):
    """Tests that the run method returns a list of CommentRecord objects."""
    mocker.patch('agile_calculator.tasks.extractors.github_extractor.Github', return_value=mock_github_client)

    extractor = CommentExtractor(repo_name="test/repo", users=("test_user", "another_user"), since_days=5)
    result = extractor.run()

    assert len(result) == 2
    assert all(isinstance(record, CommentRecord) for record in result)
    assert result[0].user == "test_user"
    assert result[1].user == "another_user"

def test_run_filters_by_since_days(mocker, mock_github_client):
    """Tests that the run method filters pull requests by since_days."""
    mocker.patch('agile_calculator.tasks.extractors.github_extractor.Github', return_value=mock_github_client)

    extractor = CommentExtractor(repo_name="test/repo", users=(), since_days=5)
    result = extractor.run()

    # The second PR is older than 5 days, so it should be ignored.
    assert len(result) == 2

    extractor_long_duration = CommentExtractor(repo_name="test/repo", users=(), since_days=20)
    result_long_duration = extractor_long_duration.run()
    assert len(result_long_duration) == 2 # mock_pr2 has no comments

def test_run_filters_by_users(mocker, mock_github_client):
    """Tests that the run method filters comments by users."""
    mocker.patch('agile_calculator.tasks.extractors.github_extractor.Github', return_value=mock_github_client)

    extractor = CommentExtractor(repo_name="test/repo", users=("test_user",), since_days=5)
    result = extractor.run()

    assert len(result) == 1
    assert result[0].user == "test_user"

def test_run_handles_no_pull_requests(mocker, mock_github_client):
    """Tests that the run method returns an empty list when there are no pull requests."""
    mock_github_client.get_repo.return_value.get_pulls.return_value = []
    mocker.patch('agile_calculator.tasks.extractors.github_extractor.Github', return_value=mock_github_client)

    extractor = CommentExtractor(repo_name="test/repo", users=(), since_days=5)
    result = extractor.run()

    assert len(result) == 0

def test_run_handles_no_comments(mocker, mock_github_client):
    """Tests that the run method returns an empty list when there are no comments."""
    mock_pr = MagicMock()
    mock_pr.created_at = datetime.now()
    mock_pr.get_comments.return_value = []
    mock_github_client.get_repo.return_value.get_pulls.return_value = [mock_pr]
    mocker.patch('agile_calculator.tasks.extractors.github_extractor.Github', return_value=mock_github_client)

    extractor = CommentExtractor(repo_name="test/repo", users=(), since_days=5)
    result = extractor.run()

    assert len(result) == 0
