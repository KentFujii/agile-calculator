from agile_calculator.tasks.transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)
from agile_calculator.tasks.transformers.review_comments_transformer import (
    ReviewCommentsTransformer,
)
from agile_calculator.workflows.loading.lead_time_for_changes_workflow import (
    LeadTimeForChangesWorkflow,
)
from agile_calculator.workflows.loading.review_comments_workflow import ReviewCommentsWorkflow


class PullRequestWorkflow:
    def __init__(self, extractor):
        self._extractor = extractor

    def lead_time_for_changes(self):
        """
        変更のリードタイムを計算します。
        """
        return LeadTimeForChangesWorkflow(
            extractor=self._extractor,
            transformer=LeadTimeForChangesTransformer()
        )

    def review_comments(self):
        """
        Pull Requestのレビューコメント数を計算します。
        """
        return ReviewCommentsWorkflow(
            extractor=self._extractor,
            transformer=ReviewCommentsTransformer()
        )
