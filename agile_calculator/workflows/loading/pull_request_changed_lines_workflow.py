from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader
from agile_calculator.tasks.transformers.pull_request_changed_lines_transformer import (
    PullRequestChangedLinesTransformer,
)


class PullRequestChangedLinesWorkflow:
    def __init__(self, extractor: PullRequestExtractor, transformer: PullRequestChangedLinesTransformer) -> None:
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self) -> None:
        """
        計算結果をMatplotlibへ出力します。
        """
        MatplotlibLoader(
            "Pull Request Changed Lines (MA)",
            "Merged Date",
            "Changed Lines"
        ).run(
            self._transformer.run(
                self._extractor.run()
            )
        )
