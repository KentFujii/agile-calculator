from unittest.mock import MagicMock
from agile_calculator.tasks.transformers.passthrough_transformer import PassthroughTransformer
from agile_calculator.records.extracted.pull_request_record import PullRequestRecord

class TestPassthroughTransformer:
    def test_passthrough_transformer(self):
        """
        Tests that the PassthroughTransformer correctly stores the records.
        """
        mock_records = MagicMock(spec=PullRequestRecord)
        transformer = PassthroughTransformer(mock_records)
        assert transformer.records == mock_records
