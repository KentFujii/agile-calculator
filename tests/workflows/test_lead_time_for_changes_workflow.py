import os

from src.agile_calculator.workflows.lead_time_for_changes_workflow import (
    LeadTimeForChangesWorkflow,
)


class TestLeadTimeForChangesWorkflow:
    def test_lead_time_for_changes_workflow_integration(self):
        token = os.environ.get("GITHUB_CLASSIC_TOKEN")
        workflow = LeadTimeForChangesWorkflow(token, 'itandi/nomad-cloud', since_days=360)
        records = workflow.run()
