from agile_calculator.records.transformed.pull_request_details_record import (
    PullRequestDetailsRecord,
)
from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.loaders.csv_loader import CsvLoader
from agile_calculator.tasks.transformers.pull_request_details_transformer import (
    PullRequestDetailsTransformer,
)


class PullRequestDetailsWorkflow:
    def __init__(self, extractor: PullRequestExtractor, transformer: PullRequestDetailsTransformer) -> None:
        self._extractor = extractor
        self._transformer = transformer

    def csv(self) -> None:
        """
        計算結果をCSVへ出力します。
        """
        CsvLoader(PullRequestDetailsRecord).run(
            self._transformer.run(
                self._extractor.run()
            )
        )
