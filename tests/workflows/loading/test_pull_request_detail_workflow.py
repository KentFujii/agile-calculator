from unittest.mock import MagicMock, patch

from agile_calculator.workflows.loading.pull_request_detail_workflow import (
    PullRequestDetailWorkflow,
)


class TestPullRequestDetailWorkflow:
    @patch("agile_calculator.workflows.loading.pull_request_detail_workflow.CsvLoader", autospec=True)
    def test_csv(self, mock_csv_loader):
        # Arrange
        mock_extractor = MagicMock()
        mock_transformer = MagicMock()

        extractor_output = [MagicMock()]
        transformer_output = [MagicMock()]

        mock_extractor.run.return_value = extractor_output
        mock_transformer.run.return_value = transformer_output

        workflow = PullRequestDetailWorkflow(mock_extractor, mock_transformer)

        output_path = "/tmp/test.csv"
        columns = ["col1", "col2"]

        # Act
        workflow.csv(output_path, columns)

        # Assert
        mock_extractor.run.assert_called_once()
        mock_transformer.run.assert_called_once_with(extractor_output)
        mock_csv_loader.assert_called_once_with(output_path, columns)
        mock_csv_loader.return_value.run.assert_called_once_with(transformer_output)
