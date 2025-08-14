from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader


class LeadTimeForChangesWorkflow:
    def __init__(self, extractor, transformer):
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self):
        """
        計算結果をMatplotlibへ出力します。
        """
        MatplotlibLoader(
            "Lead Time for Changes (MA)",
            "Merged Date",
            "Lead Time (hours)"
        ).run(
            self._transformer.run(
                self._extractor.run()
            )
        )
