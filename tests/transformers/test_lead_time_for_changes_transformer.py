import datetime

from src.agile_calculator.records.lead_time_for_changes_record import (
    LeadTimeForChangesRecord,
)
from src.agile_calculator.records.pull_request_record import PullRequestRecord
from src.agile_calculator.transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)


class TestLeadTimeForChangesTransformer:
    def test_transform_returns_correct_lead_time(self):
        created_at = datetime.datetime(2024, 1, 1, 12, 0, 0)
        merged_at = datetime.datetime(2024, 1, 2, 12, 0, 0)
        pr = PullRequestRecord(
            number=1,
            title="テストPR",
            created_at=created_at,
            merged_at=merged_at
        )
        transformer = LeadTimeForChangesTransformer(pr)
        result = transformer.transform()
        assert isinstance(result, LeadTimeForChangesRecord)
        assert result.number == 1
        assert result.title == "テストPR"
        assert result.created_at == created_at
        assert result.merged_at == merged_at
        assert result.lead_time == 86400.0  # 1日分の秒数

    def test_transform_returns_none_lead_time_if_not_merged(self):
        created_at = datetime.datetime(2024, 1, 1, 12, 0, 0)
        pr = PullRequestRecord(
            number=2,
            title="未マージPR",
            created_at=created_at,
            merged_at=None
        )
        transformer = LeadTimeForChangesTransformer(pr)
        result = transformer.transform()
        assert result.lead_time is None
