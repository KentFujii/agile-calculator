from agile_calculator.records.base_record import BaseRecord


class PullRequestRecord(BaseRecord):
    def __init__(
        self,
        number=None,
        title=None,
        draft=None,
        user=None,
        created_at=None,
        updated_at=None,
        merged_at=None,
        closed_at=None,
        state=None,
        base_ref=None,
        head_ref=None,
        merged=None,
        merge_commit_sha=None,
        comments=None,
        review_comments=None,
        commits=None,
        additions=None,
        deletions=None,
        changed_files=None
    ):
        self.number = number
        self.title = title
        self.draft = draft
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at
        self.merged_at = merged_at
        self.closed_at = closed_at
        self.state = state
        self.base_ref = base_ref
        self.head_ref = head_ref
        self.merged = merged
        self.merge_commit_sha = merge_commit_sha
        self.comments = comments
        self.review_comments = review_comments
        self.commits = commits
        self.additions = additions
        self.deletions = deletions
        self.changed_files = changed_files
        self.number = number
        self.title = title
        self.draft = draft
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at
        self.merged_at = merged_at
        self.closed_at = closed_at
        self.state = state
        self.base_ref = base_ref
        self.head_ref = head_ref
        self.merged = merged
        self.merge_commit_sha = merge_commit_sha
        self.comments = comments
        self.review_comments = review_comments
        self.commits = commits
        self.additions = additions
        self.deletions = deletions
        self.changed_files = changed_files

    def __repr__(self):
        return f"<PullRequestRecord #{self.number} {self.title}>"
