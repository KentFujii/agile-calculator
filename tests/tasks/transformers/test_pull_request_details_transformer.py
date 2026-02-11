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
        # Using **record.__dict__ requires fields to be present in __dict__.
        # Setting attributes on MagicMock places them in its __dict__.
        mock_record.number = 1
        mock_record.title = "Test"
        mock_record.draft = False
        mock_record.user = "testuser"
        mock_record.created_at = None
        mock_record.updated_at = None
        mock_record.merged_at = None
        mock_record.closed_at = None
        mock_record.state = "closed"
        mock_record.base_ref = "main"
        mock_record.head_ref = "feature"
        mock_record.merged = False
        mock_record.merge_commit_sha = None
        mock_record.comments = 0
        mock_record.review_comments = 0
        mock_record.commits = 1
        mock_record.additions = 10
        mock_record.deletions = 5
        mock_record.changed_files = 2

        # Note: MagicMock.__dict__ will contain these fields PLUS internal _mock_ attributes.
        # PullRequestDetailsRecord must be able to handle extra fields (default behavior: ignore).

        mock_records = [mock_record]
        transformer = PullRequestDetailsTransformer()
        result = transformer.run(mock_records)
        assert all(isinstance(r, PullRequestDetailsRecord) for r in result)
        assert result[0].number == 1
        assert result[0].title == "Test"

    def test_pull_request_details_transformer_maps_record(self):
        """
        PullRequestRecordがPullRequestDetailsRecordに変換されることをテスト
        """
        pr = PullRequestRecord(
            number=1,
            title="Test PR",
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
