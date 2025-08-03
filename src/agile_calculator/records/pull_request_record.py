from .base_record import BaseRecorder

class PullRequestRecord(BaseRecorder):
    def __init__(self, number, title, draft, user, created_at, updated_at, merged_at, closed_at, state,
                 base_ref, head_ref, merged, merge_commit_sha, comments, review_comments, commits,
                 additions, deletions, changed_files):
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
