import csv
from datetime import timedelta
from typing import Sequence, Any

from agile_calculator.records.transformed_record import TransformedRecord
from agile_calculator.tasks.loaders.base_loader import BaseLoader


class CsvLoader(BaseLoader):
    """
    TransformedRecordのリストを指定されたカラムに基づいてCSVファイルに出力するクラス
    """
    def __init__(self, output_path: str, columns: Sequence[str]) -> None:
        """
        CsvLoaderのコンストラクタ

        Args:
            output_path (str): CSVファイルの出力先パス
            columns (Sequence[str]): CSVのヘッダーとなるカラム名のシーケンス
        """
        self.output_path = output_path
        self.columns = columns

    def run(self, records: Sequence[TransformedRecord]) -> None:
        """
        レコードのリストを指定されたパスにCSVファイルとして書き出す。
        レコードが空の場合でもヘッダーのみのファイルを作成する。
        """
        with open(self.output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)

            for record in records:
                row_data = [self._format_value(getattr(record, col, None)) for col in self.columns]
                writer.writerow(row_data)

    def _format_value(self, value: Any) -> str:
        """
        値をCSVに適した文字列にフォーマットする

        - timedeltaは合計秒数に変換する
        - Noneは空文字に変換する
        - それ以外は文字列に変換する
        """
        if isinstance(value, timedelta):
            return str(value.total_seconds())
        if value is None:
            return ""
        return str(value)
