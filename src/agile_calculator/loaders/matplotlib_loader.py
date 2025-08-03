from collections import defaultdict

import matplotlib.pyplot as plt

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
            if r.merged_at is not None and r.lead_time_seconds is not None:
                merged_dict[r.merged_at] += r.lead_time_seconds
        x = list(merged_dict.keys())
        y = list(merged_dict.values())
        plt.plot(x, y, marker='o')
        plt.xlabel('Merged At')
        plt.ylabel('Lead Time (seconds)')
        plt.title('Lead Time for Changes per Merged Date')
        plt.savefig("lead_time_chart.png")
        plt.close()
