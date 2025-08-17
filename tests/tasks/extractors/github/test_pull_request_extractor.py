import os

import pytest

from agile_calculator.tasks.extractors.github.pull_request_extractor import (
    PullRequestExtractor,
)


class TestPullRequestExtractor:
    @pytest.mark.skip(reason="Not implemented")
    def test_extract(self):
        token = os.environ.get("GITHUB_CLASSIC_TOKEN")
        github_extractor = PullRequestExtractor(token=token)
        for pull_request in github_extractor.extract(repo_name="itandi/nomad-cloud"):
            print(pull_request)
