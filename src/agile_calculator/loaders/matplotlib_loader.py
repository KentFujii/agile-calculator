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
        x = list(merged_dict.keys())
        y = list(merged_dict.values())
        plt.plot(x, y, marker='o')
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.xlabel('Merged Date')
        plt.ylabel('Lead Time (seconds)')
        plt.title('Lead Time for Changes per Merged Date')
        plt.savefig("lead_time_chart.png")
        plt.close()
