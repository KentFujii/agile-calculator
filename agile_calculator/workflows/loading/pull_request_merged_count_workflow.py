from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader
from agile_calculator.tasks.transformers.pull_request_merged_count_transformer import (
    PullRequestMergedCountTransformer,
)


class PullRequestMergedCountWorkflow:
    def __init__(self, extractor: PullRequestExtractor, transformer: PullRequestMergedCountTransformer) -> None:
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self) -> None:
        """
        計算結果をMatplotlibへ出力します。
        """
        MatplotlibLoader(
            "Number of Merged Pull Requests",
            "Merged Date",
            "Merged Counts"
        ).run(
            self._transformer.run(
                self._extractor.run()
            )
        )
