import fire
from agile_calculator.workflows.root_workflow import RootWorkflow

def main():
    fire.Fire(RootWorkflow, name='agile-calculator')

if __name__ == "__main__":
    main()
