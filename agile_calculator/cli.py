import fire

from .workflows.github_workflow import GitHubWorkflow

class Cli:
    def github(self):
        return GitHubWorkflow()

def main():
    fire.Fire(Cli, name='agile-calculator')

if __name__ == "__main__":
    main()
