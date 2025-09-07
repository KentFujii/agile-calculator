import csv
import os
from datetime import timedelta
from unittest.mock import MagicMock

import pytest

from agile_calculator.records.transformed_record import TransformedRecord
from agile_calculator.tasks.loaders.csv_loader import CsvLoader


@pytest.fixture
def sample_records():
    record1 = MagicMock(spec=TransformedRecord)
    record1.name = "test1"
    record1.duration = timedelta(seconds=100)
    record1.description = "desc1"
    record1.optional = None

    record2 = MagicMock(spec=TransformedRecord)
    record2.name = "test2"
    record2.duration = timedelta(seconds=200)
    record2.description = "desc2"
    record2.optional = "value2"

    return [record1, record2]

def test_csv_loader_run(tmpdir, sample_records):
    output_path = os.path.join(tmpdir, "output.csv")
    columns = ["name", "duration", "description", "optional"]
    loader = CsvLoader(output_path, columns)
    loader.run(sample_records)

    assert os.path.exists(output_path)

    with open(output_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == columns
    assert rows[1] == ["test1", "100.0", "desc1", ""]
    assert rows[2] == ["test2", "200.0", "desc2", "value2"]

def test_csv_loader_run_with_no_records(tmpdir):
    output_path = os.path.join(tmpdir, "output.csv")
    columns = ["name", "duration"]
    loader = CsvLoader(output_path, columns)
    loader.run([])

    assert os.path.exists(output_path)

    with open(output_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == columns
    assert len(rows) == 1
