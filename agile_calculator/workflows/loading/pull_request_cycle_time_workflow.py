from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader
from agile_calculator.tasks.transformers.pull_request_cycle_time_transformer import (
    PullRequestCycleTimeTransformer,
)


class PullRequestCycleTimeWorkflow:
    def __init__(self, extractor: PullRequestExtractor, transformer: PullRequestCycleTimeTransformer) -> None:
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self) -> None:
        """
        計算結果をMatplotlibへ出力します。
        """
        MatplotlibLoader(
            "Pull Request Cycle Time (MA)",
            "Merged Date",
            "Lead Time (hours)"
        ).run(
            self._transformer.run(
                self._extractor.run()
            )
        )
