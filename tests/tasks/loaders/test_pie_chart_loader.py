import pytest
from unittest.mock import MagicMock, patch
from agile_calculator.records.transformed.approval_count_record import ApprovalCountRecord
from agile_calculator.tasks.loaders.pie_chart_loader import PieChartLoader

class TestPieChartLoader:
    @patch("agile_calculator.tasks.loaders.pie_chart_loader.plt")
    def test_run_generates_pie_chart(self, mock_plt):
        records = [
            ApprovalCountRecord(user="user1", count=10),
            ApprovalCountRecord(user="user2", count=5),
        ]

        loader = PieChartLoader(title="Approvals")
        loader.run(records)

        mock_plt.figure.assert_called_once()
        mock_plt.pie.assert_called_once()
        args, kwargs = mock_plt.pie.call_args

        # Check sizes (first arg)
        assert args[0] == [10, 5]
        # Check labels
        assert kwargs['labels'] == ["user1", "user2"]

        mock_plt.title.assert_called_with("Approvals")
        mock_plt.savefig.assert_called_with("loader.png", bbox_inches='tight')
        mock_plt.close.assert_called_once()

    @patch("agile_calculator.tasks.loaders.pie_chart_loader.plt")
    def test_run_empty_records(self, mock_plt):
        loader = PieChartLoader(title="Approvals")
        loader.run([])

        mock_plt.pie.assert_not_called()
