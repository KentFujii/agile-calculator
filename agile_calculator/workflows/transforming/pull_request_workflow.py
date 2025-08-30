from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.transformers.pull_request_cycle_time_transformer import (
    PullRequestCycleTimeTransformer,
)
from agile_calculator.tasks.transformers.review_comments_transformer import (
    ReviewCommentsTransformer,
)
from agile_calculator.workflows.transforming.loading.pull_request_cycle_time_workflow import (
    PullRequestCycleTimeWorkflow,
)
from agile_calculator.workflows.transforming.loading.review_comments_workflow import (
    ReviewCommentsWorkflow,
)


class PullRequestWorkflow:
    def __init__(self, extractor: PullRequestExtractor) -> None:
        self._extractor = extractor

    def pull_request_cycle_time(self) -> PullRequestCycleTimeWorkflow:
        """
        Pull Requestのリードタイムを、一日ごとの移動平均推移で計算します。
        """
        return PullRequestCycleTimeWorkflow(
            extractor=self._extractor,
            transformer=PullRequestCycleTimeTransformer()
        )

    def review_comments(self) -> ReviewCommentsWorkflow:
        """
        Pull Requestのレビューコメント数を、一日ごとの移動平均推移で計算します。
        """
        return ReviewCommentsWorkflow(
            extractor=self._extractor,
            transformer=ReviewCommentsTransformer()
        )
