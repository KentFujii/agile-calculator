from agile_calculator.tasks.extractors.github.comment_extractor import (
    CommentExtractor,
)
from agile_calculator.tasks.transformers.comment_details_transformer import (
    CommentDetailsTransformer,
)
from agile_calculator.workflows.loading.comment_details_workflow import (
    CommentDetailsWorkflow,
)


class CommentWorkflow:
    def __init__(self, extractor: CommentExtractor) -> None:
        self._extractor = extractor

    def details(self) -> CommentDetailsWorkflow:
        """
        Commentの詳細情報をCSV形式で出力します。
        """
        return CommentDetailsWorkflow(
            extractor=self._extractor,
            transformer=CommentDetailsTransformer(),
        )
