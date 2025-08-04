from collections import defaultdict

import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt



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
        # merged_atごとにlead_time_secondsを合計
        merged_dict = defaultdict(float)
        for r in self.records:
            merged_dict[r.merged_date] += r.lead_time_seconds
        # 日付でソート
        sorted_items = sorted(merged_dict.items())
        x = [k for k, v in sorted_items]
        y = [v for k, v in sorted_items]  # 秒のまま
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
