from typing import Optional

from ..extractors.github.pull_request_extractor import PullRequestExtractor
from ..transformers.lead_time_for_changes_transformer import LeadTimeForChangesTransformer
from ..loaders.matplotlib_loader import MatplotlibLoader

class GitHubInterface:
    def pull_request(self, repo_name: str, users: tuple, since_days: int):
        return PullRequest(
            extractor=PullRequestExtractor(repo_name, users, since_days)
        )

class PullRequest:
    def __init__(self, extractor):
        self._extractor = extractor

    def lead_time_for_changes(self):
        return LeadTimeForChanges(
            extractor=self._extractor,
            transformer=LeadTimeForChangesTransformer()
        )

class LeadTimeForChanges:
    def __init__(self, extractor, transformer):
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self):
        MatplotlibLoader().run(
            self._transformer.run(
                self._extractor.run()
            )
        )

