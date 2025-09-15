from agile_calculator.tasks.extractors.github.comment_extractor import (
    CommentExtractor,
)
from agile_calculator.tasks.transformers.comment_details_transformer import (
    CommentDetailsTransformer,
)
from agile_calculator.tasks.loaders.csv_loader import CsvLoader


class CommentDetailsWorkflow:
    def __init__(self, extractor: CommentExtractor, transformer: CommentDetailsTransformer) -> None:
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
