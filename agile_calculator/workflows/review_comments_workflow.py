from agile_calculator.tasks.loaders.matplotlib_loader import MatplotlibLoader


class ReviewCommentsWorkflow:
    def __init__(self, extractor, transformer):
        self._extractor = extractor
        self._transformer = transformer

    def matplotlib(self):
        """
        計算結果をMatplotlibへ出力します。
        """
        pass
        # MatplotlibLoader().run(
        #     self._transformer.run(
        #         self._extractor.run()
        #     )
        # )

