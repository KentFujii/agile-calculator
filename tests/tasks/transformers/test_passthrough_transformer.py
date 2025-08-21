from unittest.mock import MagicMock
from agile_calculator.tasks.transformers.passthrough_transformer import PassThroughTransformer
from agile_calculator.records.extracted.pull_request_record import PullRequestRecord

class TestPassThroughTransformer:
    def test_passthrough_transformer(self):
        """
        Tests that the PassthroughTransformer correctly stores the records.
        """
        mock_records = MagicMock(spec=PullRequestRecord)
        transformer = PassThroughTransformer(mock_records)
        assert transformer.records == mock_records
