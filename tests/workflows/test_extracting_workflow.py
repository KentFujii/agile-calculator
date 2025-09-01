from unittest.mock import patch

from agile_calculator.workflows.extracting_workflow import ExtractingWorkflow


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

        # Act
        result = workflow.pull_requests(repo_name, users, since_days)

        # Assert
        mock_extractor.assert_called_once_with(repo_name, users, since_days)
        mock_workflow.assert_called_once_with(extractor=mock_extractor.return_value)
        assert result == mock_workflow.return_value
