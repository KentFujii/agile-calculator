import fire

from agile_calculator.workflows.extracting_workflow import ExtractingWorkflow


def main():
    fire.Fire(ExtractingWorkflow, name='agile-calculator')

if __name__ == "__main__":
    main()
