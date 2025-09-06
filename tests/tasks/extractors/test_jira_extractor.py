from unittest.mock import MagicMock, PropertyMock, patch

from agile_calculator.tasks.extractors.jira_extractor import JiraExtractor


class TestJiraExtractor:
    @patch('agile_calculator.tasks.extractors.jira_extractor.JIRA')
    def test_run(self, mock_jira_class):
        """
        Tests the run method of JiraExtractor with a mocked JIRA client.
        """
        # Arrange
        mock_jira_instance = MagicMock()
        mock_jira_class.return_value = mock_jira_instance

        # Mock the return value of client.fields()
        mock_jira_instance.fields.return_value = [
            {'name': 'Story point estimate', 'id': 'customfield_10016'},
            {'name': 'Sprint', 'id': 'customfield_10020'}
        ]

        # Mock the return value of client.search_issues()
        mock_issue = MagicMock()
        mock_issue.key = 'TEST-1'
        # Using PropertyMock for attributes of mock_issue.fields
        type(mock_issue.fields).summary = PropertyMock(return_value='Test Summary')
        status_mock = MagicMock()
        type(status_mock).name = PropertyMock(return_value='Done')
        type(mock_issue.fields).status = PropertyMock(return_value=status_mock)
        type(mock_issue.fields).assignee = PropertyMock(return_value=MagicMock(displayName='Test User'))
        # To mock attribute access like `issue.fields.customfield_10016`
        setattr(type(mock_issue.fields), 'customfield_10016', PropertyMock(return_value=5))
        # To mock attribute access like `issue.fields.customfield_10020`
        sprint_mock = MagicMock()
        sprint_mock.name = 'Sprint 1'
        setattr(type(mock_issue.fields), 'customfield_10020', PropertyMock(return_value=[sprint_mock]))


        mock_jira_instance.search_issues.return_value = [mock_issue]

        # Act
        extractor = JiraExtractor(server='http://test.jira.com', email='test@user.com', token='test_token')
        issues = list(extractor.run(project_key='TEST', assignee='Test User'))

        # Assert
        assert len(issues) == 1
        issue_info = issues[0]
        assert issue_info.key == 'TEST-1'
        assert issue_info.summary == 'Test Summary'
        assert issue_info.status == 'Done'
        assert issue_info.assignee == 'Test User'
        assert issue_info.story_points == 5
        assert issue_info.sprints == ['Sprint 1']

        mock_jira_class.assert_called_once_with('http://test.jira.com', basic_auth=('test@user.com', 'test_token'))
        mock_jira_instance.search_issues.assert_called_once_with('project = "TEST" AND assignee = "Test User" ORDER BY created DESC')
