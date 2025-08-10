from ..extractors.github.pull_request_extractor import PullRequestExtractor
from ..loaders.matplotlib_loader import MatplotlibLoader
from ..transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)

class GithubWorkflow:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        self.loader.run(
            self.transformer.run(
                self.extractor.run()
            )
        )
