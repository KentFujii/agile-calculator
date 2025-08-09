from ..extractors.github.pull_request_extractor import PullRequestExtractor
from ..loaders.matplotlib_loader import MatplotlibLoader
from ..transformers.lead_time_for_changes_transformer import (
    LeadTimeForChangesTransformer,
)


class LeadTimeForChangesWorkflow:
    def __init__(self, github_token, repo_name, since_days=None, users=None):
        self.github_token = github_token
        self.repo_name = repo_name
        self.since_days = since_days if since_days is not None else 14
        self.users = users if users is not None else []

    def run(self):
        self._load(
            self._transform(
                self._extract()
            )
        )

    def _extract(self):
        extracted_records = PullRequestExtractor(self.github_token).run(
            self.repo_name, since_days=self.since_days, users=self.users
        )
        return extracted_records

    def _transform(self, extracted_records):
        transformed_records = [
            LeadTimeForChangesTransformer(pr).run() for pr in extracted_records if pr.merged_at
        ]
        return transformed_records

    def _load(self, transformed_records):
        MatplotlibLoader(transformed_records).run()
