from collections import defaultdict

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class MatplotlibLoader:
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
        y = [v for k, v in sorted_items]
        plt.plot(x, y, marker='o')
        plt.xlabel('Merged Date')
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
        plt.ylabel('Lead Time (seconds)')
        plt.title('Lead Time for Changes per Merged Date')
        plt.savefig("lead_time_chart.png")
        plt.close()
