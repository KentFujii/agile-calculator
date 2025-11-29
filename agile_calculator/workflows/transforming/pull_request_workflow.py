from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.transformers.pull_request_approval_transformer import (
    PullRequestApprovalTransformer,
)
from agile_calculator.tasks.transformers.pull_request_changed_lines_transformer import (
    PullRequestChangedLinesTransformer,
)
from agile_calculator.tasks.transformers.pull_request_cycle_time_transformer import (
    PullRequestCycleTimeTransformer,
)
from agile_calculator.tasks.transformers.pull_request_details_transformer import (
    PullRequestDetailsTransformer,
)
from agile_calculator.tasks.transformers.pull_request_merged_count_transformer import (
    PullRequestMergedCountTransformer,
)
from agile_calculator.tasks.transformers.pull_request_review_comments_transformer import (
    PullRequestReviewCommentsTransformer,
)
from agile_calculator.workflows.loading.pull_request_approval_workflow import (
    PullRequestApprovalWorkflow,
)
from agile_calculator.workflows.loading.pull_request_changed_lines_workflow import (
    PullRequestChangedLinesWorkflow,
)
from agile_calculator.workflows.loading.pull_request_cycle_time_workflow import (
    PullRequestCycleTimeWorkflow,
)
from agile_calculator.workflows.loading.pull_request_details_workflow import (
    PullRequestDetailsWorkflow,
)
from agile_calculator.workflows.loading.pull_request_merged_count_workflow import (
    PullRequestMergedCountWorkflow,
)
from agile_calculator.workflows.loading.pull_request_review_comments_workflow import (
    PullRequestReviewCommentsWorkflow,
)


class PullRequestWorkflow:
    def __init__(self, extractor: PullRequestExtractor) -> None:
        self._extractor = extractor

    def approvals(self) -> PullRequestApprovalWorkflow:
        """
        Pull Requestの承認回数を集計します。
        """
        return PullRequestApprovalWorkflow(
            extractor=self._extractor,
            transformer=PullRequestApprovalTransformer(),
        )

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

    def merged_count(self) -> PullRequestMergedCountWorkflow:
        """
        日ごとのマージされたPR数の合計を計算します。
        """
        return PullRequestMergedCountWorkflow(
            extractor=self._extractor,
            transformer=PullRequestMergedCountTransformer(),
        )

    def changed_lines(self) -> PullRequestChangedLinesWorkflow:
        """
        Pull Requestの変更行数（additions + deletions）を、一日ごとの移動平均推移で計算します。
        """
        return PullRequestChangedLinesWorkflow(
            extractor=self._extractor,
            transformer=PullRequestChangedLinesTransformer(),
        )

    def details(self) -> PullRequestDetailsWorkflow:
        """
        Pull Requestの詳細情報をCSV形式で出力します。
        """
        return PullRequestDetailsWorkflow(
            extractor=self._extractor,
            transformer=PullRequestDetailsTransformer(),
        )
