from datetime import date

import pytest

from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader


class TestMatplotlibLoader:
    @pytest.fixture
    def mock_plt(self, mocker):
        return mocker.patch("agile_calculator.tasks.loaders.matplotlib_loader.plt")

    @pytest.fixture
    def mock_mdates(self, mocker):
        return mocker.patch("agile_calculator.tasks.loaders.matplotlib_loader.mdates")

    def test_run(self, mock_plt, mock_mdates):
        # Setup mock data
        class MockRecord:
            def __init__(self, x_val, y_val):
                self._x = x_val
                self._y = y_val

            def x(self):
                return self._x

            def y(self):
                return self._y

        records = [
            MockRecord(date(2023, 1, 1), 10),
            MockRecord(date(2023, 1, 2), 20),
        ]
        y_data = [record.y() for record in records]

        # Instantiate the loader
        title = "Test Title"
        x_label = "Test X Label"
        y_label = "Test Y Label"
        loader = MatplotlibLoader(title, x_label, y_label)

        # Execute
        loader.run(records)

        # Assertions for plt calls
        mock_mdates.date2num.assert_called()
        x_date_nums = [mock_mdates.date2num.return_value for _ in records]
        mock_plt.plot_date.assert_called_once_with(x_date_nums, y_data, 'o-')
        mock_plt.xlabel.assert_called_once_with(x_label)
        mock_plt.ylabel.assert_called_once_with(y_label)
        mock_plt.xticks.assert_called_once_with(rotation=45)
        mock_plt.title.assert_called_once_with(title)
        mock_plt.savefig.assert_called_once_with(loader.OUTPUT_FILENAME, bbox_inches='tight')
        mock_plt.close.assert_called_once()

        # Assertion for gca and xaxis calls
        mock_gca = mock_plt.gca.return_value
        mock_xaxis = mock_gca.xaxis
        mock_mdates.DayLocator.assert_called_once_with(interval=loader.DEFAULT_INTERVAL_DAYS)
        mock_xaxis.set_major_locator.assert_called_once_with(mock_mdates.DayLocator.return_value)

    def test_init(self):
        title = "Test Title"
        x_label = "Test X Label"
        y_label = "Test Y Label"
        loader = MatplotlibLoader(title, x_label, y_label)
        assert loader.title == title
        assert loader.x_label == x_label
        assert loader.y_label == y_label
