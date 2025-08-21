from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader
from agile_calculator.tasks.transformers.review_comments_transformer import (
    ReviewCommentsTransformer,
)


class ReviewCommentsWorkflow:
    def __init__(self, extractor: PullRequestExtractor, transformer: ReviewCommentsTransformer) -> None:
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self) -> None:
        """
        計算結果をMatplotlibへ出力します。
        """
        MatplotlibLoader(
            "Number of Review Comments (MA)",
            "Merged Date",
            "Review Comments Counts"
        ).run(
            self._transformer.run(
                self._extractor.run()
            )
        )
