import fire

# https://github.com/google/python-fire/blob/master/docs/guide.md#grouping-commands

class LeadTimeForChanges:
    def matplotlib(self, ticks):
        print(ticks)
        print('matplotlib')

class PullRequest:
    def lead_time_for_changes(self, per_days):
        print(per_days)
        return LeadTimeForChanges()

class GitHub:
    def pull_request(self, repo_name: str, since_days: int = 14, users: list = None):
        """
        GitHubのPull Requestからデータを抽出します。

        :param repo_name: リポジトリ名 (例: 'owner/repo')
        :param since_days: 何日前からのデータを取得するか
        """
        print(repo_name)
        print('pull_request')
        return PullRequest()

class Cli:
    def github(self):
        return GitHub()

    def jira(self):
        pass

def main():
    fire.Fire(Cli, name='agile-calculator')

if __name__ == "__main__":
    main()
