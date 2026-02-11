from unittest.mock import MagicMock
from agile_calculator.tasks.transformers.pull_request_details_transformer import PullRequestDetailsTransformer
from agile_calculator.records.extracted.pull_request_record import PullRequestRecord
from agile_calculator.records.transformed.pull_request_details_record import PullRequestDetailsRecord

class TestPullRequestDetailsTransformer:
    def test_pull_request_details_transformer_with_mock(self):
        """
        MagicMockの場合でも変換できることをテスト
        """
        mock_record = MagicMock(spec=PullRequestRecord)
        mock_record.model_dump.return_value = {
            "number": 1, "title": "Test", "body": "test body", "draft": False, "user": "testuser",
            "created_at": None, "updated_at": None, "merged_at": None,
            "closed_at": None, "state": "closed", "base_ref": "main",
            "head_ref": "feature", "merged": False, "merge_commit_sha": None,
            "comments": 0, "review_comments": 0, "commits": 1,
            "additions": 10, "deletions": 5, "changed_files": 2
        }
        mock_records = [mock_record]
        transformer = PullRequestDetailsTransformer()
        result = transformer.run(mock_records)
        assert all(isinstance(r, PullRequestDetailsRecord) for r in result)
        assert result[0].number == 1
        assert result[0].title == "Test"
        assert result[0].body == "test body"

    def test_pull_request_details_transformer_maps_record(self):
        """
        PullRequestRecordがPullRequestDetailsRecordに変換されることをテスト
        """
        pr = PullRequestRecord(
            number=1,
            title="Test PR",
            body="test body description",
            draft=False,
            user="user1",
            created_at=None,
            updated_at=None,
            merged_at=None,
            closed_at=None,
            state="open",
            base_ref="main",
            head_ref="feature",
            merged=False,
            merge_commit_sha="abc123",
            comments=5,
            review_comments=2,
            commits=3,
            additions=10,
            deletions=2,
            changed_files=1,
        )
        transformer = PullRequestDetailsTransformer()
        result = transformer.run([pr])
        assert len(result) == 1
        details = result[0]
        assert isinstance(details, PullRequestDetailsRecord)
        assert details.number == pr.number
        assert details.title == pr.title
        assert details.body == pr.body
        assert details.user == pr.user
        assert details.state == pr.state
        assert details.base_ref == pr.base_ref
        assert details.head_ref == pr.head_ref
        assert details.merged == pr.merged
        assert details.merge_commit_sha == pr.merge_commit_sha
        assert details.comments == pr.comments
        assert details.review_comments == pr.review_comments
        assert details.commits == pr.commits
        assert details.additions == pr.additions
        assert details.deletions == pr.deletions
        assert details.changed_files == pr.changed_files
