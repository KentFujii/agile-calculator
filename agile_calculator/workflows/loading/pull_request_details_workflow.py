from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.loaders.csv_loader import CsvLoader
from agile_calculator.tasks.transformers.passthrough_transformer import (
    PassthroughTransformer,
)


class PullRequestDetailsWorkflow:
    def __init__(self, extractor: PullRequestExtractor, transformer: PassthroughTransformer) -> None:
        self._extractor = extractor
        self._transformer = transformer

    def csv(self) -> None:
        """
        計算結果をCSVへ出力します。
        """
        CsvLoader().run(
            self._transformer.run(
                self._extractor.run()
            )
        )
