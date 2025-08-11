import datetime

import pytest

from agile_calculator.records.transformed.lead_time_for_changes_record import (
    LeadTimeForChangesRecord,
)
from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader


class TestMatplotlibLoader:
    @pytest.mark.skip(reason="Not implemented")
    def test_matplotlib_loader_sum(self, monkeypatch):
        # テスト用データ: merged_atが重複するケース
        records = [
            LeadTimeForChangesRecord(number=1, title='A', merged_date=datetime.date(2023, 1, 1), lead_time_seconds=100),
            LeadTimeForChangesRecord(number=2, title='B', merged_date=datetime.date(2023, 1, 1), lead_time_seconds=200),
            LeadTimeForChangesRecord(number=3, title='C', merged_date=datetime.date(2023, 1, 2), lead_time_seconds=300),
            LeadTimeForChangesRecord(number=4, title='D', merged_date=datetime.date(2023, 1, 2), lead_time_seconds=400),
            LeadTimeForChangesRecord(number=5, title='E', merged_date=datetime.date(2023, 1, 3), lead_time_seconds=500),
        ]
        loader = MatplotlibLoader(records)
        loader.load()
