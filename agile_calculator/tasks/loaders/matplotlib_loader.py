from datetime import datetime
from typing import Sequence

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from agile_calculator.records.transformed_record import TransformedRecord


class MatplotlibLoader:
    DEFAULT_INTERVAL_DAYS = 7
    OUTPUT_FILENAME = "matplotlib.png"

    def __init__(self, title: str, x_label: str, y_label: str) -> None:
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def run(self, records: Sequence[TransformedRecord]) -> None:
        x = [mdates.date2num(datetime.combine(record.x(), datetime.min.time())) for record in records]
        y = [record.y() for record in records]
        plt.plot_date(x, y, 'o-')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=self.DEFAULT_INTERVAL_DAYS))
        plt.xticks(rotation=45)
        plt.title(self.title)
        plt.savefig(self.OUTPUT_FILENAME, bbox_inches='tight')
        plt.close()
