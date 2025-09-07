import csv
from datetime import timedelta
from typing import Any, Sequence

from agile_calculator.records.transformed_record import TransformedRecord
from agile_calculator.tasks.loaders.base_loader import BaseLoader


class CsvLoader(BaseLoader):
    """
    TransformedRecordのリストを指定されたカラムに基づいてCSVファイルに出力するクラス
    """
    OUTPUT_PATH = "csv_loader.csv"

    def run(self, records: Sequence[TransformedRecord]) -> None:
        """
        レコードのリストを指定されたパスにCSVファイルとして書き出す。
        レコードが空の場合でもヘッダーのみのファイルを作成する。
        TransformedRecordの型からフィールドを自動抽出し、CSVの列として扱う。
        """
        # フィールド名の抽出
        if records:
            # dataclassの場合
            if hasattr(records[0], "__dataclass_fields__"):
                columns = list(records[0].__dataclass_fields__.keys())
            else:
                columns = [attr for attr in dir(records[0]) if not attr.startswith('_') and not callable(getattr(records[0], attr))]
        else:
            # recordsが空の場合はTransformedRecordからフィールドを抽出
            if hasattr(TransformedRecord, "__dataclass_fields__"):
                columns = list(TransformedRecord.__dataclass_fields__.keys())
            else:
                columns = [attr for attr in dir(TransformedRecord) if not attr.startswith('_') and not callable(getattr(TransformedRecord, attr))]

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
