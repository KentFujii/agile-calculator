from unittest.mock import patch, MagicMock
from agile_calculator.workflows.extracting_workflow import ExtractingWorkflow
from agile_calculator.workflows.transforming.pull_request_workflow import PullRequestWorkflow
from agile_calculator.tasks.extractors.github.pull_request_extractor import PullRequestExtractor
from agile_calculator.workflows.transforming.comment_workflow import CommentWorkflow
from agile_calculator.tasks.extractors.github.comment_extractor import CommentExtractor


class TestExtractingWorkflow:
    @patch("agile_calculator.workflows.extracting_workflow.PullRequestExtractor", autospec=True)
    @patch("agile_calculator.workflows.extracting_workflow.PullRequestWorkflow", autospec=True)
    def test_pull_requests(self, mock_workflow, mock_extractor):
        """
        Tests that the pull_requests method returns a PullRequestWorkflow
        with a correctly configured PullRequestExtractor.
        """
        # Arrange
        workflow = ExtractingWorkflow()
        repo_name = "test/repo"
        users = ("user1", "user2")
        since_days = 7
        base_branch = "main"

        # Act
        result = workflow.pull_requests(repo_name, users, since_days, base_branch)

        # Assert
        mock_extractor.assert_called_once_with(repo_name, users, since_days, base_branch)
        mock_workflow.assert_called_once_with(extractor=mock_extractor.return_value)
        assert result == mock_workflow.return_value

    @patch("agile_calculator.workflows.extracting_workflow.CommentExtractor", autospec=True)
    @patch("agile_calculator.workflows.extracting_workflow.CommentWorkflow", autospec=True)
    def test_comments(self, mock_workflow, mock_extractor):
        """
        Tests that the comments method returns a CommentWorkflow
        with a correctly configured CommentExtractor.
        """
        # Arrange
        workflow = ExtractingWorkflow()
        repo_name = "test/repo"
        users = ("user1", "user2")
        since_days = 7
        base_branch = "main"

        # Act
        result = workflow.comments(repo_name, users, since_days, base_branch)

        # Assert
        mock_extractor.assert_called_once_with(repo_name, users, since_days, base_branch)
        mock_workflow.assert_called_once_with(extractor=mock_extractor.return_value)
        assert result == mock_workflow.return_value
