import os
import csv
from dataclasses import dataclass
from datetime import date, timedelta
from agile_calculator.records.transformed_record import TransformedRecord
from agile_calculator.tasks.loaders.csv_loader import CsvLoader

# Define the MockTransformedRecord for testing purposes
@dataclass
class MockTransformedRecord(TransformedRecord):
    name: str
    value: int
    duration: timedelta
    empty_field: None = None

    def x(self) -> date:
        """Abstract method implementation, not directly used in this test."""
        return date.today()

    def y(self) -> int | float:
        """Abstract method implementation, not directly used in this test."""
        return self.value

    def __repr__(self) -> str:
        """Abstract method implementation."""
        return f"MockTransformedRecord(name='{self.name}', value={self.value})"

def test_csv_loader_run():
    """Tests the CsvLoader with a typical set of records."""
    output_path = "test_output.csv"
    columns = ["name", "value", "duration", "empty_field", "non_existent_field"]
    records = [
        MockTransformedRecord(name="record1", value=100, duration=timedelta(seconds=50)),
        MockTransformedRecord(name="record2", value=200, duration=timedelta(minutes=2)),
    ]

    loader = CsvLoader(output_path=output_path, columns=columns)

    try:
        loader.run(records)

        with open(output_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            # Check header
            header = next(reader)
            assert header == columns

            # Check data rows
            expected_rows = [
                ["record1", "100", "50.0", "", ""],
                ["record2", "200", "120.0", "", ""],
            ]
            actual_rows = list(reader)
            assert actual_rows == expected_rows

    finally:
        # Clean up the created file
        if os.path.exists(output_path):
            os.remove(output_path)

def test_csv_loader_run_empty_records():
    """Tests the CsvLoader with an empty list of records."""
    output_path = "test_output_empty.csv"
    columns = ["header1", "header2"]
    records = []

    loader = CsvLoader(output_path=output_path, columns=columns)

    try:
        loader.run(records)

        with open(output_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            # Check header
            header = next(reader)
            assert header == columns

            # Check that there are no more rows
            try:
                next(reader)
                assert False, "CSV should not have any data rows"
            except StopIteration:
                pass  # This is expected

    finally:
        if os.path.exists(output_path):
            os.remove(output_path)
