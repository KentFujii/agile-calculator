from agile_calculator.tasks.transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)
from agile_calculator.workflows.transforming.lead_time_for_changes_workflow import (
    LeadTimeForChangesWorkflow,
)


class PullRequestWorkflow:
    def __init__(self, extractor):
        self._extractor = extractor

    def lead_time_for_changes(self):
        return LeadTimeForChangesWorkflow(
            extractor=self._extractor,
            transformer=LeadTimeForChangesTransformer()
        )
