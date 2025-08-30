from datetime import datetime

from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_detail_record import (
    PullRequestDetailRecord,
)
from agile_calculator.tasks.transformers.passthrough_transformer import (
    PassthroughTransformer,
)


class TestPassthroughTransformer:
    def test_run(self):
        records = [
            PullRequestRecord(
                number=1,
                title="Test PR 1",
                created_at=datetime(2023, 1, 1, 10, 0, 0),
                state="closed",
            ),
            PullRequestRecord(
                number=2,
                title="Test PR 2",
                created_at=datetime(2023, 1, 2, 10, 0, 0),
                state="open",
            ),
        ]

        transformer = PassthroughTransformer()
        result = transformer.run(records)

        assert len(result) == 2
        assert all(isinstance(r, PullRequestDetailRecord) for r in result)

        assert result[0].number == 1
        assert result[0].title == "Test PR 1"
        assert result[0].created_at == datetime(2023, 1, 1, 10, 0, 0)
        assert result[0].state == "closed"

        assert result[1].number == 2
        assert result[1].title == "Test PR 2"
        assert result[1].created_at == datetime(2023, 1, 2, 10, 0, 0)
        assert result[1].state == "open"

    def test_run_with_empty_list(self):
        transformer = PassthroughTransformer()
        result = transformer.run([])
        assert len(result) == 0
