from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)
from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader
from agile_calculator.tasks.transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)


class LeadTimeForChangesWorkflow:
    def __init__(self, extractor: PullRequestExtractor, transformer: LeadTimeForChangesTransformer) -> None:
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self) -> None:
        """
        計算結果をMatplotlibへ出力します。
        """
        MatplotlibLoader(
            "Lead Time for Changes (MA)",
            "Merged Date",
            "Lead Time (hours)"
        ).run(
            self._transformer.run(
                self._extractor.run()
            )
        )
