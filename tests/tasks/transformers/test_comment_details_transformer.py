import pytest

from agile_calculator.tasks.transformers.comment_details_transformer import CommentDetailsTransformer
from agile_calculator.records.extracted.comment_record import CommentRecord
from datetime import datetime

class TestCommentDetailsTransformer:
    def test_run_returns_same_records(self):
        """Tests that the run method returns the same list of records it receives."""
        records = [
            CommentRecord(
                id=1,
                body="This is a comment",
                user="test_user",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                pull_request_url="https://github.com/test/repo/pull/1",
                author_association="OWNER",
                url="https://api.github.com/repos/test/repo/pulls/comments/1",
                html_url="https://github.com/test/repo/pull/1#discussion_r1"
            ),
            CommentRecord(
                id=2,
                body="Another comment",
                user="another_user",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                pull_request_url="https://github.com/test/repo/pull/1",
                author_association="CONTRIBUTOR",
                url="https://api.github.com/repos/test/repo/pulls/comments/2",
                html_url="https://github.com/test/repo/pull/1#discussion_r2"
            )
        ]

        transformer = CommentDetailsTransformer()
        result = transformer.run(records)

        assert result == records

    def test_run_with_empty_list(self):
        """Tests that the run method returns an empty list when given an empty list."""
        transformer = CommentDetailsTransformer()
        result = transformer.run([])
        assert result == []
