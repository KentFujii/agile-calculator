import fire


class LeadTimeForChanges:
    def matplotlib(self, ticks):
        print(ticks)
        print('matplotlib')

class PullRequest:
    def lead_time_for_changes(self, per_days):
        print(per_days)
        return LeadTimeForChanges()


class Cli:
    def github(self):
        return GitHub()

    def jira(self):
        pass

def main():
    fire.Fire(Cli, name='agile-calculator')

if __name__ == "__main__":
    main()
