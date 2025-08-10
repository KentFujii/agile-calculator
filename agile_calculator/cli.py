import fire

from .interfaces.github_interface import GitHubInterface

class Cli:
    def github(self):
        return GitHubInterface()

def main():
    fire.Fire(Cli, name='agile-calculator')

if __name__ == "__main__":
    main()
