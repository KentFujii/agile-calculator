from unittest.mock import MagicMock
from agile_calculator.tasks.transformers.pull_request_details_transformer import PullRequestDetailsTransformer
from agile_calculator.records.extracted.pull_request_record import PullRequestRecord

class TestPullRequestDetailsTransformer:
    def test_pull_request_details_transformer(self):
        """
        Tests that the PullRequestDetailsTransformer correctly returns the records.
        """
        mock_records = [MagicMock(spec=PullRequestRecord)]
        transformer = PullRequestDetailsTransformer()
        result = transformer.run(mock_records)
        assert result == mock_records
