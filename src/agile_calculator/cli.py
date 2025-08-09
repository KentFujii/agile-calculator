import fire

class Cli:
    """Agile Calculator CLI"""

    def (self, name: str = "world") -> None:
        """Prints a greeting."""
        print(f"Hello, {name}!")

def main() -> None:
    """CLI entry point."""
    fire.Fire(Cli)

if __name__ == "__main__":
    main()
