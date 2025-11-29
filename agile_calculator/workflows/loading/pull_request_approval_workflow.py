from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.loaders.pie_chart_loader import PieChartLoader
from agile_calculator.tasks.transformers.pull_request_approval_transformer import (
    PullRequestApprovalTransformer,
)


class PullRequestApprovalWorkflow:
    def __init__(self, extractor: PullRequestExtractor, transformer: PullRequestApprovalTransformer) -> None:
        self._extractor = extractor
        self._transformer = transformer

    def pie_chart(self) -> None:
        """
        承認回数を円グラフとして出力します。
        """
        PieChartLoader(
            "Pull Request Approvals by User"
        ).run(
            self._transformer.run(
                self._extractor.run()
            )
        )
