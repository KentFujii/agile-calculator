import matplotlib.dates as mdates
import matplotlib.pyplot as plt


class MatplotlibLoader:
    DEFAULT_INTERVAL_DAYS = 7
    OUTPUT_FILENAME = "figure.png"

    def __init__(self, title, x_label, y_label):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def run(self, records) -> None:
        x = [record.x() for record in records]
        y = [record.y() for record in records]
        plt.plot(x, y, marker='o')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=self.DEFAULT_INTERVAL_DAYS))
        plt.xticks(rotation=45)
        plt.title(self.title)
        plt.savefig(self.OUTPUT_FILENAME, bbox_inches='tight')
        plt.close()
