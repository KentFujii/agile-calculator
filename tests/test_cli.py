from unittest.mock import patch

from agile_calculator.cli import main
from agile_calculator.workflows.extracting_workflow import ExtractingWorkflow


class TestCli:
    @patch('fire.Fire')
    def test_main(self, mock_fire):
        """
        Tests that the main function calls fire.Fire with the correct arguments.
        """
        main()
        mock_fire.assert_called_once_with(ExtractingWorkflow, name='agile-calculator')
