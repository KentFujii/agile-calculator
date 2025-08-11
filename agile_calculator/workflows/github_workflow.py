# from ..tasks.extractors.github.pull_request_extractor import PullRequestExtractor
from ..tasks.transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)
from ..tasks.loaders.matplotlib_loader import MatplotlibLoader


class PullRequestWorkflow:
    def __init__(self, extractor):
        self._extractor = extractor

    def lead_time_for_changes(self):
        return LeadTimeForChangesWorkflow(
            extractor=self._extractor,
            transformer=LeadTimeForChangesTransformer()
        )

class LeadTimeForChangesWorkflow:
    def __init__(self, extractor, transformer):
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self):
        MatplotlibLoader().run(
            self._transformer.run(
                self._extractor.run()
            )
        )

