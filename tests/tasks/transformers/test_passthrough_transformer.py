from unittest.mock import MagicMock

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.tasks.transformers.passthrough_transformer import (
    PassthroughTransformer,
)


class TestPassthroughTransformer:
    def test_passthrough_transformer(self):
        """
        Tests that the PassthroughTransformer correctly returns the records.
        """
        mock_records = [MagicMock(spec=PullRequestRecord)]
        transformer = PassthroughTransformer()
        result = transformer.run(mock_records)
        assert result == mock_records
