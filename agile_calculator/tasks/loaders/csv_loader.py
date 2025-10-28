import csv
from datetime import timedelta
from typing import Any, Sequence, Type

from agile_calculator.records.transformed_record import TransformedRecord
from agile_calculator.tasks.loaders.base_loader import BaseLoader


class CsvLoader(BaseLoader):
    """
    TransformedRecordのリストを指定されたカラムに基づいてCSVファイルに出力するクラス
    """
    OUTPUT_PATH = "loader.csv"

    def __init__(self, record_type: Type[TransformedRecord]):
        self._record_type = record_type

    def run(self, records: Sequence[TransformedRecord]) -> None:
        """
        レコードのリストを指定されたパスにCSVファイルとして書き出す。
        レコードが空の場合でもヘッダーのみのファイルを作成する。
        TransformedRecordの型からフィールドを自動抽出し、CSVの列として扱う。
        """
        # フィールド名の抽出
        if records:
            columns = list(records[0].model_fields.keys())
        else:
            columns = list(self._record_type.model_fields.keys())

        with open(self.OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(columns)

            for record in records:
                row_data = [self._format_value(getattr(record, col, None)) for col in columns]
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
