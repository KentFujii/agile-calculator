import fire

class AgileCalculatorCLI:
    """Agile Calculator CLI"""

    def hello(self, name: str = "world") -> None:
        """Prints a greeting."""
        print(f"Hello, {name}!")

def main() -> None:
    """CLI entry point."""
    fire.Fire(AgileCalculatorCLI)

if __name__ == "__main__":
    main()
