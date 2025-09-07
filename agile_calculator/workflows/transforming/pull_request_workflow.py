from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.transformers.passthrough_transformer import (
    PassthroughTransformer,
)
from agile_calculator.tasks.transformers.pull_request_cycle_time_transformer import (
    PullRequestCycleTimeTransformer,
)
from agile_calculator.tasks.transformers.pull_request_review_comments_transformer import (
    PullRequestReviewCommentsTransformer,
)
from agile_calculator.workflows.loading.pull_request_cycle_time_workflow import (
    PullRequestCycleTimeWorkflow,
)
from agile_calculator.workflows.loading.pull_request_details_workflow import (
    PullRequestDetailsWorkflow,
)
from agile_calculator.workflows.loading.pull_request_review_comments_workflow import (
    PullRequestReviewCommentsWorkflow,
)


class PullRequestWorkflow:
    def __init__(self, extractor: PullRequestExtractor) -> None:
        self._extractor = extractor

    def cycle_time(self) -> PullRequestCycleTimeWorkflow:
        """
        Pull Requestのサイクルタイムを、一日ごとの移動平均推移で計算します。
        """
        return PullRequestCycleTimeWorkflow(
            extractor=self._extractor,
            transformer=PullRequestCycleTimeTransformer()
        )

    def review_comments(self) -> PullRequestReviewCommentsWorkflow:
        """
        Pull Requestのレビューコメント数を、一日ごとの移動平均推移で計算します。
        """
        return PullRequestReviewCommentsWorkflow(
            extractor=self._extractor,
            transformer=PullRequestReviewCommentsTransformer()
        )

    def details(self) -> PullRequestDetailsWorkflow:
        """
        Pull Requestの詳細情報をCSV形式で出力します。
        """
        return PullRequestDetailsWorkflow(
            extractor=self._extractor,
            transformer=PassthroughTransformer()
        )
