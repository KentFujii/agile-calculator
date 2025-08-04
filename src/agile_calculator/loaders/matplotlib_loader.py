from collections import defaultdict
from statistics import mean

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class MatplotlibLoader:
    DEFAULT_INTERVAL_DAYS = 7
    SECONDS_PER_HOUR = 3600
    OUTPUT_FILENAME = "lead_time_chart.png"
    X_LABEL = "Merged Date"
    Y_LABEL = "Lead Time (hours)"
    TITLE = "Lead Time for Changes per Merged Date"

    def __init__(self, records):
        """
        records: List[LeadTimeForChangesRecord]
        """
        self.records = records

    def load(self):
        # merged_dateごとにlead_time_secondsの平均を算出
        merged_dict = defaultdict(list)
        for r in self.records:
            merged_dict[r.merged_date].append(r.lead_time_seconds)
        # 日付でソートし、平均値を算出
        sorted_items = sorted((k, mean(v)) for k, v in merged_dict.items())
        x = [k for k, v in sorted_items]
        y = [v for k, v in sorted_items]  # 秒のまま（平均）
        plt.plot(x, y, marker='o')
        plt.xlabel(self.X_LABEL)
        plt.ylabel(self.Y_LABEL)
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=self.DEFAULT_INTERVAL_DAYS))
        plt.gca().yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, pos: f'{x/self.SECONDS_PER_HOUR:.1f}')
        )
        plt.title(self.TITLE)
        plt.savefig(self.OUTPUT_FILENAME)
        plt.close()
