import os
import pytest
from src.agile_calculator.workflows.lead_time_for_changes_workflow import LeadTimeForChangesWorkflow

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_NAME = os.environ.get("GITHUB_REPO_NAME")

@pytest.mark.skipif(not GITHUB_TOKEN or not REPO_NAME, reason="GITHUB_TOKENとGITHUB_REPO_NAME環境変数が必要です")
class TestLeadTimeForChangesWorkflow:
    def test_lead_time_for_changes_workflow_integration(self):
        """
        実際のGitHubリポジトリとトークンを使ってワークフローの結合テストを行います。
        GITHUB_TOKEN, GITHUB_REPO_NAME環境変数が必要です。
        """
        workflow = LeadTimeForChangesWorkflow(GITHUB_TOKEN, REPO_NAME)
        records = workflow.run()