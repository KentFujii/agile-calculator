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

    def __init__(self, title):
        self.title = title

    def run(self, records) -> None:
        # merged_dateごとにlead_time_secondsの平均を算出
        merged_dict = defaultdict(list)
        for r in records:
            merged_dict[r.merged_date].append(r.lead_time_seconds)
        # 日付でソートし、平均値を算出
        sorted_items = sorted((k, mean(v)) for k, v in merged_dict.items())
        x = [k for k, v in sorted_items]
        y = [v for k, v in sorted_items]  # 秒のまま（平均）
        plt.plot(x, y, marker='o')
        plt.xlabel(self.X_LABEL)
        plt.ylabel(self.Y_LABEL)
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=self.DEFAULT_INTERVAL_DAYS))
        plt.xticks(rotation=45)
        plt.gca().yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, pos: f'{x/self.SECONDS_PER_HOUR:.1f}')
        )
        plt.title(self.title)
        plt.savefig(self.OUTPUT_FILENAME, bbox_inches='tight')
        plt.close()
