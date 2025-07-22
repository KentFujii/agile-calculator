import unittest
from unittest.mock import patch, MagicMock
from src.agile_calculator.clients.jira_client import JiraClient, get_jira_client

class TestJiraClient(unittest.TestCase):

    @patch('src.agile_calculator.clients.jira_client.JIRA')
    def test_get_issues_success(self, mock_jira):
        # Arrange
        mock_jira_instance = MagicMock()
        mock_jira.return_value = mock_jira_instance
        mock_jira_instance.search_issues.return_value = ['issue1', 'issue2']

        client = JiraClient(server='https://jira.example.com', token='fake_token')

        # Act
        issues = client.get_issues('PROJ')

        # Assert
        self.assertEqual(len(issues), 2)
        mock_jira_instance.search_issues.assert_called_once_with('project=PROJ')

    @patch('src.agile_calculator.clients.jira_client.JIRA')
    def test_get_issues_failure(self, mock_jira):
        # Arrange
        mock_jira_instance = MagicMock()
        mock_jira.return_value = mock_jira_instance
        from jira.exceptions import JIRAError
        mock_jira_instance.search_issues.side_effect = JIRAError(text="Failed to connect")

        client = JiraClient(server='https://jira.example.com', token='fake_token')

        # Act
        issues = client.get_issues('PROJ')

        # Assert
        self.assertEqual(len(issues), 0)
        mock_jira_instance.search_issues.assert_called_once_with('project=PROJ')

    @patch.dict('os.environ', {'JIRA_SERVER': 'https://jira.example.com', 'JIRA_TOKEN': 'fake_token'})
    @patch('src.agile_calculator.clients.jira_client.JIRA')
    def test_get_jira_client(self, mock_jira):
        # Arrange
        mock_jira_instance = MagicMock()
        mock_jira.return_value = mock_jira_instance

        # Act
        client = get_jira_client()

        # Assert
        self.assertIsInstance(client, JiraClient)
        self.assertEqual(client.server, 'https://jira.example.com')

    def test_get_jira_client_missing_env_vars(self):
        # Act & Assert
        with self.assertRaises(ValueError):
            get_jira_client()

if __name__ == '__main__':
    unittest.main()
