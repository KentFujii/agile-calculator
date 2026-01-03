import csv
import os
from datetime import datetime, timedelta, date
from dataclasses import dataclass

import pytest

from agile_calculator.tasks.loaders.csv_loader import CsvLoader
from agile_calculator.records.transformed_record import TransformedRecord

@dataclass
class MockDataClassRecord:
    """A mock dataclass record for testing."""
    name: str
    duration: timedelta
    completed_at: datetime
    notes: str | None

class MockPydanticRecord(TransformedRecord):
    """A mock Pydantic record for testing."""
    name: str
    value: int

    def x(self) -> date:
        return date(2023, 1, 1)

    def y(self) -> int | float:
        return self.value

class TestCsvLoader:
    @pytest.fixture
    def csv_loader(self, tmp_path):
        """Fixture to create a CsvLoader instance with a temporary output path."""
        loader = CsvLoader()
        loader.OUTPUT_PATH = os.path.join(tmp_path, "test_output.csv")
        return loader

    def test_run_with_dataclass_records(self, csv_loader):
        """Tests that the run method correctly writes dataclass records to a CSV file."""
        records = [
            MockDataClassRecord(
                name="Test 1",
                duration=timedelta(seconds=120),
                completed_at=datetime(2023, 1, 1, 12, 0, 0),
                notes="This is a note."
            ),
            MockDataClassRecord(
                name="Test 2",
                duration=timedelta(minutes=5),
                completed_at=datetime(2023, 1, 2, 15, 30, 0),
                notes=None
            )
        ]

        csv_loader.run(records)

        with open(csv_loader.OUTPUT_PATH, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            expected_header = ["name", "duration", "completed_at", "notes"]
            assert header == expected_header

            row1 = next(reader)
            assert row1 == ["Test 1", "120.0", "2023-01-01 12:00:00", "This is a note."]

            row2 = next(reader)
            assert row2 == ["Test 2", "300.0", "2023-01-02 15:30:00", ""]

    def test_run_with_pydantic_records(self, csv_loader):
        """Tests that the run method correctly writes Pydantic records to a CSV file without internal fields."""
        records = [
            MockPydanticRecord(name="Alice", value=100),
            MockPydanticRecord(name="Bob", value=200)
        ]

        csv_loader.run(records)

        with open(csv_loader.OUTPUT_PATH, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            # Check that model_ fields are NOT present
            model_fields = [c for c in header if c.startswith("model_")]
            assert len(model_fields) == 0, f"Found unexpected model_ fields: {model_fields}"

            # Check expected fields
            expected_header = ["name", "value"]
            # Note: Pydantic model_fields order is preserved
            assert header == expected_header

            row1 = next(reader)
            assert row1 == ["Alice", "100"]

            row2 = next(reader)
            assert row2 == ["Bob", "200"]

    def test_run_with_empty_records(self, csv_loader):
        """Tests that the run method creates a CSV with only a header when given no records."""
        csv_loader.run([])

        with open(csv_loader.OUTPUT_PATH, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            # TransformedRecord is a BaseModel with no fields, so header should be empty
            # confirming that we are not dumping Pydantic internals anymore.
            assert header == []

            with pytest.raises(StopIteration):
                next(reader)

    def test_format_value(self):
        """Tests the _format_value method with different data types."""
        loader = CsvLoader()

        assert loader._format_value(timedelta(days=1, seconds=30)) == "86430.0"
        assert loader._format_value(None) == ""
        assert loader._format_value("hello") == "hello"
        assert loader._format_value(123) == "123"
        assert loader._format_value(datetime(2023, 1, 1, 10, 0, 0)) == "2023-01-01 10:00:00"
