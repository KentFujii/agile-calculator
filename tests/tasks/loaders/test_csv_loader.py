import csv
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

import pytest

from agile_calculator.records.transformed.pull_request_detail_record import (
    PullRequestDetailRecord,
)
from agile_calculator.tasks.loaders.csv_loader import CsvLoader


class TestCsvLoader:
    @pytest.fixture
    def temp_output_dir(self, tmp_path: Path):
        return tmp_path

    def test_run(self, temp_output_dir: Path):
        output_path = temp_output_dir / "test.csv"
        columns = ["number", "title", "created_at", "merged_at"]
        records = [
            PullRequestDetailRecord(
                number=1,
                title="Test PR 1",
                created_at=datetime(2023, 1, 1, 10, 0, 0),
                merged_at=datetime(2023, 1, 2, 10, 0, 0),
            ),
            PullRequestDetailRecord(
                number=2,
                title="Test PR 2",
                created_at=datetime(2023, 1, 3, 10, 0, 0),
                merged_at=None,
            ),
        ]

        loader = CsvLoader(str(output_path), columns)
        loader.run(records)

        assert os.path.exists(output_path)

        with open(output_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            assert header == columns

            row1 = next(reader)
            assert row1 == ["1", "Test PR 1", "2023-01-01 10:00:00", "2023-01-02 10:00:00"]

            row2 = next(reader)
            assert row2 == ["2", "Test PR 2", "2023-01-03 10:00:00", ""]

    def test_run_with_no_records(self, temp_output_dir: Path):
        output_path = temp_output_dir / "empty.csv"
        columns = ["number", "title"]
        records = []

        loader = CsvLoader(str(output_path), columns)
        loader.run(records)

        assert os.path.exists(output_path)

        with open(output_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            assert header == columns
            with pytest.raises(StopIteration):
                next(reader)

    def test_format_value(self):
        loader = CsvLoader("", [])
        assert loader._format_value(timedelta(days=1, hours=2)) == "93600.0"
        assert loader._format_value(None) == ""
        assert loader._format_value("test") == "test"
        assert loader._format_value(123) == "123"
        assert loader._format_value(datetime(2023, 1, 1)) == "2023-01-01 00:00:00"
