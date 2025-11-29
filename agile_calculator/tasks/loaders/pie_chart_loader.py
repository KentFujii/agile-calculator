from typing import Sequence

import matplotlib.pyplot as plt

from agile_calculator.records.transformed.approval_count_record import (
    ApprovalCountRecord,
)
from agile_calculator.tasks.loaders.base_loader import BaseLoader


class PieChartLoader(BaseLoader):
    OUTPUT_FILENAME = "loader.png"

    def __init__(self, title: str) -> None:
        self.title = title

    def run(self, records: Sequence[ApprovalCountRecord]) -> None:
        if not records:
             return

        labels = [r.user for r in records]
        sizes = [r.count for r in records]

        plt.figure(figsize=(10, 7))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(self.title)
        plt.savefig(self.OUTPUT_FILENAME, bbox_inches='tight')
        plt.close()
